"""
Predicting linguistic annotations:
    We will now get to try one of spaCy's trained pipeline packages and see its predictions in action. 
    Feel free to try it out on your own text! To find out what a tag or label means, we call spacy.explain in the loop 
    For example spacy.explain("PROPN") or spacy.explain("GPE").
"""

'''
Part 1
    - Process the text with the nlp object and create a doc. 
    - For each token, print the token text, the token's .pos_ (part-of-speech-tag) and the token's .dep_ (dependency label). 
'''

import spacy 

nlp = spacy.load("en_core_web_sm")

text = "It's official: Apple is the first U.S. public cpmpany to reach a $1 trillion market value"

# Process the text 
doc = nlp(text)

for token in doc:
    # Get the token text, part-of-speech tag and dependency label 
    token_text = token.text 
    token_pos_ = token.pos_ 
    token_dep = token.dep_ 
    # This is for formatting only 
    print(f"{token_text:<12}{token_pos_:<10}{token_dep:<10}")

print()
'''
Part 2
    - Process the text and create a doc object. 
    - Iterate over the doc.ents and print the entity text and label_ attribute. 
'''

# Iterate over the predicted entities
for ent in doc.ents:
    # Print the entity text and its label
    print(ent.text, ent.label_)