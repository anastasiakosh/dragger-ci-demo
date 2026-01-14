import string

def analyze_sentiment(text: str) -> str:
    positive_words = {'good', 'great', 'awesome', 'cool'}
    
    text = text.translate(str.maketrans('', '', string.punctuation)).lower()
    
    words = set(text.split())
    if words.intersection(positive_words):
        return "positive"
    return "neutral"
