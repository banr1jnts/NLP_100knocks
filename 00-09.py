import re
import textwrap
import random

def main():
    print('00. 文字列の逆順')
    token = 'stressed'
    target = token[::-1]
    print(target)

    print('01. 「パタトクカシーー」')
    token = 'パタトクカシーー'
    target = token[0::2]
    print(target)

    print('02. 「パトカー」＋「タクシー」＝「パタトクカシーー」')
    token1 = 'パトカー'
    token2 = 'タクシー'
    target = ''
    for char1, char2 in zip(token1, token2):
        target += char1
        target += char2
    print(target)

    print('03. 円周率')
    sentence = \
        'Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.'
    tokens = re.sub('[,.]', '', sentence).split(' ')
    target = [len(token) for token in tokens]
    print(target)

    print('04. 元素記号')
    sentence = ('Hi He Lied Because Boron Could Not Oxidize Fluorine. '
                'New Nations Might Also Sign Peace Security Clause. Arthur King Can.')
    tokens = re.sub('[,.]', '', sentence).split(' ')
    one_list = [1, 5, 6, 7, 8, 9, 15, 16, 19]
    target = {}
    for i, token in enumerate(tokens):
        num = i + 1
        if num in one_list:
            head = token[:1]
            target[head] = num
        else:
            head = token[:2]
            target[head] = num
    print(target)

    print('05. n-gram')
    def create_ngram(sequence: list, n: int) -> list:
        ngram = []
        for i in range(len(sequence) - n + 1):
            ngram.append(sequence[i: i+n])
        return ngram
    
    sentence = 'I am an NLPer'
    target1 = create_ngram(sentence, 2)
    words = sentence.split(' ')
    target2 = create_ngram(words, 2)
    print(target1, target2)

    print('06. 集合')
    str1 = 'paraparaparadise'
    str2 = 'paragraph'
    X = set(create_ngram(str1, 2))
    Y = set(create_ngram(str2, 2))
    target1 = (X | Y), (X & Y), (X - Y)
    target2 = ('se' in X), ('se' in Y)
    print(target1, '\n', target2)

    print('07. テンプレートによる文生成')
    def create_sentence(x: int, y: str, z: float) -> str:
        return f"{x}時の{y}は{z}"
    
    target = create_sentence(12, '気温', 22.4)
    print(target)

    print('08. 暗号文')
    def cipher(string: str) -> str:
        transformed_string = ''
        for char in string:
            if char.islower():
                transformed_char = chr(219 - ord(char))
                transformed_string += transformed_char
            else:
                transformed_string += char
        return transformed_string
    
    sentence = 'You are so cool! I ate 2 apples.'
    target = cipher(sentence)
    print(target)

    print('09. Typoglycemia')
    def create_typoglycemia(sentence: str) -> str:
        words = sentence.split(' ')
        typoglycemia = ''
        for word in words:
            if len(word) <= 4:
                typoglycemia += word + ' '
            else:
                typo_word_middle = list(word[1:-1])
                random.shuffle(typo_word_middle)
                typoglycemia += word[0] + ''.join(typo_word_middle) + word[-1] + ' '
        return typoglycemia

    sentence = ('I couldn’t believe that I could actually understand what I was reading : '
                'the phenomenal power of the human mind .')
    target = create_typoglycemia(sentence)
    print(target)

if __name__ == '__main__':
    main()
