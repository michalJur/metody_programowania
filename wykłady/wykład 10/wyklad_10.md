# Wykład 10 [WIP]


## Algorytmn Bellmana-Forda
https://pl.wikipedia.org/wiki/Algorytm_Bellmana-Forda
- Złożoność czasowa O(|V||E|) ()= O(|V|^3) dla gęstych grafów
- Złożoność pamięciowa O(|V|)
- Kluczowe założenie - nie istnieją cykle o ujemnej wadze osiągalne ze źródła
- W k-tym kroku "wykryjemy" wszystkie ścieżki o długości k - indukcja.
- Możliwość usprawnienia - 'early exit' w przypadku brajku zmian w iteracji
- Sprawdzenie poprawności założenia - wykonanie dodatkowej iteracji algorytmu i sprawdzenie czy koszt się zmniejszył (jeśli tak, to istnieje cykl o powyższym opisie). Wyjaśnienie czemu tylko jedna dodatkowa iteracja jest wymagana - przykład: s->...->1->2->-3, i 1, 2, 3 tworzą negatywny cykl - po kolejnej iteracji dostajemy s->...->1->2->3->2 do 2 dojdziemy zmniejszając koszt.

https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm
- Proof
- Pierwszy akapit Improvements (early exit)

https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/


<!-- https://www.w3schools.com/dsa/dsa_algo_graphs_bellmanford.php -->
<!-- https://www.geeksforgeeks.org/detect-negative-cycle-graph-bellman-ford/ -->


## Algorytm Floyda-Warshalla
https://pl.wikipedia.org/wiki/Algorytm_Floyda-Warshalla
- Złożoność czasowa O(|V|^3)
- Złożoność pamięciowa O(|V|^2)

https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/

https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm
- Algorithm

<!-- https://claude.ai/chat/935b9fb8-ed4b-4de2-858a-a78106aa5add -->


## Minimalne drzewo rozpinające
https://www.geeksforgeeks.org/what-is-minimum-spanning-tree-mst/


## Algorytm Kruskala
https://pl.wikipedia.org/wiki/Algorytm_Kruskala

https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
- bez struktury zbiorów rozłącznych (będzie później (?))
- opis złożoności z błędem (The find and union operations can take at most O(logV) time) - patrz Wikipedia. 

https://en.wikipedia.org/wiki/Kruskal%27s_algorithm
- Proof of correctness


Złożoność czasowa: O(|E|log|V|)
<!-- Kruskal -->


