#!/usr/bin/env python3

###############################
#
# Node controller

from ..imports import *

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
#This is a double check... Thanks Python
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

class Nodecontroller:

    def __init__(self, c = Connection()):
        self.puppetnode_obj_list = []
        self.connection = c

    def load_all_nodes(self):
        uri = '/pdb/query/v4/nodes'
        if self.connection.get_url() is not None:
          resp = requests.get(self.connection.get_url() + uri, verify=False, headers=self.connection.get_headers())
          if resp.status_code == 200 :
              for single_item in resp.json():
                  class_obj = Node()
                  class_obj.parse(single_item)
                  self.puppetnode_obj_list.append(class_obj)
          else:
              print('response code is not 200. connection:' + self.connection.get_url() )
        else:
            print('connection is None')

    def get_all_nodes(self):
        if self.puppetnode_obj_list is not None:
            return self.puppetnode_obj_list
        else:
            self.load_all_nodes()
            return self.puppetnode_obj_list
