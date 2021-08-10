import spacy
from nltk.stem import WordNetLemmatizer
import gensim
import re
import nltk


def count_sentiment(spacy_text_blob):
    '''
    This function uses spacytextblob sentiment analysis to get a count of the number of positive or negative posts.
    Note: We use the adage 'no news is good news' So neutral posts are considered positive.
    :param spacy_text_blob: a spacy nlp object that has been through a pipe with spacytextblob
    :return: count of positive and negative mentions
    '''
    positive = 0
    negative = 0
    for post in spacy_text_blob:
        if post._.polarity >= 0:
            positive += 1
        else:
            negative += 1
    return positive, negative


def apply_spacy_pipe(text_list):
    '''
    @param text_list: since nlp.pipe() works best with large amounts of data,
    it is best to use list of large amounts of text.
    @return returns a Doc object from spacy pipeline
    '''
    nlp = spacy.load("en_core_web_sm")
    nlp.add_pipe('spacytextblob')
    return nlp.pipe(text_list)


def get_topics(text_list):
    '''
    This function takes a list of different strings (posts) and finds the 10 topics that most
    represent the posts as a whole. 
    :param text_list: list of posts to be considered
    :return: List of 10 topics for the given text_list
    '''
    nlp = spacy.load("en_core_web_sm")
    doc_list = []
    for doc in text_list:
        doc = preprocess(doc)
        doc = nlp(doc)
        doc_list.append([word.text for word in doc if not word.is_stop])
    words = gensim.corpora.Dictionary(doc_list)
    flat_list = [word for doc in doc_list for word in doc]
    corpus = [words.doc2bow(flat_list)]
    lda_model = gensim.models.ldamodel.LdaModel(corpus=corpus, id2word=words, num_topics=100, random_state=2, update_every=1, passes=10, alpha='auto', per_word_topics=True)

    return [topic[0] for topic in lda_model.show_topics(num_topics=10, formatted=False)[0][1]]


def preprocess(s):
    '''
    This get's rid of websites, emoji, and punctuation
    :param s:
    :return:
    '''
    s = s.lower()
    re_url = re.compile(
        re.compile(r'(https?:\/\/[www\.]?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-z]{2,6}\b[-a-zA-Z0-9@:%_\+.~#?&//=]*)'))
    re_hashtag = re.compile(r'\B#\w*[a-zA-Z]+\w*')
    re_at = re.compile(r'\B@\w*[a-z0-9]+\w*')
    re_emoji = re.compile(r'[\U00010000-\U0010ffff]', flags=re.UNICODE)
    re_punc = re.compile(r'\W+')
    s = re.sub(re_url, '', s)
    s = re.sub(re_hashtag, '', s)
    s = re.sub(re_at, '', s)
    s = re.sub(re_emoji, '', s)
    s = re.sub(re_punc, ' ', s)

    s = re.sub(r'\d+', '', s)
    t = nltk.word_tokenize(s)
    stems = [WordNetLemmatizer().lemmatize(x) for x in t]
    stems = [x for x in stems if x not in ['rt', 'http'] and len(x) > 1]
    return " ".join(stems)
