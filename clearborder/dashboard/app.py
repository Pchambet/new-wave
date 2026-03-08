"""
ClearBorder Dashboard — Interface de gestion CBAM
"""
import os
import streamlit as st
import requests
from decimal import Decimal

# API_BASE depuis env (docker) ou localhost par défaut
API_BASE = os.getenv("API_BASE", "http://localhost:8000/api/v1")
HEALTH_URL = os.getenv("API_BASE", "http://localhost:8000").replace("/api/v1", "") + "/health"

st.set_page_config(
    page_title="ClearBorder — CBAM Compliance",
    page_icon="📦",
    layout="wide",
)

st.title("📦 ClearBorder — Moteur CBAM")
st.caption("Calcul des Specific Embedded Emissions (SEE) — Règlement UE 2023/956")


def api_get(path: str):
    try:
        r = requests.get(f"{API_BASE}{path}", timeout=5)
        return r.json() if r.ok else None
    except requests.exceptions.ConnectionError:
        return None


def api_post(path: str, json: dict):
    try:
        r = requests.post(f"{API_BASE}{path}", json=json, timeout=10)
        return r
    except requests.exceptions.ConnectionError:
        return None


# Sidebar
st.sidebar.header("Navigation")
page = st.sidebar.radio(
    "Menu",
    ["🏠 Accueil", "🔍 Classification CN", "🏭 Installations", "📦 Produits", "📄 Rapport CBAM", "⚙️ À propos"],
)

# Check API health
try:
    h = requests.get(HEALTH_URL, timeout=2)
    if not h.ok:
        st.sidebar.warning("⚠️ API non disponible")
except Exception:
    st.sidebar.warning("⚠️ Lancez l'API ou définissez API_BASE pour un déploiement distant")

if page == "🏠 Accueil":
    st.header("Bienvenue sur ClearBorder")
    st.markdown("""
    **ClearBorder** calcule automatiquement les émissions intégrées spécifiques (SEE) 
    pour vos importations soumises au CBAM (Mécanisme d'Ajustement Carbone aux Frontières).
    
    ### Fonctionnalités
    - **Installations** : Gérez vos fournisseurs et leurs données d'émissions
    - **Produits** : Déclarez vos produits avec leur BOM (précurseurs)
    - **Rapport CBAM** : Générez le XML trimestriel conforme au schéma TAXUD
    
    ### Démarrage rapide
    1. Créez une installation (fournisseur hors-UE)
    2. Ajoutez un produit avec ses précurseurs
    3. Générez le rapport CBAM
    """)

elif page == "🔍 Classification CN":
    st.header("Classification automatique CN")
    st.caption("Suggère des codes nomenclature à partir d'une description produit (ML)")
    
    desc = st.text_area("Description du produit", placeholder="Ex: Tôle d'acier laminée à chaud, épaisseur 2mm")
    if st.button("Classifier"):
        if desc.strip():
            r = api_post("/classify", {"description": desc, "top_k": 5})
            if r and r.status_code == 200:
                data = r.json()
                for i, s in enumerate(data.get("suggestions", []), 1):
                    st.markdown(f"**{i}.** `{s.get('code', '')}` — {s.get('confidence', 0)*100:.0f}% — *{s.get('description', '')}*")
            elif r:
                st.error(r.text)
            else:
                st.error("API non disponible")
        else:
            st.warning("Entrez une description")
    
    cn_codes = api_get("/cn-codes")
    if cn_codes:
        with st.expander("📋 Codes CN disponibles"):
            st.dataframe(cn_codes, use_container_width=True)

elif page == "🏭 Installations":
    st.header("Installations (fournisseurs)")
    
    with st.expander("➕ Nouvelle installation"):
        with st.form("new_installation"):
            name = st.text_input("Nom")
            country = st.text_input("Pays (code ISO)", "TR", max_chars=2)
            sector = st.selectbox("Secteur", ["iron_steel", "aluminium", "cement", "fertilisers", "hydrogen", "electricity"])
            emissions = st.number_input("Émissions (tCO2e/tonne)", min_value=0.0, value=1.5, step=0.1)
            if st.form_submit_button("Créer"):
                r = api_post("/installations", {
                    "name": name,
                    "country_code": country.upper(),
                    "sector": sector,
                    "emissions_per_tonne": float(emissions),
                })
                if r and r.status_code == 200:
                    st.success("Installation créée !")
                elif r:
                    st.error(r.text)
                else:
                    st.error("API non disponible")
    
    data = api_get("/installations")
    if data:
        st.dataframe(data, use_container_width=True)
    else:
        st.info("Aucune installation. Créez-en une ci-dessus.")

elif page == "📦 Produits":
    st.header("Produits")
    
    installations = api_get("/installations") or []
    inst_map = {str(i["id"]): i["name"] for i in installations}
    
    with st.expander("➕ Nouveau produit"):
        with st.form("new_product"):
            name = st.text_input("Nom du produit")
            cn_code = st.text_input("Code CN (8 chiffres)", "7208 10 00")
            sector = st.selectbox("Secteur", ["iron_steel", "aluminium", "cement", "fertilisers", "hydrogen", "electricity"])
            inst_id = st.selectbox("Installation", options=list(inst_map.keys()), format_func=lambda x: inst_map.get(x, x))
            activity = st.number_input("Masse totale (kg)", min_value=0.1, value=1000.0)
            attr_em = st.number_input("Émissions attribuées processus (kg CO2e)", min_value=0.0, value=0.0)
            
            st.subheader("Précurseurs (optionnel)")
            p1_mass = st.number_input("Précurseur 1 — Masse (kg)", min_value=0.0, value=0.0)
            p1_see = st.number_input("Précurseur 1 — SEE (kg CO2e/kg)", min_value=0.0, value=0.0)
            p1_real = st.checkbox("Précurseur 1 — Données réelles", False)
            
            if st.form_submit_button("Créer"):
                precursors = []
                if p1_mass > 0:
                    precursors.append({"mass_kg": float(p1_mass), "see_per_kg": float(p1_see), "is_real_data": p1_real})
                r = api_post("/products", {
                    "name": name,
                    "cn_code": cn_code.replace(" ", ""),
                    "sector": sector,
                    "installation_id": int(inst_id),
                    "activity_level": float(activity),
                    "attributed_emissions": float(attr_em),
                    "precursors": precursors,
                })
                if r and r.status_code == 200:
                    st.success("Produit créé !")
                elif r:
                    st.error(r.text)
                else:
                    st.error("API non disponible")
    
    data = api_get("/products")
    if data:
        st.dataframe(data, use_container_width=True)
    else:
        st.info("Aucun produit. Créez-en un ci-dessus.")

elif page == "📄 Rapport CBAM":
    st.header("Générer un rapport CBAM")
    
    products = api_get("/products") or []
    
    if not products:
        st.info("Ajoutez des produits avant de générer un rapport.")
    else:
        with st.form("cbam_report"):
            declarant_id = st.text_input("ID Déclarant CBAM", "EU-CBAM-2026-001")
            period = st.text_input("Période", "2026-Q1")
            
            st.subheader("Produits à inclure")
            selected = []
            for p in products:
                qty = st.number_input(
                    f"{p.get('name', '')} ({p.get('cn_code', '')}) — Quantité (tonnes)",
                    min_value=0.01,
                    value=1.0,
                    key=f"qty_{p['id']}",
                )
                selected.append({"product_id": p["id"], "quantity_tonnes": float(qty)})
            
            if st.form_submit_button("Générer le rapport"):
                r = api_post("/generate-cbam-report", {
                    "declarant_id": declarant_id,
                    "reporting_period": period,
                    "products": selected,
                })
                if r and r.status_code == 200:
                    data = r.json()
                    st.success("Rapport généré !")
                    st.json(data.get("results", []))
                    st.download_button(
                        "Télécharger XML",
                        data.get("xml_content", ""),
                        file_name=f"cbam_report_{period}.xml",
                        mime="application/xml",
                    )
                elif r:
                    st.error(r.text)
                else:
                    st.error("API non disponible")

else:
    st.header("À propos")
    st.markdown("""
    **ClearBorder** v0.1.0 — MVP RegTech
    
    - Calcul SEE conforme Annexe IV Règlement (UE) 2023/956
    - Règle 80/20 pour biens complexes
    - Export XML pour le portail CBAM
    
    *Développé dans le cadre du projet New Wave*
    """)
