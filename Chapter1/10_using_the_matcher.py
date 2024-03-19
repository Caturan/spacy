
"""

Let's try spaCy's rule-based Matcher. We'll be using the example from the previous exercise and write a pattern that can match the phrase “iPhone X” in the text.

    Import the Matcher from spacy.matcher.
    Initialize it with the nlp object's shared vocab.
    Create a pattern that matches the "TEXT" values of two tokens: "iPhone" and "X".
    Use the matcher.add method to add the pattern to the matcher.
    Call the matcher on the doc and store the result in the variable matches.
    Iterate over the matches and get the matched span from the start to the end index.

"""

import spacy 
# import the matcher
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")
doc = nlp("Upcoming iPhone X release date leaked as Apple reveals pre-orders")

# Initialize the Matcher with shared vocabulary
matcher = Matcher(nlp.vocab)

# Create a pattern matching two tokens: "iPhone", "X"
pattern = [{"TEXT":"iPhone"}, {"TEXT":"X"}]

# Add pattern to matcher
matcher.add("IPHONE_X_PATTERN", [pattern])

# Use the matcher on the doc 
matches = matcher(doc)

print("Matches:", [doc[start:end].text for match_id, start, end in matches])