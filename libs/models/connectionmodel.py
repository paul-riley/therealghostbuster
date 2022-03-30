#!/usr/bin/env python3
#
#
# model for Puppetclass

class Connection:

    def __init__(self):

        self.__url = ""
        self.__token = ""
        self.__headers = {}

    def get_url(self):
        return self.__url

    def set_url(self, url):
        self.__url = url

    def get_token(self):
        return self.__token

    def set_token(self, token):
        self.__token = token
        self.__headers = {'Accept': '*/*',
                        'Accept-Encoding': 'gzip,deflate,br',
                        'Connection': 'keep-alive',
                        'X-Authentication': token,
                        'Content-Type': 'application/json' }

    def get_headers(self):
        return self.__headers

    def set_headers(self, headers):
        self.__headers = headers

    #This is technically a controller method meh.
    def get_token_status(self):
        uri = '/rbac-api/v2/auth/token/authenticate'
        payload = json.dumps({'token':self.__token, 'update_last_activity?':False })
        resp = requests.post(self.__connection + uri, verify=False, headers=self.__headers, data=payload)
        #if resp.status_code == 200 :
        return json.dumps(resp.json())

    def get_basic_dictionary(self):
        return {'url': self.__url, 'token': self.__token, 'headers': self.__headers}
