import random
import time


random_answers = [ "yes", "no", "its not certain", "have high hopes" ]

name = input("welcome to magic 8 ball what is your name?")
name_as_str = str(name)
while True:
    question = input(" please ask a yes or no question or type e[x]it" )
    if question ==("x"):
        break
    else:
        time.sleep(3)
        print(f"Hi {name} My response to you is {random.choice(random_answers)}")




