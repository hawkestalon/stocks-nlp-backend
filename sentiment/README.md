Repository for Web Scraping component of CS-5890 group project.

# Installation
In the root directory run the following command to install all dependencies.
It is recommended to do this in a python virtual environment or conda
environment. This will walk you through the built in python `venv`.

Create the environment inside the root of the application:

`python -m venv .venv`

Activate the newly created environment with:

`source .venv/bin/activate`

Your shell should now have some indication of the environment that you
are in. You are ready to move forward with installation.

`pip install -r requirements.txt`

## Setup
SpaCy requires the following additional command for the code to work. 
This code downloads one of the models from SpaCy. We have selected to
use their faster model. See SpaCy documentation for more details.

`python -m spacy download en_core_web_sm`

# Using main.py
The main script is expecting stock tickers separated by commas as
the first argument to main.py. If they arguments are not comma separated
like the example below, it will not work.

Ex:
`python main.py GME,GE,AAPL`

The above script will scrape subreddits as configured in the pipeline
and then do sentiment and topic anaysis on them. The returned data is
written to the data directory like so:
```
data
├── AAPL.json
├── GE.json
└── GME.json
```
Each time a ticker symbol has analysis done on it, it will overwrite
this file. The data structure is json that looks like this:
```
{"ticker": "GME",
 "positive": 29,
 "negative": 2,
 "topics": ["stock", "market", "price", "ha", "company", "ford", "gme", "share", "amc", "short"]
}
```
# Getting Reddit Content

The [scraper](./stocks-web-scraper/scraper.py) module provides two functions for getting Reddit content.

## Submissions

You can get the submissions of specified subreddits via the `get_submissions` function. This function accepts a list
of subreddit names. Each element of the list is the name only—do not include an `/r` prefix. The result will be a
`pandas.DataFrame` with the following columns:

* `id`
  * **Type:** string
  * The ID of the submission
* `created`
  * **Type:** float
  * The UTC timestamp of when the submission was created
* `subreddit`
  * **Type:** string
  * The subreddit to which the submission was posted
* `title`
  * **Type:** string
  * The title of the submission  
* `content`
  * **Type:** string
  * The body content of the submission; may be empty (e.g. image-only post)
  
For each subreddit in the list argument, the `get_submissions` function attempts to grab up to 1000 of the newest
submissions.
    
### Example

```python
df_submissions = get_submissions(['wallstreetbets', 'stocks'])
print(df_submissions.head())
```
    
## Comments

You can get a number of **top-level** comments from a submission via the `get_comments` function. This function accepts
a submission ID and the maximum number of comments to return (default of `10` comments). The result will be a
`pandas.DataFrame` with the following columns:

* `id`
  * **Type:** string
  * The ID of the comment
* `created`
  * **Type:** float
  * The UTC timestamp of when the comment was posted
* `content`
  * **Type:** string
  * The body content of the comment
  
### Example

```python
df_submissions = get_submissions(['wallstreetbets'])
submission_id = df_submissions.iloc[0].id

df_comments = get_comments(submission_id)
print(df_comments.head())
```


