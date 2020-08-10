class Painting:
    museum = "Louvre"

    def __init__(self, title, artist, year):
        self.title = title
        self.artis = artist
        self.year = year

    def __repr__(self):
        return f'"{self.title}" by {self.artis} ({self.year}) hangs in the {Painting.museum}.'


print(Painting(input(), input(), int(input())))
