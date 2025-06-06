# Wykład 3 


## Sortowanie

### Definicje:
- stabilność
- działanie "w miejscu" (nie tylko dla sortowania)
- sortowanie wewnętrzne / zewnętrzne

[(O - bez wszystkich przykładów algorymów) Wikipedia - Sortowanie](
https://pl.wikipedia.org/wiki/Sortowanie)

## Komentarze
- zazwyczaj za operację elementarną przyjmujemy porównanie elementów


## Podstawowe algorytmy sortowania "w miejscu"$

### Bubble Sort
[(O) GeeksForGeeks - Bubble Sort](https://www.geeksforgeeks.org/bubble-sort-algorithm/)
> W kodzie pojawiają się 2 usprawnienia: 
> - kończenie każdego przejścia coraz wczesniej (zmniejszenie o około połowę operacji elementarnych, bez zmiany złożoności średniej / pesymistycznej)
> - zatrzymanie algorytmu po wykryciu posorrtowanej tablicy (przyśpieszenie dla szczególnych przypadków, bez zmiany złożoności średniej / pesymistycznej)

### Cocktail Sort
[(O) GeeksForGeeks - Cocktail Sort](https://www.geeksforgeeks.org/cocktail-sort/)
> Dalsze usorawnienie Bubble Sort'a.
> Polega na naprzemiennym kierunku sortowania.
> Daje znaczne przyśpieszenie w praktce (patrz link).


### Selection Sort
[(O) GeeksForGeeks - Selection Sort](https://www.geeksforgeeks.org/selection-sort-algorithm-2/)

### Insertion Sort
[(O) GeeksForGeeks - Insertion Sort](https://www.geeksforgeeks.org/insertion-sort-algorithm/)


## Algorytmy sortowania wykorzysujące dodatkowe założenia lub pamięć

### Counting Sort
[(O) GeeksForGeeks - Counting Sort](https://www.geeksforgeeks.org/counting-sort/)
> - Niska (liniowa) złożoność czasowa, będąca konsekwencją dodatkowego założenia o danych (częsty motyw w matematyce).
> - Po stworzeniu sum prefixowych tablica countArray dla indexu i zawiera liczby opisujące w którym miejscu tablicy znajduje się pierwszy element większy od i.
> - Uwaga: Przedstawiona wersja zakłada, że sortowane wartości są nieujemnymi liczbami naturalnym (rozszerzenie do liczb całkowitych - ćwiczenie). 

### Radix Sort
[(O) GeeksForGeeks - Radix Sort](https://www.geeksforgeeks.org/radix-sort/)
> Opiera się na Counting Sorcie i jego stabilności.
> Nie działa w miejstu, wymaga dodatkowej pamięci.


### Bucket Sort
[(O)  GeeksForGeeks - Bucket Sort](https://www.geeksforgeeks.org/bucket-sort-2/)
> k := liczba kubełków

[(O) Wikipedia - Bucket Sort](https://pl.wikipedia.org/wiki/Sortowanie_kube%C5%82kowe)


## Inne materiały

### Materiały uzupełniające

[(d) Radix Sort vs Bucket Sort](https://www.geeksforgeeks.org/radix-sort-vs-bucket-sort/?ref=lbp)

[(d) YouTube - Insertion Sort in 2min](https://www.youtube.com/watch?v=JU767SDMDvA)

### Analizy

[(d) Computerphile - Getting Sorted & Big O Notation](https://www.youtube.com/watch?v=kgBjXUE_Nwc)

[(p/r) YouTube - The Bubble Sort Curve](https://www.youtube.com/watch?v=Gm8v_MR7TGk)
> Ciekawa analiza krzywej wyznaczanej przez Bubble Sort

[(r) YouTube - Bubble-sort with Hungarian ("Csángó") folk dance](
https://www.youtube.com/watch?v=lyZQPjUT5B4)
> Sortowanie przez taniec

[(r) 10 Forbidden Sorting Algorithms](https://www.youtube.com/watch?v=ktgxMtWMflU)

[(d) Sorting Secret - Computerphile](https://www.youtube.com/watch?v=pcJHkWwjNl4)
> Siekawe spojrzenie na podobieństwo Insertion i Selection Sort, uwaga - to różne algorytmy, ale przedstawiona reprezentacja (sieć sortująca) ich nie rozróżnia

### Szalone wizualizacje

[(r) YouTube - 15 Sorting Algorithms in 6 Minutes](https://www.youtube.com/watch?v=kPRA0W1kECg)

[(r) YouTube - Pushing Sorts to their Limits](https://www.youtube.com/watch?v=8MsTNqK3o_w)


### Inne (od niewydajnych do absurdalnych) algorytmy sortowania

[(r) Wikipedia - Bogo Sort](https://pl.wikipedia.org/wiki/Bogosort)

[(r) GeeksForGeeks - Bogo Sort](https://www.geeksforgeeks.org/bogosort-permutation-sort/)

[(p) StackOverflow - złożoność Bogo Sort](https://stackoverflow.com/questions/19879556/what-is-the-average-time-complexity-of-bogosort)

[(r) Wikipedia - Gnome Sort](https://pl.wikipedia.org/wiki/Sortowanie_gnoma)



<!--
https://www.semanticscholar.org/paper/Sorting-the-Slow-Way%3A-An-Analysis-of-Perversely-Gruber-Holzer/a69e045125bdf7c017d3f84a68c0df4688298059?p2df

https://math.uni.wroc.pl/~jagiella/p2python/skrypt_html/wyklad1.html

https://www.lucc.pl/inf/egzamin_inzynierski/kierunkowe/[K][5]%20Ocena%20zlozonosci%20algorytmow/tekst/1.pdf -->




