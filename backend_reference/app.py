import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from fastapi import FastAPI, Request

from fastapi.middleware.cors import CORSMiddleware

nltk.download('vader_lexicon')
sentiment_analyzer = SentimentIntensityAnalyzer()

app = FastAPI()

# this (along with the import) will not be included in the demo; it's just for things to work for the frontend presentation
app.add_middleware(
    CORSMiddleware,
    allow_origins=['*'],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

def get_sentiment(text):
	sentiment_score = sentiment_analyzer.polarity_scores(text)['compound']
	if sentiment_score < -0.5:
		return sentiment_score, 'negative'
	elif sentiment_score > 0.5:
		return sentiment_score, 'positive'
	return sentiment_score, 'neutral'

@app.post("/sentiment")
async def sentiment(request: Request):
	request_json = await request.json()
	text = request_json['text']
	sentiment_score, sentiment_description = get_sentiment(text)
	return {"sentiment_score": sentiment_score, "sentiment_description": sentiment_description}

# while True:
# 	print(get_sentiment(input()))