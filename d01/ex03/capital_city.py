import sys


def find_state(state, states, capital_cities):
    code = states.get(state, None)
    if code:
        return capital_cities[code]
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
        state = find_state(argv[1], states, capital_cities)
        print(state) if state is not None else print('Unknown state')

if __name__ == "__main__":
    main()
