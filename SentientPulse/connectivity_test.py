import os
from dotenv import load_dotenv
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure, OperationFailure

# 1. Load the secrets
load_dotenv()

def final_test():
    uri = os.getenv("MONGO_URI")
    
    print("--- 🛡️ Pulse AI: Final Connectivity Check ---")
    print(f"Connecting to: {uri.split('@')[-1]}") # Prints the cluster address only for safety

    try:
        # 2. Attempt the connection
        client = MongoClient(uri, serverSelectionTimeoutMS=5000)
        
        # 3. The 'ping' command is the ultimate test
        client.admin.command('ping')
        
        print("\n✅ STATUS: SUCCESS")
        print("🌍 Connection to MongoDB Atlas is LIVE.")
        print("📂 Database 'SentientPulse' is ready for storage.")
        
    except ConnectionFailure:
        print("\n❌ STATUS: FAILED")
        print("ERROR: Could not connect to the server. Check your Internet or IP Whitelist.")
    except OperationFailure as e:
        print("\n❌ STATUS: FAILED")
        print(f"ERROR: Authentication failed. Your Username or Password in the .env is wrong.")
    except Exception as e:
        print("\n❌ STATUS: FAILED")
        print(f"ERROR: {e}")

if __name__ == "__main__":
    final_test()