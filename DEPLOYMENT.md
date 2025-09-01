# Deployment Guide

## GitHub Pages Deployment

This repository is configured to automatically deploy the frontend to GitHub Pages when changes are pushed to the `main` branch.

### How it works

1. The `.github/workflows/static.yml` workflow automatically deploys the `frontend/` directory to GitHub Pages
2. The frontend is configured to work in different environments via `config.js`
3. When deployed to GitHub Pages, it runs in "demo mode" since GitHub Pages only serves static content

### Accessing the Deployed App

Once deployed, the frontend will be available at:
`https://fullstacks-us.github.io/wtmr/`

### Backend Deployment

Since this is a FastAPI Python application with a separate backend, you'll need to deploy the backend separately:

#### Option 1: Local Development
```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # or `venv\Scripts\activate` on Windows
pip install -r requirements.txt
uvicorn main:app --host 0.0.0.0 --port 8000
```

#### Option 2: Production Deployment
Deploy the backend to a cloud service like:
- **Heroku**: Use the included `requirements.txt` 
- **Railway**: Supports FastAPI out of the box
- **Render**: Free tier available for small apps
- **DigitalOcean App Platform**: Easy FastAPI deployment
- **AWS Lambda**: With Mangum ASGI adapter
- **Google Cloud Run**: Container-based deployment

#### Option 3: Tailscale (Original Design)
This app was designed for private Tailscale networks:
1. Deploy backend on a VPS with Tailscale
2. Configure frontend `config.js` with your Tailscale backend URL
3. Access privately through your tailnet

### Configuration

To connect the frontend to your backend:
1. Edit `frontend/config.js`
2. Update the `API_BASE_URL` with your backend server URL
3. Redeploy or serve locally

### Manual Deployment

To manually trigger a deployment:
1. Go to the Actions tab in GitHub
2. Select "Deploy static content to Pages"
3. Click "Run workflow"