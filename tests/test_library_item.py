"""
Description: Unit tests for the Book class.
Usage: To execute all tests in the terminal execute 
the following command:
    python -m unittest tests/test_book.py

"""
__author__ = "Jashanpreet Sidhu"
__version__ = "1.0.0"

import unittest
from genre.genre import Genre
from library_item.library_item import LibraryItem

class TestLibraryItem(unittest.TestCase):

    def setUp(self):
        self.libraryitem = LibraryItem("Educated", "Tara Westover", Genre.NON_FICTION)
    
    def test_init_valid_inputs_attributes_set(self):
        expected = LibraryItem("Educated", "Tara Westover", Genre.NON_FICTION)

        self.assertEqual("Educated", expected._LibraryItem__title)
        self.assertEqual("Tara Westover", expected._LibraryItem__author)
        self.assertEqual(Genre.NON_FICTION, expected._LibraryItem__genre)

    def test_init_title_blank_raised_valueerror(self):
        with self.assertRaises(ValueError):
            LibraryItem(" ", "Tara Westover", Genre.NON_FICTION)

    def test_init_author_blank_raised_valueerror(self):
        with self.assertRaises(ValueError):
            LibraryItem("Educated", " ", Genre.NON_FICTION)

    def test_init_invalid_genre_raised_valueerror(self):
        with self.assertRaises(ValueError):
            LibraryItem("Educated", "Tara Westover", "horror")

    def test_title_accessor_returns_title(self):
        self.assertEqual("Educated", self.libraryitem.title)

    def test_author_accessor_returns_author(self):
        self.assertEqual("Tara Westover", self.libraryitem.author)

    def test_genre_accessor_returns_genre(self):
        self.assertEqual(Genre.NON_FICTION, self.libraryitem.genre)
    