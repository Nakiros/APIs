from fastapi import FastAPI
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
def get_item(produs_id: int):
    return inventory[produs_id]