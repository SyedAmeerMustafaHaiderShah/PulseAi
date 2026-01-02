import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

class Database:
    def __init__(self):
        # Using the exact same settings that passed your test
        self.config = {
            'host': '127.0.0.1',
            'user': 'root',
            'password': 'haidershah962', # <--- Put the password that worked here
        }
        self.db_name = "pulse_ai_db"
        self.initialize_db()

    def get_connection(self):
        return mysql.connector.connect(
            **self.config,
            database=self.db_name
        )

    def initialize_db(self):
        """Creates the DB and Table if they don't exist."""
        try:
            # 1. Connect to the MySQL server
            conn = mysql.connector.connect(**self.config)
            cursor = conn.cursor()
            
            # 2. Create the Database
            cursor.execute(f"CREATE DATABASE IF NOT EXISTS {self.db_name}")
            cursor.execute(f"USE {self.db_name}")
            
            # 3. Create the Table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS mood_logs (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    persona_name VARCHAR(100),
                    mood_label VARCHAR(50),
                    negativity_ratio INT,
                    positivity_ratio INT,
                    user_text TEXT,
                    ai_response TEXT,
                    timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            conn.commit()
            cursor.close()
            conn.close()
            print("✅ MySQL Database & Table initialized successfully.")
        except Exception as e:
            print(f"❌ Database Init Error: {e}")

    def save_chat_log(self, data):
        """Saves a full AI interaction linked to a specific user in MySQL."""
        try:
            conn = self.get_connection()
            cursor = conn.cursor()
            
            # Updated query with 7 columns and 7 placeholders (%s)
            query = """INSERT INTO mood_logs 
                       (user_id, persona_name, mood_label, negativity_ratio, positivity_ratio, user_text, ai_response) 
                       VALUES (%s, %s, %s, %s, %s, %s, %s)"""
            
            # Updated values tuple to include user_id as the first item
            values = (
                data.get('user_id'), # Captured from the login session
                data['persona'],
                data['mood'],
                data['neg_ratio'],
                data['pos_ratio'],
                data.get('user_text', 'No text provided'),
                data['ai_response']
            )
            
            cursor.execute(query, values)
            conn.commit()
            print(f"💾 Interaction saved to MySQL for User ID: {data.get('user_id')}!")
            
            cursor.close()
            conn.close()
        except Exception as e:
            print(f"❌ Error saving to MySQL: {e}")