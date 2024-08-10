def main():
    with open("./books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count(file_contents)

def word_count(content):
    count = len(content.split())
    print(count)

main()