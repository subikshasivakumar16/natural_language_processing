import nltk
from nltk.wsd import lesk
from nltk import word_tokenize, pos_tag

# Downloads
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('averaged_perceptron_tagger_eng')
nltk.download('wordnet')

# Changed the sentence and word only
sentence = "The rough bark of the old oak tree was covered in moss"
word = "bark"

tokens = word_tokenize(sentence)
tagged = pos_tag(tokens)
sense = lesk(tokens, word)

print("Word:", word)
if sense:
    print("Best Sense:", sense.name())
    print("Definition:", sense.definition())
else:
    print("No sense found")