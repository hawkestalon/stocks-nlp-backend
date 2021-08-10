import pandas as pd
import praw


def get_submissions(subreddits):
    """
    Queries up to 1000 of the newest Reddit posts from each of the given subreddits.

    :param subreddits: list of subreddits to query (name only, no "/r" prefix)
    :return: a pandas.DataFrame where each row is the ID, created UTC timestamp, subreddit, title, and content of a post
    """
    reddit = __get_reddit()

    dicts = []
    for subreddit in subreddits:
        for submission in reddit.subreddit(subreddit).new(limit=1000):
            data = {
                'id': submission.id,
                'created': submission.created_utc,
                'subreddit': subreddit,
                'title': submission.title,
                'content': submission.selftext
            }
            dicts.append(data)
    return pd.DataFrame(dicts)


def get_comments(submission_id, limit=10):
    """
    Gets up to "limit" number of top-level comments from the given submission.

    :param submission_id: the ID of the submission to get the comments of
    :param limit: the maximum number of comments to return
    :return: a pandas.DataFrame where each row is the ID, created UTC timestamp, and content of a comment
    """
    reddit = __get_reddit()
    submission = reddit.submission(submission_id)

    dicts = []
    for comment in submission.comments:
        data = {
            'id': comment.id,
            'created': comment.created_utc,
            'content': comment.body
        }
        dicts.append(data)
        if len(dicts) >= limit:
            break
    return pd.DataFrame(dicts)


def __get_reddit():
    """
    :return: A praw.Reddit instance
    """
    return praw.Reddit(
        client_id='OY2muK7IvmbFLNEDy1j1Yw',
        client_secret='VpVqqGUHafEehju-chjZr7DGQGxLXQ',
        user_agent='stocks_web_scraper',
    )
