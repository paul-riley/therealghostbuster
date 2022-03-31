#!/usr/bin/env python3

###############################
#
# Puppetclass controller

from ..imports import *

requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
#This is a double check... Thanks Python
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

class Nodeclassresourcecontroller:

    def __init__(self, c = Connection()):
        self.nodeclass_obj_list = []
        self.connection = c

    def load_all_classes(self, node_obj = Node()):
        uri = "/pdb/query/v4/nodes/" + node_obj.get_certname() + "/resources/Class"
        #print("nodeclassresourcecontroller The uri is: " + uri)
        if self.connection.get_url() is not None:
          resp = requests.get(self.connection.get_url() + uri, verify=False, headers=self.connection.get_headers())
          if resp.status_code == 200 :
              for single_item in resp.json():
                  class_obj = Nodeclassresource()
                  class_obj.parse(single_item)
                  #Apparently Settings is class name
                  if class_obj.get_title() != 'Settings':
                      if class_obj.get_title() != 'main':
                          self.nodeclass_obj_list.append(class_obj)
          else:
              print('nodeclassresourcecontroller response code is not 200. connection:' + self.connection.get_url() )
        else:
            print('connection is None')

    def get_all_classes(self):
        if self.nodeclass_obj_list is not None:
            return self.nodeclass_obj_list
        else:
            return None
