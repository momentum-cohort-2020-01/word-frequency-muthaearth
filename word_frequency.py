from collections import Counter

STOP_WORDS = [
    'a', 'an', 'and', 'are', 'as', 'at', 'be', 'by', 'for', 'from', 'has', 'he',
    'i', 'in', 'is', 'it', 'its', 'of', 'on', 'that', 'the', 'to', 'were',
    'will', 'with'
]


def open_file(file):  # open text file
    with open(file) as file:
        return file.read()


def remove_punctuation(file):  # remove punctuation iterates through text file and stores each string into char to evaluate for instance of punctuation. If none, passes string into punctLess
    punctLess = ""
    punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''
    for char in file:
        if char not in punctuations:
            punctLess += char
    return punctLess


def lowercase_and_split(file):  # transform text file to lowercase
    x = file.lower().split(" ")
    return x


def removeSW(file):  # remove stop words
    sw_removed = []
    i = 0
    while i < len(file):
        if file[i] not in STOP_WORDS:
            sw_removed.append(file[i])
        i += 1
    return sw_removed


def countSort(file):  # count and sort file
    cWords = dict(Counter(file))
    cWords = {k: v for k, v in sorted(
        cWords.items(), key=lambda item: item[1], reverse=True)}
    return cWords


def render_dict(file):  # make a dictionary
    for word, num in file.items():
        print(f"{word} | {num} " + num * "*")


def print_word_freq(file):  # display word frequency
    print(f"Instances of word in: {file}")
    text = open_file(file)
    text = remove_punctuation(text)
    text = lowercase_and_split(text)
    text = removeSW(text)
    text = countSort(text)
    render_dict(text)


print_word_freq('seneca_falls.txt')  # print text files
print_word_freq('emancipation_proclamation.txt')


if __name__ == "__main__":  # don't understand this if stmt
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
