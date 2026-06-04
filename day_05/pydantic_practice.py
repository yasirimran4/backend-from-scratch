from pydantic import BaseModel, Field, EmailStr
from fastapi import FastAPI


class User(BaseModel):
    username: str
    password: str
    age: int


app = FastAPI()

users = []

# Create User
@app.post("/users")
def create_user(user: User):
    users.append(user)
    return users


@app.get("/users")
def users():
    return users
