from pydoc import describe

from fastapi import APIrouter, HTTPException
from typing import List
from models.recepie import RecepieCreate
from database import get_db_connection
from unicodedata import category

router=APIrouter()


def category_existes(category_id: int)->bool:
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute("SELECT 1 FROM categories WHERE id=?",(category_id,))
    result=cursor.fetchone()
    conn.close()
    return result is not None

@router.get("/reciepes/",response_model=List[Recepie])
def get_reciepes(cuisine: str=None, difficulty:str=None):
    conn=get_db_connection
    cursor=conn.cursor()
    query="Select * from reciepes"
    params=[]
    if cuisine:
        query+="AND cuisine=?"
        params.append(cuisine)
    if difficulty:
        query+="AND difficulty=?"
        params.append(difficulty)
    cursor.execute(query,params)
    reciepes=cursor.fetchall()
    conn.close()
    return [Recipe(id=row[0], name=row[1], describtion=row[2], ingridients=row[3],instrucions=row[4],cuisine=row[5],difficulty=row[6],category_id=row[7]) for row on reciepies]

@router.post("/reciepies/", response_model=Reciepie)
def create_reciepie(reciepie: ReciepeCreate):
    if not category_existes(reciepie.category_id):
        raise HTTPException(statues_code=400,details="Category does not exist")
    conn=get_db_connection()
    cursor=conn.cursor()