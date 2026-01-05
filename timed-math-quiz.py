import random
import time

OPERATORS = ["+", "-", "*"]
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_PROBLEMS = 10

def generate_problem():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expr = str(left) + " " + operator + " " + str(right)
    answer = eval(expr)
    return expr, answer

while True:
    wrong = 0
    input("This is a timed math test! Try to finish in the fastest time you can. \nFor every question you answer incorrectly 0.5 seconds is added to your total time.\nPress enter to start!")
    print("---------------------")

    start_time = time.time()

    for i in range(TOTAL_PROBLEMS):
        expr, answer = generate_problem()
        while True:
            guess = input("Problem #" + str(i + 1) + ": " + expr + " = ")
            if guess == str(answer):
                break
            wrong += 1
        
    end_time = time.time()
    deduction = 0.5
    total_time = round(end_time - start_time , 2)
    deducted_time = round(total_time - (deduction * wrong), 2)
        
    print("---------------------")
    print("Nice work! You finished in", total_time, "seconds! \nYou got", wrong, "wrong, so your final time is", deducted_time, "seconds.")

    replay = input("\nWould you like to play again? (y/n): ")
    if replay.lower != "y":
        print("\nThanks for playing!")
        break