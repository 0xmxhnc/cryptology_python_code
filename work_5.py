# coding=utf-8


def fun1(num):
    """
    input the num you want to encryption
    return the result of num after grouping and filling
    """
    str_num = str(num)
    ord_num = map(ord, str_num)
    ascii_num = map(to_ascii, ord_num)
    print 'bin of the ascii:', ascii_num
    print 'the num need to fill is 368'

    fill_num = [hex(x)[2:] for x in ord_num]
    fill_num.append('80')
    while len(fill_num) != 63:
        fill_num.append('00')
    fill_num.append('50')

    merge_fill_num = []
    for x in range(0, 64, 4):
        merge_fill_num.append(''.join(fill_num[x:x+4]))

    for index, value in zip(range(16), merge_fill_num):
        print 'w%d:' % index, value


def to_ascii(num):
    """
    convert the num to it's ascii num, and fill it to 8 bits
    """
    ascii_num = bin(num)[2:]
    while len(ascii_num) < 8:
        ascii_num = '0' +ascii_num
    return ascii_num


fun1(2016122142)