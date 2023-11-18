import sqlite3

def write_data_scrape(databasename, tablename, data):
    
    print('Writing Scrapped data to database')
    print('Database name: {}'.format(databasename))

    conn = sqlite3.connect(databasename)

    cursor = conn.cursor()

    print('Table name: {}'.format(tablename))

    cursor.execute('''
    DROP TABLE IF EXISTS {}'''.format(tablename))

    cursor.execute('''
    CREATE TABLE {} (
        id INTEGER PRIMARY KEY,
        social TEXT,
        posts TEXT
        )
'''.format(tablename))
    
    cursor.executemany('''INSERT INTO {} (social, posts) VALUES (?,?)'''.format(tablename), data)

    conn.commit()
    conn.close()

    print('Scrapped Data written to database')


def write_sentiment_data(databasename, tablename, data):
    print('Writing Sentiment data to database')
    print('Database name: {}'.format(databasename))

    conn = sqlite3.connect(databasename)

    cursor = conn.cursor()

    print('Table name: {}'.format(tablename))

    cursor.execute('''
    CREATE TABLE IF NOT EXISTS {} (
        id INTEGER PRIMARY KEY,
        date DATE DEFAULT CURRENT_DATE,
        total_negative INTEGER DEFAULT 0,
        total_positive INTEGER DEFAULT 0,
        facebook_negative INTEGER DEFAULT 0,
        facebook_positive INTEGER DEFAULT 0,
        twitter_negative INTEGER DEFAULT 0,
        twitter_positive INTEGER DEFAULT 0,
        reddit_negative INTEGER DEFAULT 0,
        reddit_positive INTEGER DEFAULT 0,
        quora_negative INTEGER DEFAULT 0,
        quora_positive INTEGER DEFAULT 0,
        score INTEGER DEFAULT 0
        )
'''.format(tablename))
    
    cursor.execute('''INSERT INTO {} (total_negative, total_positive, facebook_negative, facebook_positive, twitter_negative, twitter_positive, reddit_negative, reddit_positive, quora_negative, quora_positive,  score) VALUES (?,?,?,?,?,?,?,?,?,?,?)'''.format(tablename), data)

    conn.commit()

    print('Sentiment Data written to database')

# write_sentiment_data('D:/Programming1/Python/web-scraping/Social_media_monitoring/sentiment.db', 'sentiment', (1,2,3,4,5,6,7,8,9,10,11,12,13))
# write_sentiment_data('D:/Programming1/Python/web-scraping/Social_media_monitoring/sentiment.db', 'sentiment', [1*2,2*3,3*4,4*5,5*6,7,8,9,10,11,12])
# write_sentiment_data('D:/Programming1/Python/web-scraping/Social_media_monitoring/sentiment.db', 'sentiment1', [1*2,2*3,3*4,4*5,5*6,7,8,9,10,11,12])
# write_sentiment_data('D:/Programming1/Python/web-scraping/Social_media_monitoring/sentiment.db', 'sentiment1', [1*2,2*3,3*4,4*5,5*6,7,8,9,10,11,12])

    
