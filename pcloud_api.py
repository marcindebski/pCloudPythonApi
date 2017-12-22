""" API that provides access to pCloud storage """
import json
import requests


ENDPOINT_API = 'https://api.pcloud.com/'


class AuthenticationError(Exception):
    """ Authentication Error """
    pass


class pCloudApi:
    """ pCloud API """
    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.auth = None
        self.session = requests.Session()

    def login(self, method='GET'):
        """ Login to pCloud """
        method_api = 'userinfo'
        params = dict(
            getauth=1,
            logout=1,
            username=self.username,
            password=self.password
        )
        request = self._prepare_request(method_api, params, method)
        response = self._send_request(request)
        if response['result']:
            raise AuthenticationError('Cannot authenticate')
        else:
            self.auth = response['auth']
            print('Success: You have logged in.')

    def logout(self, method='GET'):
        """ Logout from the pCloud """
        method_api = 'logout'
        params = dict(
            auth=self.auth
        )
        request = self._prepare_request(method_api, params, method)
        response = self._send_request(request)
        if response['auth_deleted']:
            print('Success: You have logged out.')
        else:
            print('Error: Token was not invalidated.')

    def create_folder(self, path, method='GET'):
        """ Create folder """
        method_api = 'createfolder'
        params = dict(
            auth=self.auth,
            path=path
        )
        request = self._prepare_request(method_api, params, method)
        response = self._send_request(request)
        if response['result']:
            print('Error: %s' % response['error'])
        else:
            print('Success: %s was created.' % path)

    def _prepare_request(self, method_api, params, method):
        """ Prepare request to send """
        url = ENDPOINT_API + method_api
        prepped = requests.Request(method, url, params=params).prepare()
        return prepped

    def _send_request(self, request):
        """ Send request """
        data = {'result': 1}
        response = self.session.send(request)
        if response.status_code == 200:
            data = json.loads(response.text)
        return data
