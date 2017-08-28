#!/usr/bin/python

"""Mpesa rest API client.

This exposes various mpesa functionalities to developers.
"""

from datetime import datetime

authorization = "Bearer <Access-Token>"
content_type = "application/json"

consumer_key = "4318nVqAGpz2skVYvy47B3PLDpuSARD8"
consumer_secret = "atXr69HNm4LQ0RBH"

basic_token = ("SjhYNFdVQUsyc3ZjWHpiNlNHd1hyNmpSV" +
               "mt3UzZBTFY6NjZRZkQ2aFlBVGlBSVFVSQ")

shortcode_1 = "600535"
initiator_name_shortcode_1 = "testapi"
security_credential_shortcode_1 = "Safaricom535!"
shortcode_2 = "600000"
test_msisdn = "254708374149"
expiry_date = "2017-08-26T20:11:52+03:00"
lipa_na_mpesa_online_shortcode = "174379"
lipa_na_mpesa_online_passkey = ("bfb279f9aa9bdbcf158e97dd71a467cd" +
                                "2e0c893059b10f78e6b72ada1ed2c919")
generated_initiator_security_credential = ("Ev5b7WnOH90dP/DYumYTLVuYGJfk3F" +
                                           "pDq4xMfk2Ymz+cP6zrdQ9Tz6wkd+O3" +
                                           "hcbYIYns7r1Q2pgd21Z2ZdYtBA+7Db" +
                                           "aSmAHE8XICiad/5p40iHm9Vxi42RUZ" +
                                           "zkrGYOFHq8SjxE5TKt7ADVjlP31ijo" +
                                           "PoDl+FUqV2SVtad/Ns2IIfQoGDLbIx" +
                                           "97MDlzcAg6whsirW50bS2eiA0JS5Y+" +
                                           "FbgfQ6jwq1/SnCH5lE1NylR2doFM/n" +
                                           "3yD9zFsQmBYGQHxKFklWCds4WDdLhS" +
                                           "8jNgykDvFDK5Ct/WRqafRJMjfs5O3Z" +
                                           "NAaKqldpll1u5KfLDE0IHlPXIYRV4/" +
                                           "/2HXBbDJKFDw==")

authorization_basic = ("SjhYNFdVQUsyc3ZjWHpiNlNHd1hyNmpSV" +
                       "mt3UzZBTFY6NjZRZkQ2aFlBVGlBSVFVSQ")
access_token = "bQ6UHJnO2Xqn0ieOsVACaTUUUvCB"


def b2b_payment_request():
    """Mpesa Transaction from one company to another."""

    url = "https://sandbox.safaricom.co.ke/mpesa/b2b/v1/paymentrequest"

    payload = {
        "Initiator": "",
        "SecurityCredential": "",
        "CommandID": "",
        "SenderIdentifierType": "",
        "RecieverIdentifierType": "",
        "Amount": "",
        "PartyA": "",
        "PartyB": "",
        "AccountReference": "",
        "Remarks": "",
        "QueueTimeOutURL": "",
        "ResultURL": ""
    }

    return payload


def b2c_payment_request():
    """Mpesa Transaction from company to client."""

    url = "https://sandbox.safaricom.co.ke/mpesa/b2c/v1/paymentrequest"

    payload = {
        "InitiatorName": "",
        "SecurityCredential": "",
        "CommandID": "",
        "Amount": "",
        "PartyA": "",
        "PartyB": "",
        "Remarks": "",
        "QueueTimeOutURL": "",
        "ResultURL": "",
        "Occassion": ""
    }

    return payload


def c2b_register_url():
    """Use this API to register validation and confirmation URLs on M-Pesa."""

    url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"

    payload = {
        "ShortCode": "",
        "ResponseType": "",
        "ConfirmationURL": "",
        "ValidationURL": ""
    }

    return payload


def c2b_simulate_transaction():
    """Use this API to simulate a C2B transaction."""

    url = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"

    payload = {
        "ShortCode": "",
        "CommandID": "CustomerPayBillOnline",
        "Amount": "",
        "Msisdn": "",
        "BillRefNumber": ""
    }

    return payload


def transation_status():
    """Use this API to check the status of transaction."""

    url = "https://sandbox.safaricom.co.ke/mpesa/transactionstatus/v1/query"

    payload = {
        "Initiator": "",
        "SecurityCredential": "",
        "CommandID": "TransactionStatusQuery",
        "TransactionID": "",
        "PartyA": "",
        "IdentifierType": "1",
        "ResultURL": "",
        "QueueTimeOutURL": "",
        "Remarks": "",
        "Occasion": ""
    }

    return payload


def account_balance():
    """Use this API for reversal transaction."""

    url = "https://sandbox.safaricom.co.ke/mpesa/accountbalance/v1/query"

    payload = {
        "Initiator": "",
        "SecurityCredential": "",
        "CommandID": "AccountBalance",
        "PartyA": "",
        "IdentifierType": "4",
        "Remarks": "",
        "QueueTimeOutURL": "",
        "ResultURL": ""
    }

    return payload


def reversal():
    """Use this API for reversal transaction."""

    url = "https://sandbox.safaricom.co.ke/mpesa/reversal/v1/request"

    payload = {
        "Initiator": "",
        "SecurityCredential": "",
        "CommandID": "TransactionReversal",
        "TransactionID": "",
        "Amount": "",
        "ReceiverParty": "",
        "RecieverIdentifierType": "4",
        "ResultURL": "",
        "QueueTimeOutURL": "",
        "Remarks": "",
        "Occasion": ""
    }

    return payload


def lipa_na_mpesa_online_query():
    """For Lipa Na M-Pesa online payment using STK Push.

    Use this API to check the status of a Lipa Na M-Pesa Online Payment."""

    url = "https://sandbox.safaricom.co.ke/mpesa/stkpushquery/v1/query"

    payload = {
        "BusinessShortCode": " ",
        "Password": " ",
        "Timestamp": " ",
        "CheckoutRequestID": " "
    }

    return payload


def lipa_na_mpesa_online_payment():
    """For Lipa Na M-Pesa online payment using STK Push.

    Use this API to initiate online payment on behalf of a customer."""

    url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"

    payload = {
        "BusinessShortCode": "",
        "Password": "",
        "Timestamp": "",
        "TransactionType": "CustomerPayBillOnline",
        "Amount": "",
        "PartyA": "",
        "PartyB": "",
        "PhoneNumber": "",
        "CallBackURL": "",
        "AccountReference": "",
        "TransactionDesc": ""
    }

    return payload


def generate_oauth_token():
    """Gives you time bound access token to call allowed APIs."""
    # url = ("https://sandbox.safaricom.co.ke/oauth/v1/generate?" +
    #        "grant_type=client_credentials")
    pass


def generate_timestamp():
    return datetime.strftime(datetime.now(), "%Y%m%d%H%M%S")
