import pprint
# TODO решить с помощью list comprehension и распечатать его
list_ = []
for i in range(16):

    dict_ = {
        "bin": bin(i),
        "dec": i,
        "hex": hex(i),
        "oct": oct(i)
    }
    list_.append(dict_)
pprint.pprint(list_)