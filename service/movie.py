from dao.model.movie import Movie
from dao.movie import MovieDAO


class MovieService:
    def __init__(self, dao: MovieDAO):
        self.dao = dao

    def get_one(self, bid):
        return self.dao.get_one(bid)

    def get_all(self, filters):
        status = filters.get("status")
        page = filters.get("page")
        if page is not None:
            page = int(page)
        if status == 'new' and page is not None:
            return self.session.querry(Movie).order_by(Movie.year.desc()).paginate(page, 12, error_out=False).items
        elif status == 'new':
            return self.session.querry(Movie).order_by(Movie.year.desc()).all
        elif page is not None:
            return self.session.querry.paginate(page, 12, error_out=False).items
        return self.dao.get_all()

    def create(self, movie_d):
        return self.dao.create(movie_d)

    def update(self, movie_d):
        self.dao.update(movie_d)
        return self.dao

    def delete(self, rid):
        self.dao.delete(rid)
