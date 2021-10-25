# problema 5
def is_palindrome(n):
    """
    Verific daca un numar n este palindrom
    :param n: numar intreg
    :return: True daca n e palindrom, False in caz contrat
    """

    for i in range(len(n) // 2):
        if n[i] != n[len(n) - i - 1]:
            return False
    return True


def test_is_palindrom():
    assert is_palindrome("55") is True
    assert is_palindrome("101") is True
    assert is_palindrome("12") is False


# problema 10

def get_n_choose_k(n, k):
    """
    Calculez combinari de n luate cate k
    :param n: nr natural
    :param k: nr natural
    :return: combinari de n luate cate k
    """

    rezultat = 1
    for i in range(1, k + 1):
        rezultat = rezultat * (n - (k - i)) // i
    return rezultat


# fac niste teste sa vad daca functia ruleaza bine
def test_get_n_choose_k():
    assert get_n_choose_k(5, 3) == 10
    assert get_n_choose_k(10, 5) == 252
    assert get_n_choose_k(6, 4) == 15


# problema 12
def get_perfect_squares(n, k):
    """
    afiseaza numerele patrate perfecte din intervalul n k
    :param n: numar intreg
    :param k: numar intreg
    :return: afisare nr patrate perfecte
    """
    lpp=[]
    for i in range(n, k + 1):
        if i**(.5) == int(i**(.5)):
            lpp.append(i)
    return lpp


def test_get_perfect_squares():
    assert get_perfect_squares(7, 10) == [9]
    assert get_perfect_squares(2, 5) == [4]

def main():
    while True:
        print(test_is_palindrom())
        print(test_get_n_choose_k())
        print(test_get_perfect_squares())
        print("1.verifica daca un nr este palindrom")
        print("2.calculeaza combinari de n luate cate k")
        print("3.afisez toate elementele patrate perfecte din intervalul n k")
        print("x.iesire")
        optiune = input("dati optiune ")
        if optiune == "1":
            n = (input("dati n "))
            print(is_palindrome(n))
        elif optiune == "2":
            n1 = int(input("dati n "))
            k1 = int(input("dati k "))
            print(get_n_choose_k(n1, k1))
        elif optiune == "3":
            n2 = int(input("dati n "))
            k2 = int(input("dati k "))
            if n2 > k2:
                print(get_perfect_squares(k2, n2))
            else:
                print(get_perfect_squares(n2, k2))
        elif optiune == "x":
            break
        else:
            print("Optiune gresita, reincercati.")


main()
