# coding=utf-8
def power_mod(base, power, n):
    """
    返回(base)^power mod n的结果
    :param base:基数
    :param power:次数
    :param n:模数
    """
    if power == 1:
        return base
    if power % 2:
        return power_mod(base, 1, n) * power_mod(base**2 % n, power / 2, n) % n
    else:
        return power_mod(base**2 % n, power/2, n) % n


def inv(e, m):
    """
    求密钥e关于模数m的乘法逆元 e*d = 1(mod m)
    :param e: 密钥
    :param m: 模数
    :return: 逆元d
    """
    for x in range(m):
        if (x*e) % m == 1:
            return x


def fun1(p=23, q=17, e=7):
    """
    返回RSA的公钥和私钥
    :param p: 素数P
    :param q: 素数q
    :param e: 公钥e
    :return: [(e,n),(d,n)]
    """
    n = p*q
    m = (p-1)*(q-1)
    d = inv(e, m)
    return [(e, n), (d, n)]


def fun2(plain_text=19, p=23, q=17, e=7):
    """
    返回加密后的密文
    :param plain_text: 原文
    :param p: 素数P
    :param q: 素数q
    :param e: 公钥e
    """
    m = (p-1)*(q-1)
    cipher_text = power_mod(plain_text, e, m)
    return cipher_text

def fun3(cipher_text, p=23, q=17, e=7):
    """
    RSA解密
    :param plain_text:密文
    :param p:素数p
    :param q:素数q
    :param e:公钥e
    :return:明文
    """
    if cipher_text == 1 or cipher_text == 0:
        cipher_text = 5
    n = p*q
    m = (p-1)*(q-1)
    d = inv(e, m)
    plain_text = power_mod(cipher_text, d, n)
    return plain_text


print(fun1(), fun2(), fun3(5))