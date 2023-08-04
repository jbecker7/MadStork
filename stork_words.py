from wonderwords import RandomWord

r = RandomWord()

def main():
    collection = {"noun": [], "adjective": [], "verb": []}
    for i in range(10):
        collection["noun"].append(r.word(include_parts_of_speech=["nouns"]))
        collection["adjective"].append(r.word(include_parts_of_speech=["adjectives"]))
        collection["verb"].append(r.word(include_parts_of_speech=["verbs"]))
    print(collection)
    return collection

main()