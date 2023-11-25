import json, os
from operator import itemgetter

class PodioControllerUsers:
    def __init__(self, name):
        self.name = name

    def getPodio(self):
        jsonDirection = os.path.dirname(__file__)
        with open(jsonDirection + "/top.json") as file:
            data = json.load(file)
            temp=data["podio"]
        return temp


    def addResult(self, user, puntaje, music):
        temp=[]
        jsonDirection = os.path.dirname(__file__)
        with open(jsonDirection + "/top.json") as file:
            data = json.load(file)
            temp=data["podio"]
            temp.append({"user":user,"tiempo":puntaje,"music":music})
            #print(temp)
            print(data)
            
            ordenado=self.ordenar(temp)

            newData={"podio":[]}
            i=0
            while i<len(ordenado):
                if i>5:
                    break
                newData["podio"].append({
                "user": ordenado[i]['user'],
                "tiempo": ordenado[i]['tiempo'],
                "music": ordenado[i]['music']})
                i+=1

            with open("top.json", "w+") as file:
                file.truncate()
                json.dump(newData, file, indent=4)
    
    def ordenar(self,lista):
        temp=lista
        ordenado= sorted(temp,key=lambda i: float(i['tiempo']))
        return ordenado[:5]
             

    def createJsonFile(self):
        data = {}
        data["podio"] = []
        with open("top.json", "w") as file:
            json.dump(data, file, indent=4)
    def verifyJsonFileExistence(self):
        if os.path.exists(os.path.dirname(__file__)+"/top.json"):
            return True
        else: return False

    def verifyPodio(self,name, puntaje):
        with open('top.json', 'r') as file:
            data = json.load(file)
        bandera=False
        if len(data['podio'])<5:
            return True
        for user in data['podio']:
            if float(user['tiempo']) >= float(puntaje):
                bandera=True
        return bandera

    def selectSong(user_given):
        with open('users.json', 'r') as file:
            data = json.load(file)
        for user in data['users']:
            if user['user'] == user_given:
                if user['music']:
                    return user['music']



"""fileManagement = JsonControllerUsers("users")
fileManagement.addUsers("jorge", "sdf", "1234", "sdf", "asfl")
fileManagement.addUsers("andrea", "cor", "123", "sdf", "asf")
fileManagement.verifyJsonFileExistence()
fileManagement.verifyUser('si','ad')"""

podio=PodioControllerUsers("podio")
podio.addResult("juapi","1","hola.mp3")
podio.addResult("peter","2","hola.mp3")
podio.addResult("paner","4","hola.mp3")
podio.addResult("mario","6","hola.mp3")
podio.addResult("redondo","2","hola.mp3")
podio.addResult("el5","6","hola.mp3")
podio.addResult("el6","2","hola.mp3")

