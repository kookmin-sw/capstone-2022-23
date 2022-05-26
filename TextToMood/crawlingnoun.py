#-*-Encoding:UTF-8 -*-#
from urllib.request import urlopen
from bs4 import BeautifulSoup
# import konlpy
import nltk
import urllib.request as req
import re
from konlpy.tag import Kkma
kkma = Kkma()
url = "https://www.naver.com/"
res = req.urlopen(url).read()
html = urlopen(url).read()


bsObject = BeautifulSoup(html, "html.parser") 
# print(bsObject) # 웹 문서 전체가 출력
# print(bsObject.get_text())
onlytext = bsObject.get_text()
# print(onlytext)
# print(type(onlytext))
# onlytext=onlytext.replace("\n","")
token = kkma.sentences(onlytext)
print(token)
onlytext = re.split(r'[ ,:,\s,\n,.]', onlytext)

# onlytext = re.split(r'\`\-\=\~\!\@\#\$\%\^\&\*\(\)\_\+\[\]\{\}\;\'\\\:\"\|\<\,\.\/\>\<\>\?\\n\\s', onlytext)
# print(type(onlytext))
# onlytext = onlytext.split(' ')
# onlytext = re.split("' '|\n|''", onlytext)
onlytext = list(map(lambda x: x.strip(), onlytext))
onlytext = list(filter(lambda x: x != '', onlytext))
# print(onlytext)
StrA = " ".join(onlytext)
# print(onlytext)
words = konlpy.tag.Twitter().pos(StrA)
# print(words)
noun = []
# print(type(words))
# for nn in words:
#     if nn[1] == 'Noun':
#         noun.append(nn[0])
# print(noun)


# print(type(words[0]))

# grammar = """
# NP: {<N.*>*<Suffix>?}   # Noun phrase
# VP: {<V.*>*}            # Verb phrase
# AP: {<A.*>*}            # Adjective phrase
# """
# parser = nltk.RegexpParser(grammar)
# chunks = parser.parse(words)
# print("# Print whole tree")
# print(chunks.pprint())
# noun = []
# print("\n# Print noun phrases only")
# for subtree in chunks.subtrees():
#     if subtree.label()=='NP':
#         print(' '.join((e[0] for e in list(subtree))))
#         print(subtree.pprint())
#         noun.append(subtree)

# # Display the chunk tree
# chunks.draw()
# print(noun)