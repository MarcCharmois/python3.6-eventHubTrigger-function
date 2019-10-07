# python3.7 eventHubTrigger function
## Desctiption
An Azure function to be triggered by an event that occurs within an Azure Event Hub. 
## Settings
 - 1 add a local.settings.json file with this structure
'''
{
  "IsEncrypted": false,
  "Values": {
    "FUNCTIONS_WORKER_RUNTIME": "python",
    "AzureWebJobsStorage": "{AzureWebJobsStorage}", 
    "receiverConnectionString":""
    SharedAccessKey="
  }
}
'''
 - 2 
Complete the receiverConnectionString value with the one of the eventhub namespace >> settings >> Shared access policies >> RootManageSharedAccessKey >> Connection string–primary key    
 - 3 replace the eventHubName value with yours in the fucntion.json file
 - 4 deploy with PowerShell or with the Azure Functions extension of Visual Studio code