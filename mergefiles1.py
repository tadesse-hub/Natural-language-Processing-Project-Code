import codecs
import glob

amharic_path = "/home/tadesse/PycharmProjects/data/amharic/books/*.txt"
geez_path = "/home/tadesse/PycharmProjects/data/geez/books/*.txt"


def read_files(path):
    ss = ""
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            for line in f:
                ss += line + "\n"
    return ss


def write_to_file(fname, am_text):
    ft = codecs.open(fname, 'w', 'utf-8')
    ft.write(am_text)
    ft.close()
    print('cont written to %s ' % fname)


def file_count():
    names = {}
    for fn in glob.glob('*.txt'):
        with open(fn) as f:
            names[fn] = sum(1 for line in f if line.strip() and not line.startswith('#'))
    return names


if __name__ == '__main__':

    # Amharic files merged into single file

    cont = read_files(amharic_path)
    am_text = "\n".join([ll.rstrip() for ll in cont.splitlines() if ll.strip()])
    write_to_file("am.txt", am_text)

#     Geez files merged into one file

    cont = read_files(geez_path)
    ge_text = "\n".join([ll.rstrip() for ll in cont.splitlines() if ll.strip()])
    write_to_file("ge.txt", ge_text)

    print(file_count())
