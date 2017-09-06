#!/usr/bin/python

"""Mpesa rest API client.

This exposes various mpesa functionalities to developers.

All class functions take in keyword arguments (kwargs) and
response returned in json.
"""

import base64
import requests
from datetime import datetime

from .urls import URL


class Pympesa:

    def __init__(self, access_token, env="production", version="v1"):
        self.headers = {"Authorization": "Bearer %s" % access_token}
        self.env = env
        self.version = version

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

        expected_keys = ["Initiator", "SecurityCredential",
                         "CommandID", "SenderIdentifierType",
                         "RecieverIdentifierType", "Amount",
                         "PartyA", "PartyB", "AccountReference",
                         "Remarks", "QueueTimeOutURL", "ResultURL"]

        payload = process_kwargs(expected_keys, kwargs)

        response = requests.post(
            URL[self.env][self.version]["b2b_payment_request"],
            json=payload, headers=self.headers)

        return response.json()

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

        expected_keys = ["InitiatorName", "SecurityCredential",
                         "CommandID", "Amount", "PartyA",
                         "PartyB", "Remarks", "QueueTimeOutURL",
                         "ResultURL", "Occassion"]

        payload = process_kwargs(expected_keys, kwargs)

        response = requests.post(
            URL[self.env][self.version]["b2c_payment_request"],
            json=payload, headers=self.headers)

        return response.json()

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

        expected_keys = ["ShortCode", "ResponseType",
                         "ConfirmationURL", "ValidationURL"]

        payload = process_kwargs(expected_keys, kwargs)

        response = requests.post(
            URL[self.env][self.version]["c2b_register_url"],
            json=payload, headers=self.headers)

        return response.json()

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

        expected_keys = ["ShortCode", "Amount",
                         "Msisdn", "BillRefNumber"]

        payload = process_kwargs(expected_keys, kwargs)
        payload["CommandID"] = "CustomerPayBillOnline"

        response = requests.post(
            URL[self.env][self.version]["c2b_simulate_transaction"],
            json=payload, headers=self.headers)

        return response.json()

    def transation_status_request(self, **kwargs):

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


           REQUEST DESCRIPTION/EXAMPLE
           ===========================

           {
            "Initiator": "Initiator",
            "SecurityCredential": ("KThCBU5kAY2Qm0RafdgWaoFY8bsbufMuve0mKSVAJeAUD6LsOsv9k5jQ6Zmm750DXc2BGpm6g4jJ9bB" +
                                   "oUJ9n/9Ar+8o+N7RFg77d+C89pMUCUpOn1MJaAcDCh7lBXCLoVuin7aaaZnVYwUysalsfYcergUO4VI3QATFYhlXzEswB/9csCt0H" +
                                   "wmgZLKTDB1bH0o9C7tHbD7OAARx5JXgQm+RBqzdUVMw0t2huwjcNLW0hZMQgdmjK0T6ss9YqmHc5rjXDx5RDrFE/8QjqstPLisX" +
                                   "64bItqZURqNMR/h02UwEJO2nh5RalzUHSLPoq4Wx2TotYvMFvAXbW4/n5z14yng=="),
            "CommandID": "Command ID - TransactionStatusQuery",
            "TransactionID": "Transaction ID e.g LC7918MI73",
            "PartyA": "Phone number that initiated the transaction",
            "IdentifierType": "1",
            "ResultURL": "https://ip_address:port/result_url",
            "QueueTimeOutURL": "https://ip_address:port/timeout_url",
            "Remarks": "Remarks",
            "Occasion": "Optional parameter"
           }


           Response Parameters
           ===================

           Name	                    | Description	                                      | Parameter Type  | Possible Values
           ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                    |                                                     |                 |
           OriginatorConversationID | The unique request ID for tracking a transaction	  | Alpha-Numeric	| alpha-numeric string of less then 20
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

        expected_keys = ["Initiator", "SecurityCredential",
                         "TransactionID", "PartyA",
                         "ResultURL", "QueueTimeOutURL",
                         "Remarks", "Occasion"]

        payload = process_kwargs(expected_keys, kwargs)
        payload["CommandID"] = "TransactionStatusQuery"
        payload["IdentifierType"] = "1"

        response = requests.post(
            URL[self.env][self.version]["transation_status_request"],
            json=payload, headers=self.headers)

        return response.json()

    def account_balance_request(self, **kwargs):

        """Use this API to enquire the balance on an M-Pesa BuyGoods (Till Number).

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


           REQUEST DESCRIPTION/EXAMPLE
           ===========================

           {
            "CommandID": "AccountBalance",
            "PartyA": "ShortCode",
            "IdentifierType": "4",
            "Remarks": "Remarks",
            "Initiator": "apitest",
            "SecurityCredential": ("KThCBU5kAY2Qm0RafdgWaoFY8bsbufMuve0mKSVAJeAUD6LsOsv9k5jQ6Zmm750DX" +
                                   "c2BGpm6g4jJ9bBoUJ9n/9Ar+8o+N7RFg77d+C89pMUCUpOn1MJaAcDCh7lBXCLoVuin7aaaZnVYwUysalsfYcerg" +
                                   "UO4VI3QATFYhlXzEswB/9csCt0HwmgZLKTDB1bH0o9C7tHbD7OAARx5JXgQm+RBqzdUVMw0t2huwjcNLW0hZMQgdmjK0T6ss9Y" +
                                   "qmHc5rjXDx5RDrFE/8QjqstPLisX64bItqZURqNMR/h02UwEJO2nh5RalzUHSLPoq4Wx2TotYvMFvAXbW4/n5z14yng=="),
            "QueueTimeOutURL":"http://172.29.227.122:9001/callback_mock/v1/submitResult",
            "ResultURL":"http://172.29.227.122:9001/callback_mock/v1/submitResult"
           }


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

        expected_keys = ["Initiator", "SecurityCredential", "PartyA",
                         "Remarks", "QueueTimeOutURL", "ResultURL"]

        payload = process_kwargs(expected_keys, kwargs)
        payload["CommandID"] = "AccountBalance"
        payload["IdentifierType"] = "4"

        response = requests.post(
            URL[self.env][self.version]["account_balance_request"],
            json=payload, headers=self.headers)

        return response.json()

    def reversal_request(self, **kwargs):

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


           REQUEST DESCRIPTION/EXAMPLE
           ===========================

           {
            "Initiator": "Initiator" ,
            "SecurityCredential": ("KThCBU5kAY2Qm0RafdgWaoFY8bsbufMuve0mKSVAJeAUD6LsOsv9k5jQ6Zmm750DXc2BGpm6g4jJ9bBo" +
                                   "UJ9n/9Ar+8oN7RFg77d+C89pMUCUpOn1MJaAcDCh7lBXCLoVuin7aaaZnVYwUysalsfYcergUO4VI3QATFYhlXzEswB/9csCt0Hwm" +
                                   "gZLKTDB1bH0o9C7tHbD7OAARx5JXgQm+RBqzdUVMw0t2huwjcNLW0hZMQgdmjK0T6ss9YqmHc5rjXDx5RDrFE/8Qjqst" +
                                   "PLisX64bItqZURqNMR/h02UwEJO2nh5RalzUHSLPoq4Wx2TotYvMFvAXbW4/n5z14yng=="),
            "CommandID": "Command ID e.g TransactionReversal",
            "TransactionID": "Transaction ID e.g LC7918MI73",
            "Amount": "Amount to reverse",
            "ReceiverParty": "Short code",
            "RecieverIdentifierType": "4",
            "ResultURL": "https://ip_address:port/result_url",
            "QueueTimeOutURL": "https://ip_address:port/timeout_url",
            "Remarks":"Remarks of the transaction",
            "Occasion": "Optional parameter"
           }


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

        expected_keys = ["Initiator", "SecurityCredential",
                         "TransactionID", "Amount",
                         "ReceiverParty", "ResultURL",
                         "QueueTimeOutURL", "Remarks", "Occasion"]

        payload = process_kwargs(expected_keys, kwargs)
        payload["CommandID"] = "TransactionReversal"
        payload["RecieverIdentifierType"] = "4"

        response = requests.post(
            URL[self.env][self.version]["reversal_request"],
            json=payload, headers=self.headers)

        return response.json()

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

        expected_keys = ["BusinessShortCode", "Password", "CheckoutRequestID"]

        payload = process_kwargs(expected_keys, kwargs)
        payload["Timestamp"] = generate_timestamp()

        response = requests.post(
            URL[self.env][self.version]["lipa_na_mpesa_online_query"],
            json=payload, headers=self.headers)

        return response.json()

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

        expected_keys = ["BusinessShortCode", "Password",
                         "Amount", "PartyA", "PartyB",
                         "PhoneNumber", "CallBackURL",
                         "AccountReference", "TransactionDesc"]

        payload = process_kwargs(expected_keys, kwargs)
        payload["Timestamp"] = generate_timestamp()
        payload["TransactionType"] = "CustomerPayBillOnline"

        response = requests.post(
            URL[self.env][self.version]["lipa_na_mpesa_online_payment"],
            json=payload, headers=self.headers)

        return response.json()


def oauth_generate_token(consumer_key, consumer_secret, env="production", version="v1"):

    """Authenticate your app and return an OAuth access token.

       This token gives you time bound access token to call allowed APIs.
       NOTE: The OAuth access token expires after an hour (3600 seconds),
             after which, you will need to generate another access token
             so you need to keep track of this.

       Request Keyword Parameters
       ==========================

       Name	                    | Description	                                      | Parameter Type  | Possible Values
       ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                |                                                     |                 |
       grant_type               | client_credentials grant type is supported          | Query           |
       ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                |                                                     |                 |
       Authorization            | Basic Auth over HTTPS, this is a base64 encoded     | Header          |
                                | string of an app's consumer key and consumer secret |                 |
       ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


       Query Parameters
       ================

       Name	                    | values                                              | Description
       ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                |                                                     |
       grant_type               | client_credentials 	                              | Only client_credentials grant type is supported
       (required)               |                                                     |
       ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++


       Response Parameters
       ===================

       Name	                    | Description	                                      | Parameter Type  | Possible Values
       ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                |                                                     |                 |
       Expiry                   | Token expiry time in seconds. 	                  | JSON Response   |
                                |                                                     | Body	        |
       ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
                                |                                                     |                 |
       Access_Token             | Access token to access other APIs                   | JSON Response   |
                                |                                                     | Body            |
       ++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    """

    return requests.get(URL[env][version]["oauth_generate_token"],
                        auth=requests.auth.HTTPBasicAuth(consumer_key, consumer_secret))


def encode_password(shortcode, passkey, timestamp):

    """Generate and return a base64 encoded password for online access."""

    return base64.encode(shortcode + passkey + timestamp)


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
