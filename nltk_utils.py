import nltk
import numpy as np
#nltk.download('punkt')

from nltk.stem.porter import PorterStemmer

stemmer = PorterStemmer()

def tokenize(sentence):
    return nltk.word_tokenize(sentence)

def stemming(word):
    return stemmer.stem(word.lower())

def bag_of_words(all_sentences, all_word):
    tokenize_sentence = [stemming(w) for w in all_sentences]
    bag = np.zeros(len(all_word),dtype=np.float32)
    for idx,w in enumerate(all_word):
        if w in tokenize_sentence:
            bag[idx]=1.0;
    return bag





a = "hey jarvis how are you?"
a1 = ["hey","me","good", "you","do","they"]
b= tokenize(a)
print(b)
c=[stemming(w) for w in b]
print(c)
d = bag_of_words(b,a1)
print(d)