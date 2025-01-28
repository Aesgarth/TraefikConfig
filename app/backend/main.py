from fastapi import FastAPI, HTTPException
import yaml
from pathlib import Path

app = FastAPI()

CONFIG_FILE = "/app/config/dynamic.yml"

@app.get("/config")
def get_config():
    try:
        with open(CONFIG_FILE, "r") as file:
            return yaml.safe_load(file)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error reading config: {str(e)}")

@app.post("/config")
def update_config(new_config: dict):
    try:
        with open(CONFIG_FILE, "w") as file:
            yaml.dump(new_config, file)
        return {"message": "Configuration updated successfully"}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error writing config: {str(e)}")
