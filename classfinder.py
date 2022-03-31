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

#make sure that we setup the url and token
if (url and token):
    pe_conn = Connection()
    pe_conn.set_url('https://' + url + ':4433')
    pe_conn.set_token(token)

    #put some logic in for different PDBs from PE. This will likely happen.
    pdb_conn = Connection()
    pdb_conn.set_url('https://' + url + ':8081')
    pdb_conn.set_token(token)

    #list of strings for holding used and ununsed class lists.
    used_class_name_list = []
    unused_class_name_list = []

    #get the classes that are attached to groups.
    print("\n\nThese are the group classes in PE,\n")
    grp_ref = Groupcontroller(pe_conn)
    grp_ref.load_group_list()

    #Loop through group objects and spit out the classes
    for grp_obj in grp_ref.get_group_list():
        class_list = grp_obj.get_classes().keys()
        for item in class_list:
            #unused_class_list.append(item)
            print(grp_obj.get_name() + ',' + item)

    #get all the classes from PE.
    print("\n\nThese are all the known classes in PE,\n")
    class_ref = Puppetclasscontroller(pe_conn)
    class_ref.load_api_classes()

    for pe_class in class_ref.get_api_classes():
        unused_class_name_list.append(pe_class.get_name())
        if re.search('^pe_', pe_class.get_name()) and not re.search('^puppet_enterprise', pe_class.get_name()):
            print(pe_class.get_name())

    #get list of nodes from puppetdb. pagination is not being used. i suspect
    #  that will need to be turned on to not slow down puppetdb.
    node_ref = Nodecontroller(pdb_conn)
    node_ref.load_all_nodes()
    node_list = node_ref.get_all_nodes()

    #this goes through our node_list from above and gets the classes for that nodes
    #  this going to need be thread on a per node basis because it does an api
    #  call for each node to get the list.
    for node_obj in node_list:
        class_obj = Nodeclassresourcecontroller(pdb_conn)
        class_obj.load_all_classes(node_obj)

        #This is going to loop through the list of clases w/ a node and
        # move them from the unused array to the used class array.
        #print ("\n\nNode: " + node_obj.get_certname())
        for node_class_obj in class_obj.get_all_classes():
            counter = 0
            for single_class in unused_class_name_list:
                #print("Comparing " + unused_class_obj.get_name().lower() + " to " + node_class_obj.get_title().lower() )
                if single_class.lower().strip() == node_class_obj.get_title().lower().strip():
                    unused_class_name_list.pop(counter)
                    used_class_name_list.append(single_class)
                counter+=1

            #print (node_class_obj.get_title())

    print("\n\nThese are the used classes:\n")
    for item in used_class_name_list:
        if not re.search('^pe_', item) and not re.search('^puppet_enterprise', item):
            print(item)

    print("\n\nThese are the unused classes:\n")
    for item in unused_class_name_list:
        if not re.search('^pe_', item) and not re.search('^puppet_enterprise', item):
            print(item)

    print("\n\n")
    #Fin
