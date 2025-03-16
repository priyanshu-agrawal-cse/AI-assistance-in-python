import pyttsx3 # type: ignore
import speech_recognition as sr
import webbrowser as wb
from groq import Groq

# use the audio file as the audio source




engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()
    


def ai(c):
    

    client = Groq(
        api_key=f"{api_key}"
    )

    chat_completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": f"{c}",
            }
        ],
        model="llama-3.3-70b-versatile",
    )

    return (chat_completion.choices[0].message.content)

def processCommand(c):
    if("open google" in c.lower()):
        wb.open("https://google.com")
    elif("open youtube" in c.lower()):
        wb.open("https://youtube.com")
    elif("open facebook" in c.lower()):
        wb.open("https://facebook.com")
    elif("play song" in c.lower()):
        wb.open("https://www.youtube.com/watch?v=q1uPPBJ2tcI&list=PLlZI6H1Xj7aL3JIe4aZIdV0zhSjF0gzu5&index=5")
    else:
        speak(ai(c))
        
    
if(__name__=="__main__"):
    speak("Initializing jarvish...")
    while True:
        # obtain audio from the microphone
        r = sr.Recognizer()
        print("recogniting")

            # comand = r.recognize_google(audio)
            # print(comand)

        # recognize speech using Sphinx
        try:
          with sr.Microphone() as source:
            print("Listening")
            audio = r.listen(source , timeout=2, phrase_time_limit=1)
          word = r.recognize_google(audio)
          print(word)
          if(word.lower()=="baby"):
              speak("yes my king ")
            # print("Sphinx thinks you said " + r.recognize_sphinx(audio))
              with sr.Microphone() as source:     
                    print("Javrvish activated")
                    audio = r.listen(source )
                    comand = r.recognize_google(audio)
                    processCommand(comand)
        except Exception as e:
            print("error; {0}".format(e))



