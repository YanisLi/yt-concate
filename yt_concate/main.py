import urllib.request
import ssl
import json
from .settings import API_KEY

CHANNEL_ID = 'UCKSVUHI9rbbkXhvAXK-2uxA'  # 目標頻道ID


def get_all_video_in_channel(channel_id):
    ssl._create_default_https_context = ssl._create_unverified_context  # 不需驗證SSL驗證

    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    first_url = f'{base_search_url}key={API_KEY}&channelId={channel_id}&part=snippet,id&order=date&maxResults=25'

    video_links = []
    url = first_url
    while True:
        inp = urllib.request.urlopen(url)
        resp = json.load(inp)

        for i in resp['items']:
            if i['id']['kind'] == "youtube#video":
                video_links.append(base_video_url + i['id']['videoId'])

        try:
            next_page_token = resp['nextPageToken']
            url = first_url + '&pageToken={}'.format(next_page_token)

        except KeyError:
            break
    return video_links


video_list = get_all_video_in_channel(CHANNEL_ID)
print(len(video_list))
print(video_list)
