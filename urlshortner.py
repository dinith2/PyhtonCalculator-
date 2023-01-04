import bitly_api
 


API_USER = "username"
API_KEY = "API_Key"
bitly = bitly_api.Connection(API_USER, API_KEY)

url = (input('> Enter your url '))

response = bitly.shorten(url)
 
print(response)