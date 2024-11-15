from itertools import product

from fastapi import FastAPI
from model import Developer,Project

app=FastAPI()

@app.post("/developer/")
def create_developer(dev:Developer):
    return {"Message":"Developer created","developer":dev}

@app.post("/projects/")
def create_developer(projekti:Product):
    return {"Message":"Developer created","developer":projekti}

@app.get("/projekt/")
def get_projects():
    shembullProjekt=Projekt(
    title="Sample",
    description="this is ......",
    languages=["PHP","JS"],
    lead_developer=Developer(name="Fat",experience=2)
    )
    return {"projects":[shembullProjekt]}