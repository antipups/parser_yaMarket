import re
import requests


def parse_proxy():
    html = requests.get('https://www.ip-adress.com/proxy-list').text
    html = html[html.find('<table class="htable proxylist">'):]
    urls = list()
    html = html[html.find('<a href="'):]
    while re.search(r'title="More information about.*>.*</a>.*</td>', html) is not None:
        new_url = re.search(r'">.*</a>.*</td>', html).group()[2:-5]
        html = html[5:]
        new_url = new_url[:new_url.find('</a')] + new_url[new_url.rfind(':'):]
        urls.append(new_url)
        html = html[html.find('<a href'):]
    all_urls = re.findall(r'<a href="https:\/\/www\.ip-adress\.com\/ip-address\/.*<\/td>', html)
    for proxy in all_urls:
        urls.append(re.sub(r'</a>', '', re.search(r'">.*</td', proxy).group()[2:-4]))
    return tuple(urls)


if __name__ == '__main__':
    print(parse_proxy())