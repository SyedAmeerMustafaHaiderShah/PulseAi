import re

class TextProcessor:
    """
    Step 1: The TextProcessor (Robust Version).
    Goal: Transform raw user input into a batch list of clean sentences.
    Splits by punctuation, but also handles "run-on" sentences (no punctuation)
    to ensure the MoodAggregator has enough data points for a ratio.
    """

    def __init__(self, max_words_per_split=15):
        # Primary split: . ! or ?
        self.split_pattern = r'(?<=[.!?])\s+'
        # Secondary split: Fallback word count if punctuation is missing
        self.max_words = max_words_per_split

    def process_to_sentences(self, raw_text):
        """
        Takes raw string and returns a list of individual sentences or chunks.
        """
        if not raw_text or not isinstance(raw_text, str):
            return []

        # 1. Standardize text: Remove newlines and reduce extra spaces
        clean_text = raw_text.replace("\n", " ").strip()
        clean_text = re.sub(r'\s+', ' ', clean_text)

        # 2. Initial Split by Punctuation
        initial_chunks = re.split(self.split_pattern, clean_text)
        
        batch_list = []

        # 3. Handle "Run-on" Sentences
        for chunk in initial_chunks:
            chunk = chunk.strip()
            if not chunk:
                continue

            words = chunk.split()
            
            # If the chunk is a long "wall of text" without punctuation
            if len(words) > self.max_words:
                # Break it into smaller batches for the ML model
                for i in range(0, len(words), self.max_words):
                    sub_chunk = " ".join(words[i:i + self.max_words])
                    batch_list.append(sub_chunk)
            else:
                batch_list.append(chunk)

        return batch_list

