__author__ = 'amahouix'

import ExeptionsOfLegends
import json
import os
from Model.Champion import Champion


class PageAnalyzer():

    def __init__(self, config):
        self.champ_number = None
        if "champ_number" in config:
            self.champ_number = config["champ_number"]

    # ---------- PUBLIC ----------------

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

    def write_champion_stat(self, champion_page, champion_name, path):
        line = self.__champion_to_json(champion_page, champion_name) + "\n"
        self.__write_json(line, path)

    # ----------- PRIVATE ---------------

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

    def __write_json(self, data, path):
        with open(path, 'a') as outfile:
            outfile.write(data)

    def __champion_to_json(self, champion_page, champion_name):
        champion = self.extract_champ_stat(champion_page, champion_name)

        data_stats = json.dumps({'health': champion.health})
        data_stats += json.dumps({'health_reg': champion.health_reg})
        if champion.mana is not None:
            data_stats += json.dumps({'mana': champion.mana})
            data_stats += json.dumps({'mana_reg': champion.mana_reg})
        else:
            data_stats += json.dumps({'energy': champion.energy})
            data_stats += json.dumps({'energy_reg': champion.energy_reg})
        data_stats += json.dumps({'ad': champion.ad})
        data_stats += json.dumps({'att_speed': champion.att_speed})
        data_stats += json.dumps({'mov_speed': champion.mov_speed})
        data_stats += json.dumps({'armor': champion.armor})
        data_stats += json.dumps({'mag_res': champion.mag_res})
        data_stats += json.dumps({'range': champion.range})

        return json.dumps([champion_name, data_stats])

    def init_champ_file(self, path):
        os.remove(path)
        open(path, 'w+').close()