# create a fastapi instance and import the necessary modules
import uvicorn

# import functions from backend.py and add routes
# from backend import print_items, add_item
from backend import get_sqrt
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


@app.get("/sqrt/{number}")
def read_sqrt(number: int):
    """Endpoint to get the square root of a number."""
    print("Connecting to backend from server...")
    result = get_sqrt(number)
    return {"number": number, "sqrt": result}


@app.post("/greetings")
def create_greeting(name: str):
    """Endpoint to create a greeting message."""
    print("Creating greeting...")
    return {"message": f"Hello, {name}!"}


# Create a post route that accepts a JSON object with details: name, age and city using pydantic for validation
class UserDetails(BaseModel):
    name: str
    age: int
    city: str


@app.post("/user")
def create_user(user: UserDetails):
    """Endpoint to create a user with details."""
    print("Creating user...")
    return {"message": f"User {user.name} created successfully!", "details": user}


# @app.get("/items")
# def get_items():
#     """Endpoint to get the list of items."""
#     return {"items": print_items()}

# @app.post("/items")
# def create_item(item: str):
#     """Endpoint to add an item to the list."""
#     add_item(item)
#     return {"message": f"Item '{item}' added successfully."}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
