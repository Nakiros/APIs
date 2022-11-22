from fastapi import FastAPI, Path
from typing import Optional
app = FastAPI()

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
def get_item(produs_id: int=Path(None, description="The Id of the product you want to look-up.",gt=0, lt=3)):
    return inventory[produs_id]

@app.get("/get-by-name")
def get_item(Denumire_n: Optional[str] = None):                       #parameter is optional
    for produs_id in inventory:
        if inventory[produs_id]["Denumire"] == Denumire_n:
            return inventory[produs_id]
    return {"Data":"Not found"}