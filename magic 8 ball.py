import random
answers = ["It is certain", "It is decidedly so", "Without a doubt", "Yes definitely", "You may rely on it", "As I see it, yes", "Most likely", "Outlook good", "Yes", "Signs point to yes", "Reply hazy, try again", "Ask again later", "Better not tell you now", "Cannot predict now", "Concentrate and ask again", "Don't count on it", "My reply is no", "My sources say no", "Outlook not so good", "Very doubtful"]
print("Say your name: ")
name = input()
print("Hello", name, ",my name is Magic 8 Ball! And I know the answer to any of your questions.")
again = 'y'

while again.lower() == 'y':
    question = input('Ask your question: ')
    print(random.choice(answers))
    again = input('Will you ask one more question? (yes = y, no = n): ')
    
    if not again.lower() == 'y':
        print('Come back if you have any questions!')
