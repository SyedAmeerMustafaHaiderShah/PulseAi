class MoodAggregator:
    """
    Step 3: The MoodAggregator.
    Goal: Take raw batch results and calculate the emotional ratio.
    Filters out 'neutral' and determines the Mood Level for persona selection.
    """

    def calculate_mood_profile(self, raw_results):
        """
        Input: ['negative', 'positive', 'negative', 'neutral']
        Output: A profile dictionary with ratios and the target mood bucket.
        """
        # 1. Filter out 'neutral' as per instructions
        filtered_results = [r for r in raw_results if r != 'neutral']
        
        total_count = len(filtered_results)
        
        # Handle case where all inputs were neutral or empty
        if total_count == 0:
            return {
                "neg_ratio": 0,
                "pos_ratio": 0,
                "mood_bucket": "BALANCED",
                "intensity": "low"
            }

        # 2. Count Occurrences
        neg_count = filtered_results.count('negative')
        pos_count = filtered_results.count('positive')

        # 3. Calculate Percentages
        neg_ratio = (neg_count / total_count) * 100
        pos_ratio = (pos_count / total_count) * 100

        # 4. Map to Mood Buckets (The Logic Layer)
        if neg_ratio >= 80:
            mood_bucket = "CRISIS"       # Needs Heavy Guardians
        elif neg_ratio >= 60:
            mood_bucket = "STRUGGLE"     # Needs Motivators
        elif neg_ratio >= 40:
            mood_bucket = "BALANCED"     # Needs Friends / Observers
        else:
            mood_bucket = "POSITIVE"     # Needs Celebrators

        return {
            "neg_ratio": round(neg_ratio, 2),
            "pos_ratio": round(pos_ratio, 2),
            "mood_bucket": mood_bucket,
            "total_samples": total_count
        }

# ==========================================
# TESTING FUNCTION (Verification Block)
# ==========================================
def test_step_3():
    print("--- Testing Step 3: MoodAggregator ---")
    aggregator = MoodAggregator()

    # Test Case 1: High Negativity (Crisis)
    case_1 = ['negative', 'negative', 'negative', 'negative', 'positive'] 
    # 4/5 = 80%
    result_1 = aggregator.calculate_mood_profile(case_1)
    print(f"Test 1 (80% Neg): {result_1['mood_bucket']} (Ratio: {result_1['neg_ratio']}%)")
    assert result_1['mood_bucket'] == "CRISIS"

    # Test Case 2: Mixed with Neutrals (Should ignore neutrals)
    case_2 = ['negative', 'neutral', 'neutral', 'positive'] 
    # 1 Neg, 1 Pos (Neutrals ignored) -> 50/50
    result_2 = aggregator.calculate_mood_profile(case_2)
    print(f"Test 2 (Mixed/Neutrals): {result_2['mood_bucket']} (Ratio: {result_2['neg_ratio']}%)")
    assert result_2['mood_bucket'] == "BALANCED"

    # Test Case 3: High Positivity
    case_3 = ['positive', 'positive', 'negative', 'positive'] 
    # 1/4 = 25% Neg
    result_3 = aggregator.calculate_mood_profile(case_3)
    print(f"Test 3 (High Pos): {result_3['mood_bucket']} (Ratio: {result_3['neg_ratio']}%)")
    assert result_3['mood_bucket'] == "POSITIVE"

    print("\n[SUCCESS] Step 3: Mood Aggregation logic is solid.")

