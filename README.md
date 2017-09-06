# Pympesa

Mpesa Rest API python library for:

  * B2B
  * B2C
  * C2B
  * Transaction status
  * Account balance
  * Reversal
  * Lipa na mpesa online

Installation:

  pip install pympesa

Usage:

  1. First you create your app in https://developer.safaricom.co.ke/user/me/apps [+ Add a new App]
  2. Your app will be created having a <CONSUMER_KEY> and a <CONSUMER_SECRET>
  3. Then you need to generate a time bound oauth access token which will enable you to call this APIs.
     
     import pympesa
     import json

     response = json.loads(pympesa.oauth_generate_token(consumer_key, consumer_secret, env="production", version="v1"))
     expiry = response["Expiry"]
     access_token = response["Access_Token"]

  4. With the access token you can now call the APIs as follows:
     Example calling transaction status API.

     import pympesa
     import json

     pympesa = Pympesa(access_token="xxxyyyzzz")
     response = pympesa.transaction_status_query(
                    "Initiator": "CompanyX",
	            "SecurityCredential": ("KThCBU5kAY2Qm0RafdgWaoFY8bsbufMuve0mKSVAJeAUD6LsOsv9k5jQ6Zmm750DXc2BGpm6g4jJ9bB" +
				           "oUJ9n/9Ar+8o+N7RFg77d+C89pMUCUpOn1MJaAcDCh7lBXCLoVuin7aaaZnVYwUysalsfYcergUO4VI3QATFYhlXzEswB/9csCt0H" +
				           "wmgZLKTDB1bH0o9C7tHbD7OAARx5JXgQm+RBqzdUVMw0t2huwjcNLW0hZMQgdmjK0T6ss9YqmHc5rjXDx5RDrFE/8QjqstPLisX" +
				           "64bItqZURqNMR/h02UwEJO2nh5RalzUHSLPoq4Wx2TotYvMFvAXbW4/n5z14yng=="),
	            "CommandID": "TransactionStatusQuery",
	            "TransactionID": "LC7918MI73",
	            "PartyA": "254723456789",
	            "IdentifierType": "1",
	            "ResultURL": "https://127.0.0.1:8080/result_url",
	            "QueueTimeOutURL": "https://127.0.0.1:8080/timeout_url",
	            "Remarks": "Payment to wrong recipient",
	            "Occasion": "N/A"
	        )

     response = json.loads(response)

     originator_conversation_id = response["OriginatorConverstionID"]
     conversation_id = response["ConverstionID"]
     response_description = response["ResponseDescription"]
