""" 
Main file
"""

from fastapi import FastAPI
# from fastapi import FastAPI, Path

app = FastAPI()

students = [
    {"id": 1, "name": "John", "age": 17, "class": "Year 12"},
    {"id": 2, "name": "Jane", "age": 16, "class": "Year 11"},
    {"id": 3, "name": "Bob", "age": 16, "class": "Year 10"},
    {"id": 4, "name": "Alice", "age": 17, "class": "Year 11"},
    {"id": 5, "name": "David", "age": 15, "class": "Year 9"},
    {"id": 6, "name": "Emily", "age": 18, "class": "Year 12"},
]

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
async def get_student_by_name(name: str):
  """Get student by name"""
  for student in students:
    print(student)
    if student["name"] == name:
      return { "student": student }

  return { "message": "Student not found with name " + name }
