import json, os

class JsonControllerUsers:
    def __init__(self, name):
        self.name = name
    def addUsers(self, user, email, password, music, photo):
        jsonDirection = os.path.dirname(__file__)
        with open(jsonDirection + "/users.json") as file:
            data = json.load(file)
            data["users"].append({
                "user": user,
                "email": email,
                "password": password,
                "music": music,
                "photo": photo
            })
            with open("users.json", "w") as file:
                json.dump(data, file, indent=4)
    def createJsonFile(self):
        data = {}
        data["users"] = []
        with open("users.json", "w") as file:
            json.dump(data, file, indent=4)
    def verifyJsonFileExistence(self):
        if os.path.exists(os.path.dirname(__file__)+"/users.json"):
            return True
        else: return False

fileManagement = JsonControllerUsers("users")
fileManagement.createJsonFile()
fileManagement.addUsers("si", "cor", "asd", "sdf", "asfl")
fileManagement.addUsers("si", "cor", "asd", "sdf", "asf")
fileManagement.verifyJsonFileExistence()
