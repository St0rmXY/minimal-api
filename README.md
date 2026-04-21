# minimal-api
# Minimal API Task

A tiny FastAPI backend with three required endpoints.

## How to run locally
```bash
git clone https://github.com/YOURUSERNAME/minimal-api.git
cd minimal-api
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
uvicorn main:app --reload --port 8000
