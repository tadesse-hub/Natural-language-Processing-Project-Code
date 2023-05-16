import glob
import codecs

amharic_path = "/home/tadesse/PycharmProjects/data/amharic/books/*.txt"
geez_path = "/home/tadesse/PycharmProjects/data/geez/books/*.txt"


def count_verses_each_languages(path):
    files = glob.glob(path)
    for file in files:
        with open(file) as f:
            line_count = 1
            for line in f:
                line_count += 1
        print(line_count, file)


# def write_to_file(fname, am_count_text):
#     ft = codecs.open(fname, 'w', 'utf-8')
#     ft.write(am_count_text)
#     ft.close()
#     print('cont written to %s ' % fname)


if __name__ == '__main__':
    cont = (count_verses_each_languages(amharic_path))
    # write_to_file("am1.txt", cont)



