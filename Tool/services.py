import requests

class Services:

    def getUserIdentify(self, id):
        print(id)
        response = requests.get('http://localhost:5000/api/User/' + str(id))
        json = response.json()
        return json