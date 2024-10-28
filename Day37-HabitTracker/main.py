import requests
from datetime import datetime


username = "[YOUR_USER_NAME]"
password = "[YOUR_AUTH_TOKEN]"

data = input("How many minutes did you code today? ")

# --------------------------CREATING A NEW USER-------------------------------------

# pixela_new_user_endpoint = "https://pixe.la/v1/users"
# user_params = {
#     "token": password,
#     "username": username,
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes"
# }
#
# response = requests.post(url=pixela_new_user_endpoint, json=user_params)
# print(response.text)



# -------------------------CREATING A GRAPH-------------------------

# pixela_create_graph_endpoint = f"https://pixe.la/v1/users/{username}/graphs"
# graph_params = {
#     "id": "graph1",
#     "name": "Coding Time",
#     "unit": "minutes",
#     "type": "int",
#     "color": "momiji"
# }
#
# headers = {
#     "X-USER-TOKEN": password
# }
#
# response = requests.post(url=pixela_create_graph_endpoint, json=graph_params, headers=headers)
# print(response.text)

# -------------------------ADDING A PIXEL----------------------------------------

# today = datetime.now()
#
# pixela_add_pixel_endpoint = f"https://pixe.la/v1/users/{username}/graphs/{graph_params['id']}"
#
# pixel_params = {
#     "date": today.strftime("%Y%m%d")
#     "quantity": data,
# }
#
# response = requests.post(url=pixela_add_pixel_endpoint, json=pixel_params, headers=headers)
# print(response.text)

# ------------------------------UPDATING A PIXEL----------------------------------------

# today = datetime.now()
# pixela_pixel_update_endpoint = f"https://pixe.la/v1/users/{username}/graphs/{graph_params["id"]}/today.strftime("%Y%m%d")"
# update_pixel = {
#     "quantity": data,
# }
# response = requests.put(url=pixela_pixel_update_endpoint, json=update_pixel, headers=headers)
# print(response.text)

# ------------------------------------DELETING A PIXEL------------------------------------------

# delete_pixel_endpoint = f"https://pixe.la/v1/users/{username}/graphs/{graph_params['id']}/20241027"
# response = requests.delete(url=delete_pixel_endpoint, headers=headers)
# print(response.text)
