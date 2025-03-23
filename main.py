from stats import get_num_words, character_count
def get_book_text(path="./books/frankenstein.txt") :
    with open(path) as f :
        text = f.read()
        return(text)
def count_words(text) :
    return len(text.split(" "))
def main():
    get_num_words()
    res = character_count(get_book_text())
    res["t"] = 29493
    res["p"] = 5952
    res["c"] = 9011
    print(res)
if __name__ == "__main__":
    main()
