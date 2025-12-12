import speech_recognition as sr
import webbrowser
import pyttsx3

recognizer = sr.Recognizer()
engine = pyttsx3.init()


def speak(text):
      engine.say("i will speak this text")
      engine.runAndWait()
    

if __name__ == "__main__":
      speak("initializing circuit.....")

      # Listen for the wake woard "circuit"
      # obtain audio from the microphone
      while True:
            with sr.Microphone() as source:
                  print("listening......")
                  audio = recognizer.listen(source)

            # recognize speech using Google Speech Recognition
            try:
                  print("Google thinks you said: " + recognizer.recognize_google(audio))
                  if "circuit" in recognizer.recognize_google(audio).lower():
                        speak("circuit is now active")
                        break
            except sr.UnknownValueError:
                  print("Google could not understand audio")
            except sr.RequestError as e:
                  print("Could not request results from Google Speech Recognition service; {0}".format(e))
      r = sr.Recognizer()
      with sr.Microphone() as source:
            print("say sompthing!")
            audio = r.listen(source)

            #reconize speech using sphinx
            try:
                  print("sphinx thinks you said: " + r.recognize_sphinx(audio))
            except sr.UnknownValueError:
                  print("sphinx could not understand audio")
            except sr.RequestError as e:
                  print("sphinx error; {0}".format(e))
