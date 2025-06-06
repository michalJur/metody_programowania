# Wykład 10


## Algorytm Bellmana-Forda
[(O) Algorytm Bellmana-Forda - Wikipedia](https://pl.wikipedia.org/wiki/Algorytm_Bellmana-Forda)
- Ogólne uwagi
    - Służy do wyznaczania najkrótszych ścieżek z określonego źródła do wszystkich wierzchołków.
    - W przeciwieństwie do algorytmu Dijkstry, dopuszczamy ujemne wagi krawędzi (co przekłada się na wyższą złożoność).
    - Istotne założenie - **w grafie nie istnieją cykle o ujemnej wadze osiągalne ze źródła**.
    - W k-tym kroku "wykryjemy" wszystkie ścieżki o długości k (indukcja).
    - Istnieje możliwość usprawnienia przez 'early exit' w przypadku braku zmian w iteracji.
    - Jest przykładem programowania dynamicznego.

- Uwagi co do nieujemnych cykli
    - Algorytm może posłużyć do weryfikacji założenia.
    - W tym celu należy wykonać dodatkową iterację algorytmu i sprawdzić czy koszt się zmniejszył (jeśli tak, to istnieje cykl o powyższym opisie).
    - Wyjaśnienie czemu tylko jedna dodatkowa iteracja jest wymagana na przykładzie: s->...->1->2->-3, i 1, 2, 3 tworzą negatywny cykl - po kolejnej iteracji dostajemy s->...->1->2->3->2 do 2 dojdziemy zmniejszając koszt.

- Złożoność
    - Złożoność czasowa O(|V||E|) (więc dla gęstych grafów O(|V|³))
    - Złożoność pamięciowa O(|V|)

<!-- [(O) Bellman-Ford Algorithm - Wikipedia](https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm)
- Proof
- Pierwszy akapit Improvements (early exit) -->

[(O) Bellman–Ford Algorithm - GFG](https://www.geeksforgeeks.org/bellman-ford-algorithm-dp-23/)

<!-- https://www.w3schools.com/dsa/dsa_algo_graphs_bellmanford.php -->
<!-- https://www.geeksforgeeks.org/detect-negative-cycle-graph-bellman-ford/ -->


## Algorytm Floyda-Warshalla

[(O) Algorytm Floyda-Warshalla - Wikipedia](https://pl.wikipedia.org/wiki/Algorytm_Floyda-Warshalla)
- Uwagi
    - Służy do wyznaczania najkrótszych ścieżek pomiędzy dowolną parą wierzchołków (można uznać go za uogólnienie algorytmu Bellmana-Forda).
    - Analogicznie jak w algorytmie Bellmana-Forda, zakładamy że w grafie nie istnieją cykle o ujemnej wadze.
    - Jeśli po zakończeniu algorytmu na przekątnej pojawi się ujemna wartość (zamiast zera), to w grafie istnieje cykl o ujemnej wadze.

- Złożoność
    - Złożoność czasowa O(|V|³)
    - Złożoność pamięciowa O(|V|²)

- Szkic dowodu poprawności (za wykładem dr Roska)
```
Dane: G=(V, E), w - wagi krawędzi, V={1,...,n}
Szukane: d[i, j], i, j = 1, ..., n
Przez d⁽ᵏ⁾[i, j] będziemy oznaczać długość najkrótszej ścieżki z wierzchołka i do j, w której jako pośrednie mogą występować tylko wierzchołki {1, ..., k}.
W efekcie d⁽⁰⁾[i, j] = w[i, j],  (pojedyncze krawędzie, bez wierzchołków pośrednich).

              d⁽ᵏ⁻¹⁾[i, j]
   (i) -------------------------> (j)
    |                              ^
    | d⁽ᵏ⁻¹⁾[i, k]     d⁽ᵏ⁻¹⁾[k, j] |
    -------------> (k) -------------

Dla k>0 mamy: 
d⁽ᵏ⁾[i, j] = min(d⁽ᵏ⁻¹⁾[i, j], d⁽ᵏ⁻¹⁾[i, k] + d⁽ᵏ⁻¹⁾[k, j])
Wynika to z faktu, że najkrótsza ścieżka z i do j z ograniczeniem do pośrednich wierzchołków {1, ..., k}:
- albo nie zawiera wierzchołka k (wtedy jest równa d⁽ᵏ⁻¹⁾[i, j]),
- albo zawiera wierzchołek k, ale wtedy składa się z odcinka od i do k z pośrednimi wierzchołkami w zbiorze {1,...,k-1} oraz odcinka od k do j z pośrednimi wierzchołkami w zbiorze {1,...,k-1}.

Algorytm w k-tym kroku rozważa ścieżki d⁽ᵏ⁾[i, j], a przechodząc z k do n uzyskujemy najkrótsze ścieżki z uwzględnieniem wszystkich wierzchołków.
```

[(O) Floyd-Warshall Algorithm - GFG](https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/)

<!-- https://en.wikipedia.org/wiki/Floyd%E2%80%93Warshall_algorithm
- Algorithm -->

<!-- https://claude.ai/chat/935b9fb8-ed4b-4de2-858a-a78106aa5add -->


## Minimalne drzewo rozpinające

[(O) What is Minimum Spanning Tree - GFG](https://www.geeksforgeeks.org/what-is-minimum-spanning-tree-mst/)


<!-- 
## Algorytm Kruskala
https://pl.wikipedia.org/wiki/Algorytm_Kruskala

https://www.geeksforgeeks.org/kruskals-minimum-spanning-tree-algorithm-greedy-algo-2/
- bez struktury zbiorów rozłącznych (będzie później (?))
- opis złożoności z błędem (The find and union operations can take at most O(logV) time) - patrz Wikipedia. 

https://en.wikipedia.org/wiki/Kruskal%27s_algorithm
- Proof of correctness


Złożoność czasowa: O(|E|log|V|)
 -->

