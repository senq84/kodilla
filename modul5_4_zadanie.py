
import random   
from datetime import date

entry_start = "\n===Biblioteka filmów===\n"

movies=[]

class Film:
    def __init__(self, tytul, rok_wydania, gatunek):
        self.tytul = tytul
        self.rok_wydania = rok_wydania
        self.gatunek = gatunek
        # Variables
        self.liczba_odtworzeń = 0

    def play(self, step = 1):
        self.liczba_odtworzeń += step

    def __str__(self):
        return f'tytul:{self.tytul}, rok:{self.rok_wydania}, gatunek:{self.gatunek}, odtworzen:{self.liczba_odtworzeń} '

    def __repr__(self):
        return f'tytul:{self.tytul}, rok:{self.rok_wydania}, gatunek:{self.gatunek}, odtworzen:{self.liczba_odtworzeń} '

class Serial(Film):
    def __init__(self, numer_sezonu, numer_odcinka, *args, reverse=True, **kwargs):
        super().__init__(*args, **kwargs)
        self.numer_sezonu = numer_sezonu
        self.numer_odcinka = numer_odcinka\
        
    def __str__(self):
        txt = super().__str__()
        return f'sezon:{self.numer_sezonu}, odcinek:{self.numer_odcinka:02} ' + txt

    def __repr__(self):
        txt = super().__repr__()
        return f'sezon:{self.numer_sezonu:02}, odcinek:{self.numer_odcinka:02} ' + txt

def get_movies():
    selected = [x for x in movies if isinstance(x, Film) and not isinstance(x, Serial)]
    selected = sorted(selected, key=lambda x: x.liczba_odtworzeń, reverse=True) 
    print(selected)

def get_series():
    selected = [x for x in movies if isinstance(x, Serial)]
    selected = sorted(selected, key=lambda x: x.liczba_odtworzeń, reverse=True) 
    print(selected)

def search_movie():
    search_movie = input('Szukany tytul filmu albo serialu: ')
    for movie in movies:
        if range(movies[len('tytul')], 'class' == Film) == search_movie:
            print(movie.__repr__)
        elif range(movies[len('tytul')], 'class' == Serial) == search_movie:
            print(movie.__repr__)
        else:
            print('brak szkanego tytulu')

def generate_views():
    movie = random.choice(movies)
    i = random.randint(1, 100)
    movie.play(i)
    return movie

def generate_views_10():
    for i in range (10):
        print(generate_views())
   
def top_titles():
    selected = [x for x in movies if isinstance(x, Film)]
    if movies == Film:
        selected = sorted(get_movies(), lambda x: x.liczba_odtworzeń, reverse=True)
    elif movies == Serial:
        selected = sorted(get_series(), lambda x: x.liczba_odtworzeń, reverse=True)
    print(selected[:3]) #pierwsze 3 elementy    

def top_titles_now():
    print(f'Najpopularniejsze filmy i seriale dnia: {str(date.today())}')

if __name__ == '__main__':
    print(entry_start)

    movies = [
        Film('Jurassic Park', '1993', 'thriller'),
        Film('Terminator','1988','thriller'),
        Film('Superman', '1988', 'action'),
        Film('Batman','1989','action'),
        Film('Rainman', '1974', 'drama'),
        #Serial('Przyjaciele','1994','Serial'),
        #Serial('Przyjaciele','1994','Serial'),
        Serial('8','1', 'Przyjaciele','1994','serial'),
        Serial('8','2','Przyjaciele','1994','serial')
        #Serial('Przyjaciele','1994','Serial','8','3'),
        #Serial('Przyjaciele','1994','Serial','8','4'),
        #Serial('The Simpsons', '1994', 'Serial','1', '1'),
        #Serial('The Simpsons', '1994', 'Serial','1', '2'),
        #Serial('The Simpsons', '1994', 'Serial','1', '3'),
        #Serial('The Simpsons', '1994', 'Serial','1', '4')
        ]    

    for movie in movies:
        print(movie)
        
    generate_views()
    print()
    get_movies()
    print()
    get_series()
    print()
    generate_views() 
    print()
    generate_views_10()
    print()
    top_titles_now()
    print()
    top_titles()
    print()
    search_movie()