__author__ = 'amahouix'

class ParsedConfig():
    def __init__(self):
        with open("config.xml","rb") as config_file:
            content = config_file.readlines()

        self.config = extract_args_from_config(content)



def extract_args_from_config(content):
    kwargs = dict()
    for line in content:
        if "name" in line and "value" in line:
            name = line.split('"')[1]
            value = line.split('"')[3]
            kwargs[name] = value

    return kwargs