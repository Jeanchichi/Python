import speech_recognition as sr

r=sr.Recognizer()

with sr.Microphone() as source:
    print("Speak :")
    audio=r.listen(source)
    try:
        output=r.recognize_google_cloud(audio)
        print("you said :{}".format(output))

    except:
        print("I cant ecognizewhat u said pease speak clearly")
