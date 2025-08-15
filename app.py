from fastapi import FastAPI, Path, Query
from typing import Optional
from pydantic import BaseModel 

app = FastAPI()

# In-memory database (dictionary) to store student data
students = {
    1: {
        "name": "John",
        "age": 18,  
        "year": "year 11"
    }
}

# Pydantic model for creating new students
class Student(BaseModel):
    name: str
    age: int
    year: str

# Pydantic model for partial updates (all fields optional)
class UpdateStudent(BaseModel):
    name: Optional[str] = None
    age: Optional[int] = None
    year: Optional[str] = None

# Root endpoint - welcome message
@app.get("/")
def index():
    return {"name": "Student API", "message": "Welcome to the Student Management API"}

# Get a specific student by ID
@app.get("/get-student/{student_id}")
def get_student(student_id: int = Path(description="The ID of the student you want to view", gt=0)):
    # Check if student exists before returning
    if student_id in students:
        return students[student_id]
    return {"error": "Student not found"}

# Get student by name (using query parameters)
@app.get("/get-by-name")
def get_student_by_name(name: str = Query(description="Name of the student to search for")):
    # Loop through all students to find matching name
    for student_id in students:
        if students[student_id]["name"] == name:
            return students[student_id]
    return {"error": "Student not found"}

# Create a new student
@app.post("/create-student/{student_id}")
def create_student(student_id: int, student: Student):
    # Check if student ID already exists
    if student_id in students:
        return {"error": "Student already exists"}
    
    # Convert Pydantic model to dictionary and store
    students[student_id] = student.dict()
    return {"message": "Student created successfully", "student": students[student_id]}

# Update an existing student (partial update)
@app.put("/update-student/{student_id}")
def update_student(student_id: int, student: UpdateStudent):
    # Check if student exists
    if student_id not in students:
        return {"error": "Student does not exist"}
    
    # Update only fields that are provided (not None)
    stored_student = students[student_id]
    
    if student.name is not None:
        stored_student["name"] = student.name
    
    if student.age is not None:
        stored_student["age"] = student.age
    
    if student.year is not None:
        stored_student["year"] = student.year
    
    return {"message": "Student updated successfully", "student": stored_student}

# Delete a student
@app.delete("/delete-student/{student_id}")
def delete_student(student_id: int):
    # Check if student exists
    if student_id not in students:
        return {"error": "Student does not exist"}
    
    # Remove student from dictionary
    deleted_student = students.pop(student_id)
    return {"message": "Student deleted successfully", "deleted_student": deleted_student}

# Get all students
@app.get("/students")
def get_all_students():
    return {"students": students, "total": len(students)}