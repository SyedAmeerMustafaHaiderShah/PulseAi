import sys
import os

print("--- DIAGNOSTIC START ---")
print(f"Python Executable: {sys.executable}")
print(f"Python Version: {sys.version}")
try:
    import pymongo
    print("✅ Pymongo found in this script's path!")
except ImportError:
    print("❌ Pymongo NOT found in this script's path.")
print("--- DIAGNOSTIC END ---")