import speech_recognition as sr
cred=""
with sr.AudioFile("output.wav") as source:

	print(sr.Recognizer().recognize_google(sr.Recognizer().record(source), cred))
