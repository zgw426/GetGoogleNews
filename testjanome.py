#>>> from janome.tokenizer import Tokenizer
#Traceback (most recent call last):
#  File "<stdin>", line 1, in <module>
#ModuleNotFoundError: No module named 'janome'
#>>>
# |
# pip install janome

from janome.tokenizer import Tokenizer

col = 0
data = []
each_data = []
t = Tokenizer()
tokens = t.tokenize("今日はいい天気ですね")
for token in tokens:
    partOfSpeech = token.part_of_speech.split(',')[0]
    each_data.append(token.surface)
data.append(each_data)
each_data = []
datastr = map(str, data[0])
s1 = "-"
wStr = s1.join(datastr)

print( wStr )



#C:>testjanome.py
#Traceback (most recent call last):
#  File "C:\Users\crt02621\Data\python\GetGoogleNews-master\testjanome.py", line 22, in <module>
#    wStr = ",".join(data)
#TypeError: sequence item 0: expected str instance, list found
#
#配列に文字列以外があると join でエラー
