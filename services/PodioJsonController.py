import json, os

class PodioControllerUsers:
    def __init__(self, name):
        self.name = name

    def addResult(self, user, puntaje, music):
        jsonDirection = os.path.dirname(__file__)
        with open(jsonDirection + "/top.json") as file:
            data = json.load(file)
            if len(data["podio"])<=25:
                data["podio"].append({
                    "user": user,
                    "tiempo": puntaje,
                    "music": music,
                })
            else:
                pass
                
            with open("top.json", "w") as file:
                json.dump(data, file, indent=4)
    
    def createJsonFile(self):
        data = {}
        data["podio"] = []
        with open("top.json", "w") as file:
            json.dump(data, file, indent=4)
    def verifyJsonFileExistence(self):
        if os.path.exists(os.path.dirname(__file__)+"/top.json"):
            return True
        else: return False

    def verifyPodio(name, puntaje):
        with open('top.json', 'r') as file:
            data = json.load(file)
        bandera=False
        for user in data['podio']:
            if float(user['puntaje']) <= float(puntaje):
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

PodioMagnament = PodioControllerUsers("podio")
PodioMagnament.addResult("lpt8","2830","1234")
PodioMagnament.addResult("hwjm","230","124")

