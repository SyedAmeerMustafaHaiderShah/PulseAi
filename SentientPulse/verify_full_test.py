import sys
import os

# Ensure the root directory is in the path so we can import from 'backend'
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from backend.services.pulse_service import PulseService
from backend.database.database import Database

def run_full_integration_test():
    print("🚀 --- PULSE AI: FULL SYSTEM INTEGRATION TEST --- 🚀")
    print("1. Initializing Services...")
    
    try:
        # Initialize the AI Brain and the MySQL Database
        ai_service = PulseService()
        db = Database()
        
        # 2. Define a Test Input 
        # (This input should trigger a Persona and a Mood)
        user_input = "I've worked so hard on this project and finally it is working! I feel amazing."
        print(f"\n💬 USER INPUT: {user_input}")
        
        # 3. Process through Sentiment Module + Gemini 2.5 Flash
        print("🧠 Processing: Sentiment Analysis -> Persona Selection -> Gemini Response...")
        result = ai_service.get_pulse_response(user_input)
        
        if result:
            # 4. Prepare data for the Database
            # We add the original user_text to the dictionary
            result['user_text'] = user_input
            
            print("\n--- AI OUTPUT ---")
            print(f"🎭 Persona: {result['persona']}")
            print(f"📊 Mood:    {result['mood']}")
            print(f"📈 Positivity: {result['pos_ratio']}%")
            print(f"🤖 Response: {result['ai_response'][:100]}...") # Shows preview
            
            # 5. Save to MySQL Workbench
            print("\n💾 Saving interaction to MySQL Workbench...")
            db.save_chat_log(result)
            
            print("\n" + "="*50)
            print("✅ TEST SUCCESSFUL!")
            print("Your module, Gemini, and MySQL are now perfectly integrated.")
            print("Check your 'mood_logs' table in MySQL Workbench to see the live data.")
            print("="*50)
            
        else:
            print("❌ FAILED: AI Service returned no data.")

    except Exception as e:
        print(f"❌ CRITICAL ERROR during integration: {e}")

if __name__ == "__main__":
    run_full_integration_test()