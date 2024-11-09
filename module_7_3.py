class WordsFinder():
    def __init__(self, file_names):
        self.file_names = file_names

    def get_all_words(self):
        all_words = {}
        symbols = [',', '.', '=', '!', '?', ';', ':', ' - ']
        lines = ''
        with open(self.file_names, 'r', encoding='utf-8') as file:
            for line in file:
                line = line.lower()
                for symbol in symbols:
                    if symbol in line:
                        line = line.replace(symbol, '')
                lines = lines + line
            all_words.update({self.file_names: lines.split()})
        return all_words

    def find(self, word):
        dict_1 = {}
        for name, words in self.get_all_words().items():
            for i in range(len(words)):
                if word.lower() == words[i]:
                    dict_1.update({name: i+1})
                    return dict_1

    def count(self, word):
        dict_1 = {}
        word = word.lower()
        for name, words in self.get_all_words().items():
            dict_1.update({name: words.count(word)})
            return dict_1

finder2 = WordsFinder('test_file.txt')
print(finder2.get_all_words())  # Все слова
print(finder2.find('TEXT'))  # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего
