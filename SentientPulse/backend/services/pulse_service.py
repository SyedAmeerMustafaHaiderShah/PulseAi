import os
import sys
import google.generativeai as genai
from dotenv import load_dotenv

# --- SENIOR PATH FIX START ---
# 1. Find the Root Directory (SentientPulse_Project)
# We go up two levels from 'backend/services/' to reach the Root
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ROOT_DIR = os.path.dirname(os.path.dirname(CURRENT_DIR))

# 2. Add Root to Sys Path so Python can find 'core_engine'
if ROOT_DIR not in sys.path:
    sys.path.append(ROOT_DIR)

# 3. Now we can safely import the EmotionModule
try:
    from core_engine.emotion_module import EmotionModule
except ImportError as e:
    print(f"❌ Path Error: Could not find core_engine. Ensure ROOT_DIR is: {ROOT_DIR}")
    raise e
# --- SENIOR PATH FIX END ---

load_dotenv(os.path.join(ROOT_DIR, '.env'))

class PulseService:
    def __init__(self):
        # Initialize your Emotion Module
        self.engine = EmotionModule()
        
        # Setup Gemini 2.5 Flash
        # CORRECTED: Use the name of the variable in your .env
        api_key = os.getenv("GEMINI_API_KEY") 
        
        if not api_key:
            print("❌ Error: GEMINI_API_KEY not found in .env")
            
        genai.configure(api_key=api_key)
        self.model = genai.GenerativeModel('gemini-2.5-flash')

    def get_pulse_response(self, user_text):
        try:
            # A. Get the Secret Prompt and Metadata from your engine
            result = self.engine.get_ai_instruction(user_text)
            
            # B. Get the Gemini Response
            response = self.model.generate_content(result['secret_prompt'])
            
            # C. Combine Gemini's words with your Module's data
            return {
                "ai_response": response.text,
                "persona": result['metadata']['persona_name'],
                "mood": result['metadata']['mood_label'],
                "neg_ratio": result['metadata']['negativity_ratio'],
                "pos_ratio": result['metadata']['positivity_ratio']
            }
        except Exception as e:
            print(f"❌ Pulse Service Error: {e}")
            return None