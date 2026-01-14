def analyze_sentiment(text: str) -> str:
    positive_words = {'good', 'great', 'awesome', 'cool'}
    words = set(text.lower().split())
    if words.intersection(positive_words):
        return "positive"
    return "neutral"
