from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import requests

app = FastAPI()

# This allows your HTML file to talk to your Python code
app.add_middleware(CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"])

API_KEY = "6a60644f04b34afeb917b5a7e0df5149"

@app.get("/find-recipes")
def find_recipes(ingredients: str = ""):
    # This URL asks Spoonacular for recipes based on ingredients
    url = f"https://api.spoonacular.com/recipes/findByIngredients?ingredients={ingredients}&number=5&apiKey={API_KEY}"
    response = requests.get(url)
    return response.json()
