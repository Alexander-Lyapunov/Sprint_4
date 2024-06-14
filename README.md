# qa_python

Этот проект содержит тесты для класса `BooksCollector`

## Методы класса BooksCollector

- `add_new_book(name)` - добавляем новую книгу.
- `set_book_genre(name, genre)` - устанавливаем книге жанр.
- `get_book_genre(name)` - получаем жанр книги по её имени.
- `get_books_with_specific_genre(genre)` - выводим список книг с определённым жанром.
- `get_books_genre()` - получаем словарь books_genre.
- `get_books_for_children()` - возвращаем книги, подходящие детям.
- `add_book_in_favorites(name)` - добавляем книгу в Избранное.
- `delete_book_from_favorites(name)` - удаляем книгу из Избранного.
- `get_list_of_favorites_books()` - получаем список Избранных книг.

## Тесты

1. `test_add_new_book` - проверяет добавление новой книги.
2. `test_add_new_book_length_positive` - проверяет корректность добавления книги с допустимой длиной названия.
3. `test_add_new_book_length_negative` - проверяет, что книги с недопустимой длиной названия не добавляются.
4. `test_set_book_genre` - проверяет установку и получение жанра книги.
5. `test_get_books_with_specific_genre` - проверяет получение списка книг с определённым жанром.
6. `test_get_books_genre` - проверяет получение словаря books_genre.
7. `test_get_books_for_children` - проверяет получение списка книг, подходящих детям.
8. `test_add_book_in_favorites` - проверяет добавление книги в избранное.
9. `test_delete_book_from_favorites` - проверяет удаление книги из избранного.
10. `test_get_list_of_favorites_books` - проверяет получение списка избранных книг.

## Параметризованные тесты

Тесты `test_add_new_book_length_positive` и `test_add_new_book_length_negative` параметризованы для проверки корректности добавления книги с различной длиной названия.

