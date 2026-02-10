from nltk.util import ngrams
sentence = "i love nlp"
n = 3
words = sentence.split()
word_ngrams = ngrams(words, n)
print("Word n-grams:")
for gram in word_ngrams:
    print(gram)
char_ngrams = ngrams(sentence, n)
print("\nCharacter n-grams:")
for gram in char_ngrams:
    print("".join(gram))
