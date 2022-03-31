#!/usr/bin/env python3

#########################
#
# view/run method for api
#
from libs.imports import *

#Add url and token
url = input("\n\nPlease enter your puppet server url (ex: puppetserver.example.com): ")
token = input("Please enter your admin api token: ")
#unusedclass_bool = input(get_bool("Would you like to see the unused classes?"))

if (url and token):
    pe_conn = Connection()
    pe_conn.set_url('https://' + url + ':4433')
    pe_conn.set_token(token)

    #put some logic in for different PDBs from PE. This will likely happen.
    pdb_conn = Connection()
    pdb_conn.set_url('https://' + url + ':8081')
    pdb_conn.set_token(token)

    used_class_list = []
    unused_class_list = []

    print("\n\nThese are the group classes in PE,\n\n")
    grp_ref = Groupcontroller(pe_conn)
    grp_ref.load_group_list()

    for grp_obj in grp_ref.get_group_list():
        class_list = grp_obj.get_classes().keys()
        for item in class_list:
            unused_class_list.append(item)
            print(grp_obj.get_name() + ',' + item)

    print("\n\nThese are all the known classes in PE,\n\n")
    class_ref = Puppetclasscontroller(pe_conn)
    class_ref.load_api_classes()

    for pe_class in class_ref.get_api_classes():
        print(pe_class.get_name() + ',' + pe_class.get_environment() + ',' + pe_class.get_source() )

    print("\n\n")

    #get list of nodes from puppetdb -> make a node model
    node_ref = Nodecontroller(pdb_conn)
    node_ref.load_all_nodes()
    node_list = node_ref.get_all_nodes()

    for node_obj in node_list:
        class_obj = Nodeclassresourcecontroller(pdb_conn)
        class_obj.load_all_classes(node_obj)
        node_class_list = class_obj.get_all_classes()

        print ("\n\nNode: " + node_obj.get_certname())
        for node_class_obj in node_class_list:
            print (node_class_obj.get_title())

    #if the class is applied, mark it off as used pop it off into used_class_array
