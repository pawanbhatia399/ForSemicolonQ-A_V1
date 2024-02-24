import nltk
from nltk.corpus import wordnet

#nltk.download('punkt')
#nltk.download('wordnet')

def is_meaningful(text):
    # Tokenize the text into words
    words = nltk.word_tokenize(text)
    
    # Check if at least one word has a synonym in WordNet
    for word in words:
        synsets = wordnet.synsets(word)
        if synsets:
            return True
    
    return False
 
# Example usage:
input_text = input("Enter the text to verify its meaningfulness: ")
if is_meaningful(input_text):
    print("The input text is meaningful.")
else:
    print("The input text is garbage or trash.")