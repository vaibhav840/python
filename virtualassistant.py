import pyttsx3 #pip install pyttsx3
import speech_recognition as sr #pip install speechRecognition
import datetime
import wikipedia #pip install wikipedia
import webbrowser
import os
import smtplib
import sys
import random
# import requests
import json, pyowm
import pywhatkit as kit

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
# print(voices[1].id)
engine.setProperty('voice', voices[0].id)


owm = pyowm.OWM('28f04955531a966b1b575e9cbfee84ae')  # provide a valid API key

url = 'https://www.sms4india.com/api/v1/sendCampaign'

def sendPostRequest(reqUrl, apiKey, secretKey, useType, phoneNo, senderId, textMessage):
  req_params = {
  'apikey':apiKey,
  'secret':secretKey,
  'usetype':useType,
  'phone': phoneNo,
  'message':textMessage,
  'senderid':senderId
  }
  return requests.post(reqUrl, req_params)

# response = sendPostRequest(URL, 'R6RE2UN9DBUY39728KSK7ZK5JS0LLJ8G', '3LB55DGL8T47TOYJ', 'stage',phoneNo,"SMSIND", textMessage )

def speak(audio):
    engine.say(audio)
    engine.runAndWait()


def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!, vaibhav sir")

    elif hour>=12 and hour<18:
        speak("Good Afternoon!, vaibhav sir")   

    else:
        speak("Good Evening!, vaibhav sir")  

    speak("i am jarvis how can i help you ")       

def takeCommand():
    #It takes microphone input from the user and returns string output

    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.pause_threshold = 0.5
        audio = r.listen(source)

    try:
        print("Recognizing...")    
        query = r.recognize_google(audio, language='en-in')
        print(f"User said: {query}\n")

    except Exception as e:
        print(e)    
        print("Say that again please...")  
        return "None"
    return query

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.login('vaibhavvermaa461@gmail.com', 'veersoni')
    server.sendmail("vaibhavvermaa461@gmail.com", to, content)
    server.close()

if __name__ == "__main__":
    wishMe()
    while True:
    # if 1:
        query = takeCommand().lower()

        # Logic for executing tasks based on query

        if 'wikipedia' in query:
            speak("ofcourse ,please wait searching wikipedia")
            quermy = query.replace("wikipedia", "")
            results = wikipedia.summary(query, sentences=2)
            speak("According to Wikipedia")
            print(results)
            speak(results)
            sys.exit()

        elif 'youtube' in query:
            speak("ofcourse ,please wait")
          
            webbrowser.open("youtube.com")
            sys.exit()
        elif 'google' in query:
            speak("ofcourse ,please wait")
            webbrowser.open("google.com")
            sys.exit()

        elif "the time" in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S") 
            print(strTime)
            speak(f"sir,the time is: {strTime}")     

        elif "ok" in query:
            speak("want anything more")
            
        elif "open vs code" in query:
            speak("ofcourse ,please wait")
            codepath = "C:\\Users\\JAI HIND\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe"
            os.startfile(codepath)
            sys.exit()

        elif 'send email' in query:
            try:
                speak("to whom do u wanna send")
                recipient = takeCommand()
                if "Vaibhav" in recipient:
                    to = "vaibhavvermaa461@gmail.com"
                    speak("what should i say")
                    content = takeCommand()    
                    sendEmail(to, content)
                    speak("Email has been sent!")
                elif "Komal" in recipient:
                    to = "krverma1100@gmail.com"
                    speak("what should i say")
                    content = takeCommand()    
                    sendEmail(to, content)
                    speak("Email has been sent!")

                elif "Rajesh" in recipient:
                    to = "shreebajrangroad@gmail.com"
                    speak("what should i say")
                    content = takeCommand()    
                    sendEmail(to, content)
                    speak("Email has been sent!")

                sys.exit()

            except Exception as e:
                print(e)
                speak("Sorry my friend vaibhav. I am not able to send this email")    
                sys.exit()

        elif "start chrome" in query:
            speak("ofcourse ,please wait")
            co_path = "C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe"
            os.startfile(co_path)
            sys.exit()
          
        elif "start snake game" in query:
            speak("ofcourse ,please wait")
            path = "C:\\Users\\JAI HIND\\Desktop\\snake\\snake_game.py"
            os.startfile(path)
            sys.exit()


        elif "who are you" in query:
            speak("i am jarvis ")

        elif "what can you do" in query:
            speak("i can do any thing for you ,just say it")
        
        elif "shutdown" in query:
            speak("good bye")
            os.system("shutdown /s /t 1");
            sys.exit()

        elif "restart" in query:
            os.system("shutdown /r /t 1");
            sys.exit()

        elif "word" in query:
            speak("ofcourse ,please wait")
            co_path = "C:\\ProgramData\\Microsoft\Windows\\Start Menu\\Programs\\Microsoft Office\\microsoft office word 2007"
            os.startfile(co_path)
            sys.exit()

        elif "excel" in query:
            speak("ofcourse ,please wait")
            co_path = "C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs\\Microsoft Office\\Microsoft Office Excel 2007"
            os.startfile(co_path)
            sys.exit()
        
        elif 'jokes' in query:
            result =  webbrowser.open("https://www.hindijokes.in/best-jokes-in-hindi.html")
            speak(result) 
            sys.exit()

        elif "instagram" in query:
            speak("opening instagram")
            webbrowser.open("https://www.instagram.com/")
            sys.exit()

        elif "whatsapp" in query:
            speak("ofcourse, opening whatsapp")
            webbrowser.open("https://web.whatsapp.com/")
            sys.exit()

        elif "exit" in query:
            speak("ofcourse")         
            sys.exit()

        elif "sms" in query:
            try:
                speak("whom do yo wanna send sms")
                recipient = takeCommand()

                if "Komal" in recipient:
                    phoneNo = 9358973824
                    speak("what should i say?")
                    content = takeCommand()
                    sendPostRequest(url, 'R6RE2UN9DBUY39728KSK7ZK5JS0LLJ8G', '3LB55DGL8T47TOYJ', 'stage',phoneNo,"SMSIND", content )
                    speak("SMS sent")


                elif "Vaibhav" in recipient:
                    phoneNo = 7568834124
                    speak("what should i say?")
                    content = takeCommand()
                    sendPostRequest(url, 'R6RE2UN9DBUY39728KSK7ZK5JS0LLJ8G', '3LB55DGL8T47TOYJ', 'stage',phoneNo,"SMSIND", content )
                    speak("SMS sent")

                elif "Rajesh" in recipient:
                    phoneNo = 8058873124
                    speak("what should i say?")
                    content = takeCommand()
                    sendPostRequest(url, 'R6RE2UN9DBUY39728KSK7ZK5JS0LLJ8G', '3LB55DGL8T47TOYJ', 'stage',phoneNo,"SMSIND", content )
                    speak("SMS sent")

                elif "Manju" in recipient:
                    phoneNo = 8209449957
                    speak("what should i say?")
                    content = takeCommand()
                    sendPostRequest(url, 'R6RE2UN9DBUY39728KSK7ZK5JS0LLJ8G', '3LB55DGL8T47TOYJ', 'stage',phoneNo,"SMSIND", content )
                    speak("SMS sent")

            except Exception as e:
                print(e)
                speak("sorry my friend vaibhav, i am not able to send this message")
                sys.exit()

        elif "weather" in query:
            try:
                speak("which city")
                city = takeCommand()
                observation = owm.weather_at_place(city)
                w = observation.get_weather()
                print("wind speed is: " +str(w.get_wind()))
                print("humidity is: "+ str(w.get_humidity()))
                print(w.get_temperature('celsius'))
                speak("wind spped is" +str(w.get_wind()))
                speak("humidity is"+ str(w.get_humidity()))    
                speak(w.get_temperature('celsius'))
                

            except Exception as e:
                print(e)
                speak("sorry i am not able to show you the weather") 

        elif "chrome" in query:
            os.startfile("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe")
            sys.exit()

        elif "play on youtube" in query:
            sng_name = takeCommand()
            webbrowser.get("C:\\Program Files\\Google\\Chrome\\Application\\chrome.exe %s").open(kit.playonyt(sng_name))
            speak("ofcourse, please wait")
            sys.exit()

        # elif "send whatsapp" in query:
        #     speak("to whom do you wanna send whatsapp")
        #     rcvr = takeCommand()
            
