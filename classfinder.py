#!/usr/bin/env python3

#########################
#
# view/run method for api
#
from libs.imports import *

#Add url and token
url = input("Please enter your puppet server url (ex: puppetserver.example.com): ")
token = input("Please enter your admin api token: ")
#unusedclass_bool = input(get_bool("Would you like to see the unused classes?"))

if (url and token):
    c = Connection()
    c.set_url('https://' + url + ':4433')
    c.set_token(token)

    used_class_list = []
    unused_class_list = []

    print("\n\nThese are the used classes in PE\n\n")
    grp_ref = Groupcontroller(c)
    grp_ref.load_group_list()

    for grp_obj in grp_ref.get_group_list():
        class_list = grp_obj.get_classes().keys()
        for item in class_list:
            used_class_list.append(item)
            print(item)

   #print("\n\nThese are all the known classes in PE\n\n")

   #class_ref = Puppetclass(c)
