from sqlmodel import Enum


class Genres(Enum):
    fiction = "Fiction"
    detective = "Detective"
    biography_autobiography = "Biography/Autobiography"
    science_fiction = "ScienceFiction"
    horror = "Horror"
    adventure = "Adventure"
    mystery = "Mystery"
    dystopian = "Dystopian"
    romance = "Romance"
    comics = "Comics"
    historical = "Historical"