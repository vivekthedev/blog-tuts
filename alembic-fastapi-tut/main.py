from fastapi import Depends, FastAPI
from sqlalchemy.orm import Session
from starlette.responses import RedirectResponse

import models
from database import SessionLocal, engine
from schema import CreateBook

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


def get_db():
    try:
        db = SessionLocal()
        yield db
    finally:
        db.close()


@app.get("/")
async def index(db: Session = Depends(get_db)):
    books = db.query(models.Books).all()
    return books


@app.post("/")
async def create_book(book: CreateBook, db: Session = Depends(get_db)):
    book_model = models.Books()
    book_model.title = book.title
    book_model.price = book.price
    book_model.author = book.author
    book_model.rating = book.rating
    book_model.published = book.published
    book_model.description = book.description

    db.add(book_model)
    db.commit()

    return book


@app.get("/{id}")
async def get_book_by_id(id: int, db: Session = Depends(get_db)):
    book_model = db.query(models.Books).filter(models.Books.id == id).first()
    return book_model


@app.put("/{id}")
async def modify_book_by_id(id: int, book: CreateBook, db: Session = Depends(get_db)):
    book_model = db.query(models.Books).filter(models.Books.id == id).first()
    book_model.title = book.title
    book_model.price = book.price
    book_model.author = book.author
    book_model.rating = book.rating
    book_model.published = book.published

    db.add(todo_model)
    db.commit()
    return book_model


@app.delete("/{id}")
async def delete_book_by_id(id: int, db: Session = Depends(get_db)):
    book_model = db.query(models.Books).filter(models.Books.id == id).delte()
    return RedirectResponse(url="/", status_code=200)
