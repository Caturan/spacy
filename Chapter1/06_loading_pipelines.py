"""
Loading Pipelines:
    The pipelines we are using in this course are already pre-intalled. 
    - Use spacy.load to load the small English pipeline "en_core_web_sm". 
    - Process the text and print the document text.  
"""

import spacy 
from spacy.lang.tr import Turkish 

nlp = Turkish()

text = "merhaba naber, nasıl gidiyor"

doc = nlp(text)

print(doc.text)


nlp1 = spacy.load("en_core_web_sm")

text1 = "It's official: Apple is the first U.S. public company to reach a $1 trillion market value"

doc1 = nlp1(text1)

print(doc1.text)