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

    def set_parent(self, parent):
        self.parent = parent

    def set_environment_trumps(self, trump):
        self.environment_trumps = trump

    def set_name(self, name):
        self.name = name

    def set_rule(self, rule):
        self.rule = rule

    def set_variables(self, variables):
        self.variables = variables

    def set_id(self, id):
        self.id = id

    def set_environment(self, environment):
        self.environment = environment

    def set_last_edited(self, last_edited):
        self.last_edited = last_edited

    def set_serial_number(self, serial_number):
        self.serial_number = serial_number

    def set_classes(self, classes):
        self.classes = classes

    def set_config_data(self, config_data):
        self.config_data = config_data

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
