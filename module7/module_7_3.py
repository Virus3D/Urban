class WordsFinder():
    def __init__(self, *file) -> None:
        self.file_names = file

    def get_all_words(self) -> dict:
        all_words = {}
        for file_name in self.file_names:
            words = []
            with open(file_name) as file:
                for line in file:
                    line = line.lower()
                    for str in [',', '.', '=', '!', '?', ';', ':', ' - ', '  ']:
                        line = line.replace(str, ' ')
                    words += line.split()
            all_words[file_name] = words;

        return all_words
    
    def find(self, word:str) -> dict:
        word = word.lower();
        result = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            if word in words:
                result[file_name] = words.index(word) + 1
        return result
    
    def count(self, word:str) -> dict:
        word = word.lower();
        result = {}
        all_words = self.get_all_words()
        for file_name, words in all_words.items():
            if word in words:
                result[file_name] = words.count(word)
        return result



finder2 = WordsFinder('test_text.txt')
print(finder2.get_all_words()) # Все слова
print(finder2.find('TEXT')) # 3 слово по счёту
print(finder2.count('teXT')) # 4 слова teXT в тексте всего

finder2 = WordsFinder('test_text2.txt')
print(finder2.get_all_words())
print(finder2.find('captain'))
print(finder2.count('captain'))
