from urlextract import URLExtract
from wordcloud import WordCloud
import pandas as pd
from collections import Counter
import emoji
from textblob import TextBlob
from sklearn.feature_extraction.text import CountVectorizer
from textblob import TextBlob
import networkx as nx

extract = URLExtract()

def fetch_stats(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    num_messages = df.shape[0]
    words = []
    for message in df['message']:
        words.extend(message.split())

    num_media_messages = df[df['message'] == '<Media omitted>\n'].shape[0]

    links = []
    for message in df['message']:
        links.extend(extract.find_urls(message))

    return num_messages, len(words), num_media_messages, len(links)

def most_busy_users(df):
    x = df['user'].value_counts().head()
    df = round((df['user'].value_counts() / df.shape[0]) * 100, 2).reset_index().rename(columns={'index': 'name', 'user': 'percent'})
    return x, df

def create_wordcloud(selected_user, df):
    with open('stop_hinglish.txt', 'r') as f:
        stop_words = f.read()

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']

    def remove_stop_words(message):
        y = []
        for word in message.lower().split():
            if word not in stop_words:
                y.append(word)
        return " ".join(y)

    wc = WordCloud(width=500, height=500, min_font_size=10, background_color='white')
    temp['message'] = temp['message'].apply(remove_stop_words)
    df_wc = wc.generate(temp['message'].str.cat(sep=" "))
    return df_wc

def most_common_words(selected_user, df):
    with open('stop_hinglish.txt', 'r') as f:
        stop_words = f.read()

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']

    words = []

    for message in temp['message']:
        for word in message.lower().split():
            if word not in stop_words:
                words.append(word)

    most_common_df = pd.DataFrame(Counter(words).most_common(20))
    return most_common_df

def emoji_helper(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    emojis = []
    for message in df['message']:
        emojis.extend([c for c in message if emoji.is_emoji(c)])

    emoji_df = pd.DataFrame(Counter(emojis).most_common(len(Counter(emojis))))
    return emoji_df

def monthly_timeline(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    timeline = df.groupby(['year', 'month_num', 'month']).count()['message'].reset_index()

    time = []
    for i in range(timeline.shape[0]):
        time.append(timeline['month'][i] + "-" + str(timeline['year'][i]))

    timeline['time'] = time
    return timeline

def daily_timeline(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    daily_timeline = df.groupby('only_date').count()['message'].reset_index()
    return daily_timeline

def week_activity_map(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['day_name'].value_counts()

def month_activity_map(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    return df['month'].value_counts()

def activity_heatmap(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    user_heatmap = df.pivot_table(index='day_name', columns='period', values='message', aggfunc='count').fillna(0)
    return user_heatmap


def sentiment_analysis(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    sentiments = df['message'].apply(lambda x: TextBlob(x).sentiment.polarity)
    df['sentiment'] = sentiments
    return df

def response_time_analysis(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    df['previous_date'] = df['date'].shift(1)
    df['response_time'] = (df['date'] - df['previous_date']).dt.total_seconds() / 60
    avg_response_time = df['response_time'].mean()
    return avg_response_time

def hourly_activity(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    hourly_activity = df.groupby('hour').count()['message'].reset_index()
    return hourly_activity

def message_length_analysis(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    df['message_length'] = df['message'].apply(len)
    avg_message_length = df['message_length'].mean()
    return avg_message_length

def hashtag_analysis(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    hashtags = df['message'].apply(lambda x: [word for word in x.split() if word.startswith('#')])
    hashtags = [item for sublist in hashtags for item in sublist]
    hashtag_df = pd.DataFrame(Counter(hashtags).most_common(20))
    return hashtag_df

def mention_analysis(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    mentions = df['message'].apply(lambda x: [word for word in x.split() if word.startswith('@')])
    mentions = [item for sublist in mentions for item in sublist]
    mention_df = pd.DataFrame(Counter(mentions).most_common(20))
    return mention_df

def conversation_starters(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    conversation_starters = df['user'].shift(1) != df['user']
    df['is_conversation_starter'] = conversation_starters
    starters = df[df['is_conversation_starter']]['user'].value_counts().reset_index()
    return starters

def day_vs_night_activity(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    df['period'] = df['hour'].apply(lambda x: 'Day' if 6 <= x < 18 else 'Night')
    period_counts = df['period'].value_counts()
    return period_counts

def weekly_activity(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    df['week'] = df['date'].dt.strftime('%Y-%U')
    weekly_counts = df['week'].value_counts().sort_index()
    return weekly_counts

def user_interaction_network(df):
    from collections import defaultdict
    import networkx as nx

    interactions = defaultdict(int)
    for i in range(1, len(df)):
        user = df.iloc[i]['user']
        prev_user = df.iloc[i-1]['user']
        if user != prev_user:
            interactions[(user, prev_user)] += 1
            interactions[(prev_user, user)] += 1

    G = nx.Graph()
    for (user1, user2), count in interactions.items():
        G.add_edge(user1, user2, weight=count)

    return G

def message_type_analysis(df):
    media_types = df['message'].apply(lambda x: 'Media' if '<Media omitted>' in x else 'Text')
    media_counts = media_types.value_counts()
    return media_counts

def streak_analysis(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    streaks = []
    current_streak = 1
    for i in range(1, len(df)):
        if df.iloc[i]['user'] == df.iloc[i-1]['user']:
            current_streak += 1
        else:
            streaks.append(current_streak)
            current_streak = 1
    streaks.append(current_streak)
    longest_streak = max(streaks)
    return longest_streak

def top_ngrams(selected_user, df, n=2):
    from sklearn.feature_extraction.text import CountVectorizer

    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    temp = df[df['user'] != 'group_notification']
    temp = temp[temp['message'] != '<Media omitted>\n']

    vectorizer = CountVectorizer(ngram_range=(n, n), stop_words='english')
    ngrams = vectorizer.fit_transform(temp['message'])
    sum_ngrams = ngrams.sum(axis=0)
    ngrams_freq = [(word, sum_ngrams[0, idx]) for word, idx in vectorizer.vocabulary_.items()]
    ngrams_freq = sorted(ngrams_freq, key=lambda x: x[1], reverse=True)
    return pd.DataFrame(ngrams_freq[:20], columns=['Ngram', 'Frequency'])

def sentiment_over_time(selected_user, df):
    if selected_user != 'Overall':
        df = df[df['user'] == selected_user]

    df['sentiment'] = df['message'].apply(lambda x: TextBlob(x).sentiment.polarity)
    sentiment_timeline = df.groupby('only_date')['sentiment'].mean().reset_index()
    return sentiment_timeline
