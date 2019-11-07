import requests
from bs4 import BeautifulSoup
import sys


def filter(tag):
    return tag is not None and not tag.has_attr(
        "role") and not tag.name == "abbr" and not tag.name == "img" and tag.name == 'a'


def wiki(string_to_find):
    req = requests.get("https://en.wikipedia.org/wiki/{}".format(string_to_find))

    if req.status_code != 200 or not req:
        exit("Something wrong with Server")

    if not req.text:
        exit(f"Can't find {string_to_find}")

    soup = BeautifulSoup(req.text, 'html.parser')

    et_de_un = soup.find('div', attrs={"id": u"bodyContent"})\
        .find('div', attrs={"id": u"mw-content-text"})\
        .find('div', attrs={"class": u"mw-parser-output"})
    for child in et_de_un.children:
        if child.name == "p":
            les_a = child.find_all(filter)
            for a in les_a:
                href = str(a.get('href'))
                if href.startswith("/wiki/") \
                        and not (href.startswith("#")
                                 or href.startswith("/Wikipedia:")
                                 or href.startswith("/wiki/Help")
                                 or href.startswith('/wiki/File')
                                 or href.startswith('/wiki/Wikipedia:Citation_needed')
                                 or href.startswith('//upload.wikimedia.org/')):
                    # print("href " + href.replace("/wiki/", ""))
                    return href.replace("/wiki/", "")


def main():
    if len(sys.argv) != 2:
        exit("Usage: python3 roads_to_philosophy.py string_to_find")

    string_to_find = sys.argv[1]

    if string_to_find == "Philosophy":
        print("0 roads from Philosophy to philosophy !")
        exit(0)

    print(string_to_find)
    tab_philo = [string_to_find]
    visited = wiki(string_to_find)
    while visited is not None:
        string_to_find.replace(' ', '_')
        print(visited)
        tab_philo.append(visited)
        visited = wiki(visited)

        if visited == "Philosophy":
            iteration = len(tab_philo)
            print("{} roads from {} to Philosophy !".format(iteration, string_to_find))
            sys.exit(0)
        elif visited in tab_philo:
            print("It leads to an infinite loop ! ")
            sys.exit()


if __name__ == '__main__':
    main()
