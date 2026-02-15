 #import th erandom module 
import random


#Create subject
subjects = [
    "Shah Rukh Khan",
    "Virat Kohli",
    "Nirmala Sitharaman",
    "A Mumbai cat",
    "An overconfident startup founder",
    "That one uncle from WhatsApp",
    "A confused AI chatbot",
    "Auto-rickshaw driver with life wisdom",
    "Bollywood paparazzi",
    "A bored engineering student",
    "Street dog with political opinions",
    "Mumbai local train at peak hour"
]

actions = [
    "launches",
    "cancels",
    "eats",
    "accidentally invents",
    "rage quits",
    "announces on Twitter",
    "forgets about",
    "argues with",
    "cries over",
    "celebrates",
    "blames the government for",
    "explains using cricket analogy"
]

places_or_things = [
    "at the red carpet",
    "at Ganga ghat",
    "during a Zoom meeting",
    "inside a Mumbai local",
    "on Instagram Live",
    "at 3 AM with chai",
    "in front of confused reporters",
    "while traffic police watches silently",
    "at a wedding buffet",
    "during India-Pakistan match",
    "on national television by mistake",
    "in a serious press conference"
]

#start the headline generation loop

while True:
    subject= random.choice(subjects)
    action= random.choice(actions)
    places_or_thing= random.choice(places_or_things)
    
    headline= f"BREAKING NEWS: {subject} {action} {places_or_thing}"
    print("\n"+ headline)
    
    
    userinput= input("Do u want another headline (yes/no)").strip()
    
    if userinput!="yes":
        break

print("\n ----Thanks for using fake news generator---- ")