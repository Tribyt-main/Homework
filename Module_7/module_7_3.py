import string


class WordsFinder:
    def __init__(self, *file_names):
        self.file_names = file_names
        self.words_dict = {}

    def get_all_words(self):
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                i = file.read()
                no_punc = i.translate(str.maketrans('', '', string.punctuation))
                all_words = no_punc.split()
                self.words_dict[file_name] = all_words
                return self.words_dict

    def find(self, word):
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                i = file.read()
                no_punc = i.translate(str.maketrans('', '', string.punctuation))
                index_word = no_punc.split()
                for item in index_word:
                    index = index_word.index(word.lower()) + 1
                    if item.lower() == word.lower():
                        self.words_dict[file_name] = index
                        return self.words_dict

    def count(self, word):
        for file_name in self.file_names:
            with open(file_name, 'r', encoding='utf-8') as file:
                i = file.read()
                no_punc = i.translate(str.maketrans('', '', string.punctuation))
                all_words = no_punc.split()
                co = all_words.count(word.lower())
                self.words_dict[file_name] = co
                return self.words_dict


finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TExt'))
print((finder2.count('TexT')))
