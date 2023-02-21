# case one
# try:
#     x = 1 / 0
# except ZeroDivisionError as e:
#     print("Error Code:", e)


# case two
import requests

response = requests.get("https://google.com")
response.raise_for_status()
print(response.text)
# <!doctype html><html itemscope=""itemtype="http://schema.org/WebPage" lang="en-IN"><head><meta content="text ...

response = requests.get("https://google.com/not-found")
response.raise_for_status()
# requests.exceptions.HTTPError:404 Client Error: Not Found for url: https://google.com/not-found
