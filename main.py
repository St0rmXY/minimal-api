from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def root():
    return {"message": "API is running"}

@app.get("/health")
def health():
    return {"message": "healthy"}

@app.get("/me")
def me():
    return {
        "name": "bolaji-2026",          # ← CHANGE TO YOUR REAL NAME
        "email": "gboyegbile2020@gmail.com",        # ← CHANGE TO YOUR REAL EMAIL
        "github": "https://github.com/St0rmXY"  # ← CHANGE TO YOUR REAL GITHUB
    }
