import requests

class Services:

    def sendUserIdentify(self, id):
        r = requests.get('api/getUserIdentify/' + id)
        return r.status_code == 200