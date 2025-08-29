import pytest
from main import BooksCollector


@pytest.fixture
def collector():
    return BooksCollector()


@pytest.fixture
def investor_in_favorites(collector):
    collector.add_new_book("Разумный инвестор")
    collector.add_book_in_favorites("Разумный инвестор")
    return collector
