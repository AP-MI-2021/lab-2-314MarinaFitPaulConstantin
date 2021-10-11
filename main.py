# problema 5
# verific daca un numar este palindrom

def is_palindrome(n):
    # verific pas cu pas fiecare element al numarului introdus, n, pentru a putea afirma daca este sau nu palindrom
    for i in range(len(n)//2):
        if n[i]!=n[len(n)-i-1]:
            # returnez fals in cazul in care nu este indeplinita cerinta din is_palindrom, adica cifrele sa fie egale
            return False
    return True


# fac niste teste sa vad daca programu ruleaza bine
def test_is_palindrom():
    assert is_palindrome("55") is True
    assert is_palindrome("101") is True
    assert is_palindrome("12") is False




# problema 10
# calculez combinari de n luate cate k
def get_n_choose_k(n, k):

    rezultat = 1
    for i in range(1, k + 1):
        rezultat = rezultat * (n - (k - i)) // i
    return rezultat


# fac niste teste sa vad daca programmu ruleaza bine
def test_get_n_choose_k():
    assert get_n_choose_k(5, 3) == 10
    assert get_n_choose_k(10, 5) == 252
    assert get_n_choose_k(6, 4) == 15

def main():
    while True:
        print(test_is_palindrom())
        print(test_get_n_choose_k())
        print("1.verifica daca un nr este palindrom")
        print("2.calculeaza combinari de n luate cate k")
        print("x.iesire")
        optiune = input("dati optiune ")
        if optiune == "1":
           n = input("dati n ")
           print(is_palindrome(n))
        elif optiune == "2":
            n = input("dati n ")
            k = input("dati k ")
            print(get_n_choose_k(n,k))
        elif optiune == "x":
            break
        else :
            print("Optiune gresita, reincercati.")
if __name__ == '__main__':
    main()

