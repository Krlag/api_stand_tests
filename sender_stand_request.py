import configuration
import requests


def get_users_table ():
    url = configuration.URL_SERVICE + configuration.USERS_TABLE_PATH
    response = requests.get (url)
    return response

def post_new_user (user_body):
    url = configuration.URL_SERVICE + configuration.CREATE_USER_PATH
    response = requests.post (url, data = user_body)
    return response