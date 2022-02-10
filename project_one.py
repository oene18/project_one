"""blbla"""
import requests


def greet(who):
    """greeting"""
    greeting = f"Hello, {who}"
    return greeting


r = requests.get('https://coreyms.com')
print(r.status_code)
