# Déploiement ClearBorder — Cloud Run

Guide pour déployer l'API ClearBorder sur Google Cloud Run avec PostgreSQL.

---

## Prérequis

1. **Compte Google Cloud** avec facturation activée (Cloud Run a un free tier généreux)
2. **PostgreSQL** — Une des options :
   - [Neon](https://neon.tech) (gratuit, recommandé pour MVP)
   - [Supabase](https://supabase.com) (gratuit)
   - Cloud SQL (payant, ~25€/mois)

---

## Option A : Déploiement manuel (15 min)

### 1. Créer un projet GCP

```bash
gcloud projects create clearborder-prod --name="ClearBorder"
gcloud config set project clearborder-prod
```

### 2. Activer les APIs

```bash
gcloud services enable run.googleapis.com artifactregistry.googleapis.com cloudbuild.googleapis.com
```

### 3. Créer le dépôt Artifact Registry

```bash
gcloud artifacts repositories create clearborder \
  --repository-format=docker \
  --location=europe-west1 \
  --description="ClearBorder images"
gcloud auth configure-docker europe-west1-docker.pkg.dev --quiet
```

### 4. Base de données (Neon — recommandé)

1. Créer un compte sur [neon.tech](https://neon.tech)
2. Créer un projet → récupérer la connection string
3. Exemple : `postgresql://user:pass@ep-xxx.eu-central-1.aws.neon.tech/neondb?sslmode=require`

### 5. Build et déploiement

```bash
cd clearborder
gcloud run deploy clearborder-api \
  --source . \
  --region europe-west1 \
  --platform managed \
  --allow-unauthenticated \
  --set-env-vars "DATABASE_URL=postgresql://..." \
  --set-secrets "API_KEYS=api-keys:latest"  # optionnel
```

Pour passer les secrets (clés API, DB) :

```bash
# Créer un secret
echo -n "sk-prod-xxx,sk-prod-yyy" | gcloud secrets create api-keys --data-file=-

# Déployer avec le secret
gcloud run deploy clearborder-api \
  --source . \
  --region europe-west1 \
  --set-secrets "API_KEYS=api-keys:latest"
```

### 6. Seed des données (premier déploiement)

Une fois déployé, exécuter le seed à distance :

```bash
gcloud run jobs create clearborder-seed --image eu.gcr.io/PROJECT_ID/clearborder-api:latest ...
# Ou : se connecter en SSH et lancer le script (selon votre setup)
```

Alternative : lancer un Cloud Run Job ou une tâche one-off avec `python scripts/seed_data.py`.

---

## Option B : GitHub Actions (CD automatique)

### 1. Configurer Workload Identity

```bash
# Créer un service account pour le déploiement
gcloud iam service-accounts create github-deploy \
  --display-name="GitHub Deploy"

gcloud projects add-iam-policy-binding clearborder-prod \
  --member="serviceAccount:github-deploy@clearborder-prod.iam.gserviceaccount.com" \
  --role="roles/run.admin"

gcloud projects add-iam-policy-binding clearborder-prod \
  --member="serviceAccount:github-deploy@clearborder-prod.iam.gserviceaccount.com" \
  --role="roles/artifactregistry.writer"

gcloud projects add-iam-policy-binding clearborder-prod \
  --member="serviceAccount:github-deploy@clearborder-prod.iam.gserviceaccount.com" \
  --role="roles/iam.serviceAccountUser"
```

### 2. Secrets GitHub

Dans **Settings → Secrets and variables → Actions**, ajouter :

| Secret | Description |
|--------|-------------|
| `GCP_PROJECT_ID` | ID du projet GCP |
| `GCP_SA_KEY` | Clé JSON du service account (ou utiliser Workload Identity) |
| `DATABASE_URL` | Connection string PostgreSQL |

### 3. Déclencher le déploiement

Le workflow `deploy.yml` se déclenche sur push sur `main`. À la première exécution, vérifier que les secrets sont bien configurés.

---

## Vérifications post-déploiement

```bash
# URL du service
SERVICE_URL=$(gcloud run services describe clearborder-api --region europe-west1 --format='value(status.url)')
echo $SERVICE_URL

# Health check
curl $SERVICE_URL/health

# Docs API
open $SERVICE_URL/docs
```

---

## Domaine personnalisé (optionnel)

1. Aller dans **Cloud Run → clearborder-api → Domain mappings**
2. Ajouter un domaine personnalisé (ex: `api.clearborder.com`)
3. Configurer les enregistrements DNS (CNAME ou A selon les instructions)

---

## Coûts estimés

| Service | Coût mensuel |
|---------|---------------|
| Cloud Run (API) | 0€ (free tier 2M req/mois) |
| Neon PostgreSQL | 0€ (free tier) |
| Artifact Registry | 0€ (< 0,5 GB gratuit) |
| **Total MVP** | **0€** (dans les limites free tier) |

> 📘 **Guide détaillé gratuit** : voir [DEPLOIEMENT-GRATUIT.md](DEPLOIEMENT-GRATUIT.md)

---

*ClearBorder — New Wave RegTech — mars 2026*
