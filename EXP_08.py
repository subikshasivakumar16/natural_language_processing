import nltk
from nltk.tree import Tree
def chunk(sentence):
    words = sentence.split()
    print("Words are :", words)
    chunks = []
    i = 0
    while i < len(words) - 1:
        if words[i].lower() in ['a', 'an', 'the']:
            chunks.append(Tree('NP', [words[i], words[i+1]]))
            i += 2
        else:
            chunks.append(words[i])
            i += 1
    if i == len(words) - 1:
        chunks.append(words[-1])
    tree = Tree('S', chunks)
    tree.draw()
sentence = "A little boy is playing with a small puppy in the garden"
chunk(sentence)
