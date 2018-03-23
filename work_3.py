# -*- coding: UTF-8 -*-


def fun1(plaintext, key):
    """
    fun1(plaintext) -> string

    返回经过Rijndael算法中字节代替，行移位，列混合后的输出结果
    """

    # 储存原文和密钥的16进制
    plaintext_hex, key_hex = [], []

    for char in str(plaintext):
        plaintext_hex.append(hex(ord(char))[2:])

    for char in str(key):
        key_hex.append(hex(ord(char))[2:])

    # 对原文和密钥进行填充
    plaintext_hex.append('0' + str(16 - len(plaintext_hex)))
    while len(plaintext_hex) != 16:
        plaintext_hex.insert(-1, '00')

    key_hex.append('0' + str(16 - len(key_hex)))
    while len(key_hex) != 16:
        key_hex.insert(-1, '00')

    # 字节替换
    plaintext_hex = sub_byte(plaintext_hex)

    # 将一维列表分割为二维4*4列表
    plaintext = partition(plaintext_hex, 4)
    key = partition(key_hex, 4)

    # 二维列表转置
    plaintext = map(list, zip(*plaintext))
    key = map(list, zip(*key))

    # 行位移
    shift_row(plaintext)

    # 列混合
    result = mix_columns(plaintext)
    print result


def partition(list, cols):
    """
    partiton(list) -> list

    将一个一维列表转化为二维列表,返回二维列表
    """
    new_list = []

    if len(list) % cols != 0:
        return []

    for i in range(0, len(list)/cols):
        new_list.append(list[i*cols:(i+1)*cols])

    return new_list

def sub_byte(list):
    """
    sub_byte(list) -> list

    返回字节替换后的列表
    """
    with open('AES_s_box.txt', 'r') as f:
        s_box = (f.read()).split()

    for x in range(0, len(s_box)):
        s_box[x] = s_box[x][2:]

    for x in range(len(list)):
        row, col = int(list[x][0], 16), int(list[x][1], 16)
        list[x] = s_box[row*16 + col]

    return list


def shift_row(list):
    """
    shift_row(list) -> list

    返回行位移后的列表
    """
    for x in range(len(list)):
        copy_list = list[x][:]
        for y in range(4):
            list[x][y] = copy_list[(y+x) % 4]

    return list


def mix_columns(_list):
    """
    min_columns(_list) -> _list

    返回列混合后的列表
    """
    mix_matrix = [2, 3, 1, 1, 1, 2, 3, 1, 1, 1, 2, 3, 3, 1, 1, 2]
    new_list = []

    # 转换为十进制
    for x in range(len(_list)):
        for y in range(len(_list[0])):
            int_num = int(_list[x][y], 16)
            _list[x][y] = int_num

    #转置
    _list = map(list, zip(*_list))

    #转化为矩阵
    mix_matrix = partition(mix_matrix, 4)

    for i in range(len(mix_matrix)):
        for j in range(len(_list)):
            new_list.append(hex(xtime(mix_matrix[i], _list[j])))

    new_list = partition(new_list, 4)
    return new_list


def xtime(row, col):
    """
    xtime(row, col) -> list

    伽罗华域上的乘法，返回list
    """
    result_list = []
    for i in range(len(row)):
        if row[i] == 1:
            result_list.append(col[i])
        elif row[i] == 2:
            if col[i] >= 128:
                result_list.append(((col[i] % 128) * 2) ^ 27)
            else:
                result_list.append(col[i] * 2)
        else:
            if col[i] >= 128:
                result_list.append(((col[i] % 128) * 2) ^ 27 ^ col[i])
            else:
                result_list.append(col[i] * 2 ^ col[i])
    result = result_list[0] ^ result_list[1] ^ result_list[2] ^ result_list[3]
    return result

fun1('your name', 2016122000)
