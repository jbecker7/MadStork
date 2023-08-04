from wonderwords import RandomWord
r = RandomWord()

def main():
    collection = {"noun": [], "adjective": [], "verb": []}
    for i in range(10):
        collection["noun"].append(r.word(include_parts_of_speech=["nouns"]))
        collection["adjective"].append(r.word(include_parts_of_speech=["adjectives"]))
        collection["verb"].append(r.word(include_parts_of_speech=["verbs"]))
    # print(collection)
    return collection


#The CustomWords class contains the methods to create your own word list
class CustomWords():
    @staticmethod
    def get_custom_words(): 
        global collection
        collection["noun"] = (CustomWords.word_collector("noun"))
        collection["adjective"] = (CustomWords.word_collector("adjective"))
        print("Please enter verbs in the infinitive form without to, e.g. 'run' instead of 'to run'.")
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



main()