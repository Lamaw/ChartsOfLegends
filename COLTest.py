from Utility.WebClient import WebClient
from Utility.xmlParser import ParsedConfig
from Utility.PageAnalyzer import PageAnalyzer
from Model.ChartBoard import ChartBoard

"""GLOBAL CONFIGURATION"""
# PROXY = None
PROXY = "http://proxy-jf.intel.com:911"
URL = "http://leagueoflegends.wikia.com/wiki"


"""Objects Instanciation"""
config = ParsedConfig()
client = WebClient(URL, PROXY)
analyzer = PageAnalyzer(config.config)

"""Build the champion name list"""
response = client.get_web_page("champions")
page = response.read()
champ_name_list = analyzer.extract_champ_list(page)

"""Get the champion stats""" #This is the step to work on as an interface : if get the data from web is on, go with this execution, else, read from local content (TODO)
champ_list = list()
for champ in champ_name_list:
    champion = analyzer.extract_champ_stat(client.get_web_page(champ).read(), champ)
    champ_list.append(champion)

"""Instanciate the board where stats are processed"""
stat_board = ChartBoard(champ_list)

"""Get processing results"""
means = stat_board.process_means(champ_list)
for key, value in means.items():
    print str(key), str(value)
