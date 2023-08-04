import random
import stork_image
import stork_wikipedia
import stork_words

#Need to consider tense, maybe incorporate wikipedia api for madlib source (random), load in JSON of words, default is dictionary or sth

# collection = {'noun': ['cheese', 'horse', 'dog', 'cat', 'elbow', 'La Croix', 'water', 'plane', 'obamna', 'tv'], 'adjective': ['interesting', 'thick', 'funny', 'dumb', 'desultory', 'eggshell white', 'disco', 'cursory', 'cool', 'weird'], 'verb': ['ate', 'licked', 'shot', 'dissected', 'turned nine', 'exorcised', 'slapped', 'carried', 'threw', 'yeeted']}

#This class handles the script and any operations you might need to do on it

class Script():
    def __init__(self, script):
        self.script = script
    
    def printer(self, script):
        for elem in script:
            if elem == "noun" or elem == "verb" or elem == "adjective":
                print(self.random_word(elem, collection))
            else:
                print(elem)

    def print_uno(self, word):
        pos_list = ["Noun", "noun", "NOUN", "Verb", "verb", "VERB", "Adjective", "adjective", "ADJECTIVE"]
        if word in pos_list:
            return self.random_word(word.lower(), collection)
        else:
            return word
        
    def random_word(self, pos, collection):
            index = random.choice(range(len(collection[pos])))
            return collection[pos][index]


# Starting contains the methods that decide the word list and read in a file, creating an instance of the Script class in the process
class Starting():
    @staticmethod
    def word_list():
        global collection
        print("Would you like to use pre-set words or enter your own?")
        if input() == "own":
            collection = CustomWords.get_custom_words()
            return collection

        else:
            collection = stork_words.main()
            return collection

    @staticmethod
    def file_reader():   
        print("Please enter your madlib path. If you don't have one, press enter and we will grab one from Wikipedia.")
        path = input()
        try:
            #this should work w/o quotes bc input is always a string... I THINK!
            with open(path, 'r') as file:
                words = file.read().split()
                current = Script(words)

        except:
            with open('example.txt', 'r') as file:
                words = stork_wikipedia.main()
                words = words.split()
                current = Script(words)
        
        stringy = ""
        for word in current.script:
            stringy += f" {current.print_uno(word)}"
        print(stringy)
        return stringy


#The CustomWords class contains the methods to create your own word list
class CustomWords():
    @staticmethod
    def get_custom_words(): 
        global collection
        print("Please enter 10 nouns separated")
        collection["noun"] = (CustomWords.word_collector("noun"))
        collection["adjective"] = (CustomWords.word_collector("adjective"))
        collection["verb"] = (CustomWords.word_collector("verb"))
        print(collection)
        return collection
    
    @staticmethod
    def word_collector(pos):
        words = []
        for i in range(10):
            print(f"{pos} {i+1}")
            words.append(input())
        print(words)
        return words

def main():
    Starting.word_list()
    PictureBook.make_book(Starting.file_reader())
    

#PictureBook is the class we will use to take the output of the madlibs game and feed it into the image generator
class PictureBook():
    @staticmethod
    def make_book(stringy):
        stork_image.main(stringy)

main()



