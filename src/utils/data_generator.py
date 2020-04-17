import fauxfactory

from enum import Enum


class StringType(Enum):
    alpha = "alpha"
    alphanumeric = "alphanumeric"
    cjk = "cjk"
    html = "html"
    latin1 = "latin1"
    numeric = "numeric"
    utf8 = "utf8"
    punctuation = "punctuation"


class DataGenerator:

    FILTER_KEY = "auto_test"
    LEAGUE_NAME = "League Auto_test"
    TEAM_NAME_1 = "Team auto_test 1"
    TEAM_NAME_2 = "Team auto_test 2"
    TEAM_NAME_3 = "Team auto_test 3"

    @classmethod
    def gen_string(cls,
                   size=20,
                   str_type: StringType = StringType.alphanumeric.value,
                   filter_key=True):
        if filter_key:
            return f"{cls.FILTER_KEY}_{fauxfactory.gen_string(str_type, size - len(cls.FILTER_KEY) - 1)}"
        else:
            return fauxfactory.gen_string(str_type, size)

    @classmethod
    def gen_numeric(cls, size=10, as_string=True):
        if as_string:
            return cls.gen_string(size=size, str_type=StringType.numeric.value, filter_key=False)
        else:
            return int(cls.gen_string(size=size, str_type=StringType.numeric.value, filter_key=False))
