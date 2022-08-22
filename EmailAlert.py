import email_conf
from boltiot import Email, Bolt
import json, time

minimum_limit = 200 #the minimum threshold of light value
maximum_limit = 215 #the maximum threshold of light value


mybolt = Bolt(email_conf.API_KEY, email_conf.DEVICE_ID)
mailer = Email(email_conf.MAILGUN_API_KEY, email_conf.SANDBOX_URL, email_conf.S$


while True:
    print ("Reading sensor value")
    response = mybolt.analogRead('A0')
    data = json.loads(response)
    print ("Sensor value is: " + str(data['value']))
    try:
        sensor_value = int(data['value'])
        if sensor_value > maximum_limit or sensor_value < minimum_limit:
            print("Making request to Mailgun to send an email")
            response = mailer.send_email("Alert", "The Current temperature sens$
            print("Response received from Mailgun is: " + response.text)
    except Exception as e:
        print ("Error occured: Below are the details")
        print (e)
    time.sleep(10)

