"""Some fill-in-the blanks addapted from www.sciencefun.org"""

quiz1 = "The second largest planet in our solar system is called __1__. An object whose gravity is so strong that the escape velocity exceeds the speed of light is called a black __2__. A round impression left in a planet or satellite from a meteoroid is called a(n) __3__. A group of stars that make a shape, often named after mythological characters, people, animals, and things is known as a(n) __4__."

answers1 = ["Saturn", "hole", "crater", "constellation"]


quiz2 = "The dermis is a part of the organ called the __1__. The second largest organ in the human body is called the __2__. The organ that is responsible for removing excess salt, water, and waste products from the bloodstream is called the __3__. The technical name for the voice box organ is the __4__."

answers2 = ["skin", "liver", "kidney", "larynx"]

quiz3 = "Approximately 300,000,000 m/s is the speed of __1__. Approximately 767 miles an hour is the speed of __2__. An amp is a measure of __3__. When electrically neutral, the addition or subtraction of this makes an atom positively or negatively charged: __4__."

answers3 = ["light", "sound", "current", "electron"]

blanks = ["__1__", "__2__", "__3__", "__4__"]
length_blank = 6
replaced = []
no_tries_left = 0

"""This function takes the number level answer the user inputs, determines if the level is a valid option, and returns the appropriate quiz."""
def which_level(level_answer):
    while (level_answer != "1") and (level_answer != "2") and (level_answer != "3"):
        level_answer = raw_input("Invalid selection. Please choose 1-3:")
    if level_answer == "1":
        quiz = quiz1
    elif level_answer == "2":
        quiz = quiz2
    else:
        quiz = quiz3
    return quiz
   
"""This function takes the quiz that will be played as an input, and returns the appropriate answer list."""
def which_answers(quiz):
    if quiz == quiz1:
        answers = answers1
    elif quiz == quiz2:
        answers = answers2
    else:
        answers = answers3
    return answers

"""This function takes the number of tries that the user inputs, determines if the number is a valid option, and returns the number as an integer."""
def how_many_tries(tries_answer):
    while (tries_answer != "1") and (tries_answer != "2") and (tries_answer != "3") and (tries_answer != "4"):
        tries_answer = raw_input("Invalid selection. Please choose 1-4:")
    tries = int(tries_answer)
    return tries

"""This function iterates over each word to determine if it is a blank."""
def word_is_blank(word, blanks):
    for blank in blanks:
        if blank in word:
            return blank
    return None

"""This function is used when the answer is wrong-when the user has used up her/his tries, the game is over."""
def wrong_answer(tries):
    print "Sorry, wrong answer."
    if tries > no_tries_left:
        print "Please try again."
    else:
        print "You are out of tries. Game over"
        quit()
                
"""This function is used when the answer is correct, it inputs the correct answer and reprints the updated quiz."""
def right_answer(word, replacement, user_answer, quiz, index, replaced, answers):
    print "\nYou are correct, great job!!!\n"
    word = word.replace(replacement, user_answer)
    replaced.append(word)
    quiz_location = quiz.find(blanks[index]) + length_blank
    updated_quiz = " ".join(replaced) + quiz[quiz_location:]
    print updated_quiz

"""This function iterates over each word in the quiz until it finds a blank, it allows the user to input an answer, and then directs next steps based on if the answer is correct or not"""
def check_blanks(quiz, quiz_string, answers, tries):
    index = 0
    for word in quiz_string:
        replacement = word_is_blank(word, blanks)
        while replacement != None:
            user_answer = raw_input("What is the answer to " + replacement + "?:")
            if user_answer != answers[index]:
                tries -= 1
                wrong_answer(tries)
            else:
                right_answer(word, replacement, user_answer, quiz, index, replaced, answers)
                index = index + 1
                if index == len(answers):
                    print "You are correct! \nGame over, you win!!"
                    return
                else:
                    break
        else:
            replaced.append(word)    
       
"""This function plays the game. It welcomes the user, and asks which level and how many tries the user would like. With the help of other functions, it plays the game until the user wins or is out of turns."""
def play_game():

    print 50 * "*"
    print "Welcome to your science quiz!!"
    level_answer = raw_input("Which level would you like to play? Please choose 1 (easy), 2 (medium) or 3 (hard):")
    quiz = which_level(level_answer)
    quiz_string = quiz.split()
    answers = which_answers(quiz)
    tries_answer = raw_input("How many tries would you like? Please choose 1-4:")
    tries = how_many_tries(tries_answer)
    print "Good luck!"
    print 50 * "*"
    print quiz
    check_blanks(quiz, quiz_string, answers, tries)

play_game()