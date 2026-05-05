import mysql.connector
from mysql.connector import Error

def get_db_connection():
    try:
        connection = mysql.connector.connect(
            host='localhost',
            user='root',        
            password='SoftwareEng', 
            database='bangla_sentiment_pro'
        )
        return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None

def save_to_db(text, sentiment, emotion):
    conn = get_db_connection()
    if conn:
        cursor = conn.cursor()
        query = "INSERT INTO predictions (text_content, sentiment, emotion) VALUES (%s, %s, %s)"
        cursor.execute(query, (text, sentiment, emotion))
        conn.commit()
        cursor.close()
        conn.close()

def get_analytics_data():
    conn = get_db_connection()
    if conn:
        import pandas as pd
        query = "SELECT sentiment, emotion, created_at FROM predictions"
        df = pd.read_sql(query, conn)
        conn.close()
        return df
    return None