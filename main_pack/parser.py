import datetime
from random import randint as ri
import time
import requests
import openpyxl
from main_pack import parser_proxy
import re
from PIL import Image


def read_xlsx(path):
    """
        Открываем и считываем файл xlsx для получения всех ссылок и названий товаров
    :return:
    """
    wb = openpyxl.load_workbook(path)
    ws = wb['Лист1']
    i = 1
    dict_of_product = {}
    while True:
        if ws.cell(row=i, column=2).value is not None:
            key = ws.cell(row=i, column=1).value
            if ws.cell(row=i, column=2).hyperlink is not None:
                value = ws.cell(row=i, column=2).hyperlink.target
            else:
                value = ws.cell(row=i, column=2).value
            dict_of_product.update({key: value})
            i += 1
        else:
            wb.close()
            parse(dict_of_product)
            return


def parse(dict_of_product):
    """
        Парсим ВСЕ товары с Я Маркета, с использованием прокси.
    :param dict_of_product:
    :return:
    """
    # with open('asd.txt', 'r') as f:
    all_proxies = parser_proxy.parse_proxy()
        # all_proxies = f.read().split('\n')
    headers = {
        'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'en-US,en;q=0.9,ru;q=0.8',
        'Cache-Control': 'max-age=0',
        'Connection': 'keep-alive',
        'Cookie': f'_ym_uid=1579538585539137365; mda=0; yandexuid=4775578911579527928; yuidss=4775578911579527928; i=7fpXxLZtVlknYALqfuHdIqESJ7QKPyrT/p1Ib1NKFr2+GlI6yQ4Nq8EuI7FxxNSTvC5JPW7DUgpjBnX2NCjgeBJhLQE=; my=YwA=; yandex_gid=142; gdpr=0; yandexmarket=48%2CUAH%2C1%2C%2C%2C%2C2%2C0%2C0%2C0%2C0%2C0%2C12%2C0; mOC=1; currentRegionId=142; currentRegionName=%D0%94%D0%BE%D0%BD%D0%B5%D1%86%D0%BA; cycada=vBIVPiL1OivB3zUy7Bun86lEsDT+JL2RpLjQnNHDsg4=; yabs-frequency=/4/0000000000000000/AKgmSB0wGG00/; pof=%7B%22clid%22%3A%5B%222359538%22%5D%2C%22mclid%22%3A%221002%22%2C%22distr_type%22%3A%227%22%2C%22vid%22%3A%22986%22%2C%22opp%22%3A%22900%22%7D; cpa-pof=%7B%22clid%22%3A%5B%222359538%22%5D%2C%22mclid%22%3A%221002%22%2C%22distr_type%22%3A%227%22%2C%22vid%22%3A%22986%22%2C%22opp%22%3A%22900%22%7D; oMaSefD=1; oMaSpfD=1; oMaRefD=1; Session_id=3:1587567800.5.0.1587567800047:uOvH2Q:4c.1|230517873.0.2|4:156007.208530.Ct9WborQwK5ZqYGCgMhyMgHKkSI; sessionid2=3:1587567800.5.0.1587567800047:uOvH2Q:4c.1|230517873.0.2|4:156007.666179.wzxl5em2LjckToAqLylJxzwXt3M; L=WnRGfUNYc2xfWkAFakRaBg5bYgN0cAVxGAcNIUANFBMvBwIAJw==.1587567800.14211.321094.42a247e10a7e1c492bb9a0954f71a90a; yandex_login=nick.kurkurin; skid=7141896761587577073; _ym_d=1587577075; visits=1586198458-1587549787-1587643024; lr=0; dcm=1; _ym_wasSynced=%7B%22time%22%3A1587643027213%2C%22params%22%3A%7B%22eu%22%3A0%7D%2C%22bkParams%22%3A%7B%7D%7D; _ym_isad=2; ugcp=1; yp=1581234933.com.3#1581437288.dq.1#1896019512.multib.1#1584131668.oyu.4775578911579527928#1596427321.szm.1_25%3A1536x864%3A1536x760#1902927800.udn.cDpuaWNrLmt1cmt1cmlu#1612368485.ygu.1#1894898590.yrtsi.1579538590#1587729427.yu.4775578911579527928; ymex=1590235027.oyu.4775578911579527928#1898004678.yrts.1582644678#1894898590.yrtsi.1579538590; oMaSofD=1; oMaFifD=1; spravka=dD0xNTg3NjQzNDY5O2k9MjE3LjE5OS4yMzYuMTM1O3U9MTU4NzY0MzQ2OTI1OTAwNzM2MztoPTNkZTAxZGNhNGU2NGU2MzFjNDM5MDRkYWEwODZlNWJl; uid=AABcdl6h0xFT/QBoBj78Ag==; js=1; first_visit_time={datetime.datetime.now().strftime("%Y-%m-%d")}T{datetime.datetime.now().strftime("%H")}%3A{datetime.datetime.now().strftime("%M")}%3A{datetime.datetime.now().strftime("%S")}%2B03%3A00; fonts-loaded=1; _ym_visorc_160656=b; _ym_visorc_45411513=b; metrika_enabled=1; _ym_metrika_enabled=1; HISTORY_AUTH_SESSION=edf01ebb; parent_reqid_seq=32a2e5f8f7b07ef01b1b51f5713261f1%2Cf56f71597835f3c7d2890719dde73a35%2C5929f9d6bc20b3dc7e7110c643dcfa53%2C4ccf49d0f29fea9142486001ae159458; _ym_metrika_enabled_160656=1; _ym_metrika_enabled_44910898=1; _ym_metrika_enabled_45411513=1; oMaPrfD=1',
        'Referer': '',
        'Host': 'market.yandex.kz',
        'Sec-Fetch-Dest': 'document',
        'Sec-Fetch-Mode': 'navigate',
        'Sec-Fetch-Site': 'same-origin',
        'Sec-Fetch-User': '?1',
        'Upgrade-Insecure-Requests': '1',
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36',
    }
    st = datetime.datetime.now()
    i = 0
    for index, product in enumerate(dict_of_product.items()):
        if i == 5:
            all_proxies = parser_proxy.parse_proxy()
        else:
            i += 1
        headers['Referer'] = product[1][:product[1].find('?')]
        html, title, url = '', product[0].strip(), product[1][:product[1].find('?')] + '/spec'
        print(f"Процесс - {index + 1}/{len(dict_of_product.keys())}", title, url)
        start = datetime.datetime.now()
        while html.find(title) == -1:
            proxies = {'https': all_proxies[ri(0, len(all_proxies) - 1)]}
            print(proxies)
            try:
                html = requests.get(url, headers=headers, proxies=proxies).text
            except requests.exceptions.ProxyError:
                print('Ошибка из-за неверного прокси, продолжаю работу;')
                time.sleep(3)
                continue
            else:
                print('Времени прошло - ', datetime.datetime.now() - start)
                get_info(title, url, html)
                break
    print('Закончил работу за - ', datetime.datetime.now() - st)


def get_info(title, url, html):
    """
        Получаем всю инфу о продукте.
    :return:
    """
    print('Достаю инфу с спарсенного сайта.')
    try:
        with open('1.png', 'wb') as f:
            f.write(requests.get((lambda x: x[x.rfind('https'):-2]) (re.search(r'<meta property=\"og:image\"[^>]*', html).group())).content)
    except:
        print(f"Ошибка - {title}, {url}")
        return

    dict_of_info = {'Название': title, 'Ссылка': url}
    for match in re.finditer(r"_2TxqAVjiup((?!</dd).)*", html, re.MULTILINE):
        characteristic = match.group()
        key = re.search(r'<span.[^/]*', characteristic).group()[6:-1]
        value = characteristic[characteristic.rfind('>') + 1:]
        dict_of_info.update({key: value})

    write_xlsx(dict_of_info)


def write_xlsx(dict_of_info):
    try:
        wb = openpyxl.load_workbook('2.xlsx')
    except:
        wb = openpyxl.Workbook()
        del wb['Sheet']
    finally:
        if 'Лист1' not in wb.sheetnames:
            wb.create_sheet('Лист1')
        ws = wb['Лист1']
        ws.column_dimensions['a'].width = 30
        i = 2
        dict_of_col = {}
        while ws.cell(row=2, column=i).value is not None:
            dict_of_col.update({ws.cell(row=2, column=i).value: i})
            i += 1
        else:
            for j in dict_of_info.keys():
                if j not in dict_of_col:
                    ws.cell(row=2, column=i).value = j
                    dict_of_col.update({j:i})
                    i += 1

    print('Открыл 2.xlsx.')

    row = ws.max_row + 1 if ws.max_row == 1 else ws.max_row + 14

    with Image.open('1.png') as img:
        img.thumbnail((200, 200), Image.ANTIALIAS)
        img.save('1.png')

    img = openpyxl.drawing.image.Image('1.png')
    ws.add_image(img, 'A' + str(row))

    for column, val in dict_of_info.items():
        ws.cell(row=row + 1, column=dict_of_col.get(column)).value = val

    while True:
        try:
            wb.save('2.xlsx')
        except:
            print('Закройте пожалуйста Excel файл 2.xlsx')
            time.sleep(3)
        else:
            wb.close()
            print('Закрыл 2.xlsx.')
            return


if __name__ == '__main__':
    # get_info('sex', 'asd', 'lol')
    # write_xlsx("sex")
    # read_xlsx('../1.xlsx')
    get_info('1', '1', '1')
    # write_xlsx(1)
    input('Парсер завершил свою работу, для выхода нажмите какую-либо кнопку.')