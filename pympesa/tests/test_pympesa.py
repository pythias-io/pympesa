import os
import datetime
import unittest
from pympesa import pympesa


class PympesaTests(unittest.TestCase):

    def setUp(self):
        access_token = pympesa.oauth_generate_token(
            os.getenv("TEST_MPESA_CONSUMER_KEY"),
            os.getenv("TEST_MPESA_CONSUMER_SECRET")).json().get("access_token")
        print "token: " + access_token
        self.client = pympesa.Pympesa(access_token)
        self.short_code_1 = os.getenv("TEST_MPESA_SHORT_CODE_1")
        self.initiator_name_sc_1 = os.getenv("TEST_MPESA_INITIATOR_NAME_SC_1")
        self.security_credential_sc_1 = \
            os.getenv("TEST_MPESA_SECURITY_CREDENTIAL_SC_1")
        self.short_code_2 = os.getenv("TEST_MPESA_SHORT_CODE_2")
        self.test_msisdn = os.getenv("TEST_MPESA_MSISDN")
        self.online_short_code = os.getenv("TEST_MPESA_ONLINE_SHORT_CODE")
        self.online_pass_key = os.getenv("TEST_MPESA_ONLINE_PASS_KEY")
        self.initiator_security_credential = \
            os.getenv("TEST_MPESA_INITIATOR_SECURITY_CREDENTIAL")
        self.validation_url = os.getenv("TEST_MPESA_VALIDATION_URL")
        self.confirmation_url = os.getenv("TEST_MPESA_CONFIRMATION_URL")

    def test_c2b_register_url_cancelled(self):
        resp = self.client.c2b_register_url(
            ValidationURL=self.validation_url,
            ConfirmationURL=self.confirmation_url,
            ResponseType="Cancelled",
            ShortCode=self.short_code_1
        )
        self.assertEqual(resp.status_code, 200)

    def test_c2b_register_url_completed(self):
        resp = self.client.c2b_register_url(
            ValidationURL=self.validation_url,
            ConfirmationURL=self.confirmation_url,
            ResponseType="Completed",
            ShortCode=self.short_code_1
        )
        self.assertEqual(resp.status_code, 200)

    def test_c2b_simulate_transaction(self):
        resp = self.client.c2b_simulate_transaction(
            CommandID="CustomerPayBillOnline",
            Amount=50,
            Msisdn=self.test_msisdn,
            BillRefNumber="pympesa-test",
            ShortCode=self.short_code_1
        )
        self.assertEqual(resp.status_code, 200)
        self.assertIn("ResponseDescription", resp.json())

    def test_b2c_payment_request(self):
        resp = self.client.b2c_payment_request(
            InitiatorName=self.initiator_name_sc_1,
            SecurityCredential=self.security_credential_sc_1,
            CommandID="BusinessPayment",
            Amount=50,
            PartyA=self.short_code_1,
            PartyB=self.test_msisdn,
            Remarks="Testing B2C",
            QueueTimeOutURL=self.validation_url,
            ResultURL=self.validation_url,
            Occassion="Testcases"
        )
        self.assertEqual(resp.status_code, 200)

    def test_lipa_na_mpesa_online_payment(self):
        self.skipTest("Not Working")
        resp = self.client.lipa_na_mpesa_online_payment(
                BusinessShortCode=self.online_short_code,
                Password=self.online_pass_key,
                Timestamp=pympesa.generate_timestamp(),
                TransactionType="CustomerPayBillOnline",
                Amount=100,
                PartyA=self.test_msisdn,
                PartyB=self.short_code_1,
                PhoneNumber=self.test_msisdn,
                CallBackURL=self.validation_url,
                AccountReference="pympesa-dev-test",
                TransactionDesc="pympesa-dev-test"
                )
        self.assertEqual(resp.status_code, 200)
        result = resp.json()
        self.assertIn("ResponseCode", result)

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
