import speech_recognition as sr
import webbrowser
import os
import urllib
try :
    url = "https://www.google.com"
    urllib.urlopen(url)
    status = "Connected"
except :
    status = "Not Connected"
#print status


if status=="Connected" :
	bashCommand = "arecord --format=S16_LE --duration=10 --rate=16000 output.wav"
	os.system(bashCommand)

	cred="AIzaSyCRptLxqzkiWw4JBwIefCcMuKDJaWGwadE"

	with sr.AudioFile("output.wav") as source:

		a=sr.Recognizer().recognize_google(sr.Recognizer().record(source), cred)

	print a

else:
	r = sr.Recognizer()  
	with sr.Microphone() as source:
		os.system("clear") 
   		print("Please wait. Calibrating microphone...")  
   # listen for 1 seconds and create the ambient noise energy level  
   		r.adjust_for_ambient_noise(source, duration=1)  
   		print("Say something!")  
   		audio = r.listen(source)  
   
 # recognize speech using Sphinx  
	try:  
   		print("You said '" + r.recognize_sphinx(audio) + "'")  
	except sr.UnknownValueError:  
   		print("Could not understand audio")  
	except sr.RequestError as e:  
   		print("Error; {0}".format(e))

