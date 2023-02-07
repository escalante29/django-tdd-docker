# app/tests/movies/conftest.py

import pytest

from movies.models import Movie


@pytest.fixture(scope='function')
def add_movie():
    def _add_movie(title, genre, year):
        movie = Movie.objects.create(title=title, genre=genre, year=year)
        return movie
    return _add_movie


# @pytest.fixture(scope="session")
# def django_db_setup():
#     settings.DATABASES["default"] = {
#         "ENGINE": os.environ.get("DB_TEST_ENGINE", DEFAULT_ENGINE),
#         "HOST": os.environ["DB_TEST_HOST"],
#         "NAME": os.environ["DB_TEST_NAME"],
#         "PORT": os.environ["DB_TEST_PORT"],
#         "USER": os.environ["DB_TEST_USER"],
#         "PASSWORD": os.environ["DB_TEST_PASSWORD"],
#     }