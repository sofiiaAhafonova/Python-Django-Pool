import sys


def find_state(capital, states, capital_cities):
    code = None
    for k, v in capital_cities.items():
        if v == capital:
            code = k
    if code:
        for k, v in states.items():
            if v == code:
                return k
    return None
   
def main():

    states = {
        "Oregon": "OR",
        "Alabama": "AL",
        "New Jersey": "NJ",
        "Colorado": "CO"
    }
    capital_cities = {
        "OR": "Salem",
        "AL": "Montgomery",
        "NJ": "Trenton",
        "CO": "Denver"
    }
    argv = sys.argv
    if len(argv) == 2:
        capital = find_state(argv[1], states, capital_cities)
        print(capital) if capital is not None else print('Unknown capital')


if __name__ == "__main__":
    main()
