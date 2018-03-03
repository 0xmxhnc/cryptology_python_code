# -*- coding: UTF-8 -*-


def fun1(plaintext, k, b):  # (k,b)密钥
    """仿射密码加密"""
    cipher_text = []     # 密文list
    for x in plaintext:
        c = ((ord(x) - ord('a'))*k+b) % 26+ord('a')   # 明文的所对应的数字
        print ("%d(%s)*%d+%d mod 26 = %d(%s)" % (ord(x) - ord('a'), x, k, b, c-ord('a'), chr(c)))
        cipher_text.append(chr(c))
    print "cipher_text:"+"".join(cipher_text)
    return 0


def fun2(cipher_text, k, b):
    """仿射密码解密"""
    plain_text = []     # 明文list
    k1 = inverse(k)
    for x in cipher_text:
        c = ((ord(x)-ord('a')-b)*k1) % 26 + ord('a')
        print("(%d(%s)-%d)*%d = %d (mod26)" % (ord(x)-ord('a'), x, b, k1, c-ord('a')))
        plain_text.append(chr(c))
    print "plain_text:"+"".join(plain_text)
    return 0


def fun3(plaintext, key):
    """维吉尼亚密码加密"""
    cipher_text = []
    for x in range(0, len(plaintext)):
        c = (ord(plaintext[x]) + ord(key[x % len(key)]) - 97*2) % 26 + 97
        print("%d(%s)+%d(%s)=%d(%s) mod 26" % (ord(plaintext[x]) - 97, plaintext[x], ord(key[x % len(key)]) - 97, key[x % len(key)], c - 97, chr(c)))
        cipher_text.append(chr(c))
    print "cipher_text:"+"".join(cipher_text)
    return 0


def inverse(k, _range_=range(1, 26)):    # _range_为密文空间
    """解逆元"""
    for x in _range_:
        if (x*k) % (_range_[-1]+1) == 1:
            return x


fun3('jiang', 'xin')