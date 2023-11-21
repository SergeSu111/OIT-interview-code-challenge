import random  # call the ramdom module for the random.choice() function

# I used about 40 minutes to finish and test all the code.


def display_word(word, guessed_letters):
    """This function returns a string using join function. if the ele in word and the ele in guessed_letter again.
        We put that in string instead of "_" """
    return ''.join([letter if letter in guessed_letters else "_" for letter in word])
    # return a string combined "_" and the letter if the letter in guessed_letters.


def game(list):
    """This function is the whole process of this game, passed a inputted list in it """
    print("Welcome to the picky game, just kidding. ")
    # initialized a set for guessed_letters. Because we don want duplicated letters.
    guessed_letters = set()
    # right is the letters we guess correctly, initialized 0 first
    right = 0
    # not_right is the letters we guess not correctly, initialized 0 first
    not_right = 0
    # use the random.choice() function to pick a random ele in list
    random_ele = random.choice(list)
    # get the number of random_ele
    total = len(random_ele)
    # this print function above shows the __________. because we have not guessed our letters.
    print("Hi, my dear user. there are " + str(total) + " letters in the word." + " letters: " +
          display_word(random_ele, guessed_letters))

    while right < len(random_ele):
        # while right = random_ele, which means we already guess all the right letter in this word
        guess_let = input("Please guess a letter in the word. I know you like it, don u?").lower()

        if guess_let in guessed_letters:
            print("Oh, you guessed this letter again.")
            continue  # skip the rest of this loop and go back to the while loop to guest again
        else:
            # else the guess_let is the first time to guess, so we add that in set.
            guessed_letters.add(guess_let)

        # because we pass the conditions before, so we know that the guess_let
        # is the first time we guess. we can evaluate if is in our random_ele.
        if guess_let in random_ele:
            # count() returns the number of guess in random_ele
            right += random_ele.count(guess_let)
            # instead the "__________" to the guess_corrected letter.
            print("Correct! " + display_word(random_ele, guessed_letters))
        else:
            # the guess is not right
            not_right += 1
            # show how many different letters we already guessed.
            print("Not correct, this is not the right letter; Guessed letters: " + " ".join(guessed_letters))

        # print how many times we already guessed totally, and how many tines for correct and incorrect.
        print("Guesses: " + str(right) + str(not_right) + ", Correct: " + str(right) + ", Incorrect: " + str(not_right))

    # final, user already guessed all right ele, out of loop and congratulate to users.
    print("Nice! You finished this game. You guessed the word " + random_ele + "in " + str(right) + str(not_right) +
          " guesses.")


if __name__ == '__main__':
    my_list = []  # create a empty list
    for i in range(10):  # loop 10 times because the length of list is 10
        ele = input("Please input a word in list")  # each time we input a word
        my_list.append(ele)  # we put the word in our list

    while True:
        game(my_list)  # so we can put our updated list in our function.
        again = input("Do you want to play again?").lower()
        if again != "yes":  # the reason we cant use again == "no" is that it could be no! or nooo. whatever.
            print("All right. thanks for playing the picky game.")
            break  # end of the loop.
