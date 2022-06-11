# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, an
import smtplib
import speech_recognition as sr
import pyttsx3
from email.message import EmailMessage

listener = sr.Recognizer()
engine = pyttsx3.init()

def talk(text):
    engine.say(text)
    engine.runAndwait()

def get_info():
    try:
        with sr.Microphone() as source:
            print('listening.....')
            voice = listener.listen(source)
            info = listener.recogniz_google(voice)
            print(info)
            return info.lower()
    except:
        pass

def send_email(reciever,subject,message):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    # make sure to give app access in your google acount
    server.login('Sender_Email','Sender_Email_password')
    email = EmailMessage()
    email['From'] = 'Sender_Email'
    email['To'] = reciever
    email['Subject'] = subject
    email.set_content(message)
    server.send_message(email)
#This is the list of reciever emils we assign as key value pairs for easy implementation
email_list ={
    'one': 'success07@gmail.com'
    'two': 'destructor0717@gmail.com'
}

def get_email_info():
    talk('To whom you want to send email')
    name = get_info()
    receiver = email_list[name]
    print(receiver)
    talk('What is the subject of your email?')
    subject = get_info()
    talk('tell me the text in your email')
    message = get_info()
    send_email(receiver , subject, message)
    talk('do you want to send more email?')
    send_more = get_info()
    if 'yes ' in send_more:
        get_email_info()

get_email_info()



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
