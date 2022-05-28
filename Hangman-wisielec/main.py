#miasta do listy: 'prague', 'dubrovnik', 'barcelona', 'bratislava', 'lisbon', 'budapest'
# def pick_password_comp():
import random
password_list = ['cracow' ]
chosen_password = random.choice(password_list)
    # return chosen_password

# print(type(chosen_password))
# pick_password_comp()
# user_name = input('Hello. What\'s your name? ')
# print(len(chosen_password))

chosen_password_list = list(chosen_password)
print(chosen_password_list)
password_line = []
for letter in range(len(chosen_password_list)):
    password_line.append("_")
print(*password_line)

for rnd in range(10):   # nr rundy
    user_choice = str(input('Pick a letter: '))
    # if not user_choice.isalpha():
    #     print('Podałeś zły znak.')
    index = 0
    if len(user_choice) == 1:
        if chosen_password.find(user_choice) != -1:
            for letter in chosen_password_list:
                if user_choice == letter:
                    password_line[index] = letter
                index += 1
        else:
            print('Bad choice.')
    else:
        if user_choice == chosen_password:
            print('Exactly! You\'re a winner!')
            break
        else:
            print('You did not guess.')
    print(*password_line)

print('Unfortunately you lost. Try another time.')





