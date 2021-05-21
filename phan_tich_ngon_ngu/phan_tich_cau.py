# region stt
    # words = ViTokenizer.tokenize(sentences)
    # words = list(words.split(" "))
    # # words
    # devices = ['RE4', 'DC']
    # for i in devices:
    #     if i in words:
    #         ind = words.index(i)
    #         words[ind: ind + 5] = [functools.reduce(lambda i, j: i + j, words[ind: ind + 5])]
    # setting_key = open("phan_tich_ngon_ngu\setting.txt", encoding="utf8")
    # setting_key = setting_key.read()
    # setting_key = setting_key.split('\n')
    # setting_mode = open('phan_tich_ngon_ngu\mode_setting.txt', encoding="utf8")
    # setting_mode = setting_mode.read()
    # setting_mode = setting_mode.split('\n')
    # for i in words:
    #     if search(setting_key, i):
    #         sentence =  setting(words)
    #         print(sentence)
    #         break
    #     if search(setting_mode, i):
    #         sentence =  setting(words)
    #         print(sentence)
    #         break
    # endregion

# from pyvi import ViTokenizer, ViPosTagger
# import functools
# from setting_device import setting
# from re import S
import threading
from inputimeout import inputimeout, TimeoutOccurred
import numpy as np

brk1 = 1
kw1, kw2 = '', ''
device = ''

#### load data
#region load data
kw_key_st = open("phan_tich_ngon_ngu\key_word_setting.txt", encoding="utf8")
kw_key_st = kw_key_st.read()
kw_key_st = kw_key_st.split('\n')

kw_key_on = open("phan_tich_ngon_ngu\key_word_on.txt", encoding="utf8")
kw_key_on = kw_key_on.read()
kw_key_on = kw_key_on.split('\n')

kw_key_off = open("phan_tich_ngon_ngu\key_word_off.txt", encoding="utf8")
kw_key_off = kw_key_off.read()
kw_key_off = kw_key_off.split('\n')

setting_key = open("phan_tich_ngon_ngu\setting.txt", encoding="utf8")
setting_key = setting_key.read()
setting_key = setting_key.split('\n')

# kw_key_dv = open("phan_tich_ngon_ngu\key_word_device.txt", encoding="utf8")
# kw_key_dv = kw_key_dv.read().split('\n')
# kw_key_dv = kw_key_dv.split('\n')

# devices_key = open("phan_tich_ngon_ngu\devices.txt", encoding="utf8")
# devices_key = devices_key.read()
# devices_key = devices_key.split('\n')

dv_name_room = np.loadtxt('phan_tich_ngon_ngu/device_list.txt', dtype=np.object, encoding="utf-8", delimiter = ":")
dv_channel = np.loadtxt('phan_tich_ngon_ngu/channel.txt', dtype=np.object, encoding="utf-8", delimiter = ":")

#endregion

def search(list, platform):
    for i in range(len(list)):
        if list[i] == platform:
            return True
    return False
    
def find_keywwords(words):
    for i in words:
        if i in kw_key_st:
            ind_keyword = words.index(i)
            kw1, kw2 =  ' '.join(words[ind_keyword - 1 : ind_keyword + 1]), ' '.join(words[ind_keyword : ind_keyword + 2])
            return kw1, kw2
        if i in kw_key_on:
            ind_keyword_on = words.index(i)
            kw1 = ['on', ind_keyword_on]
            kw2 = i 
            return kw1, kw2
        if i in kw_key_off:
            ind_keyword_off = words.index(i)
            kw1 = ['on', ind_keyword_off]
            kw2 = i
            return kw1, kw2


while 1:

    sentences = input('>>')
    sentences = sentences.lower()
    if len(sentences) > 0:
        words = sentences.split(" ")
        kw1, kw2 = find_keywwords(words)

        ###### control
        if kw1[0] == 'on' and len(kw1) > 0:
            count_word = len(words)
            if count_word > 2:
                sentence_kw = ' '.join(words[kw1[1] :])
                channel_name = [row[0] for row in dv_channel]
                for ch_n in channel_name:
                    if ch_n in sentence_kw:
                        sentence_kw = sentence_kw.split(ch_n)[1]
                        print(sentence_kw)
                        channel_name_ind = dv_channel[np.where(ch_n in dv_channel)]
                        if len(sentence_kw) > 0:
                            for dv_n_r in dv_name_room:
                                pass         


        elif kw1 == 'off' and len(kw1) > 0:
            count_word = len(words)



        ###### Setting
        elif len(kw2) > 0 and kw2 in setting_key:
            print("Bạn muốn {0} thiết bị nào?".format(kw2))
            print("waitting.....")
            try:
                device = inputimeout(prompt='>>', timeout=10)
            except TimeoutOccurred:
                something = "Không nhận được tên thiết bị"
                print(something)

            if len(device)> 0:    
                if search(devices_key, device):
                    print("Tên thiết bị là {0}".format(device))
                    print("Bạn muốn ")

        elif len(kw1) > 0 and kw1 in setting_key:
            print("Bạn muốn {0} thiết bị nào?".format(kw1))
            print("waitting RF or voice.....")
            try:
                device = inputimeout(prompt='>>', timeout=10)
            except TimeoutOccurred:
                something = "Không nhận được tên thiết bị"
                print(something)

            if len(device)> 0:
                if search(devices_key, device):
                    print("Tên thiết bị là {0}".format(device))
                    print("Bạn muốn ")

        else:
            print("Từ khóa không có trong cơ sở dữ liệu")
            print("\U00002764 \U00002764 \U00002764  Bạn vui lòng nói hoặc nhập lại \U00002764 \U00002764 \U00002764")
            # print(u'\U00002764 \U00002764 \U00002764')

print("done")