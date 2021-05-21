import sqlite3
# import pyvi
from pyvi import ViTokenizer, ViPosTagger, ViUtils

words = ViTokenizer.tokenize(u"Trường đại học bách khoa hà nội")
# print('words : ' )
# print(words)

words1 = ViPosTagger.postagging(ViTokenizer.tokenize(u"đổi tên thiết bị RE4-11/1 trong phòng khách thành đèn chùm."))
print('words1 : ' )
print(words1)

# words2 = ViUtils.remove_accents(u"Trường đại học bách khoa hà nội")
# print('words2 : ' )
# print(words2)

# words3 = ViUtils.add_accents(u'truong dai hoc bach khoa ha noi')
# print('words3 : ' )
# print(words3)