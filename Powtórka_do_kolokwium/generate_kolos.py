import json

cells = []

def add_md(text):
    cells.append({
        "cell_type": "markdown",
        "metadata": {},
        "source": [line + "\n" for line in text.strip().split("\n")]
    })

def add_code(text):
    cells.append({
        "cell_type": "code",
        "execution_count": None,
        "metadata": {},
        "outputs": [],
        "source": [line + "\n" for line in text.strip().split("\n")]
    })

add_md("""# Intensywny Kurs Programowania w języku Python przygotowujący do kolokwium
Ten notatnik to kompleksowy przewodnik po strukturach danych, wycinaniu, iterowaniu i "python-way". Zawiera teorię oraz około 35 zadań sprawdzających Twoją wiedzę techniczną i algorytmiczną.
Zadania zostały tak dobrane, by przypominały te z ubiegłorocznych kolokwiów z Programowania 1 R. Zakres:
1. Praca ze strukturami (Listy `[]`, Krotki `()`, Słowniki `{}`)
2. Wycinanie list i krotek (Slicing `[x:y:z]`)
3. `List comprehension` i `Dict comprehension`
4. Programowanie funkcyjne: `lambda`, `map`, `filter`
5. Referencje i zaawansowane indeksowanie (w tym rozpakowywanie zmiennych)

Pamiętaj! Analizujemy, wymyślamy w głowie, a potem sprawdzamy kodem.""")

add_md("""## 1. Wycinanie, czyli Slicing `[start:stop:krok]`
Wycinanie (slicing) działa na obiektach sekwencyjnych (napisach, listach, krotkach).
Składnia: `sekwencja[start : stop : krok]`. Można pominąć jakikolwiek z parametrów: domyślny `start` to 0, `stop` to koniec, `krok` to 1.
Jeśli podamy ujemny indeks, liczymy od końca (-1 to ostatni element).
Jeśli podamy ujemny krok, idziemy od tyłu! Wtedy `start` domyślnie oznacza "od końca", a `stop` - "do początku".

Przykłady:
- `t[1:]` - od indeksu 1 do końca
- `t[:5]` - od początku do indeksu 4 włącznie (element z indeksem 5 NIE JEST brany! jest to wyłączne przedział domknięto-otwarty [start, stop) )
- `t[::2]` - weź co drugi element
- `t[::-1]` - weź wszystko, ale tyłem""")

add_code("""t = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

print("Podstawy wycinania:")
print(f"t[2:5]   = {t[2:5]}")   # [2, 3, 4]
print(f"t[:3]    = {t[:3]}")    # [0, 1, 2]
print(f"t[::3]   = {t[::3]}")   # [0, 3, 6, 9]
print(f"t[::-1]  = {t[::-1]}")  # [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]""")

for i in range(1, 6):
    add_md(f"### Zadanie {i}\nZapisz odpowiednie instrukcje dla listy `L` aby uzyskać pożądany efekt podany w komentarzu. Zrób to BEZ wypisywania ręcznie elementów (użyj wycinania).")
    task_code = [
        "L = [10, 20, 30, 40, 50, 60, 70, 80]\n# Wydziel fragment listy: [30, 40, 50, 60]\nwynik = L[...]\nprint(wynik)",
        "L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]\n# Wydziel elementy na parzystych indeksach, ale pomiń 0 (zacznij od indeksu 2, od elementów typu 2, 4, 6...)\nwynik = L[...]\nprint(wynik)",
        "L = ['k', 'o', 'l', 'o', 'k', 'w', 'i', 'u', 'm']\n# Jak wyciągnąć słowo 'owum' idąc od tyłu z odpowiednim krokiem? Kombinuj ujemnymi indeksami!\n# Ma wyniknąć: ['m', 'u', 'i', 'w', 'k', 'o', 'l', 'o', 'k'] i potem z niego co drugi? A może po prostu krok = -2?\nwynik = L[...]\nprint(wynik)",
        "L = list(range(15))\n# Wydziel wszystkie elementy, ALE nie te pierwsze 3 i ostatnie 3. [czyli odindeksu 3 do (n-3)]\nwynik = L[...]\nprint(wynik)",
        "L = [x for x in range(20)]\n# Odwróć listę L, następnie wyciągnij co 3 element. Jak zapisać to w 1 klamrach []?\nwynik = L[...]\nprint(wynik)"
    ]
    add_code(task_code[i-1])

add_md("""## 2. Różnice: Krotka (), Lista [], Słownik {}

- **Listy `[]`:** Zmienne (mutowalne). Możesz ich długość powiększać (`append`, `extend`), nadpisywać indeksy `A[0] = 5`.
- **Krotki `()`:** Niezmienne (niemutowalne). Zastosowanie: do ochrony danych (zabezpiecza przed nadpisaniem), pakowanie/rozpakowywanie zmiennych (`x, y = 5, 3`). Przez to, że są niemutowalne, KROTKI PIONĄ BYĆ KLUCZAMI SŁOWNIKÓW, A LISTY NIE!
- **Słowniki `{key: value}`:** Kolekcje, które nie grupują na bazie indeksu od 0, ale od DOWOLNEGO klucza niemutowalnego. Dostęp robisz po kluczu: `slownik["Polska"] = "Warszawa"`.
- **Zbiory `{set}`**: Podobne do słowników nawiasy klamrowe, ale jest `{1, 2, 3}` bez `:`. Są szybkie i wymuszają UNIKALNOŚĆ - brak powtórzeń! Nie można używać na nich indeksowania `Z[0]`.

Zwróć uwagę na kruczki referencyjne!
Przypisanie w pythonie `lista2 = lista1` **NIE kopiuje** wartości. Zmieniając `lista2` modyfikujesz `lista1`. Kopiować trzeba przez `.copy()` lub wycięcie `lista1[:]`.""")

for i in range(6, 12):
    add_md(f"### Zadanie {i}\nSprawdźmy jak czujesz struktury danych.")
    task_code = [
        "# Spróbuj poprawić ten kod i stworzyć słownik, w którym krotka będzie kluczem (np. krotka ze współrzędnymi [x, y]).\n# kluczem nie moze byc lista.\nd = {}\nmoja_zmienna = [1, 2]\n# d[moja_zmienna] = 'Punkt A'  # To zwróci błąd TypeError! Zmień `moja_zmienna` tak aby działało.",
        "# Jak stworzysz pustą listę, pustą krotkę, pusty słownik oraz pusty zbiór (set)?\n# Oraz jak usunąć powtórzenia z poniższej listy?\nL = [1, 1, 2, 2, 3, 3, 4, 4, 4, 4]\nwynik = ... # Zmień na Set i wróć do listy",
        "# Podchwytliwe: Jaki bedzie finalny print? Pomysl i odpal, by zweryfikować.\na = ['A', 'B']\nb = a\nc = a.copy()\nb.append('C')\nc.append('D')\nprint(f'a: {a}\\nb: {b}\\nc: {c}')",
        "# Masz liste studentow zapakowana w krotki (imie, wiek).\n# Co przypiszesz zmiennym X i Y podczas iteracji?\nstudenci = [('Jan', 20), ('Anna', 21)]\nfor ... in studenci:\n    print(f'student ma imie', ... , 'oraz wiek', ...)",
        "# Dwa powszechne błędy. Odkomentuj każdą linie, by zobaczyć błąd i ZAMIEŃ go na kod bezbłędny by kod sie po prostu wykonal.\nkrotka = (10, 20, 30)\n# krotka[1] = 50   # O co tu chodzi?\n\nslownik = {'a': 1, 'b': 2}\n# print(slownik[0]) # Słowniki odpytujemy kluczami, nie liczbowym indeksem!",
        "# Swap dwóch zmiennych w jednej linii. Jak to zrobić z wykorzystaniem tzw. rozpakowywania krotek?\nx = 100\ny = 200\n... = ...  # ZAMIEŃ MIEJSCAMI X i Y\nprint('x:', x, 'y:', y)"
    ]
    add_code(task_code[i-6])

add_md("""## 3. List / Dict Comprehensions (Wyrażenia listowe)
Zamiast budować listę klasycznie:
```python
l = []
for i in range(10):
    if i % 2 == 0: l.append(i**2)
```
Można to zwinąć do jednego wyrażenia:
`L = [i**2 for i in range(10) if i % 2 == 0]`

Działa tak samo w słownikach! `{klucz: wartosc for element in kolekcja if warunek}`
Na kolokwiach pojawia się to na 100%. Wymagają myślenia w 'jednej linii' (tzw. one-liners).""")

for i in range(12, 19):
    add_md(f"### Zadanie {i}\nZaimplementuj list i dict comprehensions, unikając standardowych pętli i ifów.")
    task_code = [
        "# Stwórz listę liczb od 1 do 30, ale tylko takich, które są podzielne przez 3.\nwynik = ...\nprint(wynik)",
        "# Mając zadaną N, wygeneruj listę WSZYSTKICH jej dzielników (z 1 i samą sobą).\nN = 24\ndzielniki = ...\nprint(dzielniki)",
        "# Z danej listy ciągów tekstowych wygeneruj słownik. Kluczem ma być to słowo, a wartością - długość tego słowa w znakach\nslowa = ['python', 'nauka', 'kolokwium', 'bum']\n# powinnismy uzyskac -> {'python': 6, 'nauka': 5, itp}\nslownik_len = ...\nprint(slownik_len)",
        "# Utworz slownik, w ktorym kluczem sa cyfry (0-9), a wartoscia ciag tekstowy '-' o danej dlugosci,\n# czyli 2: '--', a 5: '-----'\nwynik = ...\nprint(wynik)",
        "# Stwórz listę kwadratów liczb parzystych mniejszych niż 20, do czego wykorzystasz 'range'.\nwynik = ...\nprint(wynik)",
        "# Zamiana kluczy z wartosciami. Dany jest slownik {klucz: wartosc}. Chcemy miec {wartosc: klucz}.\nd1 = {'a': 1, 'b': 2, 'c': 3}\nwynik = ...\nprint(wynik)",
        "# Trudniejsze z wieloma warunkami: Stwórz listę znaków ze słowa 'PROGRAMOWANIE' ale pomin samogłoski (A, E, I, O, U).\n# Zbuduj comprehension!\nslowo = 'PROGRAMOWANIE'\nsamogloski = 'AEIOUY'\nspolgloski = ...\nprint(spolgloski)"
    ]
    add_code(task_code[i-12])

add_md("""## 4. Lambda, map i filter

- **Lambda `lambda x: x+1`**: skrócone, jednorazowe, anonimowe funkcje. Pomijamy słowo kluczowe `def` i `return`. Świetnie nadają się przy podawaniu jako klucz sortujący `sort(key=...)`.
- **Map `map(funkcja, lista)`**: nakłada `funkcję` na każdy element z `lista`. Zwraca tzw. generator - najcześciej by go użyć musisz zapakować go z powrotem w klamrę `list(...)`.
- **Filter `filter(funkcja, lista)`**: Nakłada i wywołuje `funkcję` na elemencie `lista`. Jeśli da radę przepuścić go (funkcja zwróci True) - element "zostaje". Zwraca generator.

Przykład map + lambda: `list(map(lambda x: x*2, [1, 2, 3]))` -> `[2, 4, 6]`""")

for i in range(19, 25):
    add_md(f"### Zadanie {i}")
    task_code = [
        "# Masz funkcję typu map. Sprowadź elementy na wielkie litery przy pomocy zwykłego map() oraz lambdy.\nslowa = ['jeden', 'dwa', 'trzy']\nwynik = list(map(..., slowa))\nprint(wynik)",
        "# Masz listę wartości float. Używając funkcji filter(), wyrzuć stąd powtarzające lub ujemne tak, by zostały same dodanie wartości!\nwartosci = [-2.5, 4.0, 9.9, -15.2, 0.0, 2.5]\n# funkcja 'czy cos jest dodatnie' to lambda x: x > 0.0\nwynik = list(filter(..., wartosci))\nprint(wynik)",
        "# Posortuj podaną listę wyrazów w taki sposób, by krótsze stały pierwsze.\n# W func. L.sort() znajduje się argument key. Użyj tam len, albo lambdy wywołującej len!\nslowa = ['drzewo', 'krzew', 'ulica', 'kot', 'czwartek']\nslowa.sort(...)\nprint(slowa)",
        "# Z załączonego kolokwium: Przypiszmy listom posortowanie według porządku ROSNĄCEJ LICZBY LITER. Jak zrobisz to, ale dla drugiego elementu krotek zagnieżdżonych?\ndane = [(1, 'ala'), (2, 'dlugieslowo'), (3, 'kot')]\n# Tutaj potrzebna bedzie specjalna lambdy: lambda element: element[...]\ndane.sort(key=...)\nprint(dane)",
        "# Przewidź co się wydarzy!\nnumpy_like = list(map(lambda x: x*3, filter(lambda y: y%2==0, [0, 1, 2, 3, 4, 5])))\nprint(numpy_like)",
        "# Z kolokwium! Wypisz to, co zostało wypisane poniżej, ale najpierw pomyśl!\nlistA = list(filter(lambda x: (x%2 != 0), [c//2 for c in range(10)]))\nlistB = list(map(lambda x: x * 2, listA))\nprint(listB)"
    ]
    add_code(task_code[i-19])

add_md("""## 5. Zadania Otwierające Umysł i Zrozumieniowe
Zastanów się nad tym, co się wydarzy, zrozum logikę Pythona przy tych wredniejszych kawałkach kodu i stwórz mechanikę z głowy (której uczą zadania wybuchowe na Kolosach).""")

for i in range(25, 36):
    add_md(f"### Zadanie {i}")
    task_code = [
        "# Z kolokwium: Co wyrzuci ten kod? Najpierw wytlumacz, pozniej pusc (print pokaze odpowiedz docelowo jako krotke list).\nt = [n for n in range(6)]\n# print(t[4:])\n# print(t[0:4:2])\n# print(t[4:0:-1])\n",
        "# Z kolosa: Przypisz do zmiennej P slownik, w ktorym klucze sa liczbami podzielnymi przez 3, mniejszymi od 12,\n# zas wartosciami lancuchami 'a' pomnozonymi tyle razy ile wynosi wielkosc klucza (np. {'a' * 3})\nP = ...\nprint(P)",
        "# Z kolosa: Znajdz blad w ponizszym kodzie! Sum zwraca blad typu (TypeError) dla podanego wyrażenia:\ndata = [{'id': 20, 'd': 'x'}, {'id': 33, 'd': 'y'}]\nf = lambda x: x['id']\n# Bledny kod l = [f for f in data]\n# Popraw to poniżej - co powinno wywołanie dodawać? funkcję f do listy, czy WYNIK funkcyji f od x z listy?\nl = ...\nprint(sum(l))",
        "def tajemnica(n):\n    # zwrcaca mnozenie dwoch petli ale tylko tam gdzie suma i + j sie bez problemu dzieli na dwa.\n    return [i*j for i in range(1,n) for j in range(i,n) if (i+j)%2 == 0]\nprint(tajemnica(4)) # Rozpisz sobie jak i iteruje j dla kazdego i=1, 2, 3.",
        "# Dana jest zmienna: s = 'ALABAMA'. Zrob unikalne podliczenie - stworz slownik ile razy kazda litera wystapila w slowie!\ns = 'ALABAMA'\n# podpowiedz: litery w danym wyrazie, do tego funkcja s.count() \nwynik = ...\nprint(wynik)",
        "slownik1 = {'a': 1, 'b': 2}\nslownik2 = {'b': 3, 'c': 4}\n# Chcemy połączyć słowniki... w pythonie 3.9+ mozna slownik1 | slownik2, ale mozna tez je rozpakowac uzywajac operatora **(dwie gwiazdki)\n# wynik_zlaczenia = {**slownik1, **slownik2}\nwynik_zlaczenia = ...\nprint(wynik_zlaczenia)",
        "# Dlaczego w Pythonie należy unikać funkcji, która ma listy jako parametry domyślne np 'def foo(li=[])'?\n# Wytłumacz sobie działanie poniższego na podstawie wyników\ndef foo(v, lis=[]):\n    lis.append(v)\n    return lis\nprint(foo(1))\nprint(foo(2))",
        "# Jeśli masz listę 3wymiarową (krotki x i y), jak ją wpłaszczyć do tablicy jednowymiarowej?\npunkty = [(1,2), (3,4), (5,6)]\nplaska_lista = ...\nprint(plaska_lista)",
        "# Operator splat (*). Jak ze stringu 'PYTHON' dac zmiennej c resztę jako listę po rozdzieleniu?\na, b, *c = 'PYTHON'\nprint('a:', a)\nprint('b:', b)\nprint('c:', c)",
        "# Na kolosie w R i Pythonie musimy w pelni zdawac sobie sprawe jakie typy wyrzuca funkcja.\n# int(), str(), tuple(), set()... stwórz taką zbitkę dla N (liczby) np N=5, by wypisało: `(1, 2, 3, 4, 5)` jako KROTKĘ.\nN = 5\nwynik = ...\nprint(type(wynik))",
        "print('Koniec! Jesli przeszedles rzetelnie - podstawy nie maja przed toba tajemnic.\\nWypij ciepla kawe i odpocznij by jutro isc z podniesiona glowa!')"
    ]
    add_code(task_code[i-25])

notebook = {
    "cells": cells,
    "metadata": {"kernelspec": {"display_name": "Python 3", "language": "python", "name": "python3"}},
    "nbformat": 4,
    "nbformat_minor": 4
}

with open(r'c:\\Users\\marci\\Moje Pliki\\Szkoła\\Uniwersytet Warszawski\\Programowanie I R\\nauka_kolokwium.ipynb', 'w', encoding='utf-8') as f:
    json.dump(notebook, f, ensure_ascii=False, indent=2)
