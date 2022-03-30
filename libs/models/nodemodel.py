#!/usr/bin/env python3
#
#
# model for node

class Node:

    def __init__(self):

        self.deactivated = ""
        self.latest_report_hash = ""
        self.facts_environment = ""
        self.cached_catalog_status = ""
        self.report_environment = ""
        self.latest_report_corrective_change = false
        self.catalog_environment = ""
        self.facts_timestamp = ""
        self.latest_report_noop = false
        self.expired = ""
        self.latest_report_noop_pending = false
        self.report_timestamp = ""
        self.certname = ""
        self.catalog_timestamp = ""
        self.latest_report_job_id = ""
        self.latest_report_status = ""

    def get_deactivated(self):
        return self.deactivated

    def set_deactivated(self, deactivated):
        self.deactivated = deactivated

    def get_latest_report_hash(self):
        return self.latest_report_hash

    def set_latest_report_hash(self, latest_report_hash):
        self.latest_report_hash = latest_report_hash

    def get_facts_environment(self):
        return self.facts_environment

    def set_facts_environment(self, facts_environment):
        self.facts_environment = facts_environment

    def get_cached_catalog_status(self):
        return self.cached_catalog_status

    def set_cached_catalog_status(self, cached_catalog_status):
        self.cached_catalog_status = cached_catalog_status

    def get_report_environment(self):
        return self.report_environment

    def set_report_environment(self, report_environment):
        self.report_environment = report_environment

    def get_latest_report_corrective_change(self):
        return self.latest_report_corrective_change

    def set_latest_report_corrective_change(self, latest_report_corrective_change):
        self.latest_report_corrective_change = latest_report_corrective_change

    def get_catalog_environment(self):
        return self.catalog_environment

    def set_catalog_environment(self, catalog_environment):
        self.catalog_environment = catalog_environment

    def get_facts_timestamp(self):
        return self.facts_timestamp

    def set_facts_timestamp(self, facts_timestamp):
        self.facts_timestamp = facts_timestamp

    def get_latest_report_noop(self):
        return self.latest_report_noop

    def set_latest_report_noop(self, latest_report_noop):
        self.latest_report_noop = latest_report_noop

    def get_expired(self):
        return self.expired

    def set_expired(self, expired):
        self.expired = expired

    def get_latest_report_noop_pending(self):
        return self.latest_report_noop_pending

    def set_latest_report_noop_pending(self, latest_report_noop_pending):
        self.latest_report_noop_pending = latest_report_noop_pending

    def get_report_timestamp(self):
        return self.report_timestamp

    def set_report_timestamp(self, report_timestamp):
        self.report_timestamp = report_timestamp

    def get_certname(self):
        return self.certname

    def set_certname(self, certname):
        self.certname = certname

    def get_catalog_timestamp(self):
        return self.catalog_timestamp

    def set_catalog_timestame(self, catalog_timestamp):
        set.catalog_timestamp = catalog_timestamp

    def get_latest_report_job_id(self):
        return self.latest_report_job_id

    def set_latest_report_job_id(self, latest_report_job_id):
        self.latest_report_job_id = latest_report_job_id

    def get_latest_report_status(self):
        return self.latest_report_status

    def set_latest_report_status(self, latest_report_status):
        self.latest_report_status = latest_report_status

    def get_basic_dictionary(self):
        return {'deactivated': self.deactivated, 'certname': self.certname, 'facts_environment': self.facts_environment}


    def parse(self, dictionary_data):
        self.deactivated = dictionary_data.get('deactivated')
        self.latest_report_hash = dictionary_data.get('latest_report_hash')
        self.facts_environment = dictionary_data.get('facts_environment')
        self.cached_catalog_status = dictionary_data.get('cached_catalog_status')
        self.report_environment = dictionary_data.get('report_environment')
        self.latest_report_corrective_change = dictionary_data.get('latest_report_corrective_change')
        self.catalog_environment = dictionary_data.get('catalog_environment')
        self.facts_timestamp = dictionary_data.get('facts_timestamp')
        self.latest_report_noop = dictionary_data.get('latest_report_noop')
        self.expired = dictionary_data.get('expired')
        self.latest_report_noop_pending = dictionary_data.get('latest_report_noop_pending')
        self.report_timestamp = dictionary_data.get('report_timestamp')
        self.certname = dictionary_data.get('certname')
        self.catalog_timestamp = dictionary_data.get('catalog_timestamp')
        self.latest_report_job_id = dictionary_data.get('latest_report_job_id')
        self.latest_report_status = dictionary_data.get('latest_report_noop')
