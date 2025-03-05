import subprocess
from fastapi import FastAPI
import uvicorn

app = FastAPI()

# Route pour lancer Streamlit via subprocess
@app.get("/")
def read_root():
    # Lancer Streamlit en subprocess
    subprocess.Popen(["streamlit", "run", "app.py"])  # Remplace "app.py" par le nom de ton fichier Streamlit
    return {"message": "Streamlit app launched!"}
