from Utility.WebClient import WebClient
from Utility.xmlParser import ParsedConfig
from Utility.PageAnalyzer import PageAnalyzer
from Utility.JsonAnalyzer import JsonAnalyzer
from Model.ChartBoard import ChartBoard

"""GLOBAL CONFIGURATION"""
PROXY = None
# PROXY = "http://proxy-jf.intel.com:911"
URL = "http://leagueoflegends.wikia.com/wiki"

storage_path = "D:\\_Dev\\ChartsOfLegends\\Data\\stats.json"
get_data_from_web = False


"""Objects Instanciation"""
config = ParsedConfig().config
if get_data_from_web:
    client = WebClient(URL, PROXY)
    analyzer = PageAnalyzer(config)
    analyzer.init_champ_file(storage_path)

    """Build the champion name list"""
    response = client.get_web_page("champions")
    page = response.read()
    champ_name_list = analyzer.extract_champ_list(page)

    """Get the champion stats""" #This is the step to work on as an interface : if get the data from web is on, go with this execution, else, read from local content (TODO)
    champ_list = list()
    for champ in champ_name_list:
        page = client.get_web_page(champ).read()
        analyzer.write_champion_stat(page, champ, storage_path)

parser = JsonAnalyzer(config)
parser.json_print(storage_path)
chart_board = parser.build_chart_board(storage_path)

print


    # champion = analyzer.extract_champ_stat(client.get_web_page(champ).read(), champ)
    # champ_list.append(champion)

# """Instanciate the board where stats are processed"""
# stat_board = ChartBoard(champ_list)
#
# """Get processing results"""
# means = stat_board.process_means(champ_list)
# for key, value in means.items():
#     print str(key), str(value)
