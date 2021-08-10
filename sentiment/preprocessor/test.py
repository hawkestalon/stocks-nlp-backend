import sys
sys.path.append('../stocks_web_scraper')
import pandas as pd
from Preprocessor import remove_duplicates, create_text_list, apply_spacy_pipe
from scraper import query_new_reddit_posts

posts = query_new_reddit_posts(['wallstreetbets'])

posts = remove_duplicates(posts, 'content')

stock_text_list = create_text_list(posts, 'content')

doc = list(apply_spacy_pipe(stock_text_list))

for d in doc:
    print(f"Entities: {d.ents}\n\n\n")
    print(f"Polarity: {d._.polarity}")
    print(f"Subjectivity: {d._.subjectivity}")
    print(f"Assessments: {d._.assessments}")
    print('\n\n\n')
