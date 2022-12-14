import conf
from boltiot import Sms, Bolt
import json, time

minimum_limit = 250
maximum_limit = 305


mybolt = Bolt(conf.API_KEY, conf.DEVICE_ID)
sms = Sms(conf.SID, conf.AUTH_TOKEN, conf.TO_NUMBER, conf.FROM_NUMBER)


while True:
    print ("Reading sensor value")
    response = mybolt.analogRead('A0')
    data = json.loads(response)
    print("Sensor value is: " + str(data['value']))
    try:
        sensor_value = int(data['value'])
        if sensor_value > maximum_limit or sensor_value < minimum_limit:
            #temp=(100*sensor_value)/1024
            #print("Temperature is "+temp)
            print("Making request to Twilio to send a SMS")
            response = sms.send_sms("The Current temperature sensor value is " $
            print("Response received from Twilio is: " + str(response))
            print("Status of SMS at Twilio is :" + str(response.status))
    except Exception as e:
        print ("Error occured: Below are the details")
        print (e)
    time.sleep(10)

