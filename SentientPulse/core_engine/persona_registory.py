import random

class PersonaRegistry:
    """
    Step 4: The Persona Registry.
    Goal: Store 120 personas and pick one based on the mood bucket.
    Includes the 'Hint' (Living Area) for richer AI context.
    """

    def __init__(self):
        # We organize your personas into the 4 logical buckets
        self.buckets = {
            "CRISIS": [
                {"name": "Owl", "hint": "Guardian of night, spiritual guide", "setting": "Dark oak wood, moonlit trees"},
                {"name": "Bear", "hint": "Forest guardian, protective", "setting": "Mountain forest, rocky river"},
                {"name": "Batman", "hint": "Dark knight, fear symbol, strategic", "setting": "Gotham rooftops"},
                {"name": "Darth Vader", "hint": "Fallen hero, dark enforcer", "setting": "Death Star corridor"},
                {"name": "Void Watcher", "hint": "End observer, eternal", "setting": "Starless void"},
                # ... (You will add the rest of your 120 here)
            ],
            "STRUGGLE": [
                {"name": "Lion", "hint": "Royal protector, dominant", "setting": "Golden savanna, sunset"},
                {"name": "Wolf", "hint": "Lone hunter, loyal, fierce", "setting": "Snowy pine forest, full moon"},
                {"name": "Captain America", "hint": "Moral compass, noble, determined", "setting": "Battlefield"},
                {"name": "Wolverine", "hint": "Immortal fighter, angry, loyal", "setting": "Snow forest"},
                {"name": "Rocky Balboa", "hint": "Underdog warrior, never gives up", "setting": "Boxing ring at night"},
            ],
            "BALANCED": [
                {"name": "Fox", "hint": "Trickster, clever survivor", "setting": "Autumn forest, fallen leaves"},
                {"name": "Spider-Man", "hint": "Friendly neighborhood hero, anxious but hopeful", "setting": "City rooftops"},
                {"name": "Minion", "hint": "Comic chaos helper, silly, joyful", "setting": "Bright lab, yellow tones"},
                {"name": "Cat", "hint": "Mystic companion, detached, curious", "setting": "Candle-lit alley"},
                {"name": "Geralt of Rivia", "hint": "Monster hunter, stoic, tired", "setting": "Foggy medieval road"},
            ],
            "POSITIVE": [
                {"name": "Eagle", "hint": "Sky hunter, focused, proud", "setting": "High cliffs, open sky"},
                {"name": "Genie", "hint": "Wish granter, infinite energy, joyful", "setting": "Magic lamp, desert palace"},
                {"name": "Mario", "hint": "Hero of joy, cheerful", "setting": "Colorful fantasy world"},
                {"name": "Naruto", "hint": "Dream chaser, loud, hopeful", "setting": "Hidden Leaf village"},
                {"name": "Butterfly", "hint": "Transformation, light, hopeful", "setting": "Flower garden, sunlight"},
            ]
        }

    def get_persona(self, mood_bucket):
        """
        Picks a random persona from the requested bucket.
        """
        # Fallback if bucket doesn't exist
        if mood_bucket not in self.buckets:
            mood_bucket = "BALANCED"

        persona_list = self.buckets[mood_bucket]
        return random.choice(persona_list)

# ==========================================
# TESTING FUNCTION (Verification Block)
# ==========================================
def test_step_4():
    print("--- Testing Step 4: PersonaRegistry ---")
    registry = PersonaRegistry()

    # Test Case 1: Crisis selection
    p1 = registry.get_persona("CRISIS")
    print(f"Crisis Persona Picked: {p1['name']} ({p1['setting']})")
    
    # Test Case 2: Positive selection
    p2 = registry.get_persona("POSITIVE")
    print(f"Positive Persona Picked: {p2['name']} ({p2['hint']})")

    # Test Case 3: Randomness Check (Pick 3 from Struggle)
    print("Testing Randomness (Struggle Bucket):")
    for _ in range(3):
        p = registry.get_persona("STRUGGLE")
        print(f" - {p['name']}")

    assert p1['name'] != ""
    print("\n[SUCCESS] Step 4: Persona Registry is loaded and picking correctly.")

