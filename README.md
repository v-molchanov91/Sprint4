# 📚 Тесты для BooksCollector

## 📌 Описание проекта
`BooksCollector` — это класс для работы с коллекцией книг.  
Он позволяет:
- добавлять книги в коллекцию,
- задавать жанры,
- формировать список книг для детей (без возрастных ограничений),
- управлять списком избранного.

Для проверки его работоспособности написаны автоматизированные тесты с использованием **pytest**.

---

## ✅ Покрытые сценарии

### 1. Добавление книг
- **`test_add_new_book_add_two_books`** — проверяет, что после добавления двух книг коллекция увеличивается на 2 элемента.  
- **`test_add_new_book_invalid_length_not_added`** — книги с пустым названием или длиной >40 символов не добавляются.  

### 2. Установка жанра
- **`test_set_book_genre_valid_book_and_genre`** — корректному жанру успешно присваивается книга.  
- **`test_set_book_genre_invalid_genre_does_not_change`** — жанр не меняется, если он отсутствует в списке допустимых.  

### 3. Получение книг по жанрам
- **`test_get_books_with_specific_genre_returns_correct_list`** — возвращаются только книги указанного жанра.  
- **`test_get_books_for_children_excludes_age_restricted`** — в список «для детей» не попадают книги с возрастным ограничением.  

### 4. Работа с избранным
- **`test_add_book_in_favorites_successfully`** — книга успешно добавляется в список избранных.  
- **`test_add_book_in_favorites_twice_only_once`** — одну и ту же книгу нельзя добавить в избранное дважды.  
- **`test_delete_book_from_favorites_removes_book`** — книга удаляется из списка избранных.  
- **`test_add_book_in_favorites_book_not_in_genre_not_added`** — нельзя добавить в избранное книгу, которой нет в коллекции.  

---

## 📊 Таблица покрытия тестами

| Метод класса                     | Тесты                                                                 |
|----------------------------------|----------------------------------------------------------------------|
| `add_new_book`                   | `test_add_new_book_add_two_books`, `test_add_new_book_invalid_length_not_added` |
| `set_book_genre`                 | `test_set_book_genre_valid_book_and_genre`, `test_set_book_genre_invalid_genre_does_not_change` |
| `get_book_genre`                 | Проверяется внутри тестов установки жанра                            |
| `get_books_with_specific_genre`  | `test_get_books_with_specific_genre_returns_correct_list`            |
| `get_books_for_children`         | `test_get_books_for_children_excludes_age_restricted`                |
| `add_book_in_favorites`          | `test_add_book_in_favorites_successfully`, `test_add_book_in_favorites_twice_only_once`, `test_add_book_in_favorites_book_not_in_genre_not_added` |
| `delete_book_from_favorites`     | `test_delete_book_from_favorites_removes_book`                       |
| `get_list_of_favorites_books`    | Проверяется внутри тестов работы с избранным                         |

---
