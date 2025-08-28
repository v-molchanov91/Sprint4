import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book_add_two_books(self, collector):

        collector.add_new_book("Гордость и предубеждение и зомби")
        collector.add_new_book("Что делать, если ваш кот хочет вас убить")
        assert len(collector.get_books_genre()) == 2

    @pytest.mark.parametrize("book_name", ["", "А" * 41])
    def test_add_new_book_invalid_length_not_added(self, collector, book_name):
        collector.add_new_book(book_name)
        assert book_name not in collector.get_books_genre()

    def test_set_book_genre_valid_book_and_genre(self, collector):
        collector.add_new_book("Дюна")
        collector.set_book_genre("Дюна", "Фантастика")
        assert collector.get_book_genre("Дюна") == "Фантастика"

    def test_set_book_genre_invalid_genre_does_not_change(self, collector):
        collector.add_new_book("Лавандовая ветвь")
        collector.set_book_genre("Лавандовая ветвь", "Романтика")
        assert collector.get_book_genre("Лавандовая ветвь") == ""

    def test_get_books_with_specific_genre_returns_correct_list(self, collector):
        collector.add_new_book("Король ужасов")
        collector.add_new_book("Хроники Нарнии")
        collector.set_book_genre("Король ужасов", "Ужасы")
        collector.set_book_genre("Хроники Нарнии", "Фантастика")

        assert collector.get_books_with_specific_genre("Фантастика") == [
            "Хроники Нарнии"
        ]

    def test_get_books_for_children_excludes_age_restricted(self, collector):
        collector.add_new_book("Хроники Нарнии")
        collector.add_new_book("Король ужасов")
        collector.set_book_genre("Хроники Нарнии", "Фантастика")
        collector.set_book_genre("Король ужасов", "Ужасы")

        books_for_children = collector.get_books_for_children()
        assert books_for_children == ["Хроники Нарнии"]

    def test_add_book_in_favorites_successfully(self, investor_in_favorites):
        assert (
            "Разумный инвестор" in investor_in_favorites.get_list_of_favorites_books()
        )

    def test_add_book_in_favorites_twice_only_once(self, collector):
        collector.add_new_book("Разумный инвестор")
        collector.add_book_in_favorites("Разумный инвестор")
        collector.add_book_in_favorites("Разумный инвестор")
        assert collector.get_list_of_favorites_books().count("Разумный инвестор") == 1

    def test_delete_book_from_favorites_removes_book(self, investor_in_favorites):
        investor_in_favorites.delete_book_from_favorites("Разумный инвестор")
        assert (
            "Разумный инвестор"
            not in investor_in_favorites.get_list_of_favorites_books()
        )

    def test_add_book_in_favorites_book_not_in_genre_not_added(self, collector):
        collector.add_book_in_favorites("Неизвестная книга")
        assert collector.get_list_of_favorites_books() == []
