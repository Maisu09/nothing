import pandas
import random


def next_card(to_learn):
    current_card = random.choice(to_learn)
    print(current_card['French'] + ' == ' + current_card['English'])



def main():
    data = pandas.read_csv("data/french_words.csv")
    to_learn = data.to_dict(orient="records")
    next_card(to_learn)



if __name__ == main():
    main()