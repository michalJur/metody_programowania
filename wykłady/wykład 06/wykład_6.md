# Wykład 5

<!-- 
## 5: **Rekurencja i zarządzanie pamięcią**

- **Struktury danych**:
   - Kolejki 
   - Stosy

- **Teoria rekurencji**
   - Podstawy rekurencji: przypadki podstawowe, przypadki rekurencyjne.
   - Rekurencja ogonowa.
   - Porównanie rekurencji z iteracją pod względem wydajności i czytelności.

- **Zarządzanie pamięcią**:
   - Stosy vs. Kopce (Heaps).
   - Problemy przepełnienia stosu w przypadku rekurencji.
   - Zbieranie śmieci i wycieki pamięci.

- **Algorytmy (Rekurencja)**:
   - Ciąg Fibonacciego (podstawowe rozwiązanie rekurencyjne)


------------

Removing recursion
Merge Sort
Backpack
Hanoi

------------- -->

## Rekurencja

[(d) Recursion - Wikipedia](https://en.wikipedia.org/wiki/Recursion)

<!-- google: wpisz recursion -->

[(O) Introduction to Recursion - GFG](https://www.geeksforgeeks.org/introduction-to-recursion-2/)

[(O) Types of Recursion - GFG](https://www.geeksforgeeks.org/types-of-recursions/)
<!-- direct - bezpośrednia, indirect - pośrednia, tree - rekursja drzewiasta -->

<!-- https://www.geeksforgeeks.org/what-is-recursion/ -->

[(O) What on Earth is Recursion? - Computerphile (Factorial)](https://www.youtube.com/watch?v=Mv9NEXX1VHc)
<!-- Funkcja silnia jako przykłąd -->


## Rekurencja ogonowa

[(O) Rekurencja ogonowa - Wikipedia](https://pl.wikipedia.org/wiki/Rekurencja_ogonowa)

[(O) Tail recursion elimination - GFG](https://www.geeksforgeeks.org/tail-call-elimination/)

<!-- https://www.geeksforgeeks.org/tail-recursion/ -->

## Derekursywacja

[(O) Derekursywacja - Wikipedia](https://pl.wikipedia.org/wiki/Derekursywacja)


<!-- > Jeśli używamy rekurencji ogonowej i język/kompilator ją optymalizuje (Tail Call Optimization – TCO), stos nie rośnie i można ją wtedy pominąć w analizie. Jednak wiele języków, w tym Python, nie wspiera TCO, więc stos jest istotny. -->

<!-- https://www.geeksforgeeks.org/recursive-functions/ -->

## Rekurencja a iteracja

[(O) Difference between Recursion and Iteration - GFG](https://www.geeksforgeeks.org/difference-between-recursion-and-iteration/)
> Uwaga: Do złożoności pamięciowej wliczamy stos wywołań funkcji - w przypadku rekurencji jest to istotne.
> Overhead jest zazwyczaj wyższy dla rekurencji ze względu na wywoływanie funkcji, a złożoność pamięciowa ze względu na stos.
> Uwaga: Złożoność czasowa nie zawsze jest wyższa w iteracyjnym rozwiązaniu, zależy to od problemu i implementacji.

<!-- Tree recursion - czemu O(n) space? -->

[(O) Programming Loops vs Recursion - Computerphile](https://www.youtube.com/watch?v=HXNhEYqFo0o)



## Dziel i rządź
https://en.wikipedia.org/wiki/Divide_and_conquer

https://en.wikipedia.org/wiki/Divide-and-conquer_algorithm

https://www.geeksforgeeks.org/introduction-to-divide-and-conquer-algorithm/

Rekursja -  https://www.w3schools.com/dsa/dsa_algo_simple.php


## Merge Sort

[(O) Merge Sort - GFG](https://www.geeksforgeeks.org/merge-sort/)

[(O) Wyznaczenie złożoności Merge Sort (druga odpowiedź) - Stach Overflow](https://math.stackexchange.com/questions/54416/merge-sort-time-complexity-analysis)

[(O - Substitution method) Inna metoda wyznaczania złożoności, przez "zgadnięcie" i sprawdzenie - GFG](https://www.geeksforgeeks.org/how-to-analyse-complexity-of-recurrence-relation/)

<!-- https://www.geeksforgeeks.org/timsort/ -->

## Wieże Hanoi
[(O) Program for Tower of Hanoi Algorithm - GFG](https://www.geeksforgeeks.org/c-program-for-tower-of-hanoi/)

[(O) Recursion 'Super Power' (in Python) - Computerphile](https://www.youtube.com/watch?v=8lhxIOAfDss)


## Teoretyczne rozważania o rekurencji

[(O - pierwsza, nieformalna definicja) Primitive recursive function](https://en.wikipedia.org/wiki/Primitive_recursive_function)
 <!-- może po polsku? -->

[(O - wprowadzenie i ogólne własności) Funkcja Ackermana](https://pl.wikipedia.org/wiki/Funkcja_Ackermanna)

[(O) The Most Difficult Program to Compute? - Computerphile](https://www.youtube.com/watch?v=i7sm9dzFtEI)
> Wniosek: niektórych zagadnień nie da się rozwiązać inaczej niż rekurencyjnie.
<!-- Czasem potrzebujemy rekurencji -->


## Inne materiały

[(d) Recursive Ray Tracing - Computerphile](https://www.youtube.com/watch?v=nOCPpT-Sn0A)


<!-- One second to compute the largest Fibonacci number I can:
 https://www.youtube.com/watch?v=KzT9I1d-LlQ -->
