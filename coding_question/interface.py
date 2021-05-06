from abc import ABCMeta, abstractmethod
from numbers import Number
from typing import Any, List, Optional


class BaseList(metaclass=ABCMeta):
    """
    Interface for a custom data structure that can add, get access, and provide
    the moving average of the last N elements added.
    """

    def __init__(self, elements: Optional[List[Number]] = None):
        if elements:
            self.elements = list(elements)
        else:
            self.elements = []

    def add(self, element: Number) -> None:
        """
        Add an element to the end of the structure.

        :param element: Element to be added to the structure.
        """
        self.elements.append(element)

    def get(self, index: int) -> Number:
        """
        Return a element from the structure based on index, if index is greater
        than data structure length it raises IndexError.

        :param index: Position in the structure, starting from 0.
        """
        return self.elements[index]

    @abstractmethod
    def moving_average(self, last_n: Any) -> None:
        """
        Calculate the moving average of the last_n elements of the structure.
        """
        raise NotImplementedError
