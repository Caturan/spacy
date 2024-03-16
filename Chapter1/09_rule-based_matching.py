
"""
Why not just regular expression? 
    - Match on Doc objects, not just strings: 
        Compared to regular expressions, the mathcher wokrs with Doc and Token objects instead of only strings. 

    - Match on tokens and token attributes:
        It's also more flexible: we can search for texts but also other lexical attributes. 

    - Use a model's predictions:
        We can even write rules that use a model's predictions. 

    - Example: "duck" (verb) vs. "duck" (noun):
        For example, find the word "duck" only if it's a verb, not a noun. 
"""

"""
Match patterns
    - List of dictionaries, one per token:
        Match patterns are lists of dictionaries. Each dictionary describes one token. 
         The keys are the names of token attributes, mapped to their expected values. 

    - Match exact token texts: 
        [{"TEXT": "iPhone"}, {"TEXT": "X"}]
            In this example, we are looking for two tokens with the text "iPhone" and "X". 

    - Match lexical attributes:
        [{"LOWER": "iphone"}, {"LOWER": "x"}]
            We can also match on other token attributes. 
             Here, we are looking for two tokens whose lowercase forms equal "iphone" and "x". 

    - Match any token attributes:
        [{"LEMMA": "buy"}, {"POS": "NOUN"}]
            We can even write patterns using attributes predicted by a model. 
             Here, we are matching a token with the lemma "buy", plus a noun. 
             The lemma is the base form, so this pattern would match phrases like "buying milk" or "bought flowers".  
        
"""

# Using the Matcher (1)
import spacy 

# import the matcher
from spacy.matcher import Matcher 

# Load a pipeline and create the nlp object 
nlp = spacy.load("en_core_web_sm")

# Initialize the matcher with the shared vocab 
matcher = Matcher(nlp.vocab)

# Add the pattern to the matcher 
pattern = [{"TEXT": "iPhone"}, {"TEXT": "X"}]
matcher.add("IPHONE_PATTERN", [pattern])

# Process some text 
doc = nlp("Upcoming iPhone X release date leaked")

# Call the matcher on the doc 
matches = matcher(doc)

"""
    To use a pattern, we first import the matcher from spacy.matcher

    We also load a pipeline and create the nlp object. 

    The matcher is initialized with the shared vocabulary, nlp.vocab. We will learn more about this later-for now, just remember to always pass it in. 

    The matcher.add method lets we add a pattern. The first argument is a unique ID to identify which pattern was matched. 
     The second argument is a list of patterns. 
    
    To match the pattern on a text, we can call the matcher on any doc. 

    This will return the matches. 
"""

# Using the Matcher (2)
# Call the matcher on the doc 
doc = nlp("Upcoming iPhone X release date leaked.")
matches = matcher(doc)

# Iterate over the matches 
for match_id, start, end in matches:
    # Get the matched span 
    mathced_span = doc[start:end]
    print(mathced_span.text)
'''
    * match_id : hash value of the pattern name 
    * start : start index of matched span 
    * end : end index of matched span 
'''

"""
    When we call the matcher on a doc, it returns a list of tuples. 

    Each tuple consist of three values: the match ID, the start index and end index of the matched span. 

    This means we can iterate over the matches and create a Span object: a slice of the doc at the start and end index. 
"""

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

pattern = [
    {"IS_DIGIT": True},
    {"LOWER": "fifa"},
    {"LOWER": "world"},
    {"LOWER": "cup"},
    {"IS_PUNCT": True}
]
matcher.add("DenePattern", [pattern])


doc = nlp("2018 FIFA World Cup: France won!")
matches = matcher(doc)

for match_id, start, end in matches:
    mathced_span = doc[start:end]
    print(mathced_span.text)
"""
    Here's an example of a more complex pattern using lexical attributes. 

    We are looking for five tokens: 
     A token consisting of only digits. 
     Three case-insensitive tokens for "fifa", "world", and "cup". 
     And a token that consist of punctuation.
     The pattern matches the tokens "2018 FIFA World Cup".
"""


nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

pattern = [
    {"LEMMA": "love", "POS": "VERB"},
    {"POS": "NOUN"}
]
matcher.add("Dene2Pattern", [pattern])

doc = nlp("I loved dogs but now I love cats more.")
matches = matcher(doc)

for match_id, start, end in matches:
    mathced_span = doc[start:end]
    print(mathced_span.text)
'''
    In this example, we are looking for two tokens:
     A verb with the lemma "love", followed by a noun. 
     This pattern will match "loved dogs" and "love cats". 
'''


# Using operators and quantifiers (1)
nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

pattern = [
    {"LEMMA": "buy"},
    {"POS": "DET", "OP": "?"}, # optional: match 0 or 1 times 
    {"POS": "NOUN"}
]
matcher.add("Dene3Pattern", [pattern])

doc = nlp("I bought a smartphone. Now I'm buying apps.")
matches = matcher(doc)

for match_id, start, end in matches:
    mathced_span = doc[start:end]
    print(mathced_span.text)
'''
    Operators and quantifiers let us define how often a token should be matched. 
    They can be added using the "OP" key. 

    Here, the "?" operator makes the determiner token optional, so it will match a token with the lemma "buy", and optional article and a noun. 
'''

# Using operators and quantifiers (2)
"""
    {"OP": "!"}  Negation: match 0 times 
    {"OP": "?"}  Optional match 0 or 1 times 
    {"OP": "+"}  Match 1 or more times  
    {"OP": "*"}  Match 0 or more times   

    Operators can make our pattern a lot more powerful, but they also add more complexity-so use them wisely. 
"""

"""
    Token-based matching opens up a lot of new possibilities for information extraction.
"""