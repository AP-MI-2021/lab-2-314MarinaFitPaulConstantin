def is_palindrome(n):


 #verific pas cu pas fiecare element al numarului introdus, n, pentru a putea afirma daca este sau nu palindrom
    for i in range(0, int(len(n) / 2)):
        if n[i] != n[len(n) - i - 1]:
  # returnez valaorea de adevar a functiei is_palindrom
            return False
    return True


def test_is_palindrom(n):
    assert is_palindrome(55) is True
    assert is_palindrome(101) is True
    assert is_palindrome(12) is False

n=input("Introdu numar: ")
print(is_palindrome(n))