import pytest
from main import BooksCollector


class TestBooksCollector:

    def test_add_new_book(self,collector):
        collector.add_new_book("Гарри Поттер и философский камень")
        assert "Гарри Поттер и философский камень" in collector.get_books_genre()

    @pytest.mark.parametrize("book_name", [
        "а" * 1,
        "а" * 2,
        "а" * 39,
        "а" * 40,
        "Гарри Поттер"
    ])
    def test_add_new_book_length_positive(self, collector, book_name):
        collector.add_new_book(book_name)
        assert book_name in collector.get_books_genre()

    @pytest.mark.parametrize("book_name", [
        "",
        "а" * 41
    ])
    def test_add_new_book_length_negative(self,collector, book_name):
        collector.add_new_book(book_name)
        assert book_name not in collector.get_books_genre()

    def test_set_book_genre(self,collector):
        collector.add_new_book("Преступление и наказание")
        collector.set_book_genre("Преступление и наказание", "Детективы")
        assert collector.get_book_genre("Преступление и наказание") == "Детективы"

    def test_get_books_with_specific_genre(self, collector):
        collector.add_new_book("Гарри Поттер и узник Азкабана")
        collector.set_book_genre("Гарри Поттер и узник Азкабана", "Фантастика")
        assert collector.get_books_with_specific_genre("Фантастика") == ["Гарри Поттер и узник Азкабана"]

    def test_get_books_genre(self, collector):
        collector.add_new_book("Мастер и Маргарита")
        collector.set_book_genre("Мастер и Маргарита", "Фантастика")
        assert collector.get_books_genre() == {"Мастер и Маргарита": "Фантастика"}

    def test_get_books_for_children(self, collector):
        collector.add_new_book("Малыш и Карлсон")
        collector.set_book_genre("Малыш и Карлсон", "Мультфильмы")
        assert collector.get_books_for_children() == ["Малыш и Карлсон"]

    def test_add_book_in_favorites(self, collector):
        collector.add_new_book("Алые паруса")
        collector.add_book_in_favorites("Алые паруса")
        assert "Алые паруса" in collector.get_list_of_favorites_books()

    def test_delete_book_from_favorites(self, collector):
        collector.add_new_book("Муха-Цокотуха")
        collector.add_book_in_favorites("Муха-Цокотуха")
        collector.delete_book_from_favorites("Муха-Цокотуха")
        assert "Муха-Цокотуха" not in collector.get_list_of_favorites_books()

    def test_get_list_of_favorites_books(self, collector):
        collector.add_new_book("Чебурашка")
        collector.add_book_in_favorites("Чебурашка")
        assert set(collector.get_list_of_favorites_books()) == {"Чебурашка"}
