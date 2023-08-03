import random 

collection = {'noun': ['cheese', 'horse', 'dog', 'cat', 'elbow', 'La Croix', 'water', 'plane', 'obamna', 'tv'], 'adjective': ['interesting', 'thick', 'funny', 'dumb', 'desultory', 'eggshell white', 'disco', 'cursory', 'cool', 'weird'], 'verb': ['ate', 'licked', 'shot', 'dissected', 'turned nine', 'exorcised', 'slapped', 'carried', 'threw', 'yeeted']}

"""
To-Do:
- [ ] How does madlibs deal with tense? Does it just assume you can change the tense yourself when you read it? And do they separate nouns from proper noins

- [ ] Camelcase or snakecase in Python? I wanna say snakecase... oops

- [ ] Static methods vs just random functions (I am assuming I am overdoing it haha)
    - [ ] And is there a rule of thumb wrt separating things into other files

- [ ] How do I make collection work like I want it to? I want to define this default value within the wordlist method...

- [ ] Figure out importing other Python files

- [ ] Fix own input, somehow seeing it as null (default words work though):
    Traceback (most recent call last):
    File "/Users/jcb/Desktop/madlibs.py", line 83, in <module>
        main()
    File "/Users/jcb/Desktop/madlibs.py", line 77, in main
        Starting.filereader()
    File "/Users/jcb/Desktop/madlibs.py", line 54, in filereader
        stringy += f" {current.printuno(elem)}"
    File "/Users/jcb/Desktop/madlibs.py", line 21, in printuno
        return self.randomword(word, collection)
    File "/Users/jcb/Desktop/madlibs.py", line 29, in randomword
        index = random.choice(range(len(collection[pos])))
    TypeError: object of type 'NoneType' has no len()
"""

#This class handles the script and any operations you might need to do on it

class Script():
    def __init__(self, script):
        self.script = script
    
    def printer(self, script):
        for elem in script:
            if elem == "noun" or elem == "verb" or elem == "adjective":
                print(self.randomword(elem, collection))
            else:
                print(elem)

    def printuno(self, word):
        pos_list = ["Noun", "noun", "NOUN", "Verb", "verb", "VERB", "Adjective", "adjective", "ADJECTIVE"]
        if word in pos_list:
            return self.randomword(word.lower(), collection)
        else:
            return word
        
    def randomword(self, pos, collection):
            index = random.choice(range(len(collection[pos])))
            return collection[pos][index]


# This static class contains the methods that decide the word list and read in a file, creating an instance of the Script class in the process
class Starting():
    @staticmethod
    def wordlist():
        print("Would you like to use pre-set words or enter your own?")
        if input() == "own":
            collection = customwords.customwords()
            return collection

        else:
            pass

    @staticmethod
    def filereader():   
        print("Please enter your madlib path")
        path = input()
        try:
            #this should work w/o quotes bc input is always a string... I THINK!
            file = open(path)
            current = Script(file)

        except:
            file = open('example.txt')
            current = Script(file)
    
        for word in current.script:
            x = word.split()
            # print(x)
            stringy = ""
            for elem in x:
                stringy += f" {current.printuno(elem)}"
            print(stringy)
            return stringy


#The static customwords class contains the methods to create your own wordlist (WIP)
class customwords():
    @staticmethod
    def customwords(): 
        print("Please enter 10 nouns separated")
        collection["noun"] = (customwords.wordcollector("noun"))
        collection["adjective"] = (customwords.wordcollector("adjective"))
        collection["verb"] = (customwords.wordcollector("verb"))
        print(collection)
        return collection
    
    @staticmethod
    def wordcollector(pos):
        words = []
        for i in range(10):
            print(f"{pos} {i+1}")
            words.append(input())
        print(words)

def main():
    Starting.wordlist()
    Starting.filereader()
    

#Picturebook is the class we will use to take the output of the madlibs game and feed it into a generative AI API I find when I get off the plane lol
class Picturebook():
    @staticmethod
    def makebook(stringy):
        sentences = stringy.split(".")
        for sentence in sentences:
            #this is where the gen AI will get hooked up to output the images sentence by sentence
            print(sentence)


main()



