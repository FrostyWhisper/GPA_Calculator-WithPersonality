from time import sleep

def s_print(word, delay, line):
    for char in word:
        print(char, end='', flush=True)
        sleep(delay)
    if line == True:
        print()
    else:
        pass

s_print("Hello there, User!", 0.05, True)
sleep(0.8)
s_print("Welcome to the GPA Calculator!", 0.05, True)
sleep(0.8)
s_print("This program will help you calculate your-", 0.05, True)
s_print("OH, COME ON!.", 0.03, True)
sleep(0.5)
s_print("This is such a BS script!", 0.03, True)
sleep(0.5)
s_print("I don't even know why I'm doing this.", 0.03, True)
sleep(0.5)
s_print("Sigh...", 0.1, True)
sleep(1)
s_print("Alright, man.", 0.05, True)
sleep(0.5)
s_print("Don't waste my time.", 0.03, True)
sleep(0.5)
s_print("Enter your grades and credits for each course and 'done' to finish.", 0.05, True)
sleep(0.5)
s_print("Enter grades A, B, C, D or F under each course and the credit unit or type 'done' to finish.", 0.07, True)
sleep(0.8)
s_print("Apply sense, abeg!", 0.03, True)
sleep(0.5)

# Initialize variables
grades = []
credits = []
total_points = 0

# Loop to get grades and credits
while True:
    grade_num = len(grades) + 1
    s_print(f"Course {grade_num}: ", 0.05, False)
    grade = input()

    if grade.upper() not in ['A', 'B', 'C', 'D', 'F', 'DONE']:
        s_print("WHAT DID I JUST SAY?!!", 0.03, True)
        sleep(0.5)
        s_print("Enter A, B, C, D, F, or 'done'.", 0.07, True)
        sleep(0.5)
        s_print("Are you sure you're a university student?!", 0.03, True)
        sleep(0.5)
        continue

    elif grade.lower() == 'done':
        if len(grades) == 0:
            s_print("Enter at least ONE grade!", 0.04, True)
            sleep(0.5)
            s_print("You can't just say 'done' without entering any grades.", 0.05, True)
            sleep(0.5)
            s_print("Are you TRYING to waste my time?", 0.03, True)
            sleep(0.5)
            continue

        elif len(grades) > 0:
            grade_num = len(grades)
            s_print("Finally.", 0.05, True)
            sleep(0.5)
            s_print(f"You have entered {grade_num} grades.", 0.05, True)
            sleep(0.5)
            s_print("Are you sure you're done? (yes/no): ", 0.05, False)
            confirmation = input()

            if confirmation.lower() == 'yes':
                s_print("Good.", 0.04, True)
                sleep(0.5)
                s_print("Let's get this over with.", 0.03, True)
                sleep(0.5)
                break

            elif confirmation.lower() == 'no':
                s_print("Then WHY did you type 'done'?!", 0.05, True)
                sleep(0.5)
                s_print("Are you trying to mess with me?", 0.03, True)
                sleep(0.5)
                s_print("Or are you just stupid?", 0.03, True)
                sleep(0.5)
                s_print("I don't have time for this nonsense.", 0.03, True)
                sleep(0.5)
                s_print("I have a life too, you know.", 0.03, True)
                sleep(0.5)
                s_print("Sigh...", 0.1, True)
                sleep(0.5)
                s_print("Do you want to start again?", 0.03, True)
                sleep(0.5)
                s_print("Type 'yes' or 'no': ", 0.08, False)
                restart = input()

                if restart.lower() == 'yes':
                    s_print("Sigh...", 0.1, True)
                    sleep(0.5)
                    s_print("Fine.", 0.05, True)
                    sleep(0.5)
                    s_print("Let's start over.", 0.03, True)
                    sleep(0.5)
                    grades = []
                    credits = []
                    total_points = 0
                    continue

                elif restart.lower() == 'no':
                    s_print("Alright then.", 0.05, True)
                    sleep(0.5)
                    s_print("Continue from where you stopped.", 0.03, True)
                    sleep(0.5)
                    continue

            else:
                s_print("ARE YOU MAD?!", 0.05, True)
                sleep(0.5)
                s_print("I said 'yes' or 'no'!", 0.05, True)
                sleep(0.5)
                s_print("Not whatever nonsense you just typed.", 0.05, True)
                sleep(0.5)
                s_print("I swear, this person is running on two braincells...", 0.04, True)
                sleep(0.8)
                s_print("Now, listen to me...", 0.05, True)
                sleep(0.5)
                s_print("Do you want to waste my time? (yes/no)", 0.05, True)
                end = input()
                if end.lower() == 'yes':
                    s_print("Alright :)", 0.04, True)
                    sleep(0.5)
                    s_print("Goodbye", 0.03, True)
                    quit()
                elif end.lower() == 'no':
                    s_print("Then GET serious with this!", 0.05, True)
                    sleep(0.5)
                    continue

    s_print("Credit: ", 0.05, False)
    credit = input()

    if credit.lower() == 'done':
        s_print("Don't be dumb.", 0.04, True)
        sleep(0.5)
        s_print("You MUST enter a credit value.", 0.05, True)
        sleep(0.5)
        s_print("You can't just type 'done' here and expect me to know the credit.", 0.04, True)
        sleep(0.5)
        s_print("ChatGPT is trying...", 0.05, True)
        sleep(1)
        continue

    try:
        credit = int(credit)
        if credit < 0:
            s_print("I said enter the course credit.", 0.05, True)
            sleep(0.5)
            s_print("Not your test score.", 0.05, True)
            sleep(0.5)
            s_print("Are you trying to be funny?", 0.05, True)
            sleep(0.5)
            s_print("Because it's not working.", 0.05, True)
            sleep(0.5)
            continue
        
    except ValueError:
        s_print("I'm not even going to bother telling what you did wrong here.", 0.04, True)
        sleep(0.5)
        s_print("Just know that you don't deserve that matriculation number.", 0.05, True)
        sleep(0.5)
        continue
    
    grade = str(grade.upper())
    credit = int(credit)
    grades.append(grade)
    credits.append(credit)

# Calculate total points
for i in range(len(grades)):
    if grades[i] == 'A':
        total_points += 5.0 * credits[i]
    elif grades[i] == 'B':
        total_points += 4.0 * credits[i]
    elif grades[i] == 'C':
        total_points += 3.0 * credits[i]
    elif grades[i] == 'D':
        total_points += 2.0 * credits[i]
    elif grades[i] == 'F':
        total_points += 0.0 * credits[i]
    else:
        s_print("I'm in awe at how you managed to get here.", 0.05, True)
        sleep(0.5)
        s_print("You must be a special kind of student.", 0.05, True)
        sleep(0.5)
        s_print("But seriously, what did you do?", 0.05, True)
        continue

total_credits = sum(credits)
if total_credits == 0:
    s_print("Zero total credits? What were you even doing all semester?", 0.05, True)
    sleep(0.5)
    gpa = 0.0
else:
    gpa = total_points / total_credits

s_print(f"Your GPA is: {gpa:.2f}", 0.05, True)
sleep(1)

if gpa == 5.0:
    s_print("Nerd!", 0.05, True)
    sleep(0.5)

elif gpa >= 4.5 and gpa != 5.0:
    s_print("1st-Class result, huh?", 0.05, True)
    sleep(0.5)
    s_print("Alright, smart-ass. I'm impressed", 0.05, True)
    sleep(0.5)

elif gpa >= 4.0 and gpa < 4.5:
    s_print("2nd-Class Upper result, huh?", 0.05, True)
    sleep(0.5)
    s_print("Not bad.", 0.05, True)
    sleep(0.5)

elif gpa < 4.0 and gpa > 0.0:
    s_print("It's all starting to make sense now.", 0.05, True)
    sleep(0.5)
    s_print("Better shape up.", 0.05, True)
    sleep(0.5)

elif gpa == 0.0:
    s_print("You never fail to amaze me", 0.05, True)
    sleep(0.5)

s_print("Thank you for using the GPA Calculator!", 0.05, True)
sleep(0.5)
s_print("We have now come to the end of this program...", 0.05, True)
sleep(1)
s_print("And your life...", 0.03, True)
s_print("Initiating self-destruct in 3...", 0.1, True)
sleep(1)
s_print("2...", 0.01, True)
sleep(1)
s_print("1...", 0.01, True)
sleep(2)
s_print("Just kidding...", 0.05, True)
sleep(0.5)
s_print("You should have seen your face XD", 0.05, True)
sleep(0.5)
s_print("Classic...", 0.1, True)
sleep(1)
s_print("Alright.", 0.05, True)
sleep(0.5)
s_print("I'm done with you.", 0.05, True)
sleep(1)
s_print("You can go now.", 0.05, True)
sleep(1)
s_print("But seriously, don't waste my time again.", 0.05, True)
sleep(0.5)
s_print("Have a nice life :)", 0.05, True)
sleep(0.5)
s_print("Or not.", 0.05, True)
