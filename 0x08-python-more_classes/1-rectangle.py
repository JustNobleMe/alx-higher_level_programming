#!/usr/bin/python3
"""A class that defines a rectangle"""


class Rectangel:
    """A class representing a rectangle"""


    """Initializing width"""
    def __init__(self, width=0, height=0):
         """Initializing this rectangle class
        Args:
            width: represents the width of the rectangle
            height: represents the height of the rectangle
        Raises:
            TypeError: if size is not integer
            ValueError: if size is less than zero
        """
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """retrieve width attributes"""
        return self.__width

    @width.setter
    def width(self, value):
        """set width attributes"""
        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if not isinstance value > 0:
            raise ValueError('width must be >=0')
        self.__width = value
    
    @property
    def height(self):
        """retrieve height attributes"""
        return self.__height
    
    @height.setter
    def height(self, value):
        """set height attributs"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if not isinstance value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value