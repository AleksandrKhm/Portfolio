import random

word_list = ["Ted", "Marshall", "Robin", "Barney", "Lily", "Tracy", "Sophie", "Jesse", "Valentina", "Sid", "Charlie", "Ellen"]
def get_word():
    word = random.choice(word_list)
    return word.upper()
def display_hangman(tries):
    stages = [
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]
def play(word):
    word_completion = "_" * len(word)
    guessed = False
    guessed_letters = []
    guessed_words = []
    tries = 6

    print('Guess the name of the character from the TV show :"How I Met Your Mother"')
    print(display_hangman(tries))
    print(word_completion)
    print()

    while not guessed and tries > 0:
        guess = input("Enter full word or letter: ").upper()
        if len(guess) == 1 and guess.isalpha():
            if guess in guessed_letters:
                print("You already called the letter", guess)
            elif guess not in word:
                print("Letter", guess, "is not in the word.")
                tries -= 1
                guessed_letters.append(guess)
            else:
                print('Great job, letter', guess, 'is in the word!')
                guessed_letters.append(guess)
                word_as_list = list(word_completion)
                indices = [i for i in range(len(word)) if word[i] == guess]
                for index in indices:
                    word_as_list[index] = guess
                word_completion = ''.join(word_as_list)
                if '_' not in word_completion:
                    guessed = True
        elif len(guess) == len(word) and guess.isalpha():
            if guess in guessed_words:
                print('You already called the word', guess)
            elif guess != word:
                print('Word', guess, 'is not correct.')
                tries -= 1
                guessed_words.append(guess)
            else:
                guessed = True
                word_completion = word
        else:
            print('Введите букву или слово.')
        print(display_hangman(tries))
        print(word_completion)
        print()
    if guessed:
        print('Congratulations, you guessed the word! You win!')
    else:
        print("You didn't guess the word. The hidden word was " + word + '. Maybe next time!')
again = 'y'

while again.lower() == 'y':
    word = get_word()
    play(word)
    again = input('Are we playing again? (y = yes, n = no):')
