# python3.6 eventHubTrigger function
## Desctiption
An Azure function (Python 3.6) triggered when an event occurs within an Azure Event Hub.   
If the event body contains the string "test", send an email using SendGrid   
(You can use the project <a href="https://github.com/MarcCharmois/Python3.7-azure-eventhub-1.3.2">Python3.7 Azure Eventhub 1.3.2 - Events Sender Receiver</a> to send events containing the string "test" to the eventhub)    

## Settings 
### event-triggered part
 1. Add a local.settings.json file with this structure
```
{
  "IsEncrypted": false,
  "Values": {
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "AzureWebJobsStorage": "{AzureWebJobsStorage}", 
    "receiverConnectionString":""
  }
}
```
 2. Complete the receiverConnectionString value with the one of the eventhub namespace >> settings >> Shared access policies >> RootManageSharedAccessKey >> Connection string–primary key    
 3. Replace the eventHubName value with yours in the function.json file   

 ### mail-sending part
 1. Create a SendGrid Account resource in Azure    
 2. Register to Twilio SendGrid an get an API key    
 3. In Azure portal, add a new app setting to the function   
    - name: SENDGRID_API_KEY
    - value: send grid api key value

 ## Deployment
 Deploy with PowerShell or with the Azure Functions extension of Visual Studio code   
 You will have to create a app setting for the receiverConnectionString in the Azure Portal and put the Event Hub Connection String value.   
     
 !["Azure Portal function setting: Event Hub Connection String value"](https://raw.githubusercontent.com/MarcCharmois/python3.7-eventHubTrigger-function/master/doc/img/azure-eventhubTriggered-Function-Settings.png)
