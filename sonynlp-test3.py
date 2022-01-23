from soynlp.noun import LRNounExtractor
from soynlp.word import WordExtractor
from soynlp.tokenizer import LTokenizer
from urllib.request import urlopen
from bs4 import BeautifulSoup
from ckonlpy.tag import Twitter
import konlpy
import nltk


import re
html = urlopen("https://open-pro.dict.naver.com/_ivo/dictmain?dictID=enegdwdxdyebegdxdwdsqyofehjosqff&page=2&listType=1")  
bsObject = BeautifulSoup(html, "html.parser") 
# print(bsObject) # 웹 문서 전체가 출력
# print(bsObject.get_text())
onlytext = bsObject.get_text()
print(type(onlytext))
# onlytext=onlytext.replace("\n","")
onlytext = re.split(r'[ ,:,\s,\n,.]', onlytext)
# onlytext = re.split(r'\`\-\=\~\!\@\#\$\%\^\&\*\(\)\_\+\[\]\{\}\;\'\\\:\"\|\<\,\.\/\>\<\>\?\\n\\s', onlytext)
print(type(onlytext))
# onlytext = onlytext.split(' ')
# onlytext = re.split("' '|\n|''", onlytext)
onlytext = list(map(lambda x: x.strip(), onlytext))
onlytext = list(filter(lambda x: x != '', onlytext))
# print(onlytext)
StrA = " ".join(onlytext)
print("원본 텍스트 입니다.",onlytext)
noun_extractor = LRNounExtractor()
nouns = noun_extractor.train_extract(onlytext) # list of str like


word_extractor = WordExtractor(
    min_frequency=50, # example
    min_cohesion_forward=0.05,
    min_right_branching_entropy=0.0
)

word_extractor.train(onlytext)
words = word_extractor.extract()

cohesion_score = {word:score.cohesion_forward for word, score in words.items()}

noun_scores = {noun:score.score for noun, score in nouns.items()}
combined_scores = {noun:score + cohesion_score.get(noun, 0)
    for noun, score in noun_scores.items()}
combined_scores.update(
    {subword:cohesion for subword, cohesion in cohesion_score.items()
    if not (subword in combined_scores)}
)
tokenizer = LTokenizer(scores=combined_scores)
train_list=onlytext
# print(str(train_list[0]))
# print(tokenizer.tokenize(str(train_list[0])))
print("soynlp 로 추출해낸 명사집합입니다.",train_list)

words = konlpy.tag.Twitter().pos(StrA)
# print(words)
noun = []
# print(type(words))
for nn in words:
    if nn[1] == 'Noun':
        noun.append(nn[0])
print("konlp 로 추출해낸 명사집합입니다.",noun)
# -------------------------------------
# twitter = Twitter()
# twitter.morphs('은경이는 사무실로 갔습니다.')
# print(twitter)