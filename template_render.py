from jinja2 import Environment, FileSystemLoader


class MoviesRender:
    _ENVIRONMENT = Environment(loader=FileSystemLoader("templates/"))
    _TEMPLATE = _ENVIRONMENT.get_template("index_template.html")
    _RESULT_FILENAME = "index.html"


    def __init__(self, movies):
        self.__movies = movies
        self.__context = {
            "movies": movies
        }


    def render(self):
        with open(MoviesRender._RESULT_FILENAME, mode="w", encoding="utf-8") as result:
            result.write(MoviesRender._TEMPLATE.render(self.__context))
            print(f"Website has been successfully generated to {MoviesRender._RESULT_FILENAME}")

