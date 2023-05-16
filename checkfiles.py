import os


am = os.listdir('/home/tadesse/PycharmProjects/data/amharic/books/')
ge = os.listdir('/home/tadesse/PycharmProjects/data/geez/books/')


for i in am:
    if i not in ge:
        os.remove('/home/tadesse/PycharmProjects/data/amharic/books/'+i)

