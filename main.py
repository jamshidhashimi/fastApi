from typing import Union
from fastapi import FastAPI

app = FastAPI()

#For query parameters
student = {'id': 1, 'name': 'Jean', 'age': 25, 'year': '3'}

@app.get("/")
async def root():
    return {"message": "Hello World"}

#Path parameter example
@app.get("/items/{item_id}")
async def read_item(item_id: int):
    return {"item_id", item_id}

#Declaring type for validation
@app.get("/books/{book_id}")
async def read_item(book_id: int):
    return {"book_id": book_id}


#Query parameters
@app.get("/students/")
async def get_students(id: int, name: Union[str, None] = None):
    
    if id and name and student.get('id') == id and student.get('name') == name:
        return student
    
    if student.get('id') == id:
        return student

    if student.get('name') == name:
        return student
    
    return {"message": "Data not found"}