
movies = [
    ['Jurassic Park', '1993', 'thriller', 0], 
    ['Szczęki','1978','thriller'], 
    ['Przyjaciele','1994','Serial',0,'8','1']]
    

class Film:
    def __init__(self, tytuł, rok_wydania, gatunek, liczba_odtworzeń):
        self.tytuł = tytuł
        self.rok_wydania = rok_wydania
        self.gatunek = gatunek

        # Variables
        self.liczba_odtworzeń = 0

    def play(self, step = 1):
       self.liczba_odtworzeń += step

    def __str__(self):
        return f'{self.tytuł} {self.rok_wydania} {self.gatunek} {self.liczba_odtworzeń}'

class Serial(Film):
    def __init__(self, numer_odcinka, numer_sezonu, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.numer_odcinka = numer_odcinka
        self.numer_sezonu = numer_sezonu

    def __str__(self):
        txt = super().__str__() 
        return txt + f' {self.numer_odcinka:02} {self.numer_sezonu:02}'


def get_movies():
    #wybierz tylko filmy, alfabetycznie posortuj 
    selected = [x for x in movies if isinstance(x, Film) and not isinstance(x, Serial)]
    #tutaj sortowanie (np z lambdą)
    return selected

def get_series():
    selected = [x for x in movies if isinstance(x, Serial)]
    return selected

def search(tytuł):
    selected = [x for x in movies if x.tytuł == tytuł]
    return selected

def generate_views():
    movie = random.choice(movies)
    i = random.randint(1, 100)
    movie.play(i)
    return movie

def generate_views_10():
    for i in range (10):
        print(generate_views())

def top_titles(content_type = None):
    selected = sorted(movies, lambda x: x.liczba_odtworzeń, reverse=True)
    if content_type == "film":
        selected = sorted(get_movies(), lambda x: x.liczba_odtworzeń, reverse=True)
    elif content_type == "serial":
        selected = sorted(get_series(), lambda x: x.liczba_odtworzeń, reverse=True)

    return selected[:3] #pierwsze 3 elementy     

def content_type():
    selected = get_movies.sorted(movies, lambda x: x.liczba_odtworzeń, reverse=True)