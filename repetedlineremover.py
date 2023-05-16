import codecs

lang1_file = 'am1.txt'
lang2_file = 'ge1.txt'
# lang3_file = 'en.txt'

lang1 = codecs.open(lang1_file, 'r', 'utf-8').read()
lang2 = codecs.open(lang2_file, 'r', 'utf-8').read()
# lang3 = codecs.open(lang3_file, 'r', 'utf-8').read()


def to_dic(lang):
    dic = {}
    for count, el in enumerate(lang):
        dic[count] = el
    return dic


def write_to_file(f_name, cont):
    fn = codecs.open(f_name, 'w', 'utf-8')
    fn.write(cont)
    fn.close()


def remove_repeat(dic1, dic2):
    repeated_count = 0
    lang1_cont = ''
    lang2_cont = ''
    # lang3_cont = ''
    dic3 = {}; dic4 = {}
    for k, v in dic1.items():
        if v not in dic3.values():
            dic3[k] = v
            dic4[k] = dic2[k]
        else:
            if dic2[k] not in dic4.values():
                dic3[k] = v
                dic4[k] = dic2[k]
            else:
                repeated_count += 1

    for k, v in dic3.items():
        lang1_cont += v + "\n"
        lang2_cont += dic4[k] + "\n"

    print('%d sentence repeated '% repeated_count)
    write_to_file(lang1_file + '_pr.txt', lang1_cont)
    write_to_file(lang2_file + '_pr.txt', lang2_cont)


if __name__ == '__main__':
    lang1 = lang1.splitlines()
    lang2 = lang2.splitlines()

    dict1 = to_dic(lang1)
    dict2 = to_dic(lang2)

    remove_repeat(dict1, dict2)

