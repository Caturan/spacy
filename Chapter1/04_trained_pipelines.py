
"""
What are trained pipelines? 
    - Models that enable spaCy to predict linguistic attributes in context 
        * Part-of-speech tags 
        * Syntactic dependencies 
        * Named entities   
    - Trained on labeled example tests
    - Can be updated with more examples to fine-tune predictions 
"""

"""
Pipeline Packages: 
    $ python -m spacy download en_core_web_sm 
    
    import spacy 
    
    nlp = spacy.load("en_core_web_sm")

    - Binary weights 
    - Vocabulary 
    - Meta information 
    - Configuration file 
"""


"""
Predicting Part-of-speech Tags
"""
import spacy 

# Load the small English pipeline 
nlp = spacy.load("en_core_web_sm")

# Process a text 
doc = nlp("She ate the pizza")

# Iterate over the tokens 
for token in doc:
    # Print the text and the predicted part-of-speech-tag 
    print(token.text, token.pos_)

print()
'''
Predicting Syntactic Dependencies 
'''
for token in doc: 
    print(token.text, token.pos_, token.dep_, token.head.text)

"""
Label   Description     Example 

nsubj   nominal subject     She 
dobj    direct object       pizza
det     determine(article)  the 
"""

print()
"""
Predictin Named Entities
Apple ORG is looking at buying U.K GPE startup for $1 billion MONEY
"""
# Process a text 
doc = nlp("Apple is looking at buying U.K startup for $1 billion")

# Iterate over the predicted entities 
for ent in doc.ents:
    # Print the entity text and its label 
    print(ent.text, ent.label_)

print()

"""
Tip: the spacy.explain method 
Get quick definitions of the most common tags and labels. 
"""
print(spacy.explain("GPE"))
print(spacy.explain("NNP"))
print(spacy.explain("dobj"))
print(spacy.explain("det"))
print(spacy.explain("dobj"))
print(spacy.explain("nsubj"))

