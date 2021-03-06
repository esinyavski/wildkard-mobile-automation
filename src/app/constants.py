from enum import Enum


class Gender(Enum):
    Male = "Male"
    Female = "Female"
    Custom = "Custom"
    PreferNotToSay = "Prefer Not to Say"


class Role(Enum):
    Organizer = "Organizer"
    Official = "Official"
