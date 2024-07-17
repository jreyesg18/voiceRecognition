import speech_recognition as sr

recognizer = sr.Recognizer()

mic = sr.Microphone()

with mic as Source:

    audio = recognizer.listen(source)

text = recognizer.recognize_google(audio, language = 'es')

print(f"Has dicho: “ {text}")