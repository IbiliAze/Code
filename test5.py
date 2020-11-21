import requests

url = "http://35.223.71.184/api/org"

payload="{\r\n    \"siteName\": \"Lon\",\r\n    \"email\": \"ibili3@gmail.com\",\r\n    \"orgName\": \"Afenia5\",\r\n    \"password\": \"cisco12345\"\r\n}"
headers = {
  'Content-Type': 'application/json'
}

response = requests.request("POST", url, headers=headers, data=payload)

print(response.text)
