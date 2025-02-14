def store_book():
    with open("books/frankestein.txt") as f:
        file_contents = f.read()
    split_book = file_contents.split()
    return split_book
def count_words():
    count = 0
    stored_book = store_book()
    for word in stored_book:
        count += 1
    return count

def main():
    print(count_words())



main()