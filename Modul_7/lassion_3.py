# тема "Оператор "with"
import string

class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names

    def get_all_words(self):
        """Подготовительный метод, который возвращает словарь следующего вида"""
        all_words = {}
        for file_name in self.file_names: # названия файлов.
            try:
                with open(file_name, 'r', encoding='utf-8') as file:
                    text = file.read().lower()
                    for punct in [',', '.', '=', '!', '?', ';', ':', ' - ']:
                        text = text.replace(punct, ' ')
                    words = text.split()
                    all_words[file_name] = words
            except FileNotFoundError:
                all_words[file_name] = []
        return all_words

    def find(self, word):
        word = word.lower()
        results = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            try:
                position = words.index(word) + 1  # Преобразование в индекс, основанный на 1
                results[file_name] = position
            except ValueError:
                results[file_name] = None
        return results

    def count(self, word):
        word = word.lower()
        counts = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            counts[file_name] = words.count(word)
        return counts

# Пример использования
finder2 = WordsFinder('test_file.txt')

print(finder2.get_all_words())  # Все слова

print(finder2.find('TEXT'))  # Позиция первого вхождения 'text'

print(finder2.count('teXT'))  # Количество вхождений 'text'