import requests
from data import Urls

class UserApi:
    @staticmethod
    def create_user(body):
        return requests.post(Urls.CREATE_USER_URL, json=body)
    
    @staticmethod
    def delete_user(token):
        headers = {'Authorization': token}
        return requests.delete(Urls.DELETE_USER_URL, headers=headers)