from fastapi import FastAPI, HTTPException, Body

app = FastAPI()

# =========================================================
# Fake Databases
# =========================================================

products = [
    {"id": 1, "name": "Laptop", "category": "electronics"},
    {"id": 2, "name": "Phone", "category": "electronics"},
    {"id": 3, "name": "Shoes", "category": "fashion"},
]

users = [
    {"id": 1, "name": "Yasir", "active": True},
    {"id": 2, "name": "Esam", "active": False},
    {"id": 3, "name": "Sumama", "active": True},
]

posts = [
    {"id": 1, "title": "FastAPI Intro", "user_id": 1},
    {"id": 2, "title": "Python Basics", "user_id": 1},
    {"id": 3, "title": "AI Future", "user_id": 2},
]

movies = [
    {"id": 1, "name": "Interstellar"},
    {"id": 2, "name": "Inception"},
]

comments = [
    {"id": 1, "post_id": 1, "text": "Amazing"},
    {"id": 2, "post_id": 1, "text": "Very helpful"},
]


# =========================================================
# 1. Basic GET API
# =========================================================

@app.get("/products")
def get_products():
    return products


# =========================================================
# 2. Path Parameter API
# =========================================================

@app.get("/products/{product_id}")
def get_product(product_id: int):

    for product in products:
        if product["id"] == product_id:
            return product

    raise HTTPException(
        status_code=404,
        detail="Product not found"
    )


# =========================================================
# 3. Multiple Path Parameters
# =========================================================

@app.get("/add/{num1}/{num2}")
def add_numbers(num1: int, num2: int):

    return {
        "result": num1 + num2
    }


# =========================================================
# 4. Query Parameter API
# =========================================================

@app.get("/users/search")
def search_user(name: str):

    for user in users:
        if user["name"].lower() == name.lower():
            return user

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )


# =========================================================
# 5. Multiple Query Parameters
# =========================================================

@app.get("/posts")
def get_posts(limit: int = 10, page: int = 1):

    return {
        "limit": limit,
        "page": page,
        "posts": posts
    }


# =========================================================
# 6. Optional Query Parameters
# =========================================================

@app.get("/filter-products")
def filter_products(category: str = None):

    if category:
        filtered = [
            product
            for product in products
            if product["category"] == category
        ]

        return filtered

    return products


# =========================================================
# 7. Boolean Query Parameter
# =========================================================

@app.get("/active-users")
def get_active_users(is_active: bool):

    filtered = [
        user
        for user in users
        if user["active"] == is_active
    ]

    return filtered


# =========================================================
# 8. Mixed Path + Query Params
# =========================================================

@app.get("/users/{user_id}/posts")
def get_user_posts(user_id: int, limit: int = 5):

    user_posts = [
        post
        for post in posts
        if post["user_id"] == user_id
    ]

    return user_posts[:limit]


# =========================================================
# 9. POST API
# =========================================================

@app.post("/users")
def create_user(data = Body()):

    new_user = {
        "id": len(users) + 1,
        "name": data["name"],
        "active": True
    }

    users.append(new_user)

    return {
        "message": "User created",
        "user": new_user
    }


# =========================================================
# 10. PUT API
# =========================================================

@app.put("/users/{user_id}")
def update_user(user_id: int, data = Body()):

    for user in users:

        if user["id"] == user_id:

            user["name"] = data["name"]

            return {
                "message": "User updated",
                "user": user
            }

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )


# =========================================================
# 11. DELETE API
# =========================================================

@app.delete("/users/{user_id}")
def delete_user(user_id: int):

    for user in users:

        if user["id"] == user_id:

            users.remove(user)

            return {
                "message": "User deleted"
            }

    raise HTTPException(
        status_code=404,
        detail="User not found"
    )


# =========================================================
# 12. Sort Products API
# =========================================================

@app.get("/sorted-products")
def sorted_products(sort: str = "asc"):

    sorted_list = sorted(
        products,
        key=lambda product: product["name"]
    )

    if sort == "desc":
        sorted_list.reverse()

    return sorted_list


# =========================================================
# 13. Login API
# =========================================================

@app.post("/login")
def login(data = Body()):

    username = data["username"]
    password = data["password"]

    if username == "yasir" and password == "123":

        return {
            "message": "Login successful"
        }

    raise HTTPException(
        status_code=401,
        detail="Invalid credentials"
    )


# =========================================================
# 14. Chatbot API
# =========================================================

@app.post("/chat")
def chatbot(data = Body()):

    user_message = data["message"]

    return {
        "user": user_message,
        "assistant": f"AI says: You said '{user_message}'"
    }


# =========================================================
# 15. Nested Route Practice
# =========================================================

@app.get("/posts/{post_id}/comments")
def get_comments(post_id: int):

    post_comments = [
        comment
        for comment in comments
        if comment["post_id"] == post_id
    ]

    return post_comments


# =========================================================
# MOVIES CHALLENGE SOLUTIONS
# =========================================================

# Get all movies
@app.get("/movies")
def get_movies():
    return movies


# Get single movie
@app.get("/movies/{movie_id}")
def get_movie(movie_id: int):

    for movie in movies:
        if movie["id"] == movie_id:
            return movie

    raise HTTPException(
        status_code=404,
        detail="Movie not found"
    )


# Create movie
@app.post("/movies")
def create_movie(data = Body()):

    movie = {
        "id": len(movies) + 1,
        "name": data["name"]
    }

    movies.append(movie)

    return {
        "message": "Movie created",
        "movie": movie
    }


# Delete movie
@app.delete("/movies/{movie_id}")
def delete_movie(movie_id: int):

    for movie in movies:

        if movie["id"] == movie_id:

            movies.remove(movie)

            return {
                "message": "Movie deleted"
            }

    raise HTTPException(
        status_code=404,
        detail="Movie not found"
    )


# Search movie
@app.get("/movies/search")
def search_movie(name: str):

    for movie in movies:

        if movie["name"].lower() == name.lower():
            return movie

    raise HTTPException(
        status_code=404,
        detail="Movie not found"
    )


# Student courses
@app.get("/students/{student_id}/courses")
def student_courses(student_id: int):

    return {
        "student_id": student_id,
        "courses": [
            "Python",
            "FastAPI",
            "Databases"
        ]
    }