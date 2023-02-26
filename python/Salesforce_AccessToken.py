import requests
class SalesforceAccessToke:
     
     def pani_access_Token():
            Access_token_url = 'https://login.salesforce.com/services/oauth2/token'
            username = 'sadgun.daspalni@palni.com'
            password  = 'Sadgundas@6814OD93lhVJXmZ7BRhiz9uYbjsbR'
            client_id    ='3MVG9n_HvETGhr3CcKOcIffjIFDX_rVU3m88JMMxFPoANDql6GMY5CW2yDwsIGs3EamRaUyBjXj1cQGQ3HT9J'
            client_secret = 'A218351740DCB472DDE8F32588C963588F4DAA5BE1136566B3668BDED3448728'
            grant_type = 'password'
            headers = {
             "Content-Type": "application/x-www-form-urlencoded",
             "Accept": "application/json"
               }
            data = {
                    "grant_type": grant_type,
                    "client_id": client_id,
                    "client_secret": client_secret,
                    "username": username, 
                    "password" : password
                    }   
            response = requests.post(Access_token_url,headers=headers,data=data) 
        
            if response.status_code == requests.codes.ok:
                    # Parse the JSON response and extract the access token
                    token_json = response.json()
                    access_token = token_json["access_token"]
                    print("Access token:", access_token)
            else:
                    # Handle the error
                    print("Token request failed with status code:", response.status_code)

              