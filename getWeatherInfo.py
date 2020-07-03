
import bs4
import requests
import time
import re
from bs4 import BeautifulSoup
from azure.iot.device import IoTHubDeviceClient, Message


# The device connection string to authenticate the device with my IoT hub.
CONNECTION_STRING = "HostName=msa-20008068.azure-devices.net;DeviceId=msa-20008068;SharedAccessKey=1QQF8r+2+aAnCg9TOgT9nGb7MbKmL9rMfc8S8za0les="

# Define the JSON message to send to IoT Hub.
MSG_TXT = '{{"temperature": {temperature},"apparentTempture":{apparentTemperature},"humidity": {humidity}}}'


def iothub_client_init():
    # Create an IoT Hub client
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)

    return client


#scraping the live weather forecast website of Sydney
def getWeatherInfo():

    url = 'https://www.weatherzone.com.au/nsw/sydney/sydney'
    response = requests.get(url)

    soup = BeautifulSoup(response.text,features = 'html.parser')
    temperature = soup.find_all('div',{'class':'summary_now'})[0].find('span').text
    temperature = re.findall("\d+\.\d+",temperature)

    table = soup.find_all('div',{'class':'details_lhs'})[0].text.split()

    apparentTemperature = table[12]
    apparentTemperature = re.findall("\d+\.\d+",apparentTemperature) #obtain only digits
    humidity = table[15]
    humidity = re.sub("\\D","",humidity)


    return float(temperature[0]),float(apparentTemperature[0]),int(humidity)


def iothub_client_telemetry_sample_run():
    try:
        client = iothub_client_init()
        print ( "IoT Hub device sending periodic messages, press Ctrl-C to exit" )

        while True:
            # Build the message with simulated telemetry values.
            temperature,apparentTemperature,humidity = getWeatherInfo()
            msg_txt_formatted = MSG_TXT.format(temperature=temperature, apparentTemperature = apparentTemperature,humidity=humidity )
            message = Message(msg_txt_formatted)

            # Add a custom application property to the message.
            # An IoT hub can filter on these properties without access to the message body.
            if float(temperature) > 30:
              message.custom_properties["temperatureAlert"] = "true"
            else:
              message.custom_properties["temperatureAlert"] = "false"

            # Send the message.
            print( "Sending message: {}".format(message) )
            client.send_message(message)
            print ( "Message successfully sent" )
            time.sleep(300) #obtain data every 5 minutes

    except KeyboardInterrupt:
        print ( "IoTHubClient sample stopped" )

if __name__ == '__main__':
    print ( "running..." )
    print ( "Press Ctrl-C to exit" )
    iothub_client_telemetry_sample_run()
