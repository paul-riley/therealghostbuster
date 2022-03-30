#!/usr/bin/env python3
#
#
# model for Puppetclass

class Puppetclass:

    def __init__(self):

        self.name = ""
        self.environment = ""
        self.source = ""
        self.parameters = {}

    def get_environment(self):
        return self.environment

    def set_environment(self, environment):
        self.environment = environment

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_source(self):
        return self.source

    def set_source(self, source):
        self.source = source

    def get_parameters(self):
        return self.parameters

    def set_parameters(self, parameters):
        self.parameters = parameters

    def get_basic_class_dictionary(self):
        return {'name': self.name, 'environment': self.environment, 'parameters': self.classes}

    def parse(self, dictionary_data):
        self.name = dictionary_data.get('name')
        self.environment = dictionary_data.get('environment')
        if dictionary_data.get('parameters') is not None:
            self.parameters = dictionary_data.get('parameters')
