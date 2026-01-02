import sys
import os

# --- PROFESSIONAL INTEGRATION LOGIC ---
# This ensures internal imports work regardless of where the script is run from
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.append(CURRENT_DIR)

# Internal Imports
try:
    from text_processor import TextProcessor
    from sentiment_adapter import SentimentAdapter
    from mood_aggregator import MoodAggregator
    from persona_registory import PersonaRegistry # Using your spelling
    from prompt_constructor import PromptConstructor
except ImportError as e:
    print(f"⚠️ Internal Import Warning: {e}. Attempting relative import...")
    from .text_processor import TextProcessor
    from .sentiment_adapter import SentimentAdapter
    from .mood_aggregator import MoodAggregator
    from .persona_registory import PersonaRegistry
    from .prompt_constructor import PromptConstructor

class EmotionModule:
    """
    THE PURE ENGINE.
    No database. No reports. Just pure transformation.
    """
    def __init__(self):
        self.processor = TextProcessor()
        self.adapter = SentimentAdapter()
        self.aggregator = MoodAggregator()
        self.registry = PersonaRegistry()
        self.constructor = PromptConstructor()

    def get_ai_instruction(self, user_text):
        """
        Input: Raw User Text
        Output: { 'secret_prompt': str, 'metadata': dict }
        """
        # Step 1: Split into sentences
        sentences = self.processor.process_to_sentences(user_text)

        # Step 2: ML Batch Analysis
        analysis = self.adapter.analyze_batch(sentences)

        # Step 3: Calculate Ratios (Ignoring Neutrals)
        mood_profile = self.aggregator.calculate_mood_profile(analysis['raw_results'])

        # Step 4: Persona Selection
        persona = self.registry.get_persona(mood_profile['mood_bucket'])

        # Step 5: Final Prompt Construction
        secret_prompt = self.constructor.construct(user_text, persona, mood_profile)

        # Return everything the developer needs to run their app
        return {
            "secret_prompt": secret_prompt,
            "metadata": {
                "persona_name": persona['name'],
                "mood_label": mood_profile['mood_bucket'],
                "negativity_ratio": mood_profile['neg_ratio'],
                "positivity_ratio": mood_profile['pos_ratio']
            }
        }

    def display_summary(self, engine_output):
        """
        A helper method for developers to quickly see the results 
        of the engine in the console.
        """
        print("\n" + "="*40)
        print("🤖 EMOTION ENGINE SUMMARY")
        print("="*40)
        print(f"STIMULUS (Metadata for your DB):")
        print(f"  - Persona:  {engine_output['metadata']['persona_name']}")
        print(f"  - Mood:     {engine_output['metadata']['mood_label']}")
        print(f"  - Neg/Pos:  {engine_output['metadata']['negativity_ratio']}% / {engine_output['metadata']['positivity_ratio']}%")
        print("\nINSTRUCTION (Send this to your AI):")
        # Added a safety check for the string slicing
        prompt_preview = engine_output['secret_prompt'][:150] if engine_output['secret_prompt'] else "N/A"
        print(f"  {prompt_preview}...") 
        print("="*40 + "\n")