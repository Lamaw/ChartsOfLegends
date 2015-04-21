from Utility.WebClient import WebClient
from Utility.xmlParser import ParsedConfig
from Utility.PageAnalyzer import PageAnalyzer
from Model import ChartBoard

PROXY = None
#PROXY = "http://proxy-jf.intel.com:911"
URL = "http://leagueoflegends.wikia.com/wiki"

config = ParsedConfig()
client = WebClient(URL, PROXY)
analyzer = PageAnalyzer(config.config)

response = client.get_web_page("champions")

page = response.read()

champ_name_list = analyzer.extract_champ_list(page)
# for champ in champ_list:
#     print champ

# print page
champ_list = list()
for champ in champ_name_list:
    champion = analyzer.extract_champ_stat(client.get_web_page(champ).read(), champ)
    champ_list.append(champion)

stat_board = ChartBoard(champ_list)