#!/usr/bin/python

import os

URL = {}

URL["sandbox"] = {}
URL["sandbox"]["v1"] = {}
URL["sandbox"]["v1"]["reversal_request"] = "https://sandbox.safaricom.co.ke/mpesa/reversal/v1/request"
URL["sandbox"]["v1"]["b2c_payment_request"] = "https://sandbox.safaricom.co.ke/mpesa/b2c/v1/paymentrequest"
URL["sandbox"]["v1"]["b2b_payment_request"] = "https://sandbox.safaricom.co.ke/mpesa/b2b/v1/paymentrequest"
URL["sandbox"]["v1"]["c2b_register_url"] = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/registerurl"
URL["sandbox"]["v1"]["c2b_simulate_transaction"] = "https://sandbox.safaricom.co.ke/mpesa/c2b/v1/simulate"
URL["sandbox"]["v1"]["transation_status_request"] = "https://sandbox.safaricom.co.ke/mpesa/transactionstatus/v1/query"
URL["sandbox"]["v1"]["account_balance_request"] = "https://sandbox.safaricom.co.ke/mpesa/accountbalance/v1/query"
URL["sandbox"]["v1"]["lipa_na_mpesa_online_query"] = "https://sandbox.safaricom.co.ke/mpesa/stkpushquery/v1/query"
URL["sandbox"]["v1"]["lipa_na_mpesa_online_payment"] = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
URL["sandbox"]["v1"]["oauth_generate_token"] = "https://sandbox.safaricom.co.ke/oauth/v1/generate"

URL["production"] = {}
URL["production"]["v1"] = {}
URL["production"]["v1"]["reversal_request"] = ""
URL["production"]["v1"]["b2c_payment_request"] = ""
URL["production"]["v1"]["b2b_payment_request"] = ""
URL["production"]["v1"]["c2b_simulate_transaction"] = ""
URL["production"]["v1"]["transation_status_request"] = ""
URL["production"]["v1"]["account_balance_request"] = ""
URL["production"]["v1"]["lipa_na_mpesa_online_query"] = ""
URL["production"]["v1"]["lipa_na_mpesa_online_payment"] = os.getenv("PROD_MPESA_URL_LIPA")
URL["production"]["v1"]["oauth_generate_token"] = os.getenv("PROD_MPESA_URL_OAUTH")
