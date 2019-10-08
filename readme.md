# python3.7 eventHubTrigger function
## Desctiption
An Azure function triggered when an event occurs within an Azure Event Hub.   
If the event contains the string "test" send an email using sendgrid
## Settings 
### event-triggered part
 - 1 add a local.settings.json file with this structure
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
 - 2 
Complete the receiverConnectionString value with the one of the eventhub namespace >> settings >> Shared access policies >> RootManageSharedAccessKey >> Connection string–primary key    
 - 3 replace the eventHubName value with yours in the function.json file
 ### mail-sending part
 - 1 create a sendGrid resource in Azure    
 - 2 register to Twilio SendGrid an get an API key    
 - 3 in Azure portal, add a new app setting in the function   
    - name: SENDGRID_API_KEY
    - value: send grid api key value

 ## Deployment
 Deploy with PowerShell or with the Azure Functions extension of Visual Studio code   
 You may have to create a setting for the receiverConnectionString in the Azure Portal and put the Event Hub Connection String value.   
     
 !["Azure Portal function setting: Event Hub Connection String value"](https://raw.githubusercontent.com/MarcCharmois/python3.7-eventHubTrigger-function/master/doc/img/azure-eventhubTriggered-Function-Settings.png)
