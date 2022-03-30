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

    def load_api_classes(self):
        uri = '/classifier-api/v1/classes'
        if self.connection.get_url() is not None:
          resp = requests.get(self.connection.get_url() + uri, verify=False, headers=self.connection.get_headers())
          if resp.status_code == 200 :
              for single_item in resp.json():
                  class_obj = Puppetclass()
                  class_obj.parse(single_item)
                  class_obj.set_source('api')
                  self.puppetclass_obj_list.append(class_obj)
          else:
              print('response code is not 200. connection:' + self.connection.get_url() )
        else:
            print('connection is None')

    def get_api_classes(self):
        return self.puppetclass_obj_list

    def load_code_classes(self):
        #There is nothing to see here
        print('This is going to take some work')
