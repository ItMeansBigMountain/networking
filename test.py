import json
import requests




'''
NOTE user's self instance is going to have ['privileges'] and the name needs to include NVIDIA

SCOPE
needs to be admin
UserSelf["privileges"]["name"] ==  "NVIDIA Corp Wireless"



PROCEDURE
login to mist
grab all AP inventory from the NVIDIA privileges
    every AP's 
        name
        location 
        mac addr
        serial number

'''





# BUG LOGIN (fetch api token)
def mist_login(email , password):
    params = {
        'email'  : email ,
        'password'  : password ,
    }
    r = requests.request("POST",   "https://api.mist.com/api/v1/login"   , data=params)
    return r
# DEBUG
# token = mist_login("affan.fareed@gmail.com", "paper40gap")
# print( token )
# exit()




# # CREATE/DELETE API TOKEN
def create_api_token(token):
    headers = {
    'Authorization': f'Token {token}'
    }
    r = requests.get("https://api.mist.com/api/v1/self/apitokens", headers=headers ) 

    # success check
    if r.status_code == 200 :
        return r.json() 
    else:
        raise ValueError(r.text)
def delete_api_token(token , item):
    headers = {
    'Authorization': f'Token {token}'
    }
    # fetch id of token placement specified in item
    apitoken_id = requests.get("https://api.mist.com/api/v1/self/apitokens", headers=headers).json()[item]["id"]
    
    #  NEEDS ID OF TOKEN IN QUESTION
    r = requests.request("DELETE",   f"https://api.mist.com/api/v1/self/apitokens/{apitoken_id}" , headers=headers  )


    if r.status_code == 200 :
        return f"DELETE API TOKEN ID:  {apitoken_id}"
    else:
        raise ValueError(r.text)

    return r
# DEBUG
# print( create_api_token(  manual_token)  )
# print( delete_api_token(  manual_token , 0)  )













# all organizations
def _mist_user_data(token):
    headers = {
    'Authorization': f'Token {token}'
    }
    r = requests.request("GET",   "https://api.mist.com/api/v1/self"   , headers=headers).json()
    return r

# gets NVIDIA organization id
def mist_organization_id(token):
    # CHECKING IF TOKEN ASSOCIATED WITH NVIDIA
    userInfo = _mist_user_data(token)
    organization_ID = None
    for org in userInfo['privileges']:
        # if org['name'] == 'NVIDIA Corp Wireless':
        if 'NVIDIA' in  org['name']:
            organization_ID = org['org_id']
            return organization_ID
    # returns error if not NVIDIA corp
    raise ValueError("This token is not associated with NVIDIA")

# gets NVIDIA organization inventory
def mist_inventory(token , organization_ID):
    headers = {
    'Authorization': f'Token {token}'
    }
    r = requests.request("GET",   f"https://api.mist.com/api/v1/orgs/{organization_ID}/inventory"   , headers=headers).json()
    return r











# call functions down here...

# MANUALLY CREATE TOKEN BY GOING HERE
# https://api.mist.com/api/v1/self/apitokens
manual_token = ""

# AUTH
organization_ID = mist_organization_id(manual_token)

# inventory
inventory = mist_inventory(manual_token , organization_ID)
print(inventory)