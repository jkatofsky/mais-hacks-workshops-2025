import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from fastapi import FastAPI, Request

nltk.download('vader_lexicon')
sentiment_analyzer = SentimentIntensityAnalyzer()

app = FastAPI()

def get_sentiment(text):
	sentiment = sentiment_analyzer.polarity_scores(text)['compound']
	if sentiment < -0.5:
		return sentiment, 'negative'
	elif sentiment > 0.5:
		return sentiment, 'positive'
	return sentiment, 'neutral'

@app.post("/sentiment")
async def sentiment(request: Request):
	request_json = await request.json()
	text = request_json['text']
	sentiment, sentiment_description = get_sentiment(text)
	return {"sentiment": sentiment, "sentiment_description": sentiment_description}

# while True:
# 	print(get_sentiment(input()))