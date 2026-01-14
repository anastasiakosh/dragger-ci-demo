from fastapi import FastAPI
from app.utils import analyze_sentiment

app = FastAPI()

@app.get("/")
def read_root():
    return {"status": "ok", "service": "TextAnalyzer AI"}

@app.post("/analyze")
def analyze(text: str):
    sentiment = analyze_sentiment(text)
    return {
        "text": text,
        "sentiment": sentiment,
        "word_count": len(text.split())
    }
