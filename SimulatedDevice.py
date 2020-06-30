
import bs4
import requests
import time
from bs4 import BeautifulSoup
from azure.iot.device import IoTHubDeviceClient, Message


# The device connection string to authenticate the device with my IoT hub.
CONNECTION_STRING = "HostName=msa-20008068.azure-devices.net;DeviceId=msa-20008068;SharedAccessKey=1QQF8r+2+aAnCg9TOgT9nGb7MbKmL9rMfc8S8za0les="

# Define the JSON message to send to IoT Hub.

MSG_TXT = '{{"price":{price}}}'


def iothub_client_init():
    # Create an IoT Hub client
    client = IoTHubDeviceClient.create_from_connection_string(CONNECTION_STRING)
    return client

def priceTracker():

    url = 'https://finance.yahoo.com/quote/AAPL?p=AAPL&.tsrc=fin-srch'

    response = requests.get(url)

    soup = BeautifulSoup(response.text,'lxml')

    price = soup.find_all('div',{'class':'My(6px) Pos(r) smartphone_Mt(6px)'})[0].find('span').text

    return price

def iothub_client_telemetry_sample_run():

    try:
        client = iothub_client_init()
        print ( "IoT Hub device sending periodic messages, press Ctrl-C to exit" )

        while True:
            # Build the message with simulated telemetry values.
            price = priceTracker()
            msg_txt_formatted = MSG_TXT.format(price=price)
            message = Message(msg_txt_formatted)

            # Add a custom application property to the message.
            # An IoT hub can filter on these properties without access to the message body.
            if float(price) > 365:
              message.custom_properties["price"] = "true"
            else:
              message.custom_properties["price"] = "false"

            # Send the message.
            print( "Sending message: {}".format(message) )
            client.send_message(message)
            print ( "Message successfully sent" )
            time.sleep(1)

    except KeyboardInterrupt:
        print ( "IoTHubClient sample stopped" )

if __name__ == '__main__':
    print ( "IoT Hub Quickstart #1 - Simulated device" )
    print ( "Press Ctrl-C to exit" )
    iothub_client_telemetry_sample_run()
