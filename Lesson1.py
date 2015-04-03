import random

file = open("stop-words.txt")
stopwords = file.readlines()

openings = ["Hello", "Hi", "Hey"]
questions = ["What are you up to?", "How are you?", "What are your hobbies"]
response = ["I dunno", "Yes", "No", str.upper("Maybe")]

for word in stopwords:
    next = word.strip("you")
    print(next)

while True:
    text = raw_input("Begin: ")
    filtered = text.replace("name", " <beep> ")
    print("Your filtered text was: " + filtered)
    
    if text in openings:
    		random_openings = random.choice(openings)
    		print(random_openings)

    elif text in questions:
            random_questions = random.choice(questions)
            print(random_response)

    else:

    		print("Uh unsure")