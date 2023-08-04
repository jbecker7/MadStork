import random


class Script():
    def __init__(self, script, collection):
        self.script = script
        self.collection = collection

    def replace_words(self, word):
        pos_list = ["Noun", "noun", "NOUN", "Verb", "verb", "VERB", "Adjective", "adjective", "ADJECTIVE"]
        if word in pos_list:
            return self.random_word(word.lower(), self.collection)
        else:
            return word
        
    def random_word(self, pos, collection):
            index = random.choice(range(len(collection[pos])))
            return collection[pos][index]

    
                
        



