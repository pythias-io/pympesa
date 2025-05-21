import unittest
import base64 # Import base64 for completeness, though encode_password should handle it
from pympesa import encode_password

class TestEncoding(unittest.TestCase):

    def test_encode_password(self):
        """Test that encode_password correctly encodes the password string."""
        shortcode = "testshortcode"
        passkey = "testpasskey"
        timestamp = "20231027101010"
        
        # Expected output generated from:
        # import base64
        # password_str = "testshortcodetestpasskey20231027101010"
        # password_bytes = password_str.encode('utf-8')
        # encoded_bytes = base64.b64encode(password_bytes)
        # encoded_string = encoded_bytes.decode('utf-8')
        # print(encoded_string) # dGVzdHNob3J0Y29kZXRlc3RwYXNza2V5MjAyMzEwMjcxMDEwMTA=
        expected_encoded_password = "dGVzdHNob3J0Y29kZXRlc3RwYXNza2V5MjAyMzEwMjcxMDEwMTA="
        
        result = encode_password(shortcode, passkey, timestamp)
        self.assertEqual(result, expected_encoded_password)

if __name__ == '__main__':
    unittest.main()
