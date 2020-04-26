import re
import requests


def parse_proxy():
    html = requests.get('https://www.ip-adress.com/proxy-list').text
    urls = list()
    # for i in re.finditer(r'(\d{1,3}.){4}</a>:\d{1,4}</td>\n<td>transparent</td>', html):
    #     withouttrans = i.group()[:-26]
    #     urls.append(withouttrans[:withouttrans.find('<')] + withouttrans[withouttrans.rfind('>') + 1:])

    html = requests.get('https://free-proxy-list.net/').text
    urls = list()
    for proxy in re.finditer(r'(\d{0,3}.){4}</td><td>\d{1,6}', re.search(r'<tbody>.*</tbody>', html).group()):
        proxy = proxy.group()
        urls.append(proxy[:proxy.find('<')] + ':' + proxy[proxy.rfind('>') + 1:])
    return tuple(urls)


if __name__ == '__main__':
    print(parse_proxy())