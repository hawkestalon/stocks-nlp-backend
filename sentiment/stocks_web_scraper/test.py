from scraper import get_submissions, get_comments

if __name__ == '__main__':
    df_submissions = get_submissions(['wallstreetbets'])
    print("SUBMISSIONS")
    print(df_submissions.head())

    print()

    submission_id = df_submissions.iloc[0].id
    df_comments = get_comments(submission_id)
    print("COMMENTS OF NEWEST SUBMISSION")
    print(df_comments.head())
