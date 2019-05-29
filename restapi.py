import requests
import json
import os

#ENDPOINT = "http://127.0.0.1:8000/api/status/"



######################################################################################################################
#for handling data manipulation

# def do(method='get', data={}, is_json=True):
#     headers={}
#     if is_json:
#         headers['content-type']='application/json'
#         data=json.dumps(data)
#     r=requests.request(method, ENDPOINT, data=data, headers=headers)
#     print(r.text)
#     print(r.status_code)
#     return r
#
# do(data={'id':7})    #call to get method
#do(method='delete', data={'id':500})   #call to delete method
#do(method='put', data={'id':7, 'content':'facebook is cool', 'user':2})  #call to put method
#do(method='post', data={'content':'instagram is super cool', 'user':2})  #call to create/post method



########################################################################################################################

#For handling image
# import os
# image_path=os.path.join(os.getcwd(), "ai.jpg")
#
#
# def do_img(method='get', data={}, is_json=True, img_path=None):
#     headers={}
#     if is_json:
#         headers['content-type']='application/json'
#         data=json.dumps(data)
#     if img_path is not None:
#         with open(image_path, 'rb') as image:
#             file_data = {'image':image}
#             r=requests.request(method, ENDPOINT, data=data, headers=headers, files=file_data)
#     else:
#         r=requests.request(method, ENDPOINT, data=data, headers=headers)
#     print(r.text)
#     print(r.status_code)
#     return r

#do_img(method='post', data={'user':2, 'content':''}, is_json=False, img_path=image_path)
#do_img(method='put', data={'id':11, 'user':2, 'content':'newly created image object'}, is_json=False, img_path=image_path)

###################################################################################################################################

#permission test with python requests

# get_endpoint = ENDPOINT + str(12)
#
# post_data=json.dumps({'content': 'some random content'})
#
# r=requests.get(get_endpoint)
# print(r.text)
#
# r2=requests.get(ENDPOINT)
# print(r2.status_code)
#
# post_headers={'content-type':'application/json'}
#
# post_response=requests.post(ENDPOINT, data=post_data, headers=post_headers)
# print(post_response.text)

#######################################################################################################################################

#implemnting tests for JWT
# AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/jwt/"
# REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"
#
#
# headers = {'Content-Type': 'application/json'}
# #for posing data that creates token
# #-------------------------------------------------------------#
# data={
#     'username':'hello',
#     'password':'hii@1234'
# }
#
# r=requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
# #print(r.json())
# token = r.json()['token']
# #---------------------------------------------------------------#
#
# #for refreshing token
# refresh_data = { 'token':token }
# new_response = requests.post(REFRESH_ENDPOINT, data=json.dumps(refresh_data), headers=headers)
# new_token = new_response.json()#['token']
# print(new_token)

###############################################################################################################################################

#implemeting tests for authorization headers
# AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/jwt/"
#
# headers = {'Content-Type': 'application/json'}
#
# data={
#     'username':'hello',
#     'password':'hii@1234'
# }
#
# r=requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
# token = r.json()['token']
#
# headers = {'Content-Type': 'application/json',
#             "Authorization": "JWT " + token,
# }
#
#
# post_data=json.dumps({'content':'some random content'})
# posted_response = requests.post(ENDPOINT, data=post_data, headers=headers)
# print(posted_response.text)

############################################################################################################################################
#implemeting tests for custom authentication view

#AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/"
#REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"


# headers = {'Content-Type': 'application/json'}
# #for posing data that creates token
# #-------------------------------------------------------------#
# data={
#     'username':'hello2',
#     'password':'hii@1234',
# }
#
# r=requests.post("http://127.0.0.1:8000/api/auth/", data=json.dumps(data), headers=headers)
# token=r.json()
# print(token)

#---------------------------------------------------------------#

############################################################################################################################################
#implemeting tests for register view

# AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/register/"
# #REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"
#
#
# headers = {'Content-Type': 'application/json'}
# #for posing data that creates token
# #-------------------------------------------------------------#
# data={
#     'username':'hello12',
#     'email':'hello12@gmail.com',
#     'password':'hii@1234',
#     'password2':'hii@1234',
# }
#
# r=requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
# token=r.json()
# print(token)

############################################################################################################################################
#for testing IsOwnerOrReadOnly permission

AUTH_ENDPOINT = "http://127.0.0.1:8000/api/auth/"
REFRESH_ENDPOINT = AUTH_ENDPOINT + "refresh/"

image_path=os.path.join(os.getcwd(), "ai.jpg")


headers = {'Content-Type': 'application/json'}
#for posing data that creates token
#-------------------------------------------------------------#
data={
    'username':'hello',
    'password':'hii@1234',
}

r=requests.post(AUTH_ENDPOINT, data=json.dumps(data), headers=headers)
token=r.json()['token']
#print(token)

ENDPOINT = "http://127.0.0.1:8000/api/status/13/"

headers2 = { 'Authorization': 'JWT ' + token }

data2={
    'content':'This new content post'
}

with open(image_path, 'rb') as image:
    file_data = {'image':image}
    # r=requests.put(ENDPOINT, headers=headers2) #for updating data
    # print(r.text)
    # r=requests.post(ENDPOINT, data=data2, headers=headers2, files=file_data) #for creating data
    # print(r.text)
    r=requests.get(ENDPOINT, headers=headers2) #for getting data
    print(r.text)
