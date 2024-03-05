# import spaCy 
import spacy

# Creaete a blank English nlp object 
nlp = spacy.blank("en")

'''
    - contains the processing pipeline 
    - includes language-specific rules for tokenization etc. 
'''

'''
    The Doc object 
'''
# Created by processing a string of text with the nlp object. 
doc = nlp("Hello world!")

# Iterate over tokens in a Doc 
for token in doc:
    print(token.text)

'''
    The Token object 
'''
doc = nlp("Hello world!")

# Index into the Doc to get a single Token 
token = doc[1]

# Get the token text via the .text attribute 
print(token.text)


''' 
    The Span object 
'''
doc = nlp("Hello world!")

# A slice from the Doc is a Span object 
span = doc[1:3]

# Get the span text via the .text attribute 
print(span.text)


'''
    Lexical Attributes
'''
doc = nlp("It costs $5.")

print("Index:   ", [token.i for token in doc])
print("Text:    ", [token.text for token in doc])

print("is alpha:", [token.is_alpha for token in doc])
print("is punct:", [token.is_punct for token in doc])
print("like_num:", [token.like_num for token in doc])