from collections import Counter

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]

# open text file


def open_file(file):
    with open(file) as file:
        return file.read()

# remove punctuation iterates through text file and stores each string into char to evaluate for instance of punctuation. If none, passes string into punctLess


def remove_punctuation(file):
    punctLess = ""
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for char in file:
        if char not in punctuations:
            punctLess += char
    return punctLess

# transform text file to lowercase


def lowercase_and_split(file):
    x = file.lower().split(" ")
    return x

# remove stop words


def removeSW(file):
    sw_removed = []
    i = 0
    while i < len(file):
        if file[i] not in STOP_WORDS:
            sw_removed.append(file[i])
        i += 1
    return sw_removed

# count and sort file


def countSort(file):
    cWords = dict(Counter(file))
    cWords = {k: v for k, v in sorted(
        cWords.items(), key=lambda item: item[1], reverse=True)}
    return cWords


# make a dictionary
def render_dict(file):
    for word, num in file.items():
        print(f"{word} | {num} " + num * "*")


# display word frequency
def print_word_freq(file):
    print(f"Instances of word in: {file}")
    text = open_file(file)
    text = remove_punctuation(text)
    text = lowercase_and_split(text)
    text = removeSW(text)
    text = countSort(text)
    render_dict(text)


# print text files
print_word_freq('seneca_falls.txt')
print_word_freq('emancipation_proclamation.txt')

# don't understand this if stmt
if __name__ == "__main__":
    import argparse
    from pathlib import Path

    parser = argparse.ArgumentParser(
        description='Get word frequency in text file.')
    parser.add_argument('file', help='file to read')
    args = parser.parse_args()

    file = Path(args.file)
    if file.is_file():
        print_word_freq(file)
    else:
        print(f"{file} does not exist!")
        exit(1)
