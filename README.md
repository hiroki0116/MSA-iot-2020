# Microsoft Student Accelerator program - 2nd assignment -


### GOAL ###

1. **Send telemetry from a device to an IoT hub**  * *Web scraping was used to obtain the real-time weather data in Sydney instead of using an IoT device such as Raspberry Pi*
2. **Visualize real-time sensor data from Azure IoT hub using Power BI**


### STEPS ###
1. Create an IoT hub on Azure portal
2. Register a device using Azure CLI
```
   az iot hub device-identity create --hub-name {IoTHubName} --device-id {anyDeviceName}
   az iot hub device-identity show-connection-string --hub-name {IoTHubName} --device-id {anyDeviceName} --output table
```
3. Send real-time data by running the local python program and send to Iot hub
4. Read the telemetry from Iot hub
5. Configure Stream Analytics Jobs on Azure to trasfer the data to Power BI
6. Shape the data
