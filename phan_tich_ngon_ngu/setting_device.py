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


# import threading
# import time
  
# def run():
#     while True:
#         print('thread running')
#         global stop_threads
#         if stop_threads:
#             break
  
# stop_threads = False
# t1 = threading.Thread(target = run)
# t1.start()
# time.sleep(1)
# stop_threads = True
# t1.join()
# print('thread killed')

import threading
from threading import Condition
import time

def f(stop_event, event_obj):
    while True:
        # flag = condition_obj.acquire()
        # flag = event_obj.clear
        # flag = event_obj.is_set()
        if event_obj.is_set():
            # condition_obj.wait_for(flag, 5)
            print('thread await')
            time.sleep(5)
            print('end wait')
            # flag = False
            event_obj.clear()
            
            
        if stop_event.is_set():
            print ("Thread has been interrupted by an event.")
            return
        print ("Executing.")
        
        # time.sleep(0.25)

event_obj = threading.Event()
# condition_obj = threading.Condition()
stop_event = threading.Event()

t = threading.Thread(target=f, args=(stop_event, event_obj, ), daemon= True)
t.start()
while 1:
    sentences = input('>>')
    if sentences == 'stop':
        # time.sleep(2.0)
        stop_event.set()
        break
    elif sentences == 'pause':
        event_obj.set()
        
        # condition_obj.acquire()
        # condition_obj.notify()

# import threading

# done_counting = threading.Event()
# def count(done_counting):
#     i=0
#     while True:
#         i += 1
#         print (i)
#         done_counting.set()
    
# thread = threading.Thread(target=count, args=(done_counting, ))
# thread.start()
# print ("This may print before the event is set")
# done_counting.wait(5)
# print ("This will always print after the event is set")