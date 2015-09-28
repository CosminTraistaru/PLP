import re
import os.path


class ConfReader(object):
    """
    Assumes file looks like this:
    [section]
    key : value
    username = dhellmann
    """

    configuration = {}

    def read(self, file):
        file_location = os.path.join(os.getcwd(), file)
        if not os.path.isfile(file_location):
            raise Exception('File does not exist')

        section = ''
        with open(file_location, 'r') as f:
            for line in f:
                if line.startswith('['):
                    m = re.search('[0-9a-zA-Z]+', line)
                    section = m.group(0)
                    self.configuration[section] = {}
                    continue
                values = line.strip().split(' ')
                if len(values) == 3:
                    self.configuration[section][values[0]] = values[2]

    def all(self):
        return self.configuration

    def sections(self):
        return self.configuration.keys()

    def options(self, section):
        return self.configuration[section]

    def value(self, section, option):
        return self.configuration[section][option]

    def is_empty(self):
        return self.configuration == {}

