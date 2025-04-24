# Wykład 7

<!-- 

## 6: **Programowanie dynamiczne i algorytmy zachłanne**

- **Algorytmy (Zachłanne)**:
 - Problem plecakowy (podstawowe podejście zachłanne; przykład suboptymalnego algorytmu zachłannego z backtrackingiem)
 - Kodowanie Huffmana (przykład optymalnego algorytmu zachłannego; połączenie z entropią, drzewami)

- **Algorytmy (Programowanie dynamiczne)**:
  - Ciąg Fibonacciego (rozwiązanie z memoizacją i tabulacją).
  - Problem plecakowy (dynamiczna wersja problemu plecaka 0/1).

- **Zachłanny vs. Programowanie dynamiczne**
  - Kiedy algorytm zachłanny zawodzi i dlaczego programowanie dynamiczne bywa lepszym wyborem.


----------- -->
<!-- 
Wcześniejszy wykład
# Dziel i rządź
https://en.wikipedia.org/wiki/Divide_and_conquer

https://en.wikipedia.org/wiki/Divide-and-conquer_algorithm

https://www.geeksforgeeks.org/introduction-to-divide-and-conquer-algorithm/


Rekursja -  https://www.w3schools.com/dsa/dsa_algo_simple.php
-------------------- -->



## Algorytmy zachłanne

[(O) Greedy Algorithms - W3Schools](https://www.w3schools.com/dsa/dsa_ref_greedy.php)

[(d) Greedy Algorithm - Wikipedia](https://en.wikipedia.org/wiki/Greedy_algorithm)


## Kodowanie Huffmana

[(O do 'Praktyczne zastosowanie' włącznie) Kodowanie Huffmana - Wikipedia](https://pl.wikipedia.org/wiki/Kodowanie_Huffmana)

[(O) Huffman Coding - Programiz](https://www.programiz.com/dsa/huffman-coding)
> Złożoność kopca jako kolejki priorytetowej poznamy później

[(O) Huffman Coding - W3Schools](https://www.w3schools.com/dsa/dsa_ref_huffman_coding.php)
> Czasami pokazywane są złe wartości w liściach (np. na wejściu cyfry 1-8), ale reszta zdaje się działać proawidłowo

[(d) Dowód na optymalność kodowania Huffmana - precyzyjny](https://www.cs.utoronto.ca/~brudno/csc373w09/huffman.pdf)

[(d) Dowód na optymalność kodowania Huffmana - opisowy](https://opendsa-server.cs.vt.edu/ODSA/Books/CS3/html/HuffProof.html)
> Końcówka dowodu wymaga doprecyzowania (czemu T' może być skonstruowane przez algorytm Huffmana - bo suma dwóch najmniejszych wartości jest najmniejsza wśród sum jakichkolwiek par, więc węzeł łączący jest na wlaściwym miejscu)

<!-- https://www.geeksforgeeks.org/huffman-coding-greedy-algo-3/ -->
<!-- Nie musimy stosować min-kopca (poznamy go później), złożoność też wynika z właściwości kopca -->

<!-- https://www.cse.iitk.ac.in/users/satyadev/au17/huffman.pdf -->
<!-- Lemma 3 (inne niepotrzebne?) -->



## Programowanie dynamiczne

[(O - definicja) Dynamic Programming - GFG](https://www.geeksforgeeks.org/dynamic-programming/)

[(O) Dynamic Programming - W3Schools](https://www.w3schools.com/dsa/dsa_ref_dynamic_programming.php)

[(O) Memoization - W3Schools](https://www.w3schools.com/dsa/dsa_ref_memoization.php)

[(O) Tabulation - W3Schools](https://www.w3schools.com/dsa/dsa_ref_tabulation.php)

[(d) Tabulation vs Memoization - GFG](https://www.geeksforgeeks.org/tabulation-vs-memoization/)


## Problem plecakowy (0/1 Knapsack)

[(O) Knapsack - W3Schools](https://www.w3schools.com/dsa/dsa_ref_knapsack.php)
<!--  The 0/1 Knapsack Problem cannot be solved by a greedy algorithm because it does not fulfill the greedy choice property -->

[(O) Knapsack - GFG](https://www.geeksforgeeks.org/0-1-knapsack-problem-dp-10/#space-optimized-approach-on-x-w-time-and-ow-space)
<!-- Optymalizacja pamięci -->

## Algorytmy genetyczne na przykładzie problemu plecakowego

[(O) The Knapsack Problem & Genetic Algorithms - Computerphile](https://www.youtube.com/watch?v=MacVqujSXWE)
> Alternatywne podejście do problemu plecakowego, istotne zwłszcza dla studentów SI


## Inne materiały

[(d) Travelling salesman](https://www.w3schools.com/dsa/dsa_ref_traveling_salesman.php)

[(d) A Short Introduction to Entropy, Cross-Entropy and KL-Divergence - Youtube](https://www.youtube.com/watch?v=ErfnhcEV1O8)
> Istotne dla studentów SI

[(d) "Porażka" problemu plecakowego w kryptografii](https://www.geeksforgeeks.org/knapsack-encryption-algorithm-in-cryptography/)

<!-- https://www.tutorialspoint.com/knapsack-encryption-algorithm-in-cryptography -->



