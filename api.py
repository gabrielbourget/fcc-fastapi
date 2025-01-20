""" 
Main file
"""

from fastapi import FastAPI, Body
from pydantic import BaseModel
from typing import Optional
# from fastapi import FastAPI, Path

app = FastAPI()

class Student(BaseModel):
  """Student model"""
  id: str
  name: str
  age: int
  year: str

# import uuid

students: Student = [
    {"id": "635a067c-89fd-4de0-b481-d377aa7d75a3", "name": "John", "age": 17, "year": "Year 12"},
    {"id": "3bfde2a1-878f-4ab6-88f5-8280313eb80c", "name": "Jane", "age": 16, "year": "Year 11"},
    {"id": "d62387cd-3872-4cec-b814-95990c56ef5e", "name": "Bob", "age": 16, "year": "Year 10"},
    {"id": "58f72af7-515e-4a18-bb49-76ff1790a003", "name": "Alice", "age": 17, "year": "Year 11"},
    {"id": "3c516aa6-2556-4df7-a6db-e562d9abbe18", "name": "David", "age": 15, "year": "Year 9"},
    {"id": "08fa145d-d843-4604-890b-4e6a83980454", "name": "Emily", "age": 18, "year": "Year 12"},
]

class StudentCreate(Student):
  """Student create model"""
  id: None

  class Config:
    """Pydantic config class"""
    exclude = {"id"}

class StudentUpdate(BaseModel):
  """Student update model"""
  name: Optional[str] = None
  age: Optional[int] = None
  year: Optional[str] = None

@app.get("/")
async def root():
  """Root endpoint"""
  return {"message": "Hello World"}

@app.get("/student/{student_id}")
async def get_student(student_id: int):
  """Get student by id"""
  for student in students:
    if student["id"] == student_id:
      return { "student": student }
    return { "message": "Student not found with id " + str(student_id) }

@app.get("/student_by_name")
# async def get_student_by_name(name: str = None): -> The = None is a way to make the parameter optional 
# async def get_student_by_name(name: Optional[str]): -> Can make a parameter optional using the Optional constructor from the typing library 
async def get_student_by_name(name: str | None = None):
  """Get student by name"""
  for student in students:
    print(student)
    if student["name"] == name:
      return { "student": student }

  return { "message": "Student not found with name " + name }

@app.post("/student")
# async def create_student(student: Student = Body(..., exclude_unset={"id"})):
async def create_student(student: Student):
  """Create student"""
  for existing_student in students:
    if existing_student["id"] == student.id:
      return { "message": "Student with ID provided already exists" }

  students.append(student)
  return { "student": student, "message": "Student created successfully" }

@app.put("/student/{student_id}")
async def update_student(student_id: str, student: StudentUpdate):
  """Update student"""
  for existing_student in students:
    if existing_student["id"] == student_id:
      if student.name is not None:
        existing_student["name"] = student.name
      if student.age is not None:
        existing_student["age"] = student.age
      if student.year is not None:
        existing_student["year"] = student.year
      return { "student": existing_student, "message": "Student updated successfully" }

  return { "message": "Student with ID provided not found" }

