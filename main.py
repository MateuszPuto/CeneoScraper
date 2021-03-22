import requests

response = requests.get("https://www.ceneo.pl/22496575;02514;#tag=pp4")
print(response.text)