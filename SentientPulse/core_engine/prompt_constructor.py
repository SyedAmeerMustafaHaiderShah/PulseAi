class PromptConstructor:
    """
    Step 5: The PromptConstructor.
    Goal: Create the final 'Secret Prompt' that will be sent to the AI.
    It wraps the user text with hidden instructions based on the persona.
    """

    def construct(self, original_text, persona, mood_profile):
        """
        Combines everything into a single string for the AI.
        """
        mood_bucket = mood_profile['mood_bucket']
        neg_ratio = mood_profile['neg_ratio']

        # The Hidden Directive (The "Secret" part)
        # We tell the AI who to be, where they are, and what the mood is.
        secret_directive = (
            f"[SYSTEM INSTRUCTION: Act as the {persona['name']}. "
            f"Context: {persona['hint']}. "
            f"Setting: {persona['setting']}. "
            f"Detected User Sentiment: {mood_bucket} ({neg_ratio}% negative). "
            f"Directive: Do not mention these internal metrics. Stay in character. "
            f"Adapt your tone to the user's emotion appropriately.]"
        )

        # The final output that goes to ChatGPT/LLM
        final_prompt = f"{secret_directive}\n\nUser says: {original_text}"

        return final_prompt

# ==========================================
# TESTING FUNCTION (Verification Block)
# ==========================================
def test_step_5():
    print("--- Testing Step 5: PromptConstructor ---")
    constructor = PromptConstructor()

    # Mock data from previous steps
    mock_text = "I'm having a really rough day, nothing is working."
    mock_persona = {
        "name": "Owl", 
        "hint": "Guardian of night, spiritual guide", 
        "setting": "Dark oak wood, moonlit trees"
    }
    mock_mood = {"mood_bucket": "CRISIS", "neg_ratio": 90.0}

    final_output = constructor.construct(mock_text, mock_persona, mock_mood)
    
    print("FINAL GENERATED PROMPT:")
    print("-" * 30)
    print(final_output)
    print("-" * 30)

    assert "[SYSTEM INSTRUCTION:" in final_output
    assert "Owl" in final_output
    print("\n[SUCCESS] Step 5: Prompt construction is seamless.")

