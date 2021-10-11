#problema 5
#verific daca un numar este palindrom
def is_palindrome(n):

 #verific pas cu pas fiecare element al numarului introdus, n, pentru a putea afirma daca este sau nu palindrom
    for i in range(0, int(len(n) / 2)):
        if n[i] != n[len(n) - i - 1]:
  # returnez valaorea de adevar a functiei is_palindrom
            return False
    return True
#fac niste teste sa vad daca programmu ruleaza bine
def test_is_palindrom(n):
    assert is_palindrome(55) is True
    assert is_palindrome(101) is True
    assert is_palindrome(12) is False

n=input("Introdu numar: ")
print(is_palindrome(n))


#problema 10
#calculez combinari de n luate cate k
def get_n_choose_k(n,k):
    rezultat = 1
    for i in range(1,k+1):
        rezultat = rezultat * (n-(k-i))//i
    return rezultat
#fac niste teste sa vad daca programmu ruleaza bine
def test_get_n_choose_k(n,k):
  assert get_n_choose_k(5, 3) == 10
  assert get_n_choose_k(10, 5) == 252
  assert get_n_choose_k(6, 4) == 15


n = int(input("Dati n: "))
k = int(input("Dati k: "))
print(get_n_choose_k(n,k))
