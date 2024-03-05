
"""
    Use spacy.blank to create a blank English ("en") nlp object. 
    Create a doc and prints its text. 
"""
import spacy 

# Create the English nlp object 
nlp = spacy.blank("en")

# Process a text 
doc = nlp("This is a sentence.")

# Print the document text 
print(doc.text)