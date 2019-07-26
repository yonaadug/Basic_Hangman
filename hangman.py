import random

def pick_random(word_list):
    return random.choice(word_list);

def replace_char(string,letter,index):
    string_list = list(string)
    string_list[index] = letter
    return ''.join(string_list);

def guessProcess(hangman_word, blanks, guessed_letter, lives_left):

    if hangman_word.find(guessed_letter) == -1:
        lives_left = lives_left - 1
    while True:
        index = hangman_word.find(guessed_letter)

        if index == -1:
            break
        

        hangman_word = replace_char(hangman_word,'_',index)
        blanks = replace_char(blanks,guessed_letter,index)


    return hangman_word,blanks,lives_left;

def main():
    f = open("words.txt", "r")
    word_list = f.readlines()
    lives_left = 6

    hangman_word = pick_random(word_list)
    blanks = '_'*(len(hangman_word)-1)

    while True:

        print(hangman_word)
        print("Chances left: "+ str(lives_left))
        print("Guess a letter: " + blanks)

        guessed_letter = input("Letter: ")

        hangman_word, blanks, lives_left = guessProcess(hangman_word,blanks,guessed_letter,lives_left)

        print(blanks)

        if lives_left == 0:
            print("You lost. The word is: "+hangman_word)
            break;


if __name__ == "__main__":
    main()


