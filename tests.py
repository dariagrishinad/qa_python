from main import BooksCollector
import pytest

class TestBooksCollector:

    @pytest.mark.parametrize('name', ['Что делать, если ваш кот хочет вас убить??', ''])
    def test_add_new_book_invalid_length(self, name):

        collector = BooksCollector()
        collector.add_new_book(name)

        assert len(collector.get_books_genre()) == 0

    def test_set_book_genre_add_genre(self):

        collector = BooksCollector()
        collector.add_new_book('Что делать, если кот хочет вас убить')
        collector.set_book_genre('Что делать, если кот хочет вас убить', 'Ужасы')

        assert collector.get_book_genre('Что делать, если кот хочет вас убить') == 'Ужасы'

    @pytest.mark.parametrize('genre', ['Драма', ''])
    def test_set_book_genre_set_invalid_genre(self, genre):

        collector = BooksCollector()
        collector.add_new_book('Что делать, если кот хочет вас убить')
        collector.set_book_genre('Что делать, если кот хочет вас убить', genre)

        assert collector.get_book_genre('Что делать, если кот хочет вас убить') == ''

    def test_get_book_genre_get_book_genre(self):

        collector = BooksCollector()
        collector.add_new_book('Что делать, если кот хочет вас убить')
        collector.set_book_genre('Что делать, если кот хочет вас убить', 'Ужасы')

        assert collector.get_book_genre('Что делать, если кот хочет вас убить') == 'Ужасы'

    def test_get_books_with_specific_genre_get_books(self):

        collector = BooksCollector()
        collector.add_new_book('Что делать, если кот хочет вас убить')
        collector.add_new_book('Сияние')
        collector.set_book_genre('Что делать, если кот хочет вас убить', 'Ужасы')
        collector.set_book_genre('Сияние', 'Ужасы')

        assert collector.get_books_with_specific_genre('Ужасы') == ['Что делать, если кот хочет вас убить', 'Сияние']

    @pytest.mark.parametrize('genre', ['Мистика', ''])
    def test_get_books_with_specific_genre_invalid_genre(self, genre):

        collector = BooksCollector()

        assert collector.get_books_with_specific_genre(genre) == []

    def test_get_books_genre_get_books_genre(self):

        collector = BooksCollector()
        collector.add_new_book('Что делать, если кот хочет вас убить')
        collector.add_new_book('Сияние')
        collector.set_book_genre('Что делать, если кот хочет вас убить', 'Ужасы')
        collector.set_book_genre('Сияние', 'Ужасы')

        assert collector.get_books_genre() == {'Что делать, если кот хочет вас убить': 'Ужасы', 'Сияние': 'Ужасы'}

    def test_get_books_for_children_for_children(self):

        collector = BooksCollector()
        collector.add_new_book('Что делать, если кот хочет вас убить')
        collector.set_book_genre('Что делать, если кот хочет вас убить', 'Мультфильмы')

        assert collector.get_books_for_children() == ['Что делать, если кот хочет вас убить']

    def test_get_books_for_children_not_for_children(self):

        collector = BooksCollector()
        collector.add_new_book('Что делать, если кот хочет вас убить')
        collector.set_book_genre('Что делать, если кот хочет вас убить', 'Ужасы')

        assert collector.get_books_for_children() == []

    def test_add_book_in_favorites_add_book(self):

        collector = BooksCollector()
        collector.add_new_book('Что делать, если кот хочет вас убить')
        collector.add_book_in_favorites('Что делать, если кот хочет вас убить')

        assert collector.get_list_of_favorites_books() == ['Что делать, если кот хочет вас убить']

    def test_add_book_in_favorites_add_book_not_in_books_genre(self):

        collector = BooksCollector()
        collector.add_book_in_favorites('Что делать, если кот хочет вас убить')

        assert collector.get_list_of_favorites_books() == []

    def test_delete_book_from_favorites_delete_book(self):

        collector = BooksCollector()
        collector.add_new_book('Что делать, если кот хочет вас убить')
        collector.add_book_in_favorites('Что делать, если кот хочет вас убить')
        collector.delete_book_from_favorites('Что делать, если кот хочет вас убить')

        assert collector.get_list_of_favorites_books() == []

    @pytest.mark.parametrize('book', ['Приключения Шурика', ''])
    def test_delete_book_from_favorites_delete_book_not_in_favorites(self, book):

        collector = BooksCollector()
        collector.add_new_book('Что делать, если кот хочет вас убить')
        collector.add_book_in_favorites('Что делать, если кот хочет вас убить')
        collector.delete_book_from_favorites(book)

        assert collector.get_list_of_favorites_books() == ['Что делать, если кот хочет вас убить']

    def test_get_list_of_favorites_books_get_list(self):

        collector = BooksCollector()
        collector.add_new_book('Что делать, если кот хочет вас убить')
        collector.add_book_in_favorites('Что делать, если кот хочет вас убить')

        assert collector.get_list_of_favorites_books() == ['Что делать, если кот хочет вас убить']
