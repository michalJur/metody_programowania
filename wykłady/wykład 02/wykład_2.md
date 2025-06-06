# Wykład 2

## Notacje asymptotyczne

### (O - Wprowadzenie, Notacja asymptotyczna) Ważniak - Matematyka Dyskretna, Wykład 9
https://wazniak.mimuw.edu.pl/index.php?title=Matematyka_dyskretna_1/Wyk%C5%82ad_9:_Asymptotyka


## Złożoność

### (O) Wikipedia - Złożoność oczekiwana
https://pl.wikipedia.org/wiki/Z%C5%82o%C5%BCono%C5%9B%C4%87_oczekiwana

### (O) Wikipedia - Złożoność pesymistyczna
https://pl.wikipedia.org/wiki/Z%C5%82o%C5%BCono%C5%9B%C4%87_pesymistyczna

### (r) Fireship - Big-O Notation in 100 Seconds
https://www.youtube.com/watch?v=g2o22C3CRfU

### Komentarze
- złożoność może odnosić się do różnych zasobów, zazwyczaj czasu (liczba operacji) i pamięci (liczba komórek pamięci)
- definicja złożoności optymistycznej - analogicznie, ale z $inf$
- zbiór danych D w definicji może być indeksowany rozmiarem danych n (np. D_n := tablice liczb rzeczywistych o rozmiarze n)
- możemy wyznaczyć złożoność optymistyczną ($opt$) / pesymistyczną  ($pes$) / oczekiwaną ($exp$) dla danych o określonym rozmiarze (i tak zazwyczaj robimy)
- $opt(n) := \inf\{f(d):d\in D_n\}$
- $pes(n) := \sup\{f(d):d\in D_n\}$
- $exp(n) := \frac{1}{|D|}\sum_{d\in D_n} f(d)$


## Analiza algorytmów - definicje:
- operacja dominująca (elementarna)
- niezmiennik pętli / algorytmu
- własność stopu
- poprawność algorytmu


### (O - Wprowadzenie, tylko definicje - operacja dominująca, niezmiennik algorytmu, własność stopu) Ważniak - Algorytmy i Struktury Danych, Wstęp 
https://wazniak.mimuw.edu.pl/index.php?title=Algorytmy_i_struktury_danych/Wst%C4%99p:_poprawno%C5%9B%C4%87_i_z%C5%82o%C5%BCono%C5%9B%C4%87_algorytmu

### (O) Wikipadia - Operacja elementarna
https://pl.wikipedia.org/wiki/Operacja_elementarna

### (O) Wikipedia - Niezmiennik pętli
https://pl.wikipedia.org/wiki/Niezmiennik_p%C4%99tli

### (O - tylko definicja problemu stopu) Wikipedia - Problem stopu
https://pl.wikipedia.org/wiki/Problem_stopu

### (O) Wikipedia - Poprawność częściowa i całkowita
https://pl.wikipedia.org/wiki/Poprawno%C5%9B%C4%87_ca%C5%82kowita


## Zagadnienie: wyszukiwanie maksymalnej podtablicy
- Naiwny O(N^3) (brute force)
- Naiwny O(N^2)
- Kadane O(N) (dziel i zwyciężaj)

### (O) GeeksForGeeks
https://www.geeksforgeeks.org/largest-sum-contiguous-subarray/?ref=gcse_outind


### (O) Medium
https://medium.com/@mz.ebrahimi/solving-the-maximum-subarray-problem-from-brute-force-to-kadanes-algorithm-b476bf4c8b14


<!-- Algorytm 2. Szukanie sumy -->