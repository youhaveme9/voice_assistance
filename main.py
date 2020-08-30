import pyttsx3
import datetime
import speech_recognition as sr
import os
import wikipedia
import webbrowser
import os
# initializing voice engine using pyttsx module
engine=pyttsx3.init('sapi5')
voices= engine.getProperty('voices')
print(voices[1].id)
engine.setProperty('voice',voices[1].id)

def speak(audio):
    # speaks given string
    engine.say(audio)
    engine.runAndWait()
    
def wishme():
    hour=int(datetime.datetime.now().hour)
    if(hour>=0 and hour<12):
        speak("Good Morning sir!!")
    elif(hour>=12 and hour<18):
        speak("Good Afternoon sir!!")
    else:
        speak("Good evening sir!!")
    speak("I am rennae, your personal assistance.")
    speak("How can I help!!")

def takecommand():
    # takes voice input from user and return output as string
    r=sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening....")
        r.pause_threshold = 1  # maximum pause time in voice
        audio = r.listen(source)
    try:
        print("Recognizing....")
        input1=r.recognize_google(audio, language='en-in')
        print("You said:", input1)
        speak(input)
    except Exception as e:
        print("Can't recognize you! Please Speak again")
        speak("Can't recognize you! Please Speak again")
        return "none"
    return input1
    



if __name__=="__main__":
    wishme()
    while(True):
        input1=takecommand().lower()
        
        if "wikipedia" in input1:
            speak("Searching wikipedia")
            input1=input1.replace("wikipedia", "")
            results=wikipedia.summary(input1, sentences=2)
            speak("According to wikipedia")
            print(results)
            speak(results)
            
        elif "open youtube" in input1:
            webbrowser.open("youtube.com")
        elif "open google" in input1:
            webbrowser.open("google.com")
        elif "open stacks overflow" in input1:
            speak("Stacksoverflow.com")
        elif "play music" in input1:
            music_d="D:\songs"
            song=os.listdir(music_d)
            print(song)
            os.startfile(os.path.join(music_d, song[0]))
        elif "the time" in input1:
            strtime=datetime.datetime.now().strftime("%H:%M:%S")
            print("The time is: ", strtime)
            speak(f"Sir, The time is {strtime}")
        elif "open code" in input1:
            speak("Opening VS code")
            os.startfile("C:\\Users\\night\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe")
        else:
            speak(f"you said {input1}")
            
        