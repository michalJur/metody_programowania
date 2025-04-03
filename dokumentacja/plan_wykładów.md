# Metody programowania - plan wykładów (może ulegać zmianom)

## 1: **Wstęp i podstawowe algorytmy wyszukiwania**

- **Przegląd kursu**
  - Wprowadzenie do zasad kursu i celów nauczania.
  - Opis materiału omawianego w trakcie kursu.

- **Struktury danych**:
   - Tablica

- **Algorytmy (Wyszukiwanie)**:
   - Wyszukiwanie liniowe
   - Wyszukiwanie binarne
   - Wyszukiwanie interpolacyjne
      
- **Wprowadzenie do Pythona**

- **Podstawy profilowania programów**
   - Metodyka pomiaru szybkości działania programu.
   - Porównanie implementacji wyszukiwania: C++, czysty Python, Python + Numpy.
   - Szybkość implementacji (C++ vs Python) a analiza teoretyczna.
   - Komentarze odnośnie wydajności Pythona i jego bibliotek.
   - Praktyczne porównanie złożoności liniowej i logarytmicznej.

## 2: **Analiza algorytmów**

- **Analiza złożoności czasowej i pamięciowej, analiza asymptotyczna**:
   - Notacje Big-O, Big-Ω, Big-Θ (najlepszy, najgorszy i średni przypadek).
   - Wprowadzenie złożonością czasowej i pamięciowej.

- **Algorytmy (Maksymalna podtablica)**
   - Naiwny O(N^3) (brute force)
   - Naiwny O(N^2)
   - Kadane O(N) (dziel i zwyciężaj)

## 3: **Podstawowe algorytmy sortowania**

- **Algorytmy (Sortowanie)**:
   - Sortowanie bąbelkowe
   - Sortowanie przez wybór
   - Sortowanie przez wstawianie
   - Inne algorytmy (np. sortowanie przez zliczanie, sortowanie koszykowe)


## 4: **Listy i drzewa**

- **Struktury danych**:
   - Listy powiązane
     - Pojedynczo lub podwójnie powiązane
     - Z lub bez głowy
   - Drzewa
     - Drzewo wyszukiwania binarnego
     - Drzewo AVL (wprowadzenie)
     - Drzewa czerwono-czarne (wprowadzenie)

- **Algorytmy (Listy i drzewa)**: 
   - Operacje na listach.
   - Operacje na drzewach, w tym przechodzenie drzewa (preorder, inorder, postorder, level-order).


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


## 6: **Programowanie dynamiczne i algorytmy zachłanne**

- **Algorytmy (Zachłanne)**:
 - Problem plecakowy (podstawowe podejście zachłanne; przykład suboptymalnego algorytmu zachłannego z backtrackingiem)
 - Kodowanie Huffmana (przykład optymalnego algorytmu zachłannego; połączenie z entropią, drzewami)

- **Algorytmy (Programowanie dynamiczne)**:
  - Ciąg Fibonacciego (rozwiązanie z memoizacją i tabulacją).
  - Problem plecakowy (dynamiczna wersja problemu plecaka 0/1).

- **Zachłanny vs. Programowanie dynamiczne**
  - Kiedy algorytm zachłanny zawodzi i dlaczego programowanie dynamiczne bywa lepszym wyborem.


## 7: **Algorytmy dziel i zwyciężaj**

- **Algorytmy (Sortowanie)**:
   - Sortowanie przez scalanie (Merge Sort)
   - Sortowanie szybkie (Quick Sort)
   
- **Algorytmy (element k-ty)**:
   - Mediana median


## 8: **Grafy i algorytmy grafowe**

- **Struktury danych**:
   - Grafy
    - Rodzaje (ukierunkowane, nieskierowane, ważone).
    - Reprezentacje (lista sąsiedztwa, macierz).

- **Algorytmy (Wyszukiwanie w grafach)**:
   - Przeszukiwanie w głąb (DFS)
   - Przeszukiwanie wszerz (BFS)
   - Algorytm Dijkstry
   
- **Przykłady zastosowań**

## 9: **Zaawansowane algorytmy grafowe**

- **Algorytmy (Grafy)**:
   - Algorytm Floyda-Warshalla
   - Algorytm Kruskala
   - Algorytm A*

- **Przykłady zastosowań**


## 10: **Kopce i haszowanie**

- **Haszowanie**:
  - Wprowadzenie do tabel haszujących, techniki rozwiązywania kolizji (probowanie liniowe, łańcuchowanie).
  - Zastosowania haszowania w bazach danych i pamięciach podręcznych.

- **Struktury danych**:
   - Kopce

- **Algorytmy (Kopiec)**:
   - Upheap i Downheap
   - Sortowanie przez kopce (Heap Sort)


## 11: **Algorytmy w uczeniu maszynowym**

- **Algorytmy (Uczenie maszynowe)**:
  - K-Średnich (K-Means)
  - K-Najbliżsi sąsiedzi (k-NN)
  - Q-Learning
  - Monte Carlo Tree Search

<!-- Inne:
- **Podstawy teorii złożoności**:
  - Problem P vs NP
  - NP-zupełość (podstawowe wprowadzenie) -->