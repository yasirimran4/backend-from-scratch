from fastapi import FastAPI, HTTPException
import logging
from uuid import UUID, uuid4

app = FastAPI()

users = [
    {"id": 1, "name": "Yasir", "is_active": True},
    {"id": 2, "name": "Esam", "is_active": False},
    {"id": 3, "name": "Sumama", "is_active": True},
]


# Simple get API
# @app.get("/users")
# def get_users():
#     if len(users) < 1:
#         raise HTTPException(status_code=404, detail="No user found")
#     return {"users": users}


# Dynamic Route
@app.get("/users/{user_id}")
def get_user(user_id: int):
    user = next((u for u in users if u["id"] == user_id), None)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    return {"user": user}


# Multiple path parameter
@app.get("/add/{num_1}/{num_2}")
def add(num_1: int, num_2: int):
    return num_1 + num_2


# Query paramters


# @app.get("/users")
# def filter_user(name: str):
#     user = next(
#         (u for u in users if u["name"].lower().strip() == name.lower().strip()), None
#     )

#     if user:
#         return user

#     raise HTTPException(status_code=404, detail="User not found")


# Pagination Api


@app.get("/users/{page_no}/{limit}")
def pagination_check(page_no: int = 1, limit: int = 10):
    return page_no, limit


# Filter by is_active


@app.get("/users")
def filter_user(is_active: bool):
    filter_users = [u for u in users if u["is_active"] == is_active]

    if filter_users:
        return filter_users

    raise HTTPException(status_code=404, detail="No user found")


# Create User


@app.post("/users")
def create_user(id: int, name: str, is_active: bool = True):

    user = next((u for u in users if u["id"] == id), None)

    if user:
        raise HTTPException(status_code=400, detail="User already exist with this id")

    user = {"id": id, "name": name, "is_active": is_active}
    users.append(user)
    return user


# Update name


@app.put("/users")
def update_user(name: str, user_id: int):
    for user in users:
        if user["id"] == user_id:
            user["name"] = name
            return user

    # In case if user not updated
    raise HTTPException(status_code=400, detail="User does not exist with this id")


@app.delete("/users")
def delete_user(user_id: int):

    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return user

    # In case if user not deleted
    raise HTTPException(status_code=400, detail="User does not exist with this id")
