__author__ = 'amahouix'

import ExeptionsOfLegends


class PageAnalyzer():

    def __init__(self, config):
        self.champ_number = None

        if "champ_number" in config:
            self.champ_number = config["champ_number"]


    def extract_champ_list(self, champions_page):
        if self.champ_number is None:
            raise ExeptionsOfLegends.ConfigException("champion number")
        names = list()
        count = 0
        while count < int(self.champ_number):
            for line in champions_page.split("\n"):
                if '<li style="display:inline-block;width:10em;"><div style="text-align:center;">' \
                   '<span style="float:left; height:22px; width:22px;"><a href="/wiki/' in line:
                    name = line.split('<a href="/wiki/')[1]
                    name = name.split('"')[0]
                    names.append(name)
                    count += 1
        return names

    def __replace_space_char(self, text):
        return text.replace()