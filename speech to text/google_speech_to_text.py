import speech_recognition as sr
cred="AIzaSyCRptLxqzkiWw4JBwIefCcMuKDJaWGwadE"
with sr.AudioFile("output.wav") as source:

	print(sr.Recognizer().recognize_google(sr.Recognizer().record(source), cred))