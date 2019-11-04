import sys


def find_capital(state, states, capital_cities):
    code = states.get(state, None)
    if code:
        return capital_cities[code]
    return None


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
        examples = [e.strip() for e in argv[1].split(',') if e.strip() != '']
        for e in examples:
            to_find = ' '.join([s.capitalize() for s in e.lower().split()])
            capital = find_capital(to_find, states, capital_cities)
            state = find_state(to_find, states, capital_cities)
            if state:
                capital = find_capital(state, states, capital_cities)
                print(f'{capital} is the capital of {state}')
            elif capital:
                state = find_state(capital, states, capital_cities)
                print(f'{capital} is the capital of {state}')
            else:
                print(f'{e} is neither a capital city nor a state')


if __name__ == "__main__":
    main()
