import requests
import re


def parse_from_kaspi(url):
    headers = {
    "Cache-Control": "max-age=0",
    "Connection": "keep-alive",
    "Cookie": "ks-cart=19620e73-e46f-482e-96a7-66f59768c332; JSESSIONID=AC6DBA88930E59DF7E0C6A091CFBCED0; user-device-type=Desktop; kaspi-region-confirm-shown=true; kaspi-payment-region=18; kaspi-trusted-region-id=18; dd__persistedKeys=[%22user.anonymousId%22]; dd_user.anonymousId=e1fc4dd0-8730-11ea-bb85-7931190d9d84; test.user.group=22; _ga=GA1.2.1330592494.1587845461; _gid=GA1.2.325824161.1587845461; _fbp=fb.1.1587845461156.1371247961; _hjid=f060976e-cab2-4f0f-a918-24e3de98e9c4; k_stat=6aa126df-72b1-4128-96b2-a37c8e96cab3; ks.tg=97; __zzatgib-w-kaspi=MDA0dBA=Fz2+aQ==; rees46_session_id=cf2399a0-4c8c-4655-af44-4e939f64b1ec; tmr_lvid=3b7f0270b4a69b144af2e4d8f155e17f; tmr_lvidTS=1587845469993; _ym_uid=1587845470419968063; _ym_d=1587845470; kaspi.storefront.cookie.city=750000000; ks.cc=18; maps_access=ZL42267S924W9XAV; NSC_lbtqj.la-nbjo=6bbea3d117c99e924245729ba49dde27537724deec8d615563c38439359009805b212da7; start-banners=%5B%7B%22Id%22%3A233%2C%22Position%22%3A1%2C%22IsNew%22%3Afalse%7D%2C%7B%22Id%22%3A2%2C%22Position%22%3A2%2C%22IsNew%22%3Afalse%7D%2C%7B%22Id%22%3A9%2C%22Position%22%3A3%2C%22IsNew%22%3Afalse%7D%2C%7B%22Id%22%3A234%2C%22Position%22%3A4%2C%22IsNew%22%3Afalse%7D%5D; ks.ngs.s=2831746020959a463b5dc5c78e658456; ks.sa=Web; _gat_reserve=1; rees46_session_code=9f378c5a-ba03-432b-b6af-c92333aea258; _gat_ddl=1; _ym_isad=2; _ym_visorc_32819392=b; tmr_detect=0%7C1587919932855; rees46_session_last_act=1587919940143; __tld__=null; amplitude_id_07837f813af2319a800677ff9c177d3ekaspi.kz=eyJkZXZpY2VJZCI6IjFlNDI3ZWFmLWIxOTctNDhiMi1iYTJhLWVmNjIxZWNjZDc1OVIiLCJ1c2VySWQiOm51bGwsIm9wdE91dCI6ZmFsc2UsInNlc3Npb25JZCI6MTU4NzkxOTkyMjUyOCwibGFzdEV2ZW50VGltZSI6MTU4NzkxOTk0MDcxMCwiZXZlbnRJZCI6NSwiaWRlbnRpZnlJZCI6NSwic2VxdWVuY2VOdW1iZXIiOjEwfQ==; cfidsgib-w-kaspi=A2UIs3Ncjf1keBshkv6h4/5eninT23JGb7/zc6ddRyRzFPdG1b6vMnuzRKATYMKJTQ2hphquk2V9JY+sHg/P4v9PuhmgKYIPPIKVff+/mT8R1dKOMV42KUuiAnOphZQYhlq0vz/KX1Kp3a/38D9sAGiNyC2HDf22fBSUkQ==; gsscgib-w-kaspi=+6L8d71MqwGpsofAZLaTHy4XxqpnQxmt+o25Yi62Ets25ETANpu364C2wFa6XMphaGqy92tr3AzmzYDhb189m0j7x0xUzakisLccycvsQ4nIt/g4YRj8qmdcC0LnnAFQJnPkp8rvbXeX8wok1iRMpON1Z8mCyTWwpzUHh9dGXgl/stVLdNZwlQJAABo=; tmr_reqNum=62",
    "Host": "kaspi.kz",
    "Sec-Fetch-Dest": "document",
    "Sec-Fetch-Mode": "navigate",
    "Sec-Fetch-Site": "same-origin",
    "Sec-Fetch-User": "?1",
    "Upgrade-Insecure-Requests": "1",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/81.0.4044.122 Safari/537.36",
    }




if __name__ == '__main__':
    parse_from_kaspi('https://kaspi.kz/shop/p/hankook-tire-dynapro-i-cept-rw08-215-55-r18-95q-12705901/?c=750000000')