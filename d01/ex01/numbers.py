def print_numbers():
    with open('./numbers.txt', 'r') as file:
        data = file.read().split(',')
        for e in data:
            print(e.strip())
         

if __name__ == "__main__":
    print_numbers()
