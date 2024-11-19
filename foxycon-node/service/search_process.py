from foxycon import Search
from foxycon import StatisticianSocNet
from data_structures.schemes import YoutubeChannels, ContentsYoutube, InstagramPages, ContentsInstagram

from multiprocessing import Process

proxy = [
    "http://shapdi:8b3yGiQBjy1D@93.183.125.176:3128",
    "http://shapdi2:BVZzY5xENsN1@194.246.82.177:3128",
]

class SearchProcess(Process):
    def __init__(self, search_object: Search, link:str, statistic_object: StatisticianSocNet):
        super().__init__()
        self._search_object = search_object
        self._link = link
        self._statistic_object = statistic_object


    @staticmethod
    async def get_data(data, statistic_object):
        if data.analytics_obj.social_network == 'youtube':

            cn = await YoutubeChannels(system_id=data.channel_id).get_youtube_channels_system_id()
            if not cn:
                st = await statistic_object.get_data(data.channel_url)
                channel_id = await YoutubeChannels(system_id=st.channel_id, name=st.name, link=st.link,
                                                   country=st.country,
                                                   views=st.view_count,
                                                   subscribers=st.subscriber).add_youtube_channels()

                await ContentsYoutube(system_id=data.system_id, title=data.title, link=data.link,
                                      number_views=data.views, number_likes=data.likes,
                                      view_content=data.analytics_obj.content_type, release_date=data.publish_date,
                                      youtube_channels_id=channel_id).add_contents_youtube()
            else:
                await ContentsYoutube(system_id=data.system_id, title=data.title, link=data.link,
                                      number_views=data.views, number_likes=data.likes,
                                      view_content=data.analytics_obj.content_type, release_date=data.publish_date,
                                      youtube_channels_id=cn.id).add_contents_youtube()

        elif data.analytics_obj.social_network == 'instagram':

            cn = await InstagramPages(system_id=data.author.user_id).get_instagram_pages_system_id()

            if not cn:
                page_id = await InstagramPages(system_id=data.author.user_id,
                                               name=data.author.username,
                                               link=f"https://www.instagram.com/{data.author.username}"
                                               ).add_instagram_pages()
                await ContentsInstagram(system_id=data.media_id, title=data.description,
                                        link=f"https://www.instagram.com/reel/{data.code}",
                                        types_content=data.analytics_obj.content_type, number_views=data.view_count,
                                        number_likes=data.like_count,
                                        release_date=data.publish_date,
                                        instagram_page_id=page_id
                                        ).add_contents_instagram()

            else:

                await ContentsInstagram(system_id=data.media_id, title=data.description,
                                        link=f"https://www.instagram.com/reel/{data.code}",
                                        types_content=data.analytics_obj.content_type, number_views=data.view_count,
                                        number_likes=data.like_count,
                                        release_date=data.publish_date,
                                        instagram_page_id=cn.id
                                        ).add_contents_instagram()

    async def run(self):
        search = await Search(proxy=proxy, subtitles=True).search('https://www.youtube.com/watch?v=yydTXyC9StM&t=139s')
        async for i in search():
            print(i)