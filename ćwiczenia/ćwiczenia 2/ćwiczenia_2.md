## Złożoność - liczba operacji dostępu do elementu

- Binary search (na tablicy)
- for i in ranage(0, N): for j in ranage(i, N): a[j]+=1
- for i in ranage(0, N): for j in ranage(i, N): for k in ranage(j, N): a[k]+=1

https://www.wolframalpha.com/input?i2d=true&i=Sum%5BSum%5BSum%5B1%2C%7Bk%2Cj%2CN%7D%5D%2C%7Bj%2Ci%2CN%7D%5D%2C%7Bi%2C1%2CN%7D%5D

## Wyszukiwanie interpolacyjne
https://www.geeksforgeeks.org/interpolation-search-in-python/

## Zadanie z aktywności (1.5pkt)

Kod w Pythonie:
- generowanie danych - dwa przypadki
    - N danych z rozkładu jednostajnego liczb naturalnych 1- M)
    - N kolejnych danych 1-N (1,2,3,...N-1,N) zaburzonych +-0,1, lub 2 (wylosowane z rozkładu jednostajnego)
- wyszukiwanie liniowe i binarne (własny kod)
- testy na kliku przykładach
0.5 pkt

- wyszukiwanie interpolacyjne (własny kod)
- pomiar czasu i pomiar liczby operacji sprawdzenia elementu pod indeksem
0.5 pkt

- pesymistyczny przypadek wyszukiwania interpolacyjnego - dane w tablicy, wyszukiwana liczba, uzasadnienie
0.5 pkt
