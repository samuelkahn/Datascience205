


def peek_print_dict(d):
    for key in d.keys()[:10]:
        print '{}: {}'.format(key, d.get(key))

def peek_print_list(l):
    for i in range(10):
        print '{}: {}'.format(i, l[i])
