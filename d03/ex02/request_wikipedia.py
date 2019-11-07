import requests
from dewiki import parser
import sys


def get_wiki_data(string_to_find):
    endpoint = 'https://en.wikipedia.org/w/api.php'
    search_params = {
        'action': 'query',
        'titles': string_to_find,
        'prop': 'revisions',
        'rvprop': 'content',
        'format': 'json'
    }
    resp = requests.get(endpoint, params=search_params)
    if not resp.ok:
        exit(f"Error {resp.status_code}  :: {resp.reason}")
    response = resp.json()
    if 'error' in response.keys():
        exit(f"Error in response: {response['error']['info']}")
    if 'query' not in response.keys():
        exit(f"No result for the search.")
    return response


def clear_response(response):
    pages = response["query"]["pages"]
    buf = None
    for _, page in pages.items():
        buf = page.get("revisions")
        if buf is not None:
            break
    my_parser = parser.Parser()
    good = buf[0]['*']
    to_write = my_parser.parse_string(good)
    return to_write


def main():
    if len(sys.argv) != 2:
        exit("Usage: request_wikipedia.py string_to_find")
    string_to_find = sys.argv[1]
    try:
        response = get_wiki_data(string_to_find)
        wiki_string = clear_response(response)
        with open(string_to_find + '.wiki', 'w') as fd:
            fd.write(wiki_string)
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
