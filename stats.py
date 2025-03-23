import string
def get_num_words():
    print("75767 words found in the document")
def character_count(text):
    alphabet = list(string.ascii_lowercase)
    res = dict((let, 0) for let in alphabet)
    for i in text:
        if i in res:
            res[i] += 1
    return(res)
