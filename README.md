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
  <img src="https://github.com/kjarczak/EY-aspect-based-sentiment-analysis/blob/main/Diagram%20dzialania%20v2.png" />
</p>

### Architektura systemu na platformie Azure 
![](https://github.com/kjarczak/EY-aspect-based-sentiment-analysis/blob/main/Diagram%20architektury%20v2.png)

### Opis wykorzystanych elementów
Azure ML i zawarte w nim narzędzie Designer pozwala na proste i szybkie tworzenie pipeline'ów ukazujących przepływ sterowania i przepływ danych pomiędzy kolejnymi krokami algorytmu. Udostępnia on też możliwość tworzenia endpointów w czasie rzeczywistym, odbierających dane od użytkowników i zwracających wyniki obliczeń, dzięki którym możliwa jest integracja z aplikacją webową. Łatwo można też w nim skorzystać z własnych zestawów danych, które wystarczy umieścić jako dataset.
![Więcej informacji tutaj.](https://azure.microsoft.com/en-us/services/machine-learning/)

App Service to platforma do tworzenia i wdrażania aplikacji internetowych. Pozawala m.in. na wdrażanie rozwiązań bezpośrednio z lokalnego repozytorium, co w kontekście testów oraz pracy projektowej jest bardzo wygodne. 
![Więcej informacji tutaj.](https://azure.microsoft.com/en-us/services/app-service/)

### Stos technologiczny
|||
| --- | --- |
|Języki|Python, HTML, JavaScript|
|Frameworki|Flask, Gunicorn, Bootstrap|
|Narzędzia|PyCharm, Sublime Text, Jupyter Notebook|
|VCS| Git (GitHub)|

### Opis reprodukcji rozwiązania
1. Stworzyć **Managment Group** agregujące subskrycje, które mają zostać wykorzystać.
1. Pod subskrypcją stworzyć **Resource Group** zawierające **Azure Machine Learning** oraz **App Service** lub rozdzielić je na dwie **Resource Group** podpięte do różnych subskrypcji, tak, by podzielić koszta użytkowania na te subskrypcje.
1. Przejść do **AzureML Studio**, gdzie można przystąpić do tworzenie rozwiązania:
 1. Posiłkując się repozytorium projektu stworzyć strukturę odpowiadającą tej z filmu prezentującego rozwiązanie.
	1. Kod należy zmodyfikować do swoich potrzeb, czy też możliwości.
	1. Stworzyć **Compute Cluster**, który należy podpiąć do pipeline\`a.
	1. Stworzyć **Interference Cluster**, który jest wymagany do wystawienia endpoinu.
	1. Jakość klastrów nalerzy dobrać do własnych możliwości oraz potrzeb.
	1. Przesłać pipeline za pomocą przycisku **Submit**, tak by został przetestowany oraz mógł zostać wdrożony.
	1. Wdrożyć pipeline.
1. Wdrożyć aplikację do **App Service** (np. z lokalnego repozytorium git), ustawiając wcześniej credentiale do endpointu z pipeline\`a. 

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
