from uzwords import words
from difflib import get_close_matches


# print(len(words))
# print(words[0])
# print(words[-1])
# print(words[7777])
# print(words[22222])

# print(get_close_matches('тарих', words))
# print(get_close_matches('тарик', words))
# print(get_close_matches('муомала', words))
# print(get_close_matches('мактап', words))



def checkWord(word, words=words):
    word = word.lower()
    matches = set(get_close_matches(word, words))
    available = False #Bunday so'z mavjud emas

    if word in matches:
        available = True #Mavjud
        matches = word

    elif 'ҳ' in word:
        word = word.replace('ҳ', 'х')
        matches.update(get_close_matches(word, words))

    elif  'х' in word:
        word = word.replace('х', 'ҳ')
        matches.update(get_close_matches(word, words))

    return {'available':available, 'matches':matches}


if __name__ == '__main__':
    print(checkWord('хато'))
    print(checkWord('олма'))
    print(checkWord('ҳато'))
