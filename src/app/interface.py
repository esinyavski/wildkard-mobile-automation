from abc import abstractmethod

from src.wrappers.driver import Driver
from src.utils.data_generator import DataGenerator


class Interface(Driver):
    __pages = []

    def __init__(self, page, **kwargs):
        super().__init__(**kwargs)
        if page not in self.__class__.__pages:
            self.validate()

    @abstractmethod
    def validate(self):
        pass

    @property
    def dummy(self):
        return DataGenerator

