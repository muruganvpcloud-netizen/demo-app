# demo-app
 
Small Flask web app used to practise CI/CD on Google Kubernetes Engine
with GitHub Actions, Helm and Argo CD.
 
## Run locally
 
    python3 -m venv .venv
    source .venv/bin/activate
    pip install -r requirements-dev.txt
    pytest
    python app.py

Notes: this app is deployed to GKE with GitHub Actions and Argo CD.
