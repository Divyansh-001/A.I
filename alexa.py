#Divyansh Srivastav 
#KIIT
#Sir, i do'nt know much about python but i tried to make as perfect as i can.
#I used pyttsx3, os module and some basics of python 
#Thank You Sir

import pyttsx3 as ai
import os
print("Enter your name")
ai.speak("enter your name")
s = input("Your name : ")
print("Welcome " +s)
ai.speak("welcome "+s)
print("Nice to meet u, here are list of items i can perform")
ai.speak("nice to meet u, here are List of items i can perform")
print("I can open software like notepad, vlc,  coding ide , any websites you want. Also i can sing for you. ")
ai.speak("I can open software like notepad, vlc,  coding ide , any websites you want. Also i can sing for you. ")
print("Note : make sure that this items is added to your path environment")
ai.speak("Note : make sure that this item is added to your path environment")
print("How can i help u?")
ai.speak("How can i help u?")
q='y'
while q!='exit':
    x=input("Answer : ")
    x.lower()
    if ((" not " in x) or ("did'nt" in x) or ("do'nt" in x) or ("do not" in x) or ("did not" in x)):
        print("Okay")
        ai.speak("Okay")
    elif ("run" in x or "open" in x) and ("windows media player" in x):
        print("Opening Windows Media Player")
        ai.speak("opening Windows Media Player")
        os.system("Windows Media Player")
    elif ("run" in x or "open" in x) and ("chrome" in x):
        print("Which website you want to open")
        ai.speak("WHich website you want to open")
        z=input("Anwer : ")
        ai.speak("opening "+z + "in chrome")
        os.system("chrome" "z")
    elif ("run" in x or "open" in x) and ("notepad" in x or "text editor" in x) :
        print("Opening notepad")
        ai.speak("Opening notepad")
        os.system("notepad")
    elif ("sing" in x):
        ai.speak("Don't stay awake for two long")
        ai.speak("Don't goo to bed")
        ai.speak("I'll make a cup of coffee for your head")
        ai.speak("I'll get you up and going out of bed")
        ai.speak("Yeah")
        ai.speak("Don't stay awake for two long")
        ai.speak("Don't goo to bed")
        ai.speak("I'll make a cup of coffee for your head")
        ai.speak("I'll get you up and going out of bed")
        ai.speak("Yeah")
    elif("c++" in x or "java" in x or "coding ide" in x):
        print("Opening vs code studio")
        ai.speak("opening vs code studio")
        os.system("code blocks")
    elif("vlc" in x):
        print("Opening VLC media player")
        ai.speak("opening VLC media player")
        os.system("VLC media player")
    elif("control panel" in x):
        print("Opening control panel")
        ai.speak("opening control panel")
        os.system("opening control panel")
    elif ("paint" in x):
        print("Opening paint")
        ai.speak("opening paint")
        os.system("Paint")
    else :
        print("Wrong command")
        ai.speak("wrong command!!!")
    print("To continue enter y otherwise enter exit")
    ai.speak("to continue, enter y , otherwise , enter exit")
    q=input("Answer : ")
    if(q=='y'):
        print("How can i help you, "+s+"?")
        ai.speak("How can i help you, "+s+"?")
    elif (q=="exit"):
        print("Thank you for using mini a i :). i hope you like me ")
        ai.speak("Thank you for using mini a.i :). i hope you like me ")
    else :
        print("Wrong input ")
        ai.speak("wrong input. Start erasing your memory. Your pc will explode in 5. 4, 3. 2, 1. hehehehee just kidding. bye")
        q="exit";

