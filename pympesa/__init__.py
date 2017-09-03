#!/usr/bin/python

"""Mpesa rest API client.

This exposes various mpesa functionalities to developers.

CLASSES
=======

class Pympesa:

    def __init__(self, access_token)

    def b2b_payment_request(access_token, **kwargs)

    def b2c_payment_request(access_token, **kwargs)

    def c2b_register_url(access_token, **kwargs)

    def c2b_simulate_transaction(access_token, **kwargs)

    def transation_status(access_token, **kwargs)

    def account_balance(access_token, **kwargs)

    def reversal(access_token, **kwargs)

    def lipa_na_mpesa_online_query(access_token, **kwargs)

    def lipa_na_mpesa_online_payment(access_token, **kwargs)

FUNCTIONS
=========

def generate_oauth_access_token(consumer_key, consumer_secret)
"""

import requests
from requests.auth import HTTPBasicAuth
from datetime import datetime


class Pympesa:

    def __init__(self, access_token):
        self.access_token = access_token

    def b2b_payment_request(self, **kwargs):

        """Mpesa Transaction from one company to another.

           Request Keyword Parameters
           ==========================

           Name	                    | Description                                         | Parameter Type  | Possible Values
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           CommandID                | The command id used to carry out a B2B payment      | String          | BusinessPayBill
                                    |                                                     |                 | BusinessBuyGoods
                                    |                                                     |                 | DisburseFundsToBusiness
                                    |                                                     |                 | BusinessToBusinessTransfer
                                    |                                                     |                 | BusinessTransferFromMMFToUtility
                                    |                                                     |                 | BusinessTransferFromUtilityToMMF
                                    |                                                     |                 | MerchantToMerchantTransfer
                                    |                                                     |                 | MerchantTransferFromMerchantToWorking
                                    |                                                     |                 | MerchantServicesMMFAccountTransfer
                                    |                                                     |                 | AgencyFloatAdvance
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           Amount                   | The amount been transacted	                      | Numeric         | 1
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           PartyA                   | Organization Sending the transaction	              | Numeric         | Shortcode (6 digits)
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           SenderIdentifier         | Type of organization sending the transaction        | Numeric         | 1 - MSISDN
                                    |                                                     |                 | 2 - Till Number
                                    |                                                     |                 | 4 - Organization short code
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           PartyB                   | Organization Receiving the funds	                  | Numeric         |  Shortcode (6 digits)
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           RecieverIdentifierType   | Type of organization receiving the transaction      | Numeric         | 1 - MSISDN
                                    |                                                     |                 | 2 - Till Number
                                    |                                                     |                 | 4 - Organization short code
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           Remarks                  | Comments that are sent along with the transaction   | String          | String of less then 100 characters
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           Initiator                | This is the credential/username used to             | String          | This is the credential/username used to
                                    | authenticate the transaction request.	              |                 | authenticate the transaction request
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           SecurityCredential       | This is the encrypted password to autheticate the   | String          | Encrypted password for the initiator
                                    | transaction request	                              |                 | to authenticate using the request
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           QueueTimeOutURL          | The path that stores information of time out        | URL             | https://ip or domain:port/path
                                    | transactions                                        |                 |
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           ResultURL                | The path that receives results from M-Pesa.	      | URL             | https://ip or domain:port/path
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           AccountReference         | Account Reference mandatory for                     | Alpha-Numeric   | string of less then 20 characters
                                    | "BussinessPaybill" CommandID                        |                 |
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


           Response Parameters
           ===================

           Name                     | Description	                                      | Parameter Type	| Possible value
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           OriginatorConverstionID  | The unique request ID for tracking a transaction	  | Alpha-Numeric	| alpha-numeric string of less
                                    |                                                     |                 | then 20 characters
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           ConversationID           | The unique request ID returned by mpesa for each    | Alpha-Numberic  | - Error codes
                                    | request made                                        |                 | - 500 OK
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           ResponseDescription      | Response Description message                        | String          | - The service request has failed
                                    |                                                     |                 | - The service request has been accepted
                                    |                                                     |                 |   successfully
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        """

        api_url = "https://sandbox.safaricom.co.ke/mpesa/b2b/v1/paymentrequest"
        headers = {"Authorization": "Bearer %s" % self.access_token}

        expected_keys = ["Initiator", "SecurityCredential",
                         "CommandID", "SenderIdentifierType",
                         "RecieverIdentifierType", "Amount",
                         "PartyA", "PartyB", "AccountReference",
                         "Remarks", "QueueTimeOutURL", "ResultURL"]

        payload = process_kwargs(expected_keys, kwargs)

        response = requests.post(api_url, json=payload, headers=headers)

        return response.text

    def b2c_payment_request(self, **kwargs):

        """Mpesa Transaction from company to client.

           Request Keyword Parameters
           ==========================

           Name	                    | Description	                                      | Parameter Type  | Possible Values
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           InitiatorName            | The name of the initiator initiating the request	  | Alpha-numeric	| This is the credential/username used
                                    |                                                     |                 | to authenticate the transaction request
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           SecurityCredential       | Encrypted Credential of user getting transaction    | Alpha-numeric   | Encrypted password for the initiator to
                                    | amount                                              |                 | authenticate the transaction request
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           CommandID                | Unique command for each transaction type            | Alphanumeric    |
                                    |     SalaryPayment                                   |                 | - SalaryPayment
                                    |     BusinessPayment                                 |                 | - BusinessPayment
                                    |     PromotionPayment                                |                 | - PromotionPayment
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           Amount                   | The amount been transacted	                      | Numbers	        | 00
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           PartyA                   | Organization/MSISDN sending the transaction	      | Numbers         | - Shortcode (6 digits)
                                    |                                                     |                 | - MSISDN (12 digits)
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           PartyB                   | MSISDN sending the transaction                      | PhoneNumber -   | - MSISDN (12 digits)
                                    |                                                     | CountryCode i.e |
                                    |                                                     | (254) without + |
                                    |                                                     | sign            |
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           Remarks                  | Comments that are sent along with the transaction   | Alpha-numeric	| sequence of characters upto 100
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           QueueTimeOutURL          | The path that stores information of time out        | URL             | https://ip or domain:port/path
                                    | transaction                                         |                 |
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           ResultURL                | The path that stores information of transactions	  | URL	            | https://ip or domain:port/path
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           Occassion                | Optional Parameter	                              | Alpha-numeric	| sequence of characters up to 100
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


           Response Parameters
           ===================

           Name	                    | Description	                                      | Parameter Type  | Possible Values
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           ConversationId           | Conversation Id of transaction	                  | Numeric	        | alpha-numeric string of less then 20
                                    |                                                     |                 | characters
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           OriginatorConversationId | Originator Conversation Id to track transaction	  | Alpha-numeric   | - Error codes
                                    |                                                     |                 | - 500 OK
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           ResponseDescription      | Response message description	                      | Alpha-numeric   | - The service request has failed
                                    |                                                     |                 | - The service request has been accepted
                                    |                                                     |                 |   successfully
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        """

        api_url = "https://sandbox.safaricom.co.ke/mpesa/b2c/v1/paymentrequest"
        headers = {"Authorization": "Bearer %s" % self.access_token}

        expected_keys = ["InitiatorName", "SecurityCredential",
                         "CommandID", "Amount", "PartyA",
                         "PartyB", "Remarks", "QueueTimeOutURL",
                         "ResultURL", "Occassion"]

        payload = process_kwargs(expected_keys, kwargs)

        response = requests.post(api_url, json=payload, headers=headers)

        return response.text

    def c2b_register_url(self, **kwargs):

        """Use this API to register validation and confirmation URLs on M-Pesa.

           Request Keyword Parameters
           ==========================

           Name	                    | Description	                                      | Parameter Type  | Possible Values
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           ValidationURL            | Validation URL for the client	                      | URL	            | https://ip or domain:port/path
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           ConfirmationURL          | Confirmation URL for the client	                  | URL	            | https://ip or domain:port/path
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           ResponseType             | Default response type for timeout. Incase a         | String          | - Cancelled
                                    | transaction times out, Mpesa will by default        |                 | - Completed
                                    | Complete or Cancel the transaction                  |                 |
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           ShortCode                | The short code of the organization                  | Numeric	        | 123456
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


           Response Parameters
           ===================

           Name	                    | Description	                                      | Parameter Type  | Possible Values
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           OriginatorConverstionID  | The unique request ID for tracking a transaction	  | Alpha-Numeric	| alpha-numeric string of less then 20
                                    |                                                     |                 | characters
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           ConversationID           | The unique request ID returned by mpesa for         | Alpha-Numeric   | - Error codes
                                    | each request made	Alpha-Numeric                     |                 | - 500 OK
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           ResponseDescription      | Response Description message	                      | String	        | - The service request has failed
                                    |                                                     |                 | - The service request has been accepted
                                    |                                                     |                 |   successfully
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        """

        api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
        headers = {"Authorization": "Bearer %s" % self.access_token}

        expected_keys = ["ShortCode", "ResponseType",
                         "ConfirmationURL", "ValidationURL"]

        payload = process_kwargs(expected_keys, kwargs)

        response = requests.post(api_url, json=payload, headers=headers)

        return response.text

    def c2b_simulate_transaction(self, **kwargs):

        """Use this API to simulate a C2B transaction.

           Request Keyword Parameters
           ==========================

           Name	                    | Description	                                      | Parameter Type  | Possible Values
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           CommandID                | Unique command for each transaction type.           | String          | - CustomerPayBillOnline
                                    | For C2B dafult                                      |                 | - CustomerBuyGoodsOnline
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           Amount                   | The amount being transacted	                      | Numeric	        | 1
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           Msisdn                   | Phone number (msisdn) initiating the transaction	  | Numeric	        | MSISDN(12 digits) - 254XXXXXXXXX
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           BillRefNumber            | Bill Reference Number (Optional)	                  | Alpha-Numeric	| Alpha-Numeric less then 20 digits
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           ShortCode                | Short Code receiving the amount being transacted	  | Numeric	        | Shortcode (6 digits) - XXXXXX
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


           Response Parameters
           ===================

           Name	                    | Description	                                      | Parameter Type  | Possible Values
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           OriginatorConverstionID  | The unique request ID for tracking a transaction	  | Alpha-Numeric	| alpha-numeric string of less then 20
                                    | characters                                          |                 |
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           ConversationID           | The unique request ID returned by mpesa for each    | Alpha-Numeric   | - Error codes
                                    | request made                                        | - 500 OK        | - 500 OK
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           ResponseDescription      | Response Description message	                      | String          | - The service request has failed
                                    |                                                     |                 | - The service request has been accepted
                                    |                                                     |                 |   successfully
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        """

        api_url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
        headers = {"Authorization": "Bearer %s" % self.access_token}

        expected_keys = ["ShortCode", "Amount",
                         "Msisdn", "BillRefNumber"]

        payload = process_kwargs(expected_keys, kwargs)
        payload["CommandID"] = "CustomerPayBillOnline"

        response = requests.post(api_url, json=payload, headers=headers)

        return response.text

    def transation_status(self, **kwargs):

        """Use this API to check the status of transaction.

           Request Keyword Parameters
           ==========================

           Name	                    | Description	                                      | Parameter Type  | Possible Values
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           CommandID                | Takes only 'TransactionStatusQuery' command id      | String	        | TransactionStatusQuery
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           PartyA                   | Organization/MSISDN sending the transaction	      | Numeric	        | - Shortcode (6 digits)
                                    |                                                     |                 | - MSISDN (12 Digits)
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           IdentifierType           | Type of organization receiving the transaction      | Numeric	        | 1 - MSISDN
                                    |                                                     |                 | 2 - Till Number
                                    |                                                     |                 | 4 - Organization short code
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           Remarks                  | Comments that are sent along with the transaction	  | String	        | sequence of characters up to 100
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           Initiator                | The name of Initiator to initiating  the request	  | Alpha-Numeric	| This is the credential/username used to
                                    |                                                     |                 | authenticate the transaction request
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           SecurityCredential       | Encrypted Credential of user getting transaction    | String          | Encrypted password for the initiator to
                                    | amount                                              |                 | authenticate the transaction request
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           QueueTimeOutURL          | The path that stores information of time out        | URL             | https://ip or domain:port/path
                                    | transaction                                         |                 |
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           ResultURL                | The path that stores information of transaction 	  | URL	            | https://ip or domain:port/path
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           TransactionID            | Unique identifier to identify a transaction on      | Alpha-Numeric   | LKXXXX1234
                                    | M-Pesa                                              |                 |
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           Occasion                 | Optional Parameter 	                              | String	        | sequence of characters up to 100
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


           Response Parameters
           ===================

           Name	                    | Description	                                      | Parameter Type  | Possible Values
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           OriginatorConverstionID  | The unique request ID for tracking a transaction	  | Alpha-Numeric	| alpha-numeric string of less then 20
                                    |                                                     |                 | characters
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           ConversationID           | The unique request ID returned by mpesa for each    | Alpha-Numeric   | - Error codes
                                    | request made	Alpha-Numeric                         |                 | - 500 OK
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           ResponseDescription      | Response Description message	                      | String	        | - The service request has failed
                                    |                                                     |                 | - The service request has been accepted
                                    |                                                     |                 |   successfully
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        """

        api_url = "https://sandbox.safaricom.co.ke/mpesa/transactionstatus/v1/query"
        headers = {"Authorization": "Bearer %s" % self.access_token}

        expected_keys = ["Initiator", "SecurityCredential",
                         "TransactionID", "PartyA",
                         "ResultURL", "QueueTimeOutURL",
                         "Remarks", "Occasion"]

        payload = process_kwargs(expected_keys, kwargs)
        payload["CommandID"] = "TransactionStatusQuery"
        payload["IdentifierType"] = "1"

        response = requests.post(api_url, json=payload, headers=headers)

        return response.text

    def account_balance(self, **kwargs):

        """Use this API for reversal transaction.

           Request Keyword Parameters
           ==========================

           Name	                    | Description	                                      | Parameter Type  | Possible Values
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           CommandID                | Takes only 'AccountBalance' CommandID               | String	        | AccountBalance
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           PartyA                   | Type of organization receiving the transaction	  | Numeric	        | XXXXXX
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           IdentifierType           | Type of organization receiving the transaction      | Numeric	        | 1 - MSISDN
                                    |                                                     |                 | 2 - Till Number
                                    |                                                     |                 | 4 - Organization short code
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           Remarks                  | Comments that are sent along with the transaction.  | String	        | sequence of characters up to 100
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           Initiator                | The name of Initiator to initiating  the request	  | Alpha-Numeric	| This is the credential/username used to
                                    | authenticate the transaction request                |                 |
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           SecurityCredential       | Encrypted Credential of user getting transaction    | String          | Encrypted password for the initiator to
                                    | amount                                              |                 | autheticate the transaction request
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           QueueTimeOutURL          | The path that stores information of time out        | URL             | URL https://ip or domain:port/path
                                    | transaction                                         |                 |
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           ResultURL                | The path that stores information of transaction 	  | URL	            | https://ip or domain:port/path
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


           Response Parameters
           ===================

           Name	                    | Description	                                      | Parameter Type  | Possible Values
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           OriginatorConverstionID  | The unique request ID for tracking a transaction	  | Alpha-Numeric	| alpha-numeric string of less then 20
                                    |                                                     |                 | characters
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           ConversationID           | The unique request ID returned by mpesa for each    | Alpha-Numeric   | - Error codes
                                    | request made	Alpha-Numeric	                      |                 | - 500 OK
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           ResponseDescription      | Response Description message	                      | String	        | - The service request has failed
                                    |                                                     |                 | - The service request has been accepted
                                    |                                                     |                 |   successfully
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        """

        api_url = "https://sandbox.safaricom.co.ke/mpesa/accountbalance/v1/query"
        headers = {"Authorization": "Bearer %s" % self.access_token}

        expected_keys = ["Initiator", "SecurityCredential", "PartyA",
                         "Remarks", "QueueTimeOutURL", "ResultURL"]

        payload = process_kwargs(expected_keys, kwargs)
        payload["CommandID"] = "AccountBalance"
        payload["IdentifierType"] = "4"

        response = requests.post(api_url, json=payload, headers=headers)

        return response.text

    def reversal(self, **kwargs):

        """Use this API for reversal transaction.

           Request Keyword Parameters
           ==========================

           Name	                    | Description	                                      | Parameter Type  | Possible Values
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           CommandID                | Takes only 'TransactionReversal' Command id         | String	        | TransactionReversal
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           ReceiverParty            | Organization/MSISDN sending the transaction	      | Numeric	        | - Shortcode (6 digits)
                                    |                                                     |                 | - MSISDN (12 Digits)
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           ReceiverIdentifierType   | Type of organization receiving the transaction      | Numeric	        | 1 - MSISDN
                                    |                                                     |                 | 2 - Till Number
                                    |                                                     |                 | 4 - Organization short code
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           Remarks                  | Comments that are sent along with the transaction.  | String	        | sequence of characters up to 100
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           Initiator                | The name of Initiator to initiating  the request	  | Alpha-Numeric	| This is the credential/username used to
                                    |                                                     |                 | authenticate the transaction request
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           SecurityCredential       | Encrypted Credential of user getting transaction    | String          | Encrypted password for the initiator to
                                    | amount                                              |                 | authenticate the transaction request
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           QueueTimeOutURL          | The path that stores information of time out        | URL             | https://ip or domain:port/path
                                    | transaction                                         |                 |
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           ResultURL                | The path that stores information of transaction 	  | URL	            | https://ip or domain:port/path
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           TransactionID            | Organization Receiving the funds	                  | Alpha-Numeric	| LKXXXX1234
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           Occasion                 | Optional Parameter 	                              | String	        | sequence of characters up to 100
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


           Response Parameters
           ===================

           Name	                    | Description	                                      | Parameter Type  | Possible Values
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           OriginatorConverstionID  | The unique request ID for tracking a transaction	  | Alpha-Numeric	| alpha-numeric string of less then 20
                                    |                                                     |                 | characters
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           ConversationID           | The unique request ID returned by mpesa for each    | Alpha-Numeric   | - Error codes
                                    | request made                                        |                 | - 500 OK
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           ResponseDescription      | Response Description message	                      | String	        | - The service request has failed
                                    |                                                     |                 | - The service request has been accepted
                                    |                                                     |                 |   successfully
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        """

        api_url = "https://sandbox.safaricom.co.ke/mpesa/reversal/v1/request"
        headers = {"Authorization": "Bearer %s" % self.access_token}

        expected_keys = ["Initiator", "SecurityCredential",
                         "TransactionID", "Amount",
                         "ReceiverParty", "ResultURL",
                         "QueueTimeOutURL", "Remarks", "Occasion"]

        payload = process_kwargs(expected_keys, kwargs)
        payload["CommandID"] = "TransactionReversal"
        payload["RecieverIdentifierType"] = "4"

        response = requests.post(api_url, json=payload, headers=headers)

        return response.text

    def lipa_na_mpesa_online_query(self, **kwargs):

        """For Lipa Na M-Pesa online payment using STK Push.

           Use this API to check the status of a Lipa Na M-Pesa Online Payment.

           Request Keyword Parameters
           ==========================

           Name	                    | Description	                                      | Parameter Type  | Possible Values
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           BusinessShortCode        | Business Short Code                                 | Numeric	        | Shortcode (6 digits)
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           Password                 | Password	                                          | String	        | base64.encode(Shortcode:Passkey:Timestamp)
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           Timestamp                | Timestamp	                                          | Timestamp 	    | yyyymmddhhiiss
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           CheckoutRequestID        | Checkout RequestID	                              | String	        | ws_co_123456789
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


           Response Parameters
           ===================

           Name	                    | Description	                                      | Parameter Type  | Possible Values
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           MerchantRequestID        | Merchant Request ID	                              | Numeric	        | 1234-1234-1
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           CheckoutRequestID        | Check out Request ID	                              | String	        | ws_co_123456789
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           ResponseCode             | Response Code	                                      | Numeric	        | 0
                                    |                                                     |                 | Error codes
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           ResultDesc               | Result Desc	                                      | String	        | String
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           ResponseDescription      | Response Description message	                      | String	        | - The service request has failed
                                    |                                                     |                 | - The service request has been accepted
                                    |                                                     |                 |   successfully
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           ResultCode               | Result Code	                                      | Numeric	        | 1032
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        """

        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpushquery/v1/query"
        headers = {"Authorization": "Bearer %s" % self.access_token}

        expected_keys = ["BusinessShortCode", "Password", "CheckoutRequestID"]

        payload = process_kwargs(expected_keys, kwargs)
        payload["Timestamp"] = generate_timestamp()

        response = requests.post(api_url, json=payload, headers=headers)

        return response.text

    def lipa_na_mpesa_online_payment(self, **kwargs):

        """For Lipa Na M-Pesa online payment using STK Push.

           Use this API to initiate online payment on behalf of a customer.

           Request Keyword Parameters
           ==========================

           Name	                    | Description	                                      | Parameter Type  | Possible Values
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           BusinessShortCode        | The organization shortcode used to receive the      | Numeric         | Shortcode (6 digits)
                                    | transaction                                         |                 |
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           Password                 | The password for encrypting the request	          | String	        | base64.encode(Shortcode:Passkey:Timestamp)
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           Timestamp                | The timestamp of the transaction	                  | Timestamp	    | yyyymmddhhiiss
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           TransactionType          | The transaction type to be used for the request     | String          | CustomerPayBillOnline
                                    | 'CustomerPayBillOnline'                             |                 |
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           Amount                   | The amount to be transacted	                      | Numeric	        | 1
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           PartyA                   | The entity sending the funds	                      | Numeric	        | MSISDN (12 digits)
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           PartyB                   | The organization receiving the funds                | Numeric	        | Shortcode (6 digits)
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           PhoneNumber              | The MSISDN sending the funds	                      | Numeric	        | MSISDN (12 digits)
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           CallBackURL              | Call Back URL	                                      | URL	            | https://ip or domain:port/path
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           AccountReference         | Account Reference	                                  | Alpha-Numeric	| Any combinations of letters and numbers
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           TransactionDesc          | Description of the transaction	                  | String	        | any string of less then 20 characters
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


           Response Parameters
           ===================

           Name	                    | Description	                                      | Parameter Type  | Possible Values
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           MerchantRequestID        | Merchant Request ID	                              | Numeric	        | 1234-1234-1
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           CheckoutRequestID        | Checkout Request ID	                              | String	        | ws_co_123456789
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           ResponseDescription      | Response Description message	                      | String	        | - The service request has failed
                                    |                                                     |                 | - The service request has been accepted
                                    |                                                     |                 |   successfully
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           ResponseCode             | Response Code	                                      | Numeric	        | 0
                                    |                                                     |                 | Error codes
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           CustomerMessage          | Customer Message	                                  | String	        | A sequence of less then 20 characters
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
        """

        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % self.access_token}

        expected_keys = ["BusinessShortCode", "Password",
                         "Amount", "PartyA", "PartyB",
                         "PhoneNumber", "CallBackURL",
                         "AccountReference", "TransactionDesc"]

        payload = process_kwargs(expected_keys, kwargs)
        payload["Timestamp"] = generate_timestamp()
        payload["TransactionType"] = "CustomerPayBillOnline"

        response = requests.post(api_url, json=payload, headers=headers)

        return response.text


def generate_oauth_access_token(consumer_key, consumer_secret):

    """Authenticate your app and return an OAuth access token.

       Positional Parameters
       =====================
       consumer_key    - YOUR APPs CONSUMER KEY
       consumer_secret - YOUR APPs CONSUMER SECRET

       NOTE: The OAuth access token expires after an hour (3600 seconds),
             after which, you will need to generate another access token
             so you need to keep track of this.
    """

    api_url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"

    return requests.get(api_url, auth=HTTPBasicAuth(consumer_key, consumer_secret))


def generate_timestamp():

    """Return the current timestamp formated as YYYYMMDDHHMMSS"""

    return datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")


def process_kwargs(expected_keys, kwargs):

    """Check for any expected but missing keyword arguments
       and raise a TypeError else return the keywords arguments
       repackaged in a dictionary i.e the payload.
    """
    payload = {}

    for key in expected_keys:
        value = kwargs.pop(key, False)
        if not value:
            raise TypeError("Missing keyword argument: %s" % key)
        else:
            payload[key] = value

    return payload
