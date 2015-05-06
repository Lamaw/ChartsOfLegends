from Utility.WebClient import WebClient
from Utility.xmlParser import ParsedConfig
from Utility.PageAnalyzer import PageAnalyzer
from Utility.JsonAnalyzer import JsonAnalyzer
from Model.ChartBoard import ChartBoard


"""GLOBAL CONFIGURATION"""
config = ParsedConfig().config

# storage_path = "D:\\_Dev\\ChartsOfLegends\\Data\\stats.json"
get_data_from_web = False

def retrieve_data_from_web():

    client = WebClient(config["url"], config["proxy"])
    analyzer = PageAnalyzer(config)

    """Build the champion name list"""
    response = client.get_web_page("champions")
    page = response.read()
    champ_name_list = analyzer.extract_champ_list(page)

    """Get the champion stats"""
    champ_list = list()
    for champ in champ_name_list:
        page = client.get_web_page(champ).read()
        analyzer.write_champion_stat(page, champ, config["data_path"])


"""Objects Instanciation"""

if get_data_from_web:
    retrieve_data_from_web()

parser = JsonAnalyzer(config)
parser.json_print(config["data_path"])
chart_board = parser.build_chart_board(config["data_path"])




# """Instanciate the board where stats are processed"""
# stat_board = ChartBoard(champ_list)
#
# """Get processing results"""
# means = stat_board.process_means(champ_list)
# for key, value in means.items():
#     print str(key), str(value)



