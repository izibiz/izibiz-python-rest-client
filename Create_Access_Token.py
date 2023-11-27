import json
import requests


class CreateAccessToken:
    accessToken = None

    def setAccessToken(self, deger):
        self.accessToken = deger
        with open('Files/AccessToken.txt', 'w') as file:
            file.write(self.accessToken)

    def getAccessToken(self):
        with open('Files/AccessToken.txt', 'r') as file:
            self.accessToken = file.read()
        return self.accessToken
