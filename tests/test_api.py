""" Tests of pCloud API """
import unittest
from context import pCloudApi
from context import AuthenticationError


class TestPCloudApi(unittest.TestCase):
    """ Tests of pCloud API """

    def test_invalid_username_password(self):
        """ Test if cannot log in using invalid credentials """
        pcloud_invalid_client = pCloudApi('itdoesnotexistforsure@blah.pl', 'password')
        with self.assertRaises(AuthenticationError) as ctx:
            pcloud_invalid_client.login()
        self.assertTrue('Cannot authenticate' in str(ctx.exception))


if __name__ == '__main__':
    unittest.main()
