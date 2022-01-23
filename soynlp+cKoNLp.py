from soynlp.normalizer import *

from ckonlpy.tag import Twitter
twitter = Twitter()
words=twitter.morphs(repeat_normalize(emoticon_normalize('ㅋㅋㅋㅋㅋㅋㅋㅋ어쩔티비 그냥 밥이나 먹어 하하하하')))
# noun = []
print(words)
# print(type(words))
# for nn in words:
#     if nn[1] == 'Noun':
#         noun.append(nn[0])
# print(noun)
twitter.add_dictionary('어쩔티비','Noun')
words=twitter.morphs('ㅋㅋㅋㅋㅋㅋㅋㅋ어쩔티비 그냥 밥이나 먹어 하하하하')
noun = []
print(words)