import string

#1 , 2
class Book:
    def __init__(self, filepath, title, author,genre):
        self.filepath = filepath
        self.title = title
        self.author = author
        self.genre = genre 
        self.words = {}
        self.most_common_words = []

    def __str__(self):
        return f"Title: {self.title}\nAuthor: {self.author}\nGenre: {self.genre}"

book = Book("emma.txt", "Emma", "Jane Austen", "Novel")
print(book,'\n')
""""Define process_line method, which takes a string, line, as argument, replaces
punctuation with spaces, lowers all line letters and populates words instance attribute, with
words as keys and word count as values. After being populated, words attribute should have
the following structure:"""
##{‘the’: 5268, ‘house’: 40, ‘can’: 262, ...,}
def process_file(filename):
    fin = open(filename, encoding="utf-8")
    hist = {}
    word_count = 0
    
    for line in fin:
        line = process_line(line)
        words = line.split()
        for word in words:
                hist[word] = hist.get(word, 0) + 1  
    
    return hist #e me i shfaq krejt fjalt => print(hist)
   #print hist

def process_line(line):
        line = line.translate(str.maketrans(string.punctuation, ' ' * len(string.punctuation)))
        words = line.lower().split()
        for word in words:
            word = word.strip(string.punctuation + "123456789")
        return line

"""5. Define total_words method that returns total number of words of the book."""


def total_words(hist):
     return sum(hist.values())

hist = process_file("emma.txt")

totali = total_words(hist)
print(totali, '\n')

"""6. Define different_words method that returns number of different words used in the book."""

def different_words(hist):
    return len(hist)

"""7. Define populate_most_common_words method which populates most_common_words
instance attribute with book words and their count sorted by the most used word to the least
used word. After being populated most_common_words instance attribute should have the
following structure:"""
#[(5268, ‘the ‘), (5149, ‘to’), ( 4437, ‘and’), ...,]

def most_common_words(hist):
        result = []
        for word, count in hist.items():
            result.append((count, word))
        return result


def populate_most_common_words(hist, num=10):
        words = most_common_words(hist)
        words.sort(reverse=True)
        words = words[:num]
        print(words)
        for i in range(num):
             count = words[i][0]
             word = words[i][1]
             print(f"{word}      {count}")
        
print('There are:', different_words(hist), 'different words','\n')
#print(most_common_words(hist))
print(populate_most_common_words(hist), '10 ma t perdortat, populate_most_common_words ', '\n')