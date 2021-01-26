### Zespół projektowy
* Cezary Michalski
* Kacper Jarczak

### Opis projektu
Projekt zakłada stworzenie webowej aplikacji chmurowej umożliwiającej wyświetlenie wykresów ogólnego sentymetu wiadomości serwisu Twitter. 
Zmienność sentymentu w czasie dla wiadomości zawierających określony hashtag zostanie przedstawiona użytkownikowi dzięki rozwiązaniu opracowanemu na platformie Azure.
System tworzony jest na potrzeby firmy EY. [Link do projektu](https://github.com/ekote/AI-on-Microsoft-Azure/blob/main/intro-inz/projects/EY.pdf)
 
### Główne funkcjonalności systemu
* Tworzenie wykresu zmienności średniego sentymentu tweetów z zadanym hashtagiem w zadanym czasie;
* Tworzenie wykresu liczby tweetów pozytywnych, negatywnych oraz neutralnych z zadanym hashtagiem w zadanym czasie;
* Wyświetlenie przykładowych tweetów dla zadanego hashtaga i sentymentu.

### Schemat działania rozwiązania
<p align="center">
  <img src="https://github.com/kjarczak/EY-aspect-based-sentiment-analysis/blob/main/Diagram%20dzialania.png" />
</p>

### Architektura systemu na platformie Azure 
![](https://github.com/kjarczak/EY-aspect-based-sentiment-analysis/blob/main/Diagram%20architektury%20v2.png)

### Stos technologiczny
|||
| --- | --- |
|Języki|Python, HTML, JavaScript|
|Frameworki|Flask, Gunicorn, Bootstrap|
|Narzędzia|PyCharm, Sublime Text, Jupyter Notebook|
|VCS| Git (GitHub)|

### Harmonogram
| Data | Opis |
| --- | --- |
|10.12.2020 | Pełna specyfikacja projektu.|
|21.12.2020 | Działający moduł realizujący przypisanie sentymentu do podanego tekstu.|
|30.12.2020 | Pobieranie i strukturyzacja wiadomości z serwisu Twitter.|
|05.01.2021 | Aplikacja webowa realizująca wyświelnie wykresów.|
|14.01.2021 | Działająca wersja systemu.|
|21.01.2021 | Ostateczna wersja systemu.|
|28.01.2021 | Zarejestrowana prezentacja działającego systemu.|
