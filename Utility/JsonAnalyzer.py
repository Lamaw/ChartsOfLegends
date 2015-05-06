__author__ = 'Antoine'

from Model.Champion import Champion
from Model.ChartBoard import ChartBoard
import json

class JsonAnalyzer():

    def __init__(self, config):
        self.champ_number = None
        if "champ_number" in config:
            self.champ_number = config["champ_number"]



    def __read_json(self, json):
        with open(json, "rb") as json_file:
            data = json_file.readlines()
        return data

    def json_print(self, json_file):
        json_file = self.__read_json(json_file)
        for line in json_file:
            print line

    def build_chart_board(self, json):
        champ_list = list()

        json = self.__read_json(json)

        for line in json:
            champ_list.append(self.__build_champion(line))

        return ChartBoard(champ_list)

    def __build_champion(self, line):
        split_line = line.split("{")

        name = split_line[0].split('"')[1]
        champ = Champion(name)
        champ.health = self.__get_stat_value(split_line, "health")
        champ.health_reg = self.__get_stat_value(split_line, "health_reg")
        champ.mana = self.__get_stat_value(split_line, "mana")
        champ.mana_reg = self.__get_stat_value(split_line, "mana_reg")
        champ.armor = self.__get_stat_value(split_line, "armo")
        champ.ad = self.__get_stat_value(split_line, "ad")
        champ.mag_res = self.__get_stat_value(split_line, "mag_res")
        champ.range = self.__get_stat_value(split_line, "range")
        champ.att_speed = self.__get_stat_value(split_line, "att_speed")
        champ.mov_speed = self.__get_stat_value(split_line, "mov_speed")

        if champ.mana is None:
            champ.energy = self.__get_stat_value(split_line, "energy")
            champ.energy_reg = self.__get_stat_value(split_line, "energy_reg")

        return champ

    def __get_stat_value(self, split_line, stat_name):
        value = None
        for el in split_line[1:]:
            if stat_name in el:
                value = el.split(':')[1].split("}")[0]
                break
        return value

