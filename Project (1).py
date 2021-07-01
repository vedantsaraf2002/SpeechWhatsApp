
# To run this program first you have to install speechrecognition, pyaudio, datetime, pywhatkit modules through Command Prompt/Terminal.

import speech_recognition as s  #Installed Speech recogition and pyaudio module for voice input.
import datetime                 #Installed datetime module to capture current time.
import pywhatkit as py          #Installed pywhatkit module to use 'sendwhatmsg' function.
phone_number = int(input())     #To take Receiver's whatsapp phone number. 

# Speech Recognition Code
sr=s.Recognizer()               
print("speak...")
with s.Microphone() as s:                        #To use system microphone.
    sr.adjust_for_ambient_noise(s,duration=0.6)  #To cancel background noise.
    audio=sr.listen(s,timeout=None)             
    query=sr.recognize_google(audio,language='en-IN')  #Query stores the text format of the audio.
    print(query)       

#To capture current time.
current_time = datetime.datetime.now()
current_hour = current_time.hour
current_minute = current_time.minute + 2

#sendwhatmsg Function to send the text format of the recorded audio.

py.sendwhatmsg(f"+91{phone_number}",query,current_hour,current_minute) 
 
