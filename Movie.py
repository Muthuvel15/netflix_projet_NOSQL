class Movie:
    def __init__(self, _id, show_id, type, title, director, country, date_added, release_year, rating, duration, listed_in, description):
        self._id = _id
        self.show_id = show_id
        self.type = type
        self.title = title
        self.director = director
        self.country = country
        self.date_added = date_added
        self.release_year = release_year
        self.rating = rating
        self.duration = duration
        self.listed_in = listed_in
        self.description = description