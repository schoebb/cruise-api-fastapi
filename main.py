from fastapi import FastAPI
from typing import List, Dict
import random
from datetime import datetime, timedelta

from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins (change this for security)
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)



# Sample Data
cruise_companies = ["Royal Caribbean", "Carnival", "Norwegian", "Disney", "MSC"]
destinations = ["Bahamas", "Caribbean", "Mediterranean", "Alaska", "Dubai"]
ports = [
    ["Nassau", "Cococay", "Key West"],
    ["Jamaica", "Cayman Islands", "Cozumel"],
    ["Santorini", "Mykonos", "Athens"],
    ["Juneau", "Skagway", "Ketchikan"],
    ["Abu Dhabi", "Muscat", "Doha"]
]

# Function to generate cruise data
def generate_cruise():
    company = random.choice(cruise_companies)
    departure_date = datetime.today() + timedelta(days=random.randint(10, 300))
    duration = random.randint(3, 14)  # Cruise duration in days
    destination = random.choice(destinations)
    stops = random.choice(ports)
    prices = {
        "economy": round(random.uniform(300, 1000), 2),
        "business": round(random.uniform(1500, 5000), 2),
        "luxury": round(random.uniform(6000, 15000), 2)
    }
    
    return {
        "cruise_company": company,
        "departure_date": departure_date.strftime('%Y-%m-%d'),
        "duration": duration,
        "destination": destination,
        "stopping_points": stops,
        "prices": prices
    }

@app.get("/")
def home():
    return {"message": "Welcome to the Cruise API!"}

@app.get("/cruises")
def get_cruises():
    cruises = [generate_cruise() for _ in range(10)]
    return {"cruises": cruises}
