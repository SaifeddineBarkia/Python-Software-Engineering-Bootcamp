import requests

def get_and_parse_user(base_url:str,endpoint_prefix:str ,user_id:int):
    url = base_url + endpoint_prefix + str(user_id)
    return requests.get(url)







# response = requests.get('http://127.0.0.1:8000/user/0')

# print(response.json())

# response = requests.get('http://127.0.0.1:8000/user/0')


# json_example = {
#   "short_description": "string",
#   "long_bio": "string",
#   "name": "string",
#   "liked_posts": [
#     0,2,3,4
#   ]
# }
# respone_1 = requests.post('http://127.0.0.1:8000/user' , json = json_example)
# respone_1 = requests.post('http://127.0.0.1:8000/user' , json = json_example)
# print(respone_1.json())
# print(respone_1.json())
# print('d')
# print(respone_1.status_code)