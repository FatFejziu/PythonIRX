from fastapi import FastAPI

app=FastAPI()

@app.get("/")
def root():
    return {"message":"Hello World!!!"}

@app.get("/greet/")
def greet(name:str):
    return {"message":f"Hello {name}"}

@app.get("/items/{item_id")
def read_item(item_id:int):
    return {"item_id":item_id}

@app.post("/items")
def vreate_item(name:str,price:float):
    return {"item":name, "item_price":price}

@app.put("/items/{item_id}")
def update_item(item_id:int, name:str, price:float):
    return{"message":f"Item is updated"}

@app.delete("/items/{item_id}")
def delete_item(item_id:int):
    # ketu bejne fshirjen nga databaza
    return {"message":"The iem is deleted"}