import rabbitpy
import requests
messageList =[]
myobj =  {
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

with rabbitpy.Connection('amqps://jjixgyfe:KI1ImGKoJZs0NNByfOHEJGnV3UbyI339@rat.rmq2.cloudamqp.com/jjixgyfe') as conn:
    with conn.channel() as channel:
        queue = rabbitpy.Queue(channel, 'deal')
        while len(queue) > 0:
            message = queue.get()
            messageList.append(message)
            message.pprint(True)
            message.ack()
            print('There are {} more messages in the queue'.format(len(queue)))

for message in messageList:


    jsonResponse = message.json()
    myobj['nom'] = jsonResponse['deal']['name']
    myobj['montant'] = jsonResponse['deal']['amount']//1000
    myobj['code']= jsonResponse['code']
    myobj['zone'] = "abap"
    myobj['status']="Structuring"
    myobj['lender'] = fullName(jsonResponse['deal']['dealCreator'])
    requests.post(url,data= myobj)




#print(requests.post(url,data=myobj))