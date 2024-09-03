# Python class for working with webhooks to MSTeams via workflow

### History
After MIcrosoft anounced deprecation of office 365 connectors, I decided to create a simle class,
for working with Power Automate workflows, to post messages from python scripts to Teams channel.
It's a simple class, with json formatted dictionary, can be used with basic configuration, to send
Adaptive Card to Teams channel.

### Usage

You can clone this repo, install it with pip, and use in your code.

import class:
```
from teamswebhook import TeamsWebhook
```
Make some basic configuration:
```
webhook_url = "URL" #URL generated in Power Automate workflow
tw = TeamsWebhook.TeamsWebhook() # Create class instance
tw.url = webhook_url # Forward URL to instance
tw.script_name = "Module Test" # Header for Adaptive Card, I use to show script name, that sent message
tw.request_post("Module is work") # Send request to webhook with custom message
```