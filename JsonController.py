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

    def verifyUser(self, user_given, password_given):
        with open('users.json', 'r') as file:
            data = json.load(file)
        for user in data['users']:
            if user['user'] == user_given:
                if user['password'] == password_given:
                    return True
                else:
                    return False
        return False


fileManagement = JsonControllerUsers("users")
fileManagement.createJsonFile()
fileManagement.addUsers("jorge", "sdf", "1234", "sdf", "asfl")
fileManagement.addUsers("andrea", "cor", "123", "sdf", "asf")
fileManagement.verifyJsonFileExistence()
fileManagement.verifyUser('si','ad')
