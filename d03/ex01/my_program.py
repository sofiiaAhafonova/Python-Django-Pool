from path import Path

def main():
    tmp = Path('.')
    tmp = tmp / 'test_dir'
    if not tmp.isdir():
        tmp.mkdir()
    new_file = tmp / 'new_file.txt'
    if not new_file.isfile():
        new_file.touch()
    new_file.write_lines(["Just for testing", "For fun"])
    new_file.write_text("That's it", append=True)
    for line in new_file.lines():
        print(line)

if __name__ == '__main__':
    main()
