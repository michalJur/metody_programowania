# Wykład 1


## Podstawy Pythona

### Popularność Pythona - ankieta Stack Overflow
https://survey.stackoverflow.co/

### Interpreter Pythona online
https://www.online-python.com/

### (sekcja Learn the Basics - OBOWIĄZKOWA) learnpython.org
https://www.learnpython.org/
> Interaktywny kurs Pythona - można pisać kod bezpośrednio w przeglądarce.
> Szczególnie ważne są sekcje o listach, słownikach i funkcjach.

### Polska wersja learnpython.org (polecana przez gov.pl)
https://www.gov.pl/web/koduj/learnpythonorg
> To samo, ale po polsku.

## Wyszukiwanie w posortowaniej tablicy

### (OBOWIĄZKOWY) Wyszukiwanie liniowe i binarne
https://www.geeksforgeeks.org/linear-search-vs-binary-search/

### (OBOWIĄZKOWY) Wyszukiwanie interpolacyjne
https://www.geeksforgeeks.org/interpolation-search-in-python/

### Wyszukiwanie binarne - Computerphile
https://www.youtube.com/watch?v=hDn8iOc30Tk
<!-- 
"in" wolniejszy od binary search, bo nie zakłąda posortowanych danych i przeszukuje liniowo

Komentarz pod videoz: The point made at 14:30 is arguably the most important part of this video. Specifically, it is less important to know how to write, from scratch, a particular algorithm than it is to know that different algorithms have different tradeoffs. Knowing how to pick the best algorithm (and data structures) for a particular situation is more important than being able to implement an algorithm on a whiteboard.
-->


## Mierzenie wydajności kodu - profilowanie

### (sekcja Podstawowe zasady - OBOWIĄZKOWA) ./profilowanie_poradnik.md

## Szybki kod w Pythonie

Jak można zobaczyć w załączonej implementacji, kod napisany w Pythonie jest zdecydowanie wolniejszy niż C++. Wynika to z charakterystyki języka (dynamiczne typowanie, interpreter). Python odpłaca się wygodą i szybkim prototypowaniem. Nadal możemy pisać szybki kod w Pythonie używając zewnętrznych bibliotek (z algorytmami implementowanymi np. w C++) lub bibliotek wprowadzających kompilację kodu.

### Przykłady bibliotek z algorytmami:

- Numpy
    > Podstawowa biblioteka dla operacji numerycznych (np. operacje na wektorach, macierzach).
    > Implementuje większość operacji w C++.

- SciPy
  > Zawiera zoptymalizowane implementacje wielu algorytmów.

### Przykłady bibliotek kompilujących kod:

- Numba
  > Działa automatycznie przez dekorator @jit.
  > Prosta w zastosowaniu, przydatna do optymalizacji pętli i obliczeń numerycznych.

- Cython
  > W zasadzie osobny język - Python wymieszany z C.
  > Wymaga napisania specjalnych deklaracji typów.

- Jax
  > Używana głównie w uczeniu maszynowym.
  > Wspiera obliczenia na GPU.
    
### Kompilatory JIT

- PyPy (materiał na Computerphile: https://www.youtube.com/watch?v=d7KHAVaX_Rs)
  > Just-In-Time compilation - kompilacja w trakcie działania programu.
  > PyPy to alternatywna implementacja Pythona z JIT.
  > Może przyspieszyć program bez zmian w kodzie źródłowym.