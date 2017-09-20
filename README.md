# Pympesa

Mpesa Rest API python library for:

  * Lipa na mpesa online
  * B2B
  * B2C
  * C2B
  * Transaction status
  * Account balance
  * Reversal


Installation:

  pip install pympesa

Usage:

  1. First you create your app in https://developer.safaricom.co.ke/user/me/apps [+ Add a new App]
  2. Your app will be created having a <CONSUMER_KEY> and a <CONSUMER_SECRET>
  3. Then you need to generate a time bound oauth access token which will enable you to call this APIs.
     
     import pympesa

     response = pympesa.oauth_generate_token(consumer_key, consumer_secret, env="production", version="v1").json()
     access_token = response.get("access_token")
     expiry = response.get("expires_in")
     
  4. With the access token you can now call the APIs.
  

