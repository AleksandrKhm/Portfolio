def cheking():
    while True:
        action = input('Select the desired action (0 - encrypt, 1 - decrypt): ')
        try:
            action = int(action)
        except ValueError:
            print('Unable to process result, please try again!')
        else:
            if action in [0, 1]:
                break
            else:
                print('Unable to process result, please try again!')
    while True:
        type_alphabet = input('Select the desired alphabet(0 - ru, 1 - eng): ')
        try:
            type_alphabet = int(type_alphabet)
        except ValueError:
            print('Unable to process result, please try again!')
        else:
            if type_alphabet in [0, 1]:
                break
            else:
                print('Unable to process result, please try again!')
    while True:
        key = input('Select key: ')
        try:
            key = int(key)
        except ValueError:
            print('Unable to process result, please try again!')
        else:
            break

    return abs(action), abs(type_alphabet), abs(key)

def word_processing(action, type_alphabet, key):
    text = input('Enter text: ')
    punctuation = '123456789 !\"\'\/,.#$%^&*()_-=+№;:?*'
    if type_alphabet == 0:
        rus_lower_alphabet = 'абвгдежзийклмнопрстуфхцчшщъыьэюя'
        rus_upper_alphabet = 'АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ'
        if key > 32:
            key -= 32
        if action == 0:
            cipher_text = ''
            for c in text:
                if c in punctuation:
                    cipher_text += c
                elif c.islower():
                    cipher_text += rus_lower_alphabet[(rus_lower_alphabet.find(c) + key) % 32]
                else:
                    cipher_text += rus_upper_alphabet[(rus_upper_alphabet.find(c) + key) % 32]

            return print(cipher_text)
        else:
            decrypted_text = ''
            for c in text:
                if c in punctuation:
                    decrypted_text += c
                elif c.islower():
                    decrypted_text += rus_lower_alphabet[(rus_lower_alphabet.find(c) - key) % 32]
                else:
                    decrypted_text += rus_upper_alphabet[(rus_upper_alphabet.find(c) - key) % 32]

            return print(decrypted_text)
    else:
        eng_lower_alphabet = 'abcdefghijklmnopqrstuvwxyz'
        eng_upper_alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        if key > 26:
            key -= 26
        if action == 0:
            cipher_text = ''
            for c in text:
                if c in punctuation:
                    cipher_text += c
                elif c.islower():
                    cipher_text += eng_lower_alphabet[(eng_lower_alphabet.find(c) + key) % 26]
                else:
                    cipher_text += eng_upper_alphabet[(eng_upper_alphabet.find(c) + key) % 26]

            return print(cipher_text)
        else:
            decrypted_text = ''
            for c in text:
                if c in punctuation:
                    decrypted_text += c
                elif c.islower():
                    decrypted_text += eng_lower_alphabet[(eng_lower_alphabet.find(c) - key) % 26]
                else:
                    decrypted_text += eng_upper_alphabet[(eng_upper_alphabet.find(c) - key) % 26]

            return print(decrypted_text)

action, type_alphabet, key = cheking()
word_processing(action, type_alphabet, key)
