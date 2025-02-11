import requests
import json

webhook_url = 'Paste XDR Webhook Here'

headers = {'Content-Type':'application/json', 'Accept':'application/json'}
#
# here under a tiny JSON payload for passing some data to the XDR workflow
#
post_data = { "message": " Here is my message from python script ", "list_of_stuff": [ "item1", "item2" ] }

response = requests.post(webhook_url, headers=headers,json=post_data)

print(response)
