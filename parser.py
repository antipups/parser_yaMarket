import random
import requests
import openpyxl
import parser_proxy


def read_xlsx():
    """
        Открываем и считываем файл xlsx для получения всех ссылок и названий товаров
    :return:
    """
    wb = openpyxl.load_workbook('1.xlsx')
    ws = wb['Лист1']
    i = 1
    dict_of_product = {}
    while True:
        if ws.cell(row=i, column=2).value is not None:
            dict_of_product.update({ws.cell(row=i, column=1).value: ws.cell(row=i, column=2).value})
            i += 1
        else:
            wb.close()
            break
    parse(dict_of_product)


def parse(dict_of_product):
    """
        Парсим ВСЕ товары с Я Маркета, с использованием прокси.
    :param dict_of_product:
    :return:
    """
    all_proxies = parser_proxy.parse_proxy()
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'
    }
    for title, url in dict_of_product.items():
        html = ''
        title = title.strip()
        i = 0
        while html.find(title) == -1:
            proxies = {'https': all_proxies[random.randint(0, len(all_proxies) - 1)]}
            html = requests.get('https://market.yandex.ua/product--stabilizator-napriazheniia-odnofaznyi-resanta-ach-1000-1-ts-1-kvt/12718909?slug=stabilizator-napriazheniia-odnofaznyi-resanta-ach-1000-1-ts-1-kvt&productId=12718909&show-uid=15874301878053693055916001&nid=56405&glfilter=7893318%3A7285665&text=%D0%A1%D1%82%D0%B0%D0%B1%D0%B8%D0%BB%D0%B8%D0%B7%D0%B0%D1%82%D0%BE%D1%80%20%D0%A0%D0%B5%D1%81%D0%B0%D0%BD%D1%82%D0%B0%20%D0%90%D0%A1%D0%9D-1000%2F1-%D0%A6&context=search&lr=0&rtr=142', headers=headers, proxies=proxies).text
            i += 1



def get_info():
    """
        Получаем всю инфу о продукте.
    :return:
    """


if __name__ == '__main__':
    read_xlsx()
