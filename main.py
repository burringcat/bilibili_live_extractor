#! /usr/bin/env python3
import requests
import sys
import time
import json
def get_flv_url(room_id):
    room_id = str(room_id)
    api_url = 'https://api.live.bilibili.com/room/v1/Room/playUrl?cid=' + room_id + '&quality=4&platform=web'
    r = requests.get(api_url)
    content = json.loads(r.text)
    try:
        durl = content['data']['durl'][0]['url']
        return durl
    except:
        print("Failed on room id:", room_id)
        return None
if __name__ == '__main__':
    if len(sys.argv) > 1:
        for arg in sys.argv[1:]:
             time.sleep(0.5)
             url = get_flv_url(arg)
             if url: print(url)
    else:
        exit(1)
