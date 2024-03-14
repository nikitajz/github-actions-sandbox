import requests
URL = "https://api.ipify.org"


def get_my_ip_address():
    return requests.get(URL).text


def new_func():
    print("New cool func v1")

