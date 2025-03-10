from foxycon import Search, StatisticianSocNet

from service.search_process import SearchProcess
from settings import LINK

# proxy = [
#     "http://shapdi:8b3yGiQBjy1D@93.183.125.176:3128",
#     "http://shapdi2:BVZzY5xENsN1@194.246.82.177:3128",
# ]

def start_search():
    search_object = Search(subtitles=True, proxy=None)
    statistic_object = StatisticianSocNet( subtitles=True)

    list_proces = []

    for link in LINK.split(','):
        print(link)
        sp = SearchProcess(link=link, search_object=search_object, statistic_object=statistic_object)
        list_proces.append(sp)

    for sp in list_proces:
        sp.start()




if __name__ == '__main__':
    start_search()
