
"""
    In this exercise, we will practice writing more complex match pattern 
     using different token attributes and operators.
"""

# PART1
# Write one pattern that only matches mentions of the full iOS versions: "ios 7", "iOS 11", iOS 10".

import spacy 
from spacy.matcher import Matcher

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

doc = nlp(
    "After making the iOS update you won't notice a radical system-wide "
    "redesing: nothing like the aesthetic upheaval we got with iOS 7. Most of "
    "iOS 11's furniture remains the same as in iOS 10. But you will discover "
    "some tweaks once you delve a little deeper."
)

# Write a pattern for full iOS versions ("iOS 7", "iOS 11", "iOS 10")
pattern = [{"TEXT": "iOS"}, {"IS_DIGIT": True}]

# Add the pattern to the matcher and apply the matcher to the doc 
matcher.add("IOS_VERSION_PATTERN", [pattern])
matches = matcher(doc)
print("Total matches found:", len(matches))

# Iterate over the matches and print the span text 
for match_id, start, end in matches:
    print("Match found:", doc[start:end].text)


print()

# PART2
"""
    Write one pattern that only matches forms of "download" (tokens with the lemma "download")
     followed by a token with the part-of-speech tag "PROPN" (proper noun)
"""
import spacy
from spacy.matcher import Matcher 

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

doc = nlp(
    "i downloaded Fortnite on my laptop and can't open the game at all. Help? "
    "so when I was downloading Minecraft, I got the Windows version where it "
    "is the '.zip' folder and I used the default program to unpack it... do "
    "I also need to download Winzip?"
)

# Write a pattern that matcher a form of "download" plus proper noun 
pattern = [{"LEMMA": "download"}, {"POS": "PROPN"}]

# Add the pattern to the matcher and apply the matcher to the doc 
matcher.add("DOWLOAD_THINGS_PATTERN", [pattern])
matches = matcher(doc)
print("Total matches found:", len(matches))

# Iterate over the matches and print the span text 
for match_id, start, end in matches:
    print("Match found:", doc[start:end].text)


print()


# PART3 
"""
    Write one pattern that matches adjectives ("ADJ) followed by one or two "NOUN"s (one noun and one optional noun) 
"""
import spacy 
from spacy.matcher import Matcher 

nlp = spacy.load("en_core_web_sm")
matcher = Matcher(nlp.vocab)

doc = nlp(
    "Features of the app include a beautiful design, smart search, automatic "
    "labels and optional voice responses."
)

# Write a pattern for adjective plus one or two nouns 
pattern = [{"POS": "ADJ"}, {"POS": "NOUN"}, {"POS": "NOUN", "OP": "?"}]

# Add the pattern to the matcher and apply the matcher to the doc 
matcher.add("ADJ_NOUN_PATTERN", [pattern])
matches = matcher(doc)
print("Total matches found:", len(matches))

# Iterate over the matches and print the span text 
for match_id, start, end in matches:
    print("Match found", doc[start:end].text)

