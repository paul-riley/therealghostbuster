#!/usr/bin/env python3

###############################
#
# node Group controller
# I'm not a fan of camel_case... but PEP 8 says do it this way

from .imports import *
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
#This is a double check... Thanks Python
file_dir = os.path.dirname(__file__)
sys.path.append(file_dir)

class Groupcontroller:

    def __init__(self, c = Connection()):
        self.group_obj_list = []
        self.connection = c

    #loads data in to node_obj_list
    def load_group_list(self):
        uri = '/classifier-api/v1/groups'
        if self.connection.get_url() is not None:
          resp = requests.get(self.connection.get_url() + uri, verify=False, headers=self.connection.get_headers())

          if resp.status_code == 200 :
              # Apparently... the .json method creates lists that "look" like json
              # This does not encode the json into strings correclty. Which is crap.
              # because the method is called .json() why not call it .to_dictionary()?
              # if you need to turn it in parseable json: json.loads(data.json()) :(
              for single_item in resp.json():
                  group_obj = Group()
                  group_obj.parse(single_item)
                  self.group_obj_list.append(group_obj)

                  #this is that stupid 'fake' json
                  #return json.dumps(resp.json())
                  #print(resp.json())
          else:
              print('response code is not 200. connection:' + self.connection.get_url() )

    #returns group list of type Group Objects
    def get_group_list(self):
        if self.group_obj_list:
            return self.group_obj_list
        else :
            return None

    #returns a Node
    def create_group(self, name, description = None, parent_name = None, classes = None):
        #Per the api: https://puppet.com/docs/pe/2019.8/groups_endpoint.html#post_v1_groups
        #name, parent, classes are required, but the model will handle empty classes.
        self.get_groups()
        new_group_obj = Group()
        new_group_obj.set_name(name)
        parent_obj = Group()

        if parent_name is not None:
            foundParentBool = False
            #Let's make sure the parent node it exists
            for group_obj in self.group_obj_list:
                if group_obj.name == parent_name:
                    new_group_obj.set_parent(parent_name)
                    foundParentBool = True
            if foundParentBool is False:
                #Let's set the parent to the top level
                new_group_obj.set_parent('00000000-0000-4000-8000-000000000000')
        else:
            new_group_obj.set_parent('00000000-0000-4000-8000-000000000000')
        if description is not None:
            new_group_obj.set_description()
        return new_group_obj


    def add_group(self, noderef):
        # self.group_obj_list.append(noderef)
        uri = '/classifier-api/v1/groups'
        #serliaze into json
        jsondata = json.dumps(noderef.get_basic_group_dictionary())
        resp = requests.post(self.connection.get_url() + uri, verify=False, headers=self.connection.get_headers(), data=jsondata)

        if resp.status_code == 201:
            #reload the groups into the model
            self.get_groups()

        return json.dumps(resp.json())
    #
    # def add_fact_to_group(self, group_ref, fact, value):
    #     #add node to the groups
    #
    # def add_class_to_group(self, group_ref, class_name):
    #     #yup adding class to groups
