from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Book(BaseModel):
    name: str
    publisher: str
    author: str
    genre: str


this_book = [
    {
        "name": "Steve Jobs",
        "publisher": "",
        "author": "Walter Isaacson",
        "genre": "biography",
    },
    {
        "name": "Elon Musk",
        "publisher": "",
        "author": "Walter Isaacson",
        "genre": "biography",
    },
]


@app.get("/")
async def root():
    return {"message": "what's up?"}


@app.get("/books")
async def books():
    return {
        "success": True,
        "books": this_book,
    }


@app.post("/book")
async def book(book: Book):
    this_book.append(book.model_dump())
    return {"message": book}


@app.get("/search_book/{name}")
async def search_book(name):
    # result = filter(lambda x: name in x.name, this_book)
    result = [item for item in this_book if name.lower() in item["name"].lower()]
    return {"message": "successful", "books": result}
