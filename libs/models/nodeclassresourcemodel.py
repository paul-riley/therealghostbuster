#!/usr/bin/env python3
#
#
# model for resource

class Nodeclassresource:

    def __init__(self):

        self.tags = []
        self.file = ""
        self.title = ""
        self.line = 0
        self.resource = ""
        self.environment = "production"
        self.certname = ""
        self.parameters = {}
        self.exported = False

        def get_tags(self):
            return self.tags

        def set_tags(self, tags):
            self.tags = tags

        def get_file(self):
            return self.file

        def set_file(self, file):
            self.file = file

        def get_title(self):
            return self.title

        def set_title(self, title):
            self.title = title

        def get_line(self):
            return self.line

        def set_line(self, line):
            self.line = line

        def get_resource(self):
            return self.resource

        def set_resource(self, resource):
            self.resource = resource

        def get_environment(self):
            return self.environment

        def set_environment(self, environment):
            self.environment = environment

        def get_certname(self):
            return self.certname

        def set_certname(self, certname):
            self.certname = certname

        def get_parameters(self):
            return self.parameters

        def set_parameters(self, pareameters):
            self.parameters = parameters

        def get_exported(self):
            return self.exported

        def set_exported(self, exported):
            self.exported = exported

        def get_basic_dictionary(self):
            return {'environment': self.environment, 'title': self.title, 'certname': self.certname}

        def parse(self, dictionary_data):
            self.tags = dictionary_data.get('tags')
            self.file = dictionary_data.get('file')
            self.title = dictionary_data.get('title')
            self.line = dictionary_data.get('line')
            self.resource = dictionary_data.get('resource')
            self.environment = dictionary_data.get('environment')
            self.certname = dictionary_data.get('certname')
            self.parameters = dictionary_data.get('parameters')
            self.exported = dictionary_data.get('exported')
