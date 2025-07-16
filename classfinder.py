#!/usr/bin/env python3

#########################
#
# view/run method for api
#
from libs.imports import *

url_default = 'localhost'
filename_default = 'output.csv'

#Add url and token
url = input("\n\n[Optional] Please enter your puppet server (ex: puppetserver.example.com, default: 'localhost'): ") or url_default
pdburl = input("\n\n[Optional] Please enter your pdb server (ex: pup-compiler.example.com): ")
token = input("\n\nPlease enter your admin api token: ")
filename = input("\n\n[Optional] Please enter the full name of the CSV file to store the output (default: 'output.csv'): ") or filename_default



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
      print("\n\n[ERROR] Please use an appropriate token. Thank you!")
      exit(1)


    f = open(filename, 'a')

    #list of class objects for holding used and unused class lists.
    used_class_obj_list = []
    unused_class_obj_list = []
    #list of string names for holding used and unused classes
    used_class_string_array = []
    unused_class_string_array = []
    #cleaned up string names of unused classes
    unused_class_string_array_clean = []

    #get the classes that are attached to groups.
    print("\n\nThese are the group classes in the PE classifier,\n")
    grp_ref = Groupcontroller(pe_conn)
    grp_ref.load_group_list()

    #Loop through group objects and spit out the classes
    for grp_obj in grp_ref.get_group_list():
        class_list = grp_obj.get_classes().keys()
        for item in class_list:
            print('group class: ' + grp_obj.get_name() + ',' + item)
            f.write('group class,' + grp_obj.get_name() + ',' + item + "\n")

    #get all the classes from PE.
    print("\n\nThese are all the known classes in PE,\n")
    class_ref = Puppetclasscontroller(pe_conn)
    class_ref.load_api_classes()

    for pe_class in class_ref.get_api_classes():
        unused_class_obj_list.append(pe_class)
        if re.search('^pe_', pe_class.get_name()) and not re.search('^puppet_enterprise', pe_class.get_name()):
            print('known class: ' + pe_class.get_name())
            f.write('known class,' + pe_class.get_name() + "\n")

    #get list of nodes from puppetdb. pagination is not being used. i suspect
    #  that will need to be turned on to not slow down puppetdb.
    node_ref = Nodecontroller(pdb_conn)
    node_ref.load_all_nodes()
    node_list = node_ref.get_all_nodes()

    #this goes through our node_list from above and gets the classes for that nodes
    #  this going to need be threaded on a per node basis because it does an api
    #  call for each node to get the list.
    print("\n\nProcessing nodes\n\n")

    for single_node_obj in node_list:
        node_resource_obj = Nodeclassresourcecontroller(pdb_conn)
        node_resource_obj.load_all_classes(single_node_obj)

        print('Processing classes in node: ' + single_node_obj.get_certname())

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

    # This should be reworked to be cleaner. I'm creating another array.

    for class_obj in used_class_obj_list:
        if not re.search('^pe_', class_obj.get_name()) and not re.search('^puppet_enterprise', class_obj.get_name()):
            used_class_string_array.append('used class,' + class_obj.get_environment() + ',' + class_obj.get_name())

    used_class_string_array.sort()
    for str_item in used_class_string_array:
        f.write(str_item + "\n")


    for class_obj in unused_class_obj_list:
        if not re.search('^pe_', class_obj.get_name()) and not re.search('^puppet_enterprise', class_obj.get_name()):
            unused_class_string_array.append('unused class,' + class_obj.get_environment() + ',' + class_obj.get_name())
    unused_class_string_array.sort()
    for str_item in unused_class_string_array:
        # print(str_item)
        f.write(str_item + "\n")

    # #clean sort for used and unused classes
    # for used_class_string in used_class_string_array:
    #     for unused_class_string in unused_class_string_array:
            # need to do a search for the first pattern of used strings against the unused
            # look into quick sort
            # if the pattern matches, add it to the clean array
            #if re.search('^')

    #remove duplicates from used_clean_array, write.


    print("\n\n")
    f.write("\n")
    f.close()
    #Fin
