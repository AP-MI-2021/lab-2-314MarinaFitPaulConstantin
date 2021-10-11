def get_n_choose_k(n,k):
    rezultat = 1
    for i in range(1,k+1):
        rezultat = rezultat * (n-(k-i))//i
    return rezultat



def test_get_n_choose_k(n,k):
  assert get_n_choose_k(5, 3) == 10
  assert get_n_choose_k(10, 5) == 252
  assert get_n_choose_k(6, 4) == 15


n = int(input("Dati n: "))
k = int(input("Dati k: "))
print(get_n_choose_k(n,k))