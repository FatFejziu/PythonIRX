from fastapi import FastAPI
from ProjektiFinal.auth import authors, bookd, api_key
from database import create_database
from auth.security import get_api_key

app=FastAPI(
    title="Book managment system",
    description="An API from managing book, authors and genres",
    version="1.0.0"
)
@app.on_event("startup")
def start_event():
    create_database()
app.include_router(authors.router, prefix="/api/authors", tags=["Authors"])
app.include_router(book.router, prefix="/api/books", tags=["Books"])
app.include_router(api_key.router,prefix="/api/validate_key")

@app.on_event("startup")
def startup():
    # Initialize the database tables
    create_database()