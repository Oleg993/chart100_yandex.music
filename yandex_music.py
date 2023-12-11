from pprint import pprint
import requests
import json
from time import sleep

cookies = {
    'is_gdpr': '0',
    'yandexuid': '3443440131676627157',
    'yuidss': '3443440131676627157',
    'i': 'oo7ftor4GdRjZSlbO9zd3MpbgV47l0pS6iIAA1zP+LYusAZRNpMpRv4XUCx5N+QVparZ3xVeOWjNBJt7bV3MJ4/ZgDs=',
    'yandex_login': 'alehshulhan@gmail.com',
    'gdpr': '0',
    '_ym_uid': '1678470195204397618',
    'Session_id': '3:1702301071.5.0.1683882971000:uyDWJQ:85.1.2:1|1769040955.-1.0.1:333874925.3:1683882971|17:10166030.756394.SQbnERoPAlG6C9_cP889tutSzio',
    'sessar': '1.1184.CiD1aa_GmrvzYUzjcM3RBOUQJopVyRl5wJZraTK1xX12vg.6-mrjGxDrBPIQgl0yzGRIVZKmXW79T5w1EZ8s-czWL4',
    'sessionid2': '3:1702301071.5.0.1683882971000:uyDWJQ:85.1.2:1|1769040955.-1.0.1:333874925.3:1683882971|17:10166030.756394.fakesign0000000000000000000',
    '_ym_isad': '2',
    'ymex': '1704893076.oyu.3443440131676627157#1710011547.yrts.1678475547',
    'bh': 'Ej8iR29vZ2xlIENocm9tZSI7dj0iMTE5IiwiQ2hyb21pdW0iO3Y9IjExOSIsIk5vdD9BX0JyYW5kIjt2PSIyNCIaBSJ4ODYiIhAiMTE5LjAuNjA0NS4yMDAiKgI/MDoJIldpbmRvd3MiQggiMTUuMC4wIkoEIjY0IlJcIkdvb2dsZSBDaHJvbWUiO3Y9IjExOS4wLjYwNDUuMjAwIiwiQ2hyb21pdW0iO3Y9IjExOS4wLjYwNDUuMjAwIiwiTm90P0FfQnJhbmQiO3Y9IjI0LjAuMC4wIiI=',
    'yandex_gid': '157',
    'yp': '1999242971.udn.cDphbGVoc2h1bGhhbkBnbWFpbC5jb20%3D#1702387476.yu.3443440131676627157#1704893633.ygu.1#4294967295.skin.s',
    'is_gdpr_b': 'CI7bbxDw3gEoAg==',
    'yashr': '1348556611702301633',
    '_yasc': '2xNOa3iY1tSsGWmP88IgTcgIkChJWEk2HKNhWjYeGylbfxetPwzwwssKOrRno+D8oALxIvhv',
    '_ym_d': '1702301636',
    'device_id': 'a6b7db1faca062be451102878c22ee4cf45d3fbeb',
    'lastVisitedPage': '%7B%7D',
    '_ym_visorc': 'b',
    'active-browser-timestamp': '1702301946418',
}

headers = {
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Accept-Language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'Connection': 'keep-alive',
    'Referer': 'https://music.yandex.by/chart',
    'Sec-Fetch-Dest': 'empty',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Site': 'same-origin',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/119.0.0.0 Safari/537.36',
    'X-Current-UID': '1769040955',
    'X-Requested-With': 'XMLHttpRequest',
    'X-Retpath-Y': 'https://music.yandex.by/chart',
    'X-Yandex-Music-Client-Now': '2023-12-11T16:41:11+03:00',
    'sec-ch-ua': '"Google Chrome";v="119", "Chromium";v="119", "Not?A_Brand";v="24"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"Windows"',
}

params = {
    'what': 'chart',
    'lang': 'ru',
    'external-domain': 'music.yandex.by',
    'overembed': 'false',
    'ncrnd': '0.7649685166559774',
}

response = requests.get('https://music.yandex.by/handlers/main.jsx', params=params, cookies=cookies, headers=headers)

def get_chart():
    chart = {}
    for track in response.json()['chartPositions']:
        ranking = track['chartPosition']['position']
        track_name = track['track']['title']
        singers_list = [singer['name'] for singer in track['track']['artists']]
        singers = ', '.join(singers_list)
        if ranking not in chart.keys():
            chart[ranking] = f'{track_name} - {singers}'
    return chart

def writer(data):
    with open('yandex_chart.json', 'w') as file:
        json.dump(data, file)

writer(get_chart())
