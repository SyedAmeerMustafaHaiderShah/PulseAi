import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv()

def test_mysql():
    print("🔍 Testing MySQL Connection...")
    config = {
        'host': '127.0.0.1',
        'user': 'root',
        'password': 'haidershah962' # Put your password here directly to test
    }
    
    try:
        conn = mysql.connector.connect(**config)
        print("✅ SUCCESS: Connected to MySQL Server!")
        conn.close()
    except mysql.connector.Error as err:
        print(f"❌ MYSQL ERROR: {err}")
        print(f"Error Code: {err.errno}")

test_mysql()