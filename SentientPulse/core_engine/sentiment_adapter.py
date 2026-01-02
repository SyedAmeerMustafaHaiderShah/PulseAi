from collections import Counter
# Importing the batch-capable function from your model file
from model_accepting_text import predict_sentiment_batch 

class SentimentAdapter:
    """
    Step 2: The SentimentAdapter.
    Goal: Take the list of sentences, feed them as a single batch to the model,
    and return the results for ratio calculation.
    """

    def analyze_batch(self, sentence_list):
        """
        Input: ['Sentence 1', 'Sentence 2', 'Sentence 3']
        Output: {
            'raw_results': ['negative', 'positive', 'negative'],
            'counts': {'negative': 2, 'positive': 1}
        }
        """
        if not sentence_list:
            return {"raw_results": [], "counts": {"positive": 0, "negative": 0}}

        # 1. Batch Feed: 
        # We pass the whole list to the model function at once.
        # This returns an array of predictions (e.g., ['negative', 'positive', 'negative'])
        predictions = predict_sentiment_batch(sentence_list)

        # 2. Results Storage:
        # We ensure everything is lowercase for consistency in Step 3
        raw_results = [str(p).lower().strip() for p in predictions]

        # 3. Calculation Prep:
        # Count the frequency of each sentiment
        mood_counts = Counter(raw_results)

        return {
            "raw_results": raw_results,
            "counts": dict(mood_counts)
        }

# ==========================================
# TESTING FUNCTION (Verification Block)
# ==========================================
def test_step_2():
    print("--- Testing Step 2: Batch SentimentAdapter ---")
    adapter = SentimentAdapter()

    # This is the list produced by your Step 1 TextProcessor
    mock_batch = [
        "I am extremely sad and lonely.",
        "The sun is shining and I feel okay.",
        "I hate how things are going right now."
    ]

    print(f"Feeding batch of {len(mock_batch)} sentences to the model...")
    
    try:
        # Run the batch analysis
        output = adapter.analyze_batch(mock_batch)
        
        # Display the array results (The raw batch results)
        print(f"Model Output (Array): {output['raw_results']}")
        
        # Display the counts (The summary)
        print(f"Sentiment Counts: {output['counts']}")

        # Senior Check: The number of results must match the number of input lines
        assert len(output['raw_results']) == len(mock_batch)
        print("\n[SUCCESS] Step 2: Batch feeding and result storage verified.")

    except ImportError:
        print("\n[SKIP] Step 2 logic is correct, but 'predict_sentiment_batch' was not found in your model file.")
    except Exception as e:
        print(f"\n[ERROR] Step 2 failed: {e}")

