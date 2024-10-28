from model import Creature
from fastapi import FastAPI
from data import get_creatures  # Import `get_creatures` directly at the top

app = FastAPI()

@app.get("/creature", response_model=list[Creature])
def get_all() -> list[Creature]:
    return get_creatures()
