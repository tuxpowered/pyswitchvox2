"""
Switchvox common methods

Ben DAVIS <vwjettadude@gmail_dot_com>

"""
import sys

try:
    import requests
    from requests.auth import HTTPDigestAuth
except Exception:
    sys.exit('Unable to import Requests module. Install with pip.')

try:
    import json
except ImportError:
    import simplejson as json


class Switchvox(object):
    """
    Class wrapper around switchvox API

    usage:
        switchvox = Switchvox()
        switchvox.username='100'
        switchvox.password='sup3r$eret'
        switchvox.hostname='pbx.localdomain.tld'

        switchvox.request('switchvox.users.phonebooks.getList',
                            {paramaters})

    """

    def __init__(self, version=None):
        self.user_name = None
        self.user_pass = None
        self.hostname = None
        self.url = None

    def _get_url(self):
        url = 'https://%s/json' % self.hostname
        return url

    def _request_form(self, method, parameters=None):
        if not parameters:
            parameters = {}
        parameters = dict(parameters)

        request = {"request": {
            "version": "17487",
            "method": method,
            "parameters": parameters}}
        return json.dumps(request)

    def request(self, method=None, paramaters=None, verify=True):
        """ executes switchvox api directly """

        json_request = self._request_form(method, paramaters)

        headers = {'Content-Type': 'text/json',
                   'Content-Length': str(len(json_request))}
        request = requests.post(self._get_url(), headers=headers,
                                auth=HTTPDigestAuth(self.user_name, self.user_pass),
                                verify=verify,
                                data=json_request)
        return request

    def get_errors(response):
        """
        Returns processed list of errors from switchvox response
        example output:
                expected = [{'code': 10011, 'message': 'Missing required parameter (dial_as_account_id)'}]

                expected = [{"code" : 10010, "message" : "Invalid extension (abc). Extensions may only contain digits or *."},
                            {"code" : 10010, "message" : "Invalid extension (def). Extensions may only contain digits or *."}
                            ]
        """
        ####
        # Check for no errors at all
        ####
        try:
            error = response['response']['errors']['error']
        except KeyError:
            return []

        ####
        # Test for single error situation.
        ####
        try:
            items = error.items()
        except AttributeError:
            # Multiple error situation.
            # 'error' is list object. Each 'err' is a single error dict.
            return [err for err in error]
        else:
            # 'error' is dict object: single error situation.
            return [error]
