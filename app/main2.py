# import lib

from fastapi import FastAPI, File, UploadFile
from pydantic import BaseModel
from typing import List

app = FastAPI()


# our DB
book_db = [
    {
        "title":"The C Programming",
        "price": 720
    },
    {
        "title":"Learn Python the Hard Way",
        "price": 870
    },
    {
        "title":"JavaScript: The Definitive Guide",
        "price": 1369
    },
    {
        "title":"Python for Data Analysis",
        "price": 1394
    },
    {
        "title":"Clean Code",
        "price": 1500
    },
]



class Book(BaseModel):
    title:str
    price:float




# GET Method

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/books")
async def get_books():
    return book_db

@app.get("/books/bookid={book_id}")
async def get_books(book_id:int):
    return book_db[book_id-1]







#  POST Method

@app.post("/book")
async def create_book(book:Book):
    book_db.append(book.dict())
    return book_db[-1]

# Upload file
@app.post("/img")
async def uploadbookimg(file:UploadFile=File(...)):
    size = await file.read()
    return {"file name":file.filename ,"size":len(size)}

# Upload multi files
@app.post("/multi-img")
async def uploadmultifile(files:List[UploadFile]=File(...)):
    file =[
        {
        "File name":file.filename,
        "size":len(await file.read())
        } for file in files]

    return file



# PUT Method
@app.put("/book/{book_id}")
async def edit_book(book_id:int,book:Book):
    result = book.dict()
    book_db[book_id-1].update(result)
    return result


# DELETE Method
@app.delete("/book/{book_id}")
async def delete_book(book_id:int):
    book = book_db.pop(book_id-1)
    return book