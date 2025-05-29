# Wykład 9 [WIP]

## Grafy - definicje
https://eduinf.waw.pl/inf/alg/001_search/0123.php

## Reprezentacja grafów
https://www.geeksforgeeks.org/graph-and-its-representations/

<!--(https://www.w3schools.com/dsa/dsa_theory_graphs.php) -->
<!-- https://www.w3schools.com/dsa/dsa_data_graphs_implementation.php -->


## DFS / BFS

https://www.geeksforgeeks.org/breadth-first-search-or-bfs-for-a-graph/
https://www.geeksforgeeks.org/depth-first-search-or-dfs-for-a-graph/
https://www.geeksforgeeks.org/iterative-depth-first-traversal/

- Wersje iteracyjne nieco od siebie odbiegają, ale można je tak upodobnić, że jedyna różnica to klejka vs stos

https://courses.grainger.illinois.edu/cs225/fa2022/resources/bfs-dfs/
- Obowiązuje nas pseudokod tu zaprezentowany
- Animacje zdają się nieprawidłowo prezentować kolejność działań 
- Najbardziej intuicyjna implementacja - węzeł zaznaczamy jako odwiedzony cdy go przetwarzamy (dodajemy do kolejki)

Złożoność czasowa: O(V + E)
Złożoność pamięciowa: O(V) (rekurencyjny DFS: O(V+E))

- Kolejka i stos wyzbnaczają kolejność przetwarzania węzłów, a co za tym idzie zachowanie algorytmu
- W opisach czasem podawane jest, że sprawdzamy każdą krawędź tylko raz - w grafie nieskierowanym sprawdzamy je dwukrotnie, z jednego i drugiego wierzchołka (nie zmienia to złożoności)
- Każdy wierzchołek przetwarzamy raz (O(V)), ale możemy go napotkać wielokrotnie przeglądając krawędzie (co zliczamy właśnie jako O(E)) 

- BFS może posłużyć do znalezinia najkrótszej ścieżki (w liczbie krawędzi) między wierzchołkiem startowym,a dowolnym innym końcowym - zliczając krawędzie, ale nei uwzględniając ich wagi (czyli niekoniecznie jest to "najtańsza" ścieżka)

- DFS może posłużyć do wykrywania cykli w grafie <!--  -->

<!-- https://www.w3schools.com/dsa/dsa_algo_graphs_traversal.php 
Visited w dziwnym miejscu -->



## Algorytm Dijkstry

https://pl.wikipedia.org/wiki/Algorytm_Dijkstry

- Istotne założenie - graf nie może zawierać  krawędzi o negatywnych wagach (to założenie jest wykorzystywane w dowodzie poprawności)
- Przchowując tablicę z poprzednikami jesteśmy w stanie odtworzyć ścieżkę wyznaczoną przez algorytm (idąc do poprzednika, poprzednika poprzednika itd.)

- "przejście przez jakikolwiek inny wierzchołek spoza S [do u] dałoby od razu co najmniej tak samo długą ścieżkę" - ponieważu ma najniższą odległość, to jeśli istniałaby ścieżka powadząca przez w spoza S, droga do w musiałaby być krótsza - sprzeczność z minimalnością u

- "do każdego innego dałoby się dojść krócej, nie używając u" - jeśli ostatni byłby wierzchołek w z S różny od u, to możemy dojść do niego nie dłuższą ścieżką z pominięciem u z punktu 1.

- Złośonośc czasowa z użyciem tablicy jako kolejki priorytetowej: O(|E|+|V|^2) = O(|V|^2) (|E|≤|V|^2)
- Złośonośc czasowa z użyciem kopca jako kolejki priorytetowej: O((|E|+|V|)log|V|) = O(|E|log|V|) dla grafu spójnego (wtedy |E|≥|V|-1) 
- Złożoność pamięciowa z użyciem kopca: O(|V|)


https://en.wikipedia.org/wiki/Dijkstra%27s_algorithm

- Using a priority queue
- (Proof)
- Running time (bez ostatniej uwagi)

https://www.geeksforgeeks.org/dijkstras-shortest-path-algorithm-greedy-algo-7/
Wykorzystujemy kolejkę priorytetową - poznamy ją później
- możliwe jest jak w wersji z Wikipedii zapełnienie kolejki priorytetowej na początku algorytmu
- pierwsza pozycja w kolejce pq oznaczająca dist[v] służy do określenia priorytetu (chcemy za każdym razem pobrać wierzchołek o minimalnym dist[v])


<!-- https://courses.grainger.illinois.edu/cs225/fa2022/resources/dijkstra/ -->
<!-- https://www.w3schools.com/dsa/dsa_algo_graphs_dijkstra.php -->

Zastosowania algorytmu Dijkstry
https://blog.evjang.com/2018/08/dijkstras.html




<!--

https://cp-algorithms.com/index.html 

https://courses.grainger.illinois.edu/cs225/fa2022/resources/bfs-dfs/

https://www.w3schools.com/dsa/dsa_algo_graphs_traversal.php
<!-- BFS nie powinien zaznaczać visited od razu - inaczej po zaminaie kolejki na stos to nie jest DFS

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