names = [" " ]
name = input("welcome to magic 8 ball what is your name?")
while true:
    question = input(" please ask a yes or no question or type exit" )
    if question == "exit":
        break
    else:
    print ( name + random_answers)
import random
random_answers = [ "yes", "no", "its not certain", "have high hopes" ]
random.choice(random_answers)
time.sleep(3)
names.insert ( 1, "name")
