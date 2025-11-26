def revstr(rstr):
    rev_str = ""
    for s in rstr:
        rev_str = s + rev_str
    return rev_str

def reverse_str(st):
    if len(st) <=1:
        return st
    return reverse_str(st[1:]) + st[0]


if __name__ == "__main__":
    print(revstr("sudhir"))
    print(reverse_str("amruta"))