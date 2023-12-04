'''
[Case Study Story] --> 
Imagine the first day of university for a fresher named Alex. 
Alex is excited but also overwhelmed by the vast campus, numerous courses, and the sea of new faces. 
To aid new students like Alex, the university's IT department has developed a personalised chatbot. 
This chatbot, named "UniBuddy", is designed to make the transition smoother for fresher.
Upon accessing the chatbot, Alex is prompted to enter their name, favourite colour, and age. 
Based on this input, UniBuddy offers a personalised greeting.
For instance, if Alex's favourite colour is blue,
    UniBuddy might suggest joining the university's "Blue Art Club".
If Alex is 18, the chatbot might provide information about fresher-specific events.
The chatbot also offers a feature where Alex can input specific queries, like 
    "Where is the library?" or "How do I join the debate club?", 
        and UniBuddy responds with relevant information, all while adhering to a friendly tone,
        using string transformation methods to ensure the responses feel personalised and engaging.
'''


# Dictionary of clubs to be referred to in later, colour based, recommendations
clubs = {
    "solar" : "Our solar society, meeting on Tuesday evenings.",
    "football" : "Our football club, where our teams colours are red and black, meeting on Wednesday afternoons and Sunday mornings.",
    "comedy" : "Our comedy society, meeting on Thursday evenings.",
    "disney" : "Our Disney society, meeting on Wednesday afternoons.",
    "salsa" : "Our salsa dancing society, meeting on Tuesday and Friday evenings.",
    "reading" : "Our re(a)ding society, meeting on Sunday afternoons.",
    "juice" : "Our juice making society, meeting on a Thursday evening.",
    "sailing" : "Our sailing club, meeting on Saturdays.",
    "pumpkin" : "Our pumpkin carving society, which meets all throughout October.",
    "brass band" : "Our brass band society, meeting on a Monday evening.",
    "bell ringing" : "Our bell ringing society, meeting on Sunday afternoons.",
    "environment" : "Our environment society, meeting on Monday evenings.",
    "swimming" : "Our swimming club, which host both water sports and games on a daily basis.",
    "skydiving" : "Our skydiving society, meeting on Saturdays.",
    "knitting" : "Our knitting and crochet society, meeting on Wednesday afternoons.",
    "board game" : "Our board gaming society, meeting on Thursday evenings and some Sundays.",
    "astronomy" : "Our astronomy society, meeting on Saturday evenings.",
    "anime" : "Our anime and manga society, meeting on a Tuesday evening.",
    "crafts" : "Our our crafts society, meeting on Sunday afternoons.",
    "flower" : "Our flower arranging society, meeting on a Monday afternoon.",
    "baking" : "Our baking society, meeting on a Sunday afternoon",
    "gardening" : "Our gardening society, meeting on a Thursday afternoon",
    "hummus" : "Our hummus appreciation society, meeting on a Tuesday evening",
    "painting" : "Our painting society, meeting on various days throughout the week depending on your medium of choice"
    }

# Dictionary of events to be referred to in later, age based, recommendations
events = {
    "escape room" : "If you enjoy solving puzzles, come join an escape room attempt on Monday or Wednesday evening.",
    "pub quiz" : "If you like to test your general knowledge, we have a range of themed quizzes on throughout the week at the SU bar.",
    "speed dating" : "If you're looking for love, head on down to our speed-dating event this Thursday evening.",
    "welcome talks" : "We recommend all Freshers join one of our Welcome Talks to help you find your feet, on every weekday at 1pm in the Main Hall this week.",
    "fair" : "Come check out the recommended societies, plus many more, and learn all about life here at our Freshers Fair this Saturday afternoon.",
    "comedy" : "Fancy a laugh? Come watch our comedy night on Tuesday.",
    "day trip" : "Want to see more of our town? Join one of our day trips on Monday, Wednesday or Friday afternoon.",
    "cooking" : "New to uni life, and new to cooking? We have classes on every afternoon this week to show you the basics.",
    "nights out" : "Each night of the week we have deals at a different nightclub in town, see the deals online.",
    "student raid" : "Student Raid - Our biggest night of the year, buy a ticket, get the route and join us around town."
}



# Initialise message, for first time start - asking user to enter name, age and favourite colour, followed by a welcome message
# While loop in case of unrecognised colour
while True:
    print('''
Welcome to UniBuddy! 

Your all-in-one app that makes your fresher journey a bit easier to navigate!

Please answer my questions below to get started.
    ''')

    user_name = input("Please enter your name: ").capitalize()
    user_age = int(input("Please enter your age: "))
    fav_colour = input("Please enter your favourite colour: ").lower()

    print(f"""
Welcome {user_name}, I have a few suggestions based on your choices.

As you like the colour {fav_colour}, I recommend you check out the following clubs and societies:
    """)


    # If-elif-else statements to suggest clubs and societies based on the users favourite colour
    if fav_colour == 'red':
        
        print(f"""
1. {clubs.get("football")}
2. {clubs.get("comedy")}
3. {clubs.get("disney")}
4. {clubs.get("salsa")}
5. {clubs.get("reading")}
    """)
        break
        
    elif fav_colour == 'orange':

        print(f"""
1. {clubs.get("juice")}
2. {clubs.get("solar")}
3. {clubs.get("salsa")}
4. {clubs.get("sailing")}
5. {clubs.get("pumpkin")}
    """)
        break

    elif fav_colour == 'yellow':

        print(f"""
1. {clubs.get("solar")}
2. {clubs.get("brass band")}
3. {clubs.get("bell ringing")}
4. {clubs.get("flower")} 
5. {clubs.get("hummus")}
    """)
        break
        
    elif fav_colour == 'green':

        print(f"""
1. {clubs.get("environment")}
2. {clubs.get("gardening")}
3. {clubs.get("juice")}
4. {clubs.get("football")} 
5. {clubs.get("painting")}
    """)
        break
        
    elif fav_colour == 'blue':

        print(f"""
1. {clubs.get("sailing")}
2. {clubs.get("swimming")}
3. {clubs.get("skydiving")}
4. {clubs.get("knitting")}
5. {clubs.get("board game")}
    """)
        break

    elif fav_colour == 'purple':

        print(f"""
1. {clubs.get("astronomy")}
2. {clubs.get("anime")}
3. {clubs.get("crafts")}
4. {clubs.get("baking")}
5. {clubs.get("board game")}
    """)
        break
        
    else:
        print("Sorry, I do not have recommendations for that colour, please try again.")
        continue

# If-elif-else statements to suggest events based on the users age
if user_age <= 19:

    print("Here are some events that may be of interest to our new Freshers!")
    print(f"""
{events.get("welcome talks")}
{events.get("fair")}
{events.get("nights out")}
{events.get("student raid")}
{events.get("cooking")}      
""")

elif user_age <= 25:
    print("Here are some events that may be of interest to our returning students!")
    print(f"""
{events.get("fair")}
{events.get("nights out")}
{events.get("student raid")}
{events.get("pub quiz")}
{events.get("comedy")}
""")
    
else:
    print("Here are some events that may be of interest!")
    print(f"""
{events.get("day trip")}
{events.get("pub quiz")}
{events.get("comedy")}
{events.get("escape room")}
{events.get("speed dating")}
""")

# FAQ; frequently asked questions
# while loop until user has no questions; if-elif-else statements to answer given questions
while True:

    question = input("Is there anything you would like to ask me? (type 'q' to quit): ").lower().replace("?", "")

    if question == "how is your day":
        print("I exist, so my day is going rather well!")
        continue

    elif question == "how can i join a club":
        print("""
If you wish to join a club or society, you can visit their stall at the Freshers Fair this weekend.
Alternatively, check out the SU website, where all the club details are listed - including how you can attend a first session to join!
    """)
        continue

    elif question == "where is the library":
        print("""
Looking to begin studying already? The library is the big red building right next to our wonderful, central water fountain.
Signposts around campus can point you the right way!
    """)
        continue

    elif question == "how long should i boil an egg for":
        print("""
What kind of egg are you looking for?
For a soft boiled egg, I would let it boil for around 5 minutes, and for hard boiled more towards 10!
    """)
        continue

    elif question == "what time is breakfast":
        print("""
Ah, the most important meal of the day!
Breakfast can be bought from our canteens from 7am to 11am.
    """)
        continue

    elif question == "q":
        print("No more questions for me? Enjoy your day!")
        break