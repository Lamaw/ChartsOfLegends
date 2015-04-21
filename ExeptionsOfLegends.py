__author__ = 'amahouix'


class ConfigException(Exception):
    def __init__(self, reason):
        self.args = reason,
        self.reason = reason

    def __str__(self):
        return '<config for %s is missing>' % self.reason