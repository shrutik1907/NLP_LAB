import gensim
from gensim import corpora
from gensim.utils import simple_preprocess

text1 = ["""Technology continues to revolutionize the way we live and work, with innovations like artificial 
         intelligence and automation shaping our future. From smartphones that keep us connected 24/7 to 
         breakthroughs in renewable energy, the impact of technology is profound."""]

tokens1 = [[item for item in line.split()] for line in text1]
g_dict1 = corpora.Dictionary(tokens1)

print("The dictionary has: " +str(len(g_dict1)) + " tokens\n")
print(g_dict1.token2id)


text2 = open('sample_text.txt', encoding ='utf-8')
 
tokens2 =[]
for line in text2.read().split('.'):
  tokens2.append(simple_preprocess(line, deacc = True))

g_dict2 = corpora.Dictionary(tokens2)

print("The dictionary has: " +str(len(g_dict2)) + " tokens\n")
print(g_dict2.token2id)


"""OUTPUT-
The dictionary has: 35 tokens

{'24/7': 0, 'From': 1, 'Technology': 2, 'and': 3, 'artificial': 4, 'automation': 5, 'breakthroughs': 6, 
'connected': 7, 'continues': 8, 'energy,': 9, 'future.': 10, 'impact': 11, 'in': 12, 'innovations': 13, 
'intelligence': 14, 'is': 15, 'keep': 16, 'like': 17, 'live': 18, 'of': 19, 'our': 20, 'profound.': 21, 
'renewable': 22, 'revolutionize': 23, 'shaping': 24, 'smartphones': 25, 'technology': 26, 'that': 27, 'the': 28, 
'to': 29, 'us': 30, 'way': 31, 'we': 32, 'with': 33, 'work,': 34}
The dictionary has: 0 tokens
"""