#Q.1
import requests
response=requests.get("https://api.forismatic.com/api/1.0/?method=getQuote&format=json&lang=en")
print(response.status_code)
import json
data=response.json()
print(type(data))
print(data["quoteText"])
