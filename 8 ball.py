import sys
import random
import time

print ("Hello! Welcome to the Magiical 8 ball!")
play = input("Would you like to play? yes or no - ")
if play != 'yes':
    print ("Fine! I didn't want to play with you anways:(")
    print ("Please close out of application, thank you.")
    sys.exit()
else:
    print("Okay, Great!")

name = input("To start things off. What is your name? ")
print (f"Hello {name}.")
age = input("What is your age? ")
if age >='0':
    print("Alright, perfect!")
else:
    print ("PLEASE enter a valid age.")
    age = input ("What is your age? ")
    if age >='0':
        print("Alright, perfect!")
    else:
        print("Rebel huh? Exit program.")
        quit()
        
values_responses = [1,2,3,4,5,6,7,8,9,10,11,12]
values_loading = [1,2,3,4,5,6,7,8,9]
values_greetings = [1,2,3,4,5,6,7]
value_sentences = [1,2,3]                
loading = ["*thinks*...","hmmmmmm...","Checking my sources...","Searching...","One second...","Please be patient...","interesting...","uno momento...","aha!..."]
responses = ["          Only the future will tell","          The answer lies in the future","          Ask again later","          404 Not Found","          Most likley","          No","          Yes","          Maybe","          Probably Not","          Who knows","          Calling 911","          Why don't you ask me later"]
greetings = ["Good question,","Great Question!","Interesting...","Alright,","Okay","Alright,","You can ask me any question and you ask me that?? Whatever"]
sentences = [" I will now take 3 useless seconds of your life to randomly generate my answer.","I will look into my sources.","I don't know if i have the answer to that.."]
time.sleep(2)

question = input("Would you like to ask a question? yes or no - ")
while question == "yes":
    greet_choice = random.choice(greetings)
    delay = random.choice(sentences)
    question = input("Ask me any question you'd like: ")
    print(f"{greet_choice} {delay}")
    time.sleep(3)
    print(random.choice(loading))
    time.sleep(2)
    print("                                                                                              ")
    print(random.choice(responses))
    
    print("------------------------------------------------------------")
    question = input("Would you like to ask another question? yes or no - ")
    
