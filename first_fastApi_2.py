from fastapi import FastAPI, Path, Query
from typing import Optional
from pydantic import BaseModel

app = FastAPI()

class Itemi(BaseModel):
    Denumire: str
    Pret: float
    Producator: Optional[str] = None

@app.get("/")
def home():
    return {"Data":"Test homepage"}

@app.get("/about")
def about():
    return {"Data":"Despre..."}

inventory = {
    1:{
        "Denumire":"Lapte",
        "Pret":5.89,
        "Producator":"ZuZu"
    },
    2:{
        "Denumire":"Oua",
        "Pret":2.4,
        "Producator":"Agrosol"
    }
}

@app.get("/get-item/{produs_id}")
def get_item(produs_id: int=Path(None, description="The Id of the product you want to look-up.",gt=0)):
    return inventory[produs_id]

@app.get("/get-by-name")
def get_item(Denumire: str = Query(None, title="Denumire", description="name of product",max_length=10, min_length=2)):     
    for produs_id in inventory:
        if inventory[produs_id].Denumire == Denumire:
            return inventory[produs_id]
    return {"Data":"Not found"}

@app.post("/create-item/{produs_id}")
def create_item(produs_id:int, item: Itemi):
    if produs_id in inventory:
        return {"Error":"Produs_id already exists"}
    inventory[produs_id]=item
    return inventory[produs_id]