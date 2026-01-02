import os
from backend.services.pulse_service import PulseService

def run_test():
    print("🚀 Starting Pulse AI Integration Test...")
    
    # Check if Gemini Key exists
    if not os.getenv("GEMINI_API_KEY"):
        print("❌ Error: GEMINI_API_KEY not found in .env file.")
        return

    try:
        service = PulseService()
        
        # Test Input
        user_input = "I am so tired of failing, I feel like giving up on everything."
        print(f"\n💬 USER: {user_input}")
        
        # Process through the "Brain"
        print("🧠 Processing through Sentiment Engine & Gemini...")
        data = service.get_pulse_response(user_input)
        
        if data:
            print("\n" + "="*50)
            print("🎭 PERSONA ACTIVATED:", data['persona'])
            print("📊 MOOD DETECTED:   ", data['mood'])
            print("📉 NEGATIVITY:      ", data['neg_ratio'], "%")
            print("-" * 50)
            print("🤖 AI RESPONSE:")
            print(data['ai_response'])
            print("="*50)
            print("\n✅ Integration Test Passed!")
        else:
            print("❌ Test Failed: No response received.")

    except Exception as e:
        print(f"❌ Error during test: {e}")

if __name__ == "__main__":
    run_test() 