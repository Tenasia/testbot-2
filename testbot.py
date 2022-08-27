import os
import random
from flask import Flask, request
from pymessenger import Bot

app = Flask(__name__)
PAGE_ACCESS_TOKEN = os.environ['PAGE_ACCESS_TOKEN'] 
VERIFY_TOKEN = os.environ['VERIFY_TOKEN'] 
bot = Bot(PAGE_ACCESS_TOKEN)

def process_message(text):
    formatted_message = text.lower()

    greetings = ["Awesome day!", "Good day!", "Hello iskolar!", "Greetings!"]
    thanks_response = ["You're welcome, happy to help 😊", "No problem, anytime!", "Happy to serve 😄", "My pleasure. If you have anymore concerns, don't hesitate to ask the people on this page 🙂"]
    number_reply = ["Here is the link/s that will hopfully answer your complaint.", "I hope the link/s below will help answer your complaint.", "Below is the link/s that will hopefully answer the complaint you have requested."]
    about_bot = ["Oh me?", "I see that you want to know more of me.", "You're curious about me, aren't you?", "I'm kind of new here so I understand why you asked."]
    
    if formatted_message == "1":
        response = f"[1] What are the activities for this week?\n\n{random.choice(number_reply)}\n\nAssignment List:\nhttps://bit.ly/SA-TechAssignmentList\n\nAssignment List (Due Passed):\nhttps://bit.ly/SA-TechAssignmentListForOldActivities\n\nModifiable Class Schedule:\nhttps://docs.google.com/spreadsheets/d/1Y4oQtsn8YwU1NHONJYppFkiKL2VX7dVjBBuKEpCBFqE/edit?usp=sharing\n\nPUP Calendar:\nhttps://www.pup.edu.ph/about/calendar\n\nIf you see that your question is not on the list, please comment on the page for assistance."
    elif formatted_message == "2":
        response = f"[2] Is there a place where I can access the class materials?\n\n{random.choice(number_reply)}\n\nClass G-Drive:\nhttp://bit.ly/SA-TechDrive\n\nIf you see that your question is not on the list, please comment on the page for assistance."
    elif formatted_message == "3":
        response = f"[3] Where can I learn more about PUP?\n\n{random.choice(number_reply)}\n\nSchool Handbook\nhttps://drive.google.com/file/d/0B1BuDAuN0r8SX1BWX2NSN3FURzg/view?usp=drivesdk&resourcekey=0-oi8lUy9PCFysh0FDyL5ipw\n\nPUP Main Map:\nhttps://www.pup.edu.ph/resources/images/maps/main.gif\n\nIf you see that your question is not on the list, please comment on the page for assistance." 
    elif formatted_message == "4":
        response = f"[4] Where can I request my school documents?\n\n{random.choice(number_reply)}\n\nSchool Documents:\n\nItech Document Request Form\nhttps://bit.ly/2CA28vk\n\nUniversity Document Request Form\nhttps://odrs.pup.edu.ph/\n\nPUP Appointment System\nhttps://apps.pup.edu.ph/appointment/\n\nDownloadable Forms\nhttps://drive.google.com/drive/folders/1PinhrPTWsaRXLdbtx4xdbZsfBYDQ4zg9?usp=sharing\n\nIf you see that your question is not on the list, please comment on the page for assistance."
    elif formatted_message == "5":
        response = f"[5] Where else can I submit my concerns?\n\n{random.choice(number_reply)} \n\nStudent Concerns:\n\nOSSSAC - Student Help Desk/General University Queries\nhttps://osssac.pup.edu.ph/knowledgebase.php\n\nItech Concerns Group\nhttps://www.facebook.com/groups/826853574473330\n\nSchool Contacts\n\nEmails(Itech Department):\n\nEngineering: fcruiz@pup.edu.ph or pupitechmanila@gmail.com (main email)\n\nICT/DMT: josephine_delaisla@yahoo.com.ph or jmdelaisla@pup.edu.ph\n\nRegistrar: rgsalazar@pup.edu.ph\n\nMain University Emails:\nhttps://www.pup.edu.ph/about/contactus\n\nIf you see that your question is not on the list, please comment on the page for assistance."
    elif formatted_message == "6":
        response = f"[6] How does fixing the INC in your grades work?\n\nYou follow these steps:\n\n(1)completion form\n(2) deficiencies\n(3) OR (Official Receipt)\n\nFirst you have to fill up the form (located at number 4, downloadable forms), pass the deficiencies or the requirements that you have yet to pass to the prof, and then pay 30 pesos to the PUP main cashier (either online (located at 4, univ. doc. request) or face to face) to get the receipt. Finally, other than the missing requirements, give or show the completion form and the OR to the prof as well. Contact the class president if you're done with these steps or if you have anymore concerns regarding this."
    elif formatted_message == "7":
        response = f"[7] Why were you made?\n\n{random.choice(about_bot)}I was made students to assist the volunteers of this page in answering most of the common school queries. Other than that, I don't do much so please don't expect me to be like Alexa, Google Assistant, or other really smart AIs. I mean, it may be possible but it would take a very long time."
    elif formatted_message == "8":
        response = f"[8] How can I get straight 1's on my subjects?\n\nYou don't. But that's fine because I'm here to help! :)"
    elif formatted_message == "thank you" or formatted_message == "thankyou" or formatted_message == "thanks" or formatted_message == "ty" or formatted_message == "thx" or formatted_message == "salamat" or formatted_message == "salamuch" or formatted_message == "matsala" or formatted_message == "arigato" or formatted_message == "arigathanks":
        response = f"{random.choice(thanks_response)}"
    else:
        response = f"{random.choice(greetings)} I'm ASH your Automated Student Helper, how may I help you today? Please type in the number of your choice:\n\n[1] What are the activities for this week?\n[2] Is there a place where I can access the class materials?\n[3] Where can I learn more about PUP?\n[4] Where can I request my school documents?\n[5] Where else can I submit my concerns?\n[6] How does fixing the INC in your grades work?\n[7] Why were you made?\n[8] How can I get straight 1's on my subjects?\n\n(Note: I'm just a simple bot so I'll keep repeating this response when you enter in a random text even if I don't understand it.)"
    return response

#We will receive messages that Facebook sends our bot at this endpoint

@app.route("/", methods=['POST', 'GET'])

def webhook():
    if request.method == "GET":
        if request.args.get("hub.verify_token") == VERIFY_TOKEN:
            return request.args.get("hub.challenge")

        else:
            return 'Bot not connected to Facebook. if this still shows up, it catches this !!!.'

    elif request.method == "POST":
        payload = request.json
        event = payload['entry'][0]['messaging']

        for msg in event:
            text = msg['message']['text']
            sender_id = msg['sender']['id']

            response = process_message(text)
            bot.send_text_message(sender_id, response)

        return "Message received"

    else:
        return "200"


if __name__ == "__main__":
    app.run()
#https://fb-testbot-1.herokuapp.com/
