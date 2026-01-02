
from emotion_module import EmotionModule

engine = EmotionModule()

# 2. Sample User Input
user_input = "I am have be aloted to do an assigment . it is soo hard to do so as i have no knowlege of this subject. i have my paper coming also. i have  not  preparation of this also  . help me to prepare "

# 3. Process the input
# The engine returns a structured dictionary
output = engine.get_ai_instruction(user_input)

# 4. EXPLAINING THE OUTPUT
# This is the string you send to ChatGPT / LLM API:
print("--- PROMPT FOR THE AI ---")
print(output['secret_prompt']) 

# This is the data you save to your own database for analytics:
print("\n--- METADATA FOR YOUR DATABASE ---")
print(f"Detected Mood: {output['metadata']['mood_label']}")
print(f"Persona Used:  {output['metadata']['persona_name']}")
print(f"Negativity:    {output['metadata']['negativity_ratio']}%")