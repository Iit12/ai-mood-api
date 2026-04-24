from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import random

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/analyze")
def analyze_mood(text: str = ""):
    # A simple logic for our practice project
    positive_words = ["good", "happy", "great", "love", "amazing"]
    negative_words = ["bad", "sad", "angry", "hate", "terrible"]
    
    text = text.lower()
    if any(word in text for word in positive_words):
        return {"mood": "Happy", "color": "#10b981"}
    elif any(word in text for word in negative_words):
        return {"mood": "Sad", "color": "#ef4444"}
    else:
        return {"mood": "Neutral", "color": "#64748b"}
