# Zasady profilowania kodu

Podczas profilowania kodu ważne jest, aby stosować odpowiednią metodologię, która zapewnia dokładne, wiarygodne i reprezentatywne wyniki. Oto kluczowe zasady, które warto przestrzegać:

## Podstawowe zasady:

### 1. **Analiza statystyczna, a nie jednorazowa**
   - **Uruchamiaj kod wielokrotnie**: Aby uzyskać wiarygodne wyniki, nie polegaj na jednym uruchomieniu. Wykonaj kod wielokrotnie (zwykle kilka-kilknaście razy, w zależności od zadania), aby uwzględnić zmienność czasu wykonania, spowodowaną takimi czynnikami jak pamięć podręczna CPU, operacje wejścia/wyjścia (I/O) i obciążenie systemu.
   - **Faza rozgrzewki**: W wielu przypadkach pierwsze uruchomienia mogą być wolniejsze z powodu ładowania kodu do pamięci lub buforowania. Odrzucenie tych początkowych uruchomień pomoże uniknąć wprowadzających w błąd wyników profilowania.
   - **Analiza statystyczna**: Po wielokrotnych uruchomieniach, oblicz średnią lub medianę czasu wykonania dla każdej próbki, aby uzyskać bardziej reprezentatywne wyniki.
   - **Identyfikacja i usuwanie odstających wyników**: Odstające wyniki mogą znacznie zniekształcić wyniki profilowania. Mogą się one pojawić z powodu procesów w tle, nieoczekiwanego obciążenia systemu lub przejściowych warunków. Na przykład, jeśli jedno z uruchomień trwało znacznie dłużej niż inne (więcej niż 3 odchylenia standardowe od średniej), warto odrzucić to uruchomienie.

### 2. **Dokładny pomiar czasu**
   - **Stosuj precyzyjne timery**: Podczas mierzenia czasu wykonania zawsze używaj timerów o wysokiej rozdzielczości, aby zminimalizować narzut związany z pomiarami. Narzędzia takie jak `time` w Pythonie, `QueryPerformanceCounter` w systemie Windows czy `clock_gettime()` w systemie Linux są odpowiednie do precyzyjnego pomiaru czasu.
   - **Unikaj pomiaru niewłaściwych rzeczy**: Upewnij się, że pomiar czasu obejmuje tylko istotną część kodu, pomijając czas przygotowań lub inne nieistotne narzuty wynikające z samego profilera.

### 3. **Uwzględnienie obciążenia systemu**
   - **Minimalizuj procesy w tle**: Staraj się izolować proces profilowania, minimalizując procesy w tle lub uruchamiając profilowanie na dedykowanej maszynie, aby uniknąć zakłóceń. Zewnętrzne procesy lub obciążenie systemu mogą powodować nieprzewidywalne wahania wydajności.
   - **Kontrola stanu systemu**: Jeśli profilujesz na wspólnym komputerze lub maszynie o zmiennym obciążeniu, upewnij się, że uruchamiasz kod w okresach minimalnego wpływu innych procesów.
   - **Uwzględnienie ustawień zarządzania energią**: Tryby oszczędzania energii, takie jak skalowanie częstotliwości CPU lub stany uśpienia, mogą wpływać na wydajność. Upewnij się, że profilowanie odbywa się w spójnych ustawieniach zasilania w trakcie wszystkich uruchomień.

### 4. **Uwzględnienie rozmiaru danych**
   - **Uwzględnij różne rozmiary danych wejściowych**: Upewnij się, że testujesz kod przy różnych rozmiarach danych wejściowych, ponieważ wydajność może się pogarszać wraz ze wzrostem danych (np. O(n^2) vs. O(log n)). Profilowanie w różnych zakresach danych wejściowych i korzystanie z asymptotycznej złożoności może pomóc przewidzieć zachowanie kodu przy skalowaniu.

## Dodatkowe pomysły:

### 5. **Profilowanie użycia pamięci**
   - **Mierz zużycie pamięci**: Oprócz czasu wykonania warto również profilować zużycie pamięci. Narzędzia takie jak `memory_profiler` lub `tracemalloc` w Pythonie pomagają śledzić alokację pamięci, wycieki i wzrost pamięci w trakcie profilowania.
   - **Zbieranie danych o garbage collection**: Pamiętaj, że garbage collection (GC) może wpłynąć na wydajność, zwłaszcza w językach takich jak Python czy Java. Uruchamiaj kod wielokrotnie, aby pozwolić na stabilizację GC i profiluj bez jego narzutu, uruchamiając go ręcznie, gdy zajdzie taka potrzeba.

### 6. **Korzystanie z narzędzi profilujących**
   - **Biblioteki profilujące**: Korzystaj z uznanych bibliotek i narzędzi profilujących, które mogą dostarczyć szczegółowych informacji o wąskich gardłach, takich jak `cProfile`, `line_profiler` lub `Py-Spy` w Pythonie, lub narzędzia jak `gprof` dla C/C++. Te narzędzia pomagają zidentyfikować najwolniejsze funkcje lub te, które zużywają najwięcej czasu lub pamięci.
   - **Wizualizacja wyników**: Niektóre narzędzia oferują wizualizacje, takie jak wykresy płomieniowe lub wykresy wywołań, które ułatwiają zrozumienie wyników profilowania w bardziej złożonych przypadkach.

### 7. **Profilowanie w różnych środowiskach**
   - **Testuj na różnych konfiguracjach sprzętowych**: Wyniki profilowania mogą się różnić w zależności od CPU, pamięci, dysku twardego i konfiguracji sieci. Jeśli kod ma działać w różnych środowiskach (np. na instancjach chmurowych lub urządzeniach użytkowników), warto go profilować w różnych konfiguracjach.

### 8. **Powtarzaj profilowanie po zmianach**
   - **Weryfikacja po optymalizacjach**: Po wprowadzeniu ulepszeń wydajnościowych lub zmian w kodzie, ponownie uruchom profilowanie, aby sprawdzić, czy optymalizacje rzeczywiście przyniosły poprawę. Ważne jest porównanie wyników przed i po przy użyciu tej samej metodologii.
   - **Benchmarking**: Jeśli to konieczne, przeprowadź "benchmarking" (porównanie wydajności różnych wersji kodu), aby zweryfikować, że jedna wersja jest rzeczywiście szybsza od drugiej.
