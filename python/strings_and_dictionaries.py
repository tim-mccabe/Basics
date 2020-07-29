# This file contains a few basic functions of strings and dictionaries to refer back to when writing new code

# Takes a list of documents (each document is a string) and a keyword. 
# Returns list of the index values into the original list for all documents 
# containing the keyword.

# Example:
# doc_list = ["The Learn Python Challenge Casino.", "They bought a car", "Casinoville"]
# >>> word_search(doc_list, 'casino')
# >>> [0]

def word_search(doc_list, keyword):
    indicies = []
    for i, doc in enumerate(doc_list):
        tokens = doc.split()
        normalized = [token.rstrip('.,').lower() for token in tokens]
        if keyword.lower() in normalized:
            indicies.append(i)
    return indicies

# Takes list of documents (each document is a string) and a list of keywords.  
# Returns a dictionary where each key is a keyword, and the value is a list of indices
# (from doc_list) of the documents containing that keyword

# >>> doc_list = ["The Learn Python Challenge Casino.", "They bought a car and a casino", "Casinoville"]
# >>> keywords = ['casino', 'they']
# >>> multi_word_search(doc_list, keywords)
# {'casino': [0, 1], 'they': [1]}

def multi_word_search(doc_list, keywords):
    keyword_to_indicies = {}
    for keyword in keywords:
        keyword_to_indicies[keyword] = word_search(doc_list, keyword)
    return keyword_to_indicies

