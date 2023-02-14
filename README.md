**SOAR Workbook Exporter**

**Integration**
The app does not integrate with any external service, it merely provides actions to generate and store files containing information about SOAR tasks associated with a container.

**About**
The app provides actions to create .json, .yaml, and .pdf files containing workbook information in the following format:
```
<h1> Workbooks Name
<h2> Phase
<h3> Task
<standard> Description
<bold> Actions ... <standard> Action Name
<Bold> Playbook ... <standard> Playbook Name
```
PDF and YAML files are stored in the vault associated with the container. The cleaned json file is added to the SOAR action result. 
The user needs to provide a Workbook ID, and can leave an additional comment.

Furthermore, with the app you can create a new SOAR Workbook by importing an existing .json file in the following structure:
```
{
  "name": "My Phase",
  "order": 1,
  "template_id": 10,
  "tasks": [
    {
      "name": "My Task",
      "order": 1,
      "description": "Investigate the event",
      "playbooks": [
        { "scm": "local", "playbook": "investigate" },
        { "scm": "community", "playbook": "04_07_2017 - PhishMe" }
      ],
      "actions": [ "geolocate ip", "block_ip" ]
    }...
  ]
}
```

**Security Details**
- All three actions described above retreive workbook information via Splunk Rest API call (More information about the endpoints can be found here: https://docs.splunk.com/Documentation/SOARonprem/latest/PlatformAPI/RESTWorkbook). To perform the API request, the Python module 'requests' is used. Authentication is handled via a SOAR Authentification Token and a SOAR host IP address.

- The actions for creating and storing .yaml and .pdf files in the vault are utilizing SOAR's Vault automation API, they are calling the *vault_add* function to be precise (More information on this can be found here: https://docs.splunk.com/Documentation/SOAR/current/PlaybookAPI/VaultAPI).
