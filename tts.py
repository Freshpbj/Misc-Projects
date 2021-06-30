import pyttsx3

engine = pyttsx3.init()  # object creation
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)   # changing index, changes voices. 0 for male, 1 for female
engine.say("What should I say?")
engine.runAndWait()
userwords = input('What should I say?  ')
engine.say(userwords)
engine.runAndWait()
