import asyncio

from foxycon import  StatisticianSocNet
from foxycon.search_services.search import YouTubeSearch1

from management_collected.standart_api.youtube import send_single_data_to_server
from settings import parameters_col

import multiprocessing
import time
import random

proxy = [
    parameters_col.PROXY_ONE,
    parameters_col.PROXY_TWO,
]

ssn = StatisticianSocNet(
    proxy=proxy,
)



# print(parameters_col.LINK)
# parameters_col.LINK="https://www.youtube.com/watch?v=tTBL8L-ZSAo"
# print(parameters_col.LINK)
async def worker():
    data = await YouTubeSearch1(ssn).search_recommendation_async(parameters_col.LINK)
    async for i in data():
            for data_txt in i:
                try:
                    print(data_txt)
                    try:
                        await send_single_data_to_server(data_txt)
                    except Exception as ex:
                        print(ex)
                        for text in data_txt:
                            parameters_col.LINK = text.link
                            try:
                                await send_single_data_to_server(text)
                            except:
                                continue
                except:
                    continue


def start_process():
    while True:
        process = multiprocessing.Process(target=run_worker)
        process.start()
        process.join()  # Ожидание завершения процесса, если он упадёт
        print("Перезапуск процесса...")


def run_worker():
    asyncio.run(worker())

if __name__ == "__main__":
    start_process()
