import random

names = ["Peter", "Michell", "Jane", "Steve"]
places = ["Sofia", "Plovdiv", "Varna", "Burgas"]
verbs = ["eats", "holds", "sees", "plays with", "brings"]
nouns = ["stones", "cake", "apple", "laptop", "bikes"]
adverbs = ["slowly", "diligently", "warmly", "sadly", "rapidly"]
details = ["near the river", "at home", "in the park"]

def get_random_word(words):
    return random.choice(words)

print("Welcome to the Random Sentence Generator Game!")
input("Press the [Enter] key to Start the Game.")

while True:
    random_name = get_random_word(names)
    random_place = get_random_word(places)
    random_verb = get_random_word(verbs)
    random_noun = get_random_word(nouns)
    random_adverb = get_random_word(adverbs)
    random_detail = get_random_word(details)

    print (f"\n{random_name} from {random_place} {random_adverb} {random_verb} {random_noun} {random_detail}")
    input("Press the [Enter] key to continue.")