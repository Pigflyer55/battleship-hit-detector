from abc import ABC, abstractmethod


class Ship(ABC):

    @abstractmethod  # Defining necessary Ship subclass parameters
    def __init__(self, origin, config_num):
        pass