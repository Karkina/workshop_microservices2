import requests

myobj = {
    "nom": "",
    "montant": "",
    "code": "",
    "devise": "",
    "zone": "abap",
    "brower": "",
    "lender": "",
    "status": ""
}

url = 'https://deal-service.herokuapp.com/snippets/'


def fullName(personne):
    return personne["firstName"]+"."+personne["lastName"]


def post_deals_from_rabbitmq(messageList):
    for message in messageList:

        jsonResponse = message.json()
        myobj['nom'] = jsonResponse['deal']['name']
        myobj['montant'] = jsonResponse['deal']['amount']//1000
        myobj['code'] = jsonResponse['code']
        myobj['zone'] = "abap"
        myobj['status'] = "Structuring"
        myobj['lender'] = fullName(jsonResponse['deal']['dealCreator'])
        requests.post(url, data=myobj)
