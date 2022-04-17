import json
import requests




'''

SCOPE
needs to be admin
user's self instance is going to have ['privileges'] and the name needs to include NVIDIA
    userInfo["privileges"][i]["name"] ==  "NVIDIA Corp Wireless"


PROCEDURE
login to mist
grab all AP inventory from the NVIDIA privileges
    every AP's 
        name
        location 
        mac addr
        serial number


TODO inventory.py
- need to double check if inventory api call endpoint is the same as garrets
- change manual_token to nvidias 
- return data set of clean data


'''



# all orginizations
def _mist_user_data(token):
    headers = {
    'Authorization': f'Token {token}'
    }
    r = requests.request("GET",   "https://api.mist.com/api/v1/self"   , headers=headers).json()

    print(r["privileges"])


    # multiple Orginizations
    if len(r["privileges"]) > 1:
        print("Please Identify Orginization")
        for x in range(0,len(r["privileges"]), 1):
            print(f"{x} : {r['privileges'][x]['name']}")
        # USER INPUT
        organization_name_option = int(input("please enter an option number: "))
        organization_ID = r["privileges"][organization_name_option]["org_id"]
    # ONLY ONE ORGINIZATION
    else:
        organization_ID = r["privileges"][0]["org_id"]
    return organization_ID





# endpoiints
def mist_inventory(token , organization_ID):
    headers = {
    'Authorization': f'Token {token}'
    }
    r = requests.request("GET",   f"https://api.mist.com/api/v1/orgs/{organization_ID}/inventory"   , headers=headers).json()
    return r











# call functions down here...

# MANUALLY CREATE TOKEN BY GOING HERE AFTER LOGGING INTO MIST API
# https://api.mist.com/api/v1/self/apitokens
manual_token = ""
organization_ID = _mist_user_data(manual_token)



# sorting devices
inventory = mist_inventory(manual_token , organization_ID)
print(inventory)
# [
#     {
#         "serial": "FXLH2015150025",
#         "modified_time": 1542829778,
#         "id": "00000000-0000-0000-0000-5c5b35000018"
#         "model": "AP41",
#         "type": "ap",
#         "mac": "5c5b35000018",
#         "name": "hallway",
#         "site_id": "4ac1dcf4-9d8b-7211-65c4-057819f0862b",
#         "deviceprofile_id": "6f4bf402-45f9-2a56-6c8b-7f83d3bc98e9", 
#         "status": "connected",
#         "created_time": 1542328276,
#     }
# ]





