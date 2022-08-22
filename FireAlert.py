import requests                 # for making HTTP requests
import json                     # library for handling JSON data
import time                     # module for sleep operation

from boltiot import Bolt,Sms
import configAlert as conf
mybolt = Bolt(conf.API_KEY, conf.DEVICE_ID)

minimum_limit = 250
maximum_limit = 253

mybolt = Bolt(conf.API_KEY, conf.DEVICE_ID)
sms = Sms(conf.SID, conf.AUTH_TOKEN, conf.TO_NUMBER, conf.FROM_NUMBER)
#mailer = Email(conf.MAILGUN_API_KEY,conf.SANDBOX_URL,conf.SENDER_EMAIL,conf.RECIPIENT_EMAIL)


while True:
    print ("Reading sensor value")
    response = mybolt.analogRead('A0')
    data = json.loads(response)
    print("Sensor value is: " + str(data['value']))
    try:
        sensor_value = int(data['value'])
        if sensor_value > maximum_limit or sensor_value < minimum_limit:
            temp=(100*sensor_value)/1024
            print("Making request to Twilio to send a SMS")
            response = sms.send_sms("The Current temperature sensor value is "+str(temp))
            print("Response received from Twilio is: " + str(response))
            print("Status of SMS at Twilio is :" + str(response.status))

            """
            print("Sending message to your Telegram Acoount")
            message = "Alert! The temperature has crossed beyond the threshold limit " + maximum_limit + \
                  ". The current temperature is " + str(sensor_value)
            telegram_status = send_telegram_message(message)
            print("This is the Telegram status:", telegram_status)

            print("Making request to Mailgun to send an email")
            response = mailer.send_email("Alert", "The Current temperature sensor value is " +str(sensor_value))
            print("Response received from Mailgun is: " + response.text)
            """
    except Exception as e:
        print ("Error occured: Below are the details",e)
    time.sleep(10)
