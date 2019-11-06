import antigravity
import sys

def main():
    if len(sys.argv) == 4:
        try:
            antigravity.geohash(float(sys.argv[1]), float(sys.argv[2]), sys.argv[3].encode())
        except ValueError as e:
            print(e)
    else:
        print("Usage : python3 geohashing.py latitude longitude date")
        print("Exemple : python3 geohashing.py 37.421542 -122.085589 2005-05-26-10458.68")

if __name__ == "__main__":
    main()