import requests
from  ATAKMessage_pb2  import TestMessage
message = TestMessage()


url = "https://your.api.url/your/endpoint"
headers = {'Content-Type': 'application/x-protobuf'}
response = requests.post(url, data=message.SerializeToString(), headers=headers)

if response.status_code == 200:
    print("Message envoyé avec succès")
else:
    print("Erreur lors de l'envoi du message:", response.status_code)