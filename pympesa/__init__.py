#!/usr/bin/python

"""Mpesa rest API client.

This exposes various mpesa functionalities to developers.
"""

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


def b2b():
    """Mpesa Transaction from one company to another."""
    pass


def b2c():
    """Mpesa Transaction from company to client."""
    pass


def c2b():
    """Register URL for Validation/Confirmation and Simulate transaction."""
    pass


def transation_status():
    """Use this API to check the status of transaction."""
    pass


def account_balance():
    """Use this API for reversal transaction."""
    pass


def reversal():
    """Use this API for reversal transaction."""
    pass


def lipa_na_mpesa_online():
    """For Lipa Na M-Pesa online payment using STK Push."""
    pass
