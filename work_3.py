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
    mix_columns(plaintext)


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

def mix_columns(list):
    """
    min_columns(list) -> list

    返回列混合后的列表
    """
    mix_matrix = [2, 3, 1, 1, 1, 2, 3, 1, 1, 1, 2, 3, 3, 1, 1, 2]
    new_list = []

    # 转换为二进制
    for x in range(len(mix_matrix)):
        bin_num = bin(mix_matrix[x])[2:]
        while len(bin_num) != 8:
            bin_num = '0' + bin_num
        mix_matrix[x] = bin_num

    for x in range(len(list)):
        for y in range(len(list[0])):
            bin_num = bin(int(list[x][y], 16))[2:]
            while len(bin_num) != 8:
                bin_num = '0' + bin_num
            list[x][y] = bin_num

    partition(mix_matrix, 4)



fun1('wang jia rui', 2016122125)
