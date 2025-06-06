# Wykład 9

## Grafy

[(O) Grafy - definicje](https://eduinf.waw.pl/inf/alg/001_search/0123.php)

[(O) Reprezentacja grafów - GFG](https://www.geeksforgeeks.org/graph-and-its-representations/)

<!--(https://www.w3schools.com/dsa/dsa_theory_graphs.php) -->
<!-- https://www.w3schools.com/dsa/dsa_data_graphs_implementation.php -->

## Przeszukiwanie grafu: Breadth First Search (BFS) i Depth First Search (DFS)

[(O) Breadth First Search - GFG](https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/)
[(O) Depth First Search - GFG](https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/)
[(O) Iterative DFS - GFG](https://www.geeksforgeeks.org/iterative-depth-first-traversal/)

<!-- 
https://courses.grainger.illinois.edu/cs225/fa2022/resources/bfs-dfs/
- Obowiązuje nas pseudokod tu zaprezentowany
- Animacje zdają się nieprawidłowo prezentować kolejność działań 
- Najbardziej intuicyjna implementacja - węzeł zaznaczamy jako odwiedzony gdy go przetwarzamy (dodajemy do kolejki) -->

- Złożoność
    - Złożoność czasowa: oba algorytmy O(|V|+|E|).
    - Złożoność pamięciowa: oba algorytmy O(|V|) (rekurencyjny DFS: O(|V|+|E|)).

- Uwagi 
    - Podane implementacje wersji iteracyjnych nieco od siebie odbiegają, ale można je tak upodobnić, że jedyna różnica to zamiana kolejki (BFS) na stos (DFS).

    - Kolejka i stos wyznaczają kolejność przetwarzania węzłów, a co za tym idzie zachowanie algorytmu.
    - W opisach czasem nieprecyzyjnie podawane jest, że sprawdzamy każdą krawędź tylko raz - w grafie nieskierowanym sprawdzamy je dwukrotnie, z jednego i drugiego wierzchołka (ale nie zmienia to złożoności).
    - Każdy wierzchołek przetwarzamy raz (O(|V|)), ale możemy go napotkać wielokrotnie przeglądając krawędzie (O(|E|)) .

    - BFS może posłużyć do znalezienia najkrótszej ścieżki między wierzchołkiem startowym a dowolnym innym końcowym bez uwzględniania ich wagi (czyli niekoniecznie jest to "najtańsza" ścieżka).

    - DFS może posłużyć do wykrywania cykli w grafie.

<!-- https://www.w3schools.com/dsa/dsa_algo_graphs_traversal.php 
Visited w dziwnym miejscu -->



## Algorytm Dijkstry

[(O) Algorytm Dijkstry - Wikipedia](https://pl.wikipedia.org/wiki/Algorytm_Dijkstry)


- Ogólne uwagi
    - Służy do wyznaczania najkrótszych ("najtańszych") ścieżek z określonego źródła do wszystkich wierzchołków (co jest wymagane również do tego, by znaleźć najkrótszą ścieżkę między ustaloną parą wierzchołków).
    - Istotne założenie - **graf nie może zawierać krawędzi o negatywnych wagach** (to założenie jest wykorzystywane w dowodzie poprawności).
    - Przechowując tablicę z poprzednikami jesteśmy w stanie odtworzyć ścieżkę wyznaczoną przez algorytm (od końca idziemy do poprzednika, poprzednika poprzednika itd.).
    - W niektórych implementacjach wykorzystywany jest kopiec binarny jako kolejka priorytetowa (poznamy go później).

- Uwagi do dowodu
    - "...przejście przez jakikolwiek inny wierzchołek spoza *S* [do *u*] dałoby od razu co najmniej tak samo długą ścieżkę" - ponieważ odległość do *u* jest najmniejsza, to jeśli istniałaby ścieżka prowadząca przez *w* spoza *S*, droga do *w* musiałaby być krótsza - sprzeczność z minimalnością *u*.
    - "...do każdego innego dałoby się dojść krócej, nie używając *u*" - jeśli ostatni byłby wierzchołek *w* z *S* różny od *u*, to możemy dojść do niego nie dłuższą ścieżką z pominięciem *u* z punktu 1.

- Złożoność
    - Złożoność czasowa z użyciem tablicy jako kolejki priorytetowej: O(|E|+|V|²) = O(|V|²) (|E|≤|V|²).
    - Złożoność czasowa z użyciem kopca jako kolejki priorytetowej: O((|E|+|V|)log|V|) = O(|E|log|V|) dla grafu spójnego (wtedy |E|≥|V|-1) .
    - Złożoność pamięciowa z użyciem kopca: O(|V|).

[(O - Using a priority queue, Running time - bez ostatniego zdania) Dijkstra's algorithm - Wikipedia](https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm)

[(O) Dijkstra's Algorithm - GFG](https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/)
- Uwagi
    - Możliwe jest (jak w wersji z Wikipedii) zapełnienie kolejki priorytetowej na początku algorytmu.
    - Do kolejki *pq* dodajemy parę (*dist[v]*, *v*) - chcemy za każdym razem pobrać wierzchołek o minimalnym *dist[v]*.


<!-- https://courses.grainger.illinois.edu/cs225/fa2022/resources/dijkstra/ -->
<!-- https://www.w3schools.com/dsa/dsa_algo_graphs_dijkstra.php -->

[(d) Dijkstra's in Disguise - zastosowania algorytmu Dijkstry](https://blog.evjang.com/2018/08/dijkstras.html)




<!--

https://cp-algorithms.com/index.html 

https://courses.grainger.illinois.edu/cs225/fa2022/resources/bfs-dfs/

https://www.w3schools.com/dsa/dsa_algo_graphs_traversal.php
<!-- BFS nie powinien zaznaczać visited od razu - inaczej po zamianie kolejki na stos to nie jest DFS

<!-- BFS znajduje najkrótszą ścieżkę względem długości krawędzi

https://www.w3schools.com/dsa/dsa_algo_graphs_cycledetection.php

https://courses.grainger.illinois.edu/cs225/fa2022/resources/heaps/

https://www.w3schools.com/dsa/dsa_theory_graphs_shortestpath.php

https://www.w3schools.com/dsa/dsa_algo_graphs_dijkstra.php

<!-- Nie działa dla ujemnych wag krawędzi

<!-- Invariant hypothesis: For each visited node v, dist[v] is the shortest distance from source to v, and for each unvisited node u, dist[u] is the shortest distance from source to u when traveling via visited nodes only, or infinity if no such path exists.


<!-- single source, multiple targets - we still have to check all nodes
rewlaxation procedure

https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm (proof, complexity, using a priority queue)
https://web.engr.oregonstate.edu/~glencora/wiki/uploads/dijkstra-proof.pdf

https://www.youtube.com/watch?v=_lHSawdgXpI

-->