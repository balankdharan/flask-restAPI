# can use to test the API

import requests

BASE="http://127.0.0.1:5000/"

#get all 
getResponse = requests.get(BASE)
print(getResponse.json())
# enter to continue
input()

#Add one  
postResponse = requests.post(BASE,{"id":3,"name":"Demon slayer","genere":"horror"})
print(postResponse.json())
# enter to continue
input()

#get one
getSpecificResponse = requests.get(BASE + str(2))
print(getSpecificResponse.json())

# enter to continue
input()

#update one
putResponse = requests.put(BASE + str(2),{"name":"jjk","genere":"action"})
print(putResponse.json())

# enter to continue
input()

#delete one
deleteResponse = requests.delete(BASE + str(3))
print(deleteResponse.json())