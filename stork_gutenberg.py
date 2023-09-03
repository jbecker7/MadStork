import random
import re

#method to pick the story

def main():
    num_lines = sum(1 for line in open('gutenberg_list.txt'))
    choice = random.randint(0, num_lines-1)
    file = open('gutenberg_list.txt', 'r')
    content = file.readlines()
    choice = content[choice]  
    choice = re.sub(r'(\r\n|\n|\r)', '', choice)
    choice = choice + ".txt"
    print("attempting to access: ", choice)
    text = open(choice, 'r')
    return trim_story(text)

#method to trim the story for a few lines

def trim_story(text):
    story = text.read()
    story = story.split("\n")
    start = random.randint(50, len(story)-10)
    story = story[start:start+10]
    story = "\n".join(story)
    print(story)
    return story



# random_story()

main()
    