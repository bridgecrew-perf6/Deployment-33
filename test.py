import requests, json
url = 'https://trial-model.herokuapp.com'
data = {'Pclass': 3
      , 'Age': 2
      , 'SibSp': 1
      , 'Fare': 50}
data = json.dumps(data)
send_request= requests.post(url,data)
print(send_request.json())