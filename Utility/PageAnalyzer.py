__author__ = 'amahouix'

import ExeptionsOfLegends
from Model.Champion import Champion


class PageAnalyzer():

    def __init__(self, config):
        self.champ_number = None
        if "champ_number" in config:
            self.champ_number = config["champ_number"]


    def extract_champ_stat(self, champion_page, champion_name):
        champion = Champion(champion_name)
        html_stat = self.__capture_stat_table(champion_page)


        champion.health = self.__read_stat("Health", html_stat)
        champion.ad = self.__read_stat("Attack_damage", html_stat)
        champion.health_reg = self.__read_stat("Health_regeneration", html_stat)
        champion.att_speed = self.__read_stat("Attack_speed", html_stat)
        champion.mana = self.__read_stat("Mana", html_stat)
        champion.armor = self.__read_stat("Armor", html_stat)
        champion.mana_reg = self.__read_stat("Mana_regeneration", html_stat)
        champion.mag_res = self.__read_stat("Magic_resistance", html_stat)
        champion.range = self.__read_stat("Range", html_stat)
        champion.mov_speed = self.__read_stat("Movement_speed", html_stat)

        if champion.mana is None:
            champion.energy = self.__read_stat("Energy", html_stat)
            champion.energy_reg = self.__read_stat("Energy_regeneration", html_stat)

        return champion

    def extract_champ_list(self, champions_page):
        if self.champ_number is None:
            raise ExeptionsOfLegends.ConfigException("champion number")
        names = list()
        count = 0
        for line in champions_page.split("\n"):
            if '<li style="display:inline-block;width:10em;"><div style="text-align:center;">' \
               '<span style="float:left; height:22px; width:22px;"><a href="/wiki/' in line:
                name = line.split('<a href="/wiki/')[1]
                name = name.split('"')[0]
                name = self.__replace_singlequote_char(name)
                names.append(name)
                count += 1
                if count >= int(self.champ_number):
                    break
        return names



    def __replace_singlequote_char(self, text):
        return text.replace("%27","'")

    def __capture_stat_table(self, champion_page):
        lines = champion_page.split("\n")
        count = 0
        for line in lines:
            if 'table id="champion_info-lower-preseason"' in line:
                lines = lines[count:]
            count += 1
        count = 0
        for line in lines:
            if "</table>" in line:
                lines = lines[:count]
            count += 1
        return lines

    def __read_stat(self, stat, lines):
        count = 1
        value = None
        for line in lines:
            if '<a href="/wiki/' + stat + '"' in line:
                line_to_search = lines[count]
                line_to_search = line_to_search.split(">")[2]
                value = float(line_to_search.split("<")[0])
                break
            count += 1

        return value