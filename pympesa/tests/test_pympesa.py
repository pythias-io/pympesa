import unittest, os, datetime
from pympesa import pympesa

CONSUMER_KEY = os.getenv("MPESA_CONSUMER_KEY_DEV")
CONSUMER_SECRET = os.getenv("MPESA_CONSUMER_SECRET_DEV")

class PympesaTests(unittest.TestCase):

    def setUp(self):
        #access_token = self.generate_token()
        access_token = pympesa.oauth_generate_token(
                CONSUMER_KEY, CONSUMER_SECRET).json().get("access_token")
        print "token: " + access_token
        self.client = pympesa.Pympesa(access_token)
        self.test_msisdn = "254708374149"
        self.test_short_code_1 = "603082"
        self.test_short_code_2 = "600000"

    def test_c2b_register_url(self):
        ValidationURL = "https://4ffe7395.ngrok.io/safaricom"
        ConfirmationURL = "https://4ffe7395.ngrok.io/safaricom"
        ResponseType = "Cancelled"
        ShortCode = self.test_short_code_1
        resp = self.client.c2b_register_url(
                ValidationURL=ValidationURL, 
                ConfirmationURL=ConfirmationURL,
                ResponseType=ResponseType,
                ShortCode=ShortCode
                )
        result = resp.json()
        self.assertEqual(resp.status_code, 200)
        ResponseType = "Completed"
        resp = self.client.c2b_register_url(
                ValidationURL=ValidationURL, 
                ConfirmationURL=ConfirmationURL,
                ResponseType=ResponseType,
                ShortCode=ShortCode
                )
        result = resp.json()
        self.assertEqual(resp.status_code, 200)


    def test_c2b_simulate_transaction(self):
        resp = self.client.c2b_simulate_transaction(
                CommandID="CustomerPayBillOnline",
                Amount=50,
                Msisdn=self.test_msisdn,
                BillRefNumber="pympesa-test",
                ShortCode=self.test_short_code_1
                )
        self.assertEqual(resp.status_code, 200)
        result = resp.json()
        self.assertIn("ResponseDescription", result)

    def test_generate_timestamp(self):
        timestamp = pympesa.generate_timestamp()
        print timestamp
        self.assertIsInstance(timestamp, str)
        self.assertTrue(timestamp.isdigit())
        self.assertEqual(int(timestamp[:4]), datetime.datetime.now().year)
        self.assertEqual(int(timestamp[4:6]), datetime.datetime.now().month)
        self.assertEqual(int(timestamp[6:8]), datetime.datetime.now().day)




if __name__ == "__main__":
    unittest.main()
