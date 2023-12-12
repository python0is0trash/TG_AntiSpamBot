from cfg import word_replace, deny_words
from Levenshtein import distance


def antimat(message):
    phrase = message.text.lower()

    for key, value in word_replace.items():
        for letter in value:
            for phr in phrase:
                if letter == phr:
                    phrase = phrase.replace(phr, key)

    phrase = message.text.lower().split(' ')

    for word in deny_words:
        for part in range(len(phrase)):
            fragment = phrase[part]
            if distance(fragment, word) <= len(word)*0.25:
                return True
