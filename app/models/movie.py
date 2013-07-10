class Movie():
    """Model of a movie."""

    def __init__(self, **kwargs):
        self.data = kwargs

        self.imdb_id = self.data.get('tconst')
        self.title = self.data.get('title')
        self.type = self.data.get('type')
        self.year = int(self.data.get('year'))
        self.tagline = self.data.get('tagline')
        self.plot = self.data.get('plot')
        self.runtime = self.data.get('runtime')
        self.rating = self.data.get('rating')
        self.genres = self.data.get('genres')
        self.votes = self.data.get('num_votes')

        self.plot_outline = None
        if 'plot' in self.data and 'outline' in self.data['plot']:
            self.plot_outline = self.data['plot']['outline']

        self.runtime = None
        if 'runtime' in self.data:
            #mins
            self.runtime = str(int((self.data['runtime']['time'] / 60)))

        self.poster_url = None
        if 'image' in self.data and 'url' in self.data['image']:
            self.poster_url = self.data['image']['url']

        self.cover_url = None
        if 'image' in self.data and 'url' in self.data['image']:
            self.cover_url = '{}_SX214_.jpg'.format(self.data['image']['url'].replace('.jpg', ''))

        self.release_date = None
        if 'release_date' in self.data and 'normal' in self.data['release_date']:
            self.release_date = self.data['release_date']['normal']

        self.certification = None
        if 'certificate' in self.data and 'certificate' in self.data['certificate']:
            self.certification = self.data['certificate']['certificate']

        self.trailer_img_url = None
        if ('trailer' in self.data and 'slates' in self.data['trailer'] and
                self.data['trailer']['slates']):
            self.trailer_img_url = self.data['trailer']['slates'][0]['url']

        # Directors
        self.directors = []
        if self.data.get('directors_summary'):
            for director in self.data['directors_summary']:
                self.directors.append(Person(**director))

        # Creators
        self.creators = []
        if self.data.get('creators'):
            for creator in self.data['creators']:
                self.creators.append(Person(**creator))

        # Cast summary
        self.cast_summary = []
        if self.data.get('cast_summary'):
            for cast in self.data['cast_summary']:
                self.cast_summary.append(Person(**cast))

        # Credits
        self.credits = []
        if self.data.get('credits'):
            for credit in self.data['credits']:
                """
                Possible tokens
                directors, cast, writers
                """
                if 'cast' in credit['token']:
                    for member in credit['list']:
                        self.credits.append(Person(**member))

        # Writers
        self.writers = []
        if self.data.get('writers_summary'):
            for writer in self.data['writers_summary']:
                self.writers.append(Person(**writer))

        # Trailers
        self.trailers = {}
        if 'trailer' in self.data and 'encodings' in self.data['trailer']:
            for k, v in list(self.data['trailer']['encodings'].items()):
                self.trailers[v['format']] = v['url']

