import requests

url = "https://api.imgur.com/3/image"

payload={'image': 'R0lGODlhAQABAIAAAAAAAP///yH5BAEAAAAALAAAAAABAAEAAAIBRAA7'}
files=[

]
headers = {
  'Authorization': 'Client-ID {{clientId}}'
}

response = requests.request("POST", url, headers=headers, data=payload, files=files)

print(response.text)
