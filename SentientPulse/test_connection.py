# test_connection.py
import os
from backend.database.database import Database
from dotenv import load_dotenv

# Load it here too, just to be safe
load_dotenv()

print("--- Connection Diagnostic ---")
print(f"Current Working Directory: {os.getcwd()}")
print(f"MONGO_URI found: {'Yes' if os.getenv('MONGO_URI') else 'No'}")

db_instance = Database()
if db_instance.connect():
    print("🚀 TARGET REACHED: Atlas is live!")
else:
    print("❌ Failed. Check the path printed above.")