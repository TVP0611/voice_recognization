# def search(list, platform):
#     for i in range(len(list)):
#         if list[i] in platform:
#             return True
#     return False

# def setting(sentence_in):
#     device_key = open("phan_tich_ngon_ngu\devices.txt", encoding="utf8")
#     device_key = device_key.read()
#     device_key = device_key.split('\n')

#     a = 'là'
#     if a in sentence_in:
#         sentence_in.remove(a)

#     for i in sentence_in:
#         if search(device_key, i):
#             ind_device = sentence_in.index(i)

#         if 'tên' in i:
#             index_namechange = sentence_in.index(i)
#     answer = 'Thiết bị {0} đã dược đặt tên là {1}.'.format(sentence_in[ind_device], sentence_in[index_namechange +1])
#     return answer

# if __name__ == "__main__":
#     text = ['thiết_lập', 'RE4-11/1', 'trong', 'phòng', 'khách', 'tên', 'là', 'đèn_chùm', '.']
#     result = setting(text)
#     print(result)

# from inputimeout import inputimeout, TimeoutOccurred
# try:
#     something = inputimeout(prompt='>>', timeout=10)
# except TimeoutOccurred:
#     something = 'something'
# print(something)

# device_key = open("phan_tich_ngon_ngu\device_list.txt", encoding="utf8")
# device_key = device_key.read()
# device_key = device_key.split('\n')
# if "phòng bếp" in device_key:
#     print("find")


# import numpy as np
# # # x = [['phòng khách', 12], ['phòng bếp', 13]]
# # # np.savetxt('text.txt', x, fmt='%s', delimiter =':', encoding="utf-8")
 
# # # default dtype for  np.loadtxt is also floating point, change it, to be able to load mixed data.
# y = np.loadtxt('phan_tich_ngon_ngu/device_list.txt', dtype=np.object, encoding="utf-8", delimiter = ":")
# # if "phòng khách" in y:
#     # ind = y.index('phòng khách')
#     # print(y[ind])

# # a = [row[1] for row in y]

# m = np.where("phòng khách" in y) 
# # # print(y[1])
# # # print(y[0])

# print(y[m])
# print('done')

# from pyvi import ViTokenizer, ViPosTagger

# # ViTokenizer.tokenize(u"đe")

# m = ViPosTagger.postagging(ViTokenizer.tokenize(u"đèn ban công"))
# print(m)


# text = 'bật đèn chùm phòng khách'

# if 'đèn chùm' in text:
#     print('find')
# else:
#     print('no find')

# print('done')



# text = 'bật đèn chùm phòng khách'
# t1 = text.split('đèn chùm')
# print(t1)