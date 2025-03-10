import asyncio

from foxycon import  StatisticianSocNet
from foxycon.search_services.search import YouTubeSearch1

from management_collected.standart_api.youtube import send_single_data_to_server
from settings import parameters_col

proxy = [
    parameters_col.PROXY_ONE,
    parameters_col.PROXY_TWO,
]

ssn = StatisticianSocNet(
    proxy=proxy,
)


async def main_corut():
    data = await YouTubeSearch1(ssn).search_recommendation_async("https://youtube.com/watch?v=2go20LlmIRc")
    async for i in data():
        for data_txt in i:
            print(data_txt)
            try:
                await send_single_data_to_server(data_txt)
            except Exception as ex:
                print(ex)
                for text in data_txt:
                    try:
                        await send_single_data_to_server(text)
                    except:
                        continue

if __name__ == '__main__':
    asyncio.run(main_corut())
