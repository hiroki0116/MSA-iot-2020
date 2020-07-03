# Microsoft Student Accelerator program - 2nd assignment -


### GOAL ###

1. **Send telemetry from a device to an IoT hub**  * *Web scraping was used in order to obtain the real-time weather data in Sydney instead of using an IoT device such as Raspberry Pi*
2. **Visualize the real-time data from Azure IoT hub using Power BI**


### STEPS ###
1. Create an IoT hub on Azure portal
![createHub](https://github.com/hiroki0116/MSA-iot-2020/blob/image/iotHub.png)
2. Register a device using Azure CLI
```
   az iot hub device-identity create --hub-name {IoTHubName} --device-id {anyDeviceName}
   az iot hub device-identity show-connection-string --hub-name {IoTHubName} --device-id {anyDeviceName} --output table
```
3. Send real-time data by running the local python program and send to Iot hub. Obtain live data of 'temperature', 'apparent tempereture' and 'humidiity' in Sydney every 5 minutes
![createHub](https://github.com/hiroki0116/MSA-iot-2020/blob/image/createHub.png)

4. Configure Stream Analytics Jobs on Azure to trasfer the data to Power BI
![createHub](https://github.com/hiroki0116/MSA-iot-2020/blob/image/streamAnalyticsJob.png)
5. Shape the data
![createHub](https://github.com/hiroki0116/MSA-iot-2020/blob/image/powerBI.png)


![My Power BI](https://app.powerbi.com/view?r=eyJrIjoiZjBhN2Q3M2YtNzUzNy00NjU1LWE3OTAtNWM0MGU0YjkwNGEyIiwidCI6ImM5MTI3YzM5LTVkZDgtNDNiOC1iODRiLTNlYTI4MjViMDZjNyJ9)
