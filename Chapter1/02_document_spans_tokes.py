
"""
    When we call nlp on a string, spaCy first tokenizes the text and creates a document object. 
    In this exercide, we will learn more about the Doc, as well as its views Token and Span. 
"""

'''
Step 1:
    - Use spacy.blank to create the English nlp object. 
    - Process the text and instantiate a Doc object in the variable doc. 
    - Select the first token of the Doc and prints its text. 
'''

# import spaCy and create the English nlp object 
import spacy 

nlp = spacy.blank("en")

# Proces sthe text 
doc = nlp("I like tree kangaroos and narwhals.")

# Select the first token 
first_token = doc[0]

# Print the first token's text 
print(first_token.text)


'''
Step 2:
    - Use spacy.blank to create the English nlp object. 
    - Process the text and intantiate a Doc object in the variable doc. 
    - Create a slice of the Doc for tokens "tree kangaroos" and "tree kangaroos and narwhals."
'''

# Import spaCy and create the English nlp object 
import spacy 

nlp = spacy.blank("en")

# Process the text 
doc = nlp("I like tree kangaroos and narwhals.")

# A slice of the Doc for "tree kangaroos"
tree_kangaroos = doc[2:4]
print(tree_kangaroos.text)

# A slice of the Doc for "tree kangaroos and narwhals" (without the ".")
tree_kangaroos_and_narwhals = doc[2:6]
print(tree_kangaroos_and_narwhals.text)
