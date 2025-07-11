#!/usr/bin/env python3

#########################
#
# view/run method for api
#
from libs.imports import *

url_default = 'localhost'
filename_default = 'output.csv'

#Add url and token
url = input("\n\nPlease enter your puppet server (ex: puppetserver.example.com, default: 'localhost'): ") or url_default
pdburl = input("\n\n[Optional] Please enter your pdb server (ex: pup-compiler.example.com): ")
token = input("\n\nPlease enter your admin api token: ")
filename = input("\n\nPlease enter the full name of the CSV file to store the output (default: 'output.csv'): ") or filename_default



#make sure that we setup the url and token
if (url and filename):
    pe_conn = Connection()
    pe_conn.set_url('https://' + url + ':4433')
    pe_conn.set_token(token)

    #put some logic in for different PDBs from PE. This will likely happen.
    pdb_conn = Connection()
    if pdburl:
        pdb_conn.set_url('https://' + pdburl + ':8081')
    else:
        pdb_conn.set_url('https://' + url + ':8081')

    if (token):
        pdb_conn.set_token(token)
    else:
      print("\n\nPlease use an appropriate token. Thank you!\n\n")
      exit(1)


    f = open(filename, 'a')

    #list of class objects for holding used and ununsed class lists.
    used_class_obj_list = []
    unused_class_obj_list = []

    #get the classes that are attached to groups.
    print("\n\nThese are the group classes in PE,\n")
    f.write("These are group classes in PE,\n")
    grp_ref = Groupcontroller(pe_conn)
    grp_ref.load_group_list()

    #Loop through group objects and spit out the classes
    for grp_obj in grp_ref.get_group_list():
        class_list = grp_obj.get_classes().keys()
        for item in class_list:
            print(grp_obj.get_name() + ',' + item)
            f.write(grp_obj.get_name() + ',' + item + "\n")

    #get all the classes from PE.
    print("\n\nThese are all the known classes in PE,\n")
    f.write("These are all the known classes in PE,\n")
    class_ref = Puppetclasscontroller(pe_conn)
    class_ref.load_api_classes()

    for pe_class in class_ref.get_api_classes():
        unused_class_obj_list.append(pe_class)
        if re.search('^pe_', pe_class.get_name()) and not re.search('^puppet_enterprise', pe_class.get_name()):
            print(pe_class.get_name())
            f.write(pe_class.get_name() + "\n")

    #get list of nodes from puppetdb. pagination is not being used. i suspect
    #  that will need to be turned on to not slow down puppetdb.
    node_ref = Nodecontroller(pdb_conn)
    node_ref.load_all_nodes()
    node_list = node_ref.get_all_nodes()

    #this goes through our node_list from above and gets the classes for that nodes
    #  this going to need be threaded on a per node basis because it does an api
    #  call for each node to get the list.
    for single_node_obj in node_list:
        node_resource_obj = Nodeclassresourcecontroller(pdb_conn)
        node_resource_obj.load_all_classes(single_node_obj)

        #This is going to loop through the list of clases w/ a node and
        # move them from the unused array to the used class array.
        for node_class_obj in node_resource_obj.get_all_classes():
            counter = 0
            for unused_class in unused_class_obj_list:
                if ( (unused_class.get_name().lower().strip() == node_class_obj.get_title().lower().strip()) and \
                (unused_class.get_environment() == node_class_obj.get_environment()) ):
                    unused_class_obj_list.pop(counter)
                    used_class_obj_list.append(unused_class)
                counter+=1

    #I should probably pop stuff out of the array to clear the ram... meh.

    #Used classes.
    used_class_string_array = []
    print("\n\nThese are the used classes:\n")
    f.write("These are the used classes:\n")
    for class_obj in used_class_obj_list:
        if not re.search('^pe_', class_obj.get_name()) and not re.search('^puppet_enterprise', class_obj.get_name()):
            used_class_string_array.append(class_obj.get_environment() + ',' + class_obj.get_name())
    used_class_string_array.sort()
    for str_item in used_class_string_array:
        print(str_item)
        f.write(str_item + "\n")

    #Unused Items
    unused_class_string_array = []
    print("\n\nThese are the unused classes:\n")
    f.write("These are the unused classes:\n")
    for class_obj in unused_class_obj_list:
        if not re.search('^pe_', class_obj.get_name()) and not re.search('^puppet_enterprise', class_obj.get_name()):
            unused_class_string_array.append(class_obj.get_environment() + ',' + class_obj.get_name())
    unused_class_string_array.sort()
    for str_item in unused_class_string_array:
        print(str_item)
        f.write(str_item + "\n")

    print("\n\n")
    f.write("\n\n")
    f.close()
    #Fin
