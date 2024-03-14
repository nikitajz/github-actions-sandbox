import requests


def get_my_ip_address():
    return requests.get("https://api.ipify.org").text
