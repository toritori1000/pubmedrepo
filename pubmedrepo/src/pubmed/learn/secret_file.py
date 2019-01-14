from pubmed.learn.secret_gen import get


def write(file_path):
    f = open(file_path, 'w+')

    num_list = get()
    for num in num_list:
        f.write("%s\n" % num)

    f.close()


def read(file_path):
    g = open(file_path, 'r')

    secret_numbers = []
    for line in g:
        line = line.rstrip()
        secret_numbers.append(line)

    g.close()
    return secret_numbers
