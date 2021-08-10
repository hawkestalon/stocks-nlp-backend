import sys
import json
sys.path.append("sentiment/preprocessor")
sys.path.append("sentiment/nlp")
sys.path.append("sentiment/stocks_web_scraper")
from scraper import get_submissions
from Preprocessor import remove_duplicates, create_text_list, filter_by_ticker
from sentiment import apply_spacy_pipe, count_sentiment, get_topics

if len(sys.argv) <= 1:
    print("This program requires a list of comma separated stock tickers with no spaces.\n")
else:
    stocksDF = get_submissions(["wallstreetbets", "stocks", "investing"])
    stocksDF = remove_duplicates(stocksDF, 'content')
    stocks_posts_list = create_text_list(stocksDF, 'content')

    print(sys.argv)

    # for each stock ticker, create a filtered list and then send it for sentiment analysis
    for ticker in sys.argv[1].split(','):
        filtered_by_ticker = filter_by_ticker(stocks_posts_list, ticker)
        count = count_sentiment(apply_spacy_pipe(filtered_by_ticker))
        topics = get_topics(filtered_by_ticker)
        print(ticker)
        print(f"positive: {count[0]}, negative: {count[1]}")
        print(topics)

        # create the dictionary
        data = {"ticker": ticker, "positive": count[0], "negative": count[1], "topics": topics}
        with open(f"./sentiment/data/{ticker}.json", "w") as file:
            json.dump(data, file)