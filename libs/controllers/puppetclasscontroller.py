#!/usr/bin/env python3

###############################
#
# Puppetclass controller

from ..imports import *

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
#This is a double check... Thanks Python
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

class Puppetclasscontroller:

    def __init__(self, c = Connection()):
        self.puppetclass_obj_list = []
        self.connection = c

    def get_all_classes(self, connection):
        uri = '/classifier-api/v1/groups'
        if connection.get_url() is not None:
          resp = requests.get(self.connection.get_url() + uri, verify=False, headers=self.connection.get_headers())

          if resp.status_code == 200 :
