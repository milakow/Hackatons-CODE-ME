# Hackatons-CODE-ME

# Project Name: Hangman game

General info:

Project was created during first IT workshop classes. It contains code for popular game- Hangman.
User has to guess the password which is selected by the program by entering randomly letters. Another option is to enter whole words.

Step-by-step description:

First using "random" library the program picks a password from provided list. In below game list includes names of european cities.
Then the first message appears in which user is welcomed and informed of his chances to win. In other words the user gets information about amount of rounds in one game.
In order to show user number of letters in a guessing word the password type is changed from string to list. It allows to replace each letter with an underscore sign "_" based on the length of a password.
Using a loop "for" program asks user a letter and checks:

-if correct sign was written; it means if user wrote a letter, any digit or another sign; if users wrote a letter, program continues;

-the length of written marks; user has two option; he can provide program one single letter or word;

-if user picked one letter program checks if it is included in any password's position by string method find(); if the letter appears, program checking letter by letter save the data about its position in variable "index"; it is used to print provided by user letter in correct place; if user chose letter which has not appeared in the password, program informs him by displaying a message "Bad choice."

-if user tries to guess whole password, the program compares written word with password; if they match user, user will read a message "Exactly! You're a winner!"; if they do not match, user will see "You did not guess."; user can still try to guess next letter or whole password;

-user has just 10 chances to win; if he fails, he will see "Unfortunately you lost. Try another time."
