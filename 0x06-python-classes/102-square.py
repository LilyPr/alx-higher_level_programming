#!/usr/bin/pythion3
"""Define a class Square."""


class Square:
    def __init__(self, size=0):
        self.size = size

        @property
        def size(self):
            """Get/set the current size of the square."""
            return (self.__size)

        @size.setter
        def size(self, value):
            if type (value) is not int:
                raise TypeError("size must be an integer")
            elif value < 0:
                raise ValueError("size must be >= 0")
            self.__size = value

            def __lt__(self, other):
                return self.size < other.size

            def __le__(self, other):
                return self.size <= other.size

            def __eq__(self, other):
                return self.size == other.size

            def __ne__(self, other):
                return self.size != other.size

            def __ge__(self, other):
                return self.size >= other.size

            def __gt__(self, other):
                return self.size > other.size
