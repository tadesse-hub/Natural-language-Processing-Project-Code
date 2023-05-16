import codecs
import glob

amharic_path = "/home/tadesse/PycharmProjects/data/am.txt"
geez_path ="/home/tadesse/PycharmProjects/data/ge.txt"


def read_files(path):
    ss = ""
    files = glob.glob(path)
    for name in files:
        with open(name) as f:
            for line in f:
                ss += line + "\n"
    return ss


def write_to_file(fnam, cont):

    ft = codecs.open(fnam, 'w', 'utf-8')
    ft.write(cont)
    ft.close()
    print('cont written to %s ' % fnam)


def remove_verse_number(file):
    new_cont = ''
    for line in file.splitlines():
        cleaned = " ".join(line.split()[1:])
        new_cont += cleaned + "\n"
    return new_cont


if __name__ == '__main__':

    cont = read_files(amharic_path)
    am_text = "\n".join([ll.rstrip() for ll in cont.splitlines() if ll.strip()])
    am_text = remove_verse_number(am_text)
    write_to_file("am1.txt", am_text)

    cont= read_files(geez_path)
    ge_text = "\n".join([ll.rstrip() for ll in cont.splitlines() if ll.strip()])
    ge_text = remove_verse_number(ge_text)
    write_to_file("ge1.txt", ge_text)
