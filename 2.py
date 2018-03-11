# -*- coding: UTF-8 -*-


def fun1(plaintext):
    """
    fun1(plaintext) -> string

    返回E盒拓展之后的48bit
    """
    extend_box = [32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11, 12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20,
                  21, 20, 21, 22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1]
    plaintext = to_bit(plaintext)
    cipher_text = range(0, 48)
    for i in cipher_text:
        cipher_text[i] = plaintext[extend_box[i]-1]
    return ''.join(cipher_text)


def to_bit(plaintext, printf=False):
    """
    to_bit(num) -> string

    返回字符串的位表示, printf:是否按8位一组进行打印
    """
    bit_text = []
    for char in str(plaintext):
        bit_code = (bin(ord(char))[2:])
        while len(bit_code) != 8:
            bit_code = '0' + bit_code
        bit_text.append(bit_code)
    if printf:
        print ' '.join(bit_text)
    return ''.join(bit_text)

