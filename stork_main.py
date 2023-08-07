import stork_image
import stork_wikipedia
import stork_words
import stork_script
import stork_db


class Starting:
    @staticmethod
    def word_list():
        global collection
        print(
            "Would you like to use pre-set words or enter your own? Enter 'own' if you would like to enter your own. and hit enter otherwise."
        )
        if input() == "own":
            collection = stork_words.CustomWords.get_custom_words()
            return collection

        else:
            collection = stork_words.main()
            return collection

    @staticmethod
    def file_reader(user_id):
        print(
            "Please enter your madlib path. If you don't have one, press enter and we will grab one from Wikipedia."
        )
        path = input()
        try:
            with open(path, "r") as file:
                imported_ml = file.read().split()
                current = stork_script.Script(imported_ml, collection)

        except:
            print("We will grab one from Wikipedia.")
            with open("example.txt", "r") as file:
                imported_ml = stork_wikipedia.main()
                imported_ml = imported_ml.split()
                current = stork_script.Script(imported_ml, collection)

        stringy = ""
        for word in current.script:
            stringy += f" {current.replace_words(word)}"
        print(stringy)
        stork_db.insert_story(user_id, stringy)
        return stringy


class PictureBook:
    @staticmethod
    def make_book(stringy):
        stork_image.main(stringy)


def main():
    print(
        "Would you like to read a story or write one? Enter 'read' if you would like to read one. and hit enter otherwise."
    )
    choice = input()
    if choice == "read":
        print("Please enter your username.")
        username = input()
        try:
            stork_db.get_stories_by_username(username)
        except:
            user_id = stork_db.main()
    else:
        user_id = stork_db.main()
    Starting.word_list()
    PictureBook.make_book(Starting.file_reader(user_id))


main()
