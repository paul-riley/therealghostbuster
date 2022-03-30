#!/usr/bin/env python3
#
#
# model for node

class Group:

    def __init__(self):

        self.parent = ""
        self.environment_trumps = False
        self.name = ""
        self.rule = []
        self.variables = {}
        self.id = ""
        self.environment = ""
        self.last_edited = ""
        self.serial_number = int()
        self.classes = {}
        self.config_data = {}
        self.description = ""

    def get_parent(self):
        return self.parent

    def set_parent(self, parent):
        self.parent = parent

    def get_environment_trumps(self):
        return self.environment_trumps

    def set_environment_trumps(self, trump):
        self.environment_trumps = trump

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_rule(self):
        return self.rule

    def set_rule(self, rule):
        self.rule = rule

    def get_variables(self):
        return self.variables

    def set_variables(self, variables):
        self.variables = variables

    def get_id(self):
        return self.id

    def set_id(self, id):
        self.id = id

    def get_environment(self):
        return self.environment

    def set_environment(self, environment):
        self.environment = environment

    def get_last_edited(self):
        return self.last_edited

    def set_last_edited(self, last_edited):
        self.last_edited = last_edited

    def get_serial_number(self):
        return self.serial_number

    def set_serial_number(self, serial_number):
        self.serial_number = serial_number

    def get_classes(self):
        return self.classes

    def set_classes(self, classes):
        self.classes = classes

    def get_config_data(self):
        return self.config_data

    def set_config_data(self, config_data):
        self.config_data = config_data

    def get_description(self):
        return self.config_data

    def set_description(self, desc_data):
        self.config_data = desc_data

    def get_basic_group_dictionary(self):
        return {'parent': self.parent, 'name': self.name, 'classes': self.classes}

    def parse(self, dictionary_data):
        self.parent = dictionary_data.get('parent')
        self.environment_trumps = dictionary_data.get('environment_trumps')
        self.name = dictionary_data.get('name')
        self.rule = dictionary_data.get('rule')
        self.variables = dictionary_data.get('variables')
        self.id = dictionary_data.get('id')
        self.environment = dictionary_data.get('environment')
        self.last_edited = dictionary_data.get('last_edited')
        self.serial_number = dictionary_data.get('serial_number')
        self.classes = dictionary_data.get('classes')
        self.config_data = dictionary_data.get('config_data')
        if dictionary_data.get('description') is not None:
            self.description = dictionary_data.get('description')
