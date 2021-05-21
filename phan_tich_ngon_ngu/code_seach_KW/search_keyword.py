# from re import S
import re
import numpy as np
import collections
from numpy.core.defchararray import index
from numpy.core.numeric import count_nonzero
from inputimeout import inputimeout, TimeoutOccurred
import random

list_word = []
data_cmd = []

MCE = '00000001'

#### mẫu phản hồi khi gợi ý
YES = ['đúng rồi', 'yes', 'ok', 'vâng', 'đúng']
NO = ['tắt', 'sai', 'không', 'no', 'sai rồi']

kw_media = open("phan_tich_ngon_ngu\code_seach_KW\key_word_media.txt", encoding="utf8")
kw_media = kw_media.read()
kw_media = kw_media.split('\n')

kw_on = open("phan_tich_ngon_ngu\code_seach_KW\key_word_on.txt", encoding="utf8")
kw_on = kw_on.read()
kw_on = kw_on.split('\n')

kw_off = open("phan_tich_ngon_ngu\code_seach_KW\key_word_off.txt", encoding="utf8")
kw_off = kw_off.read()
kw_off = kw_off.split('\n')

kw_setting = open("phan_tich_ngon_ngu\code_seach_KW\key_word_setting.txt", encoding="utf8")
kw_setting = kw_setting.read()
kw_setting = kw_setting.split('\n')

dv_name = np.loadtxt('phan_tich_ngon_ngu\code_seach_KW\key_word_devices_list.txt', dtype=np.object, encoding="utf-8", delimiter = ":")
dv_channel = np.loadtxt('phan_tich_ngon_ngu\code_seach_KW\device_channel.txt', dtype=np.object, encoding="utf-8", delimiter = ":")

def data_command(stt, device_type, channel):
    type = {"RE4": 4, "RE3": 3, "RE2": 2}
    # stt = check_status(setstatus, device_type)
    m = type[device_type.split('|')[0]]
    n = ':'
    h = 'X'
    ls = []
    for i in range(m):
        ls.append(h)
    ls[channel - 1] = stt
    ls_new = n.join(ls)
    return ls_new

def search_kw_in_sentence(sentence):
    for w in sentence:
        if w in kw_on:
            mode_kw = "on"
            ind_kw = sentence.index(w)
            words =  ' '.join(sentence[ind_kw + 1:])
            text = ' '.join(sentence[ind_kw : ind_kw+2])
            if text in kw_media:
                mode_kw = 'on_media'
                return mode_kw
            list_word.append(w)
            list_word.append(words)
            return mode_kw, list_word
            
        elif w in kw_off:
            mode_kw = "off"
            ind_kw = sentence.index(w)
            words =  ' '.join(sentence[ind_kw + 1:])
            text = ' '.join(sentence[ind_kw : ind_kw+2])
            if text in kw_media:
                mode_kw = 'off_media'
                return mode_kw
            list_word.append(w)
            list_word.append(words)
            return mode_kw, list_word
    for kw in kw_setting:
        sentence = ' '.join(sentence)
        if kw in sentence:
            mode_kw = 'setting'
            words = sentence.split(kw + " ")
            # words =  ' '.join(sentence[ind_kw:])
            # list_word.append(w)
            list_word.append(words[1])
            return mode_kw , list_word

def media(words):
    pass

def on(words):
    name_dv_trung_lap = []
    setstatus = 'ON'
    dv_c = dv_channel[:16, 0]
    for dv in dv_channel[:16, 0]:
        if dv in words:
            #### mapping id device_channel to devive
            ind_trung_lap = np.where(words == dv_channel[:16, 0])[0]
            # for i in ind:
                # id_name_devive = dv_channel[i, 2]
            ind_dv = np.where(dv_c==dv)[0][0]
            id_map_dv_name = dv_channel[ind_dv][2]
            id_dv_name = dv_name[:, 0]
            device_name = dv_name[np.where(id_dv_name==id_map_dv_name)[0][0], 1]
            channel_data = dv_channel[ind_dv][1]
            count = np.count_nonzero(dv_c==dv)
            text = words.split(dv)[-1]
            
            if count == 1:
                if len(text) > 0:
                    for dv_n in dv_name[:,1]:
                        if dv_n in text:
                            device_type = dv_name[np.where(id_dv_name==id_map_dv_name)[0][0], 2]
                        data_cmd = data_command(setstatus, device_type, int(channel_data))
                        command = MCE + '|' + device_type + '|' + channel_data + '|' + "setstatus" + '|' + data_cmd
                        print("{0} đã được {1}".format(dv, random.choice(kw_on[:2])))
                        print(command)
                        list_word.clear()
                        return command
                else:
                    ###### gợi ý
                        print('Có phải bạn muốn {0} {1} {2}?'.format(random.choice(kw_on[:2]), dv, device_name))
                        try:
                            phan_hoi = inputimeout(prompt='>>', timeout=10)
                        except TimeoutOccurred:
                            print("Không nhận được phản hồi ")
                            list_word.clear()
                            break

                        if phan_hoi in YES:
                            device_type = dv_name[np.where(id_dv_name==id_map_dv_name)[0][0], 2]
                            data_cmd = data_command(setstatus, device_type, int(channel_data))
                            command = MCE + '|' + device_type + '|' + channel_data + '|' + "setstatus" + '|' + data_cmd
                            print("{0} đã được {1}".format(dv, random.choice(kw_on[:2])))
                            print(command)
                            list_word.clear()
                            return command
                        elif phan_hoi in NO:
                            command = None
                            list_word.clear()
                            break
            elif count >= 2:
                for i in ind_trung_lap:
                    id_name_devive = dv_channel[i, 2]
                    device_name = dv_name[np.where(id_dv_name==id_name_devive)[0][0], 1]
                    name_dv_trung_lap.append(device_name)
                print('Phát hiện sự trùng lặp trong danh sách thiết bị')
                print('Có phải bạn muốn {0} {1} {2}?'.format(random.choice(kw_on[:2]), dv, " hay ".join(name_dv_trung_lap)))
                try:
                    phan_hoi = inputimeout(prompt='>>', timeout=10)
                except TimeoutOccurred:
                    print("không nhận được phản hồi")
                    list_word.clear()
                    list_word.clear()
                    break
                if phan_hoi in dv_name:
                    device_type = dv_name[np.where(dv_name==phan_hoi)[0][0], 2]
                    data_cmd = data_command(setstatus, device_type, int(channel_data))
                    command = MCE + '|' + device_type + '|' + channel_data + '|' + "setstatus" + '|' + data_cmd
                    print("{0} đã được {1}".format(dv, random.choice(kw_on[:2])))
                    print(command)
                    list_word.clear()
                    return command


def off(words):
    name_dv_trung_lap = []
    setstatus = 'OFF'
    dv_c = dv_channel[:16, 0]
    for dv in dv_channel[:16, 0]:
        if dv in words:
            #### mapping id device_channel to devive
            ind_trung_lap = np.where(words == dv_channel[:16, 0])[0]
            # for i in ind:
                # id_name_devive = dv_channel[i, 2]
            ind_dv = np.where(dv_c==dv)[0][0]
            id_map_dv_name = dv_channel[ind_dv][2]
            id_dv_name = dv_name[:, 0]
            device_name = dv_name[np.where(id_dv_name==id_map_dv_name)[0][0], 1]
            channel_data = dv_channel[ind_dv][1]
            count = np.count_nonzero(dv_c==dv)
            text = words.split(dv)[-1]
            
            if count == 1:
                if len(text) > 0:
                    for dv_n in dv_name[:,1]:
                        if dv_n in text:
                            device_type = dv_name[np.where(id_dv_name==id_map_dv_name)[0][0], 2]
                        data_cmd = data_command(setstatus, device_type, int(channel_data))
                        command = MCE + '|' + device_type + '|' + channel_data + '|' + "setstatus" + '|' + data_cmd
                        print("{0} đã được {1}".format(dv, random.choice(kw_off[:4])))
                        print(command)
                        list_word.clear()
                        return command
                else:
                    ###### gợi ý
                        print('Có phải bạn muốn {0} {1} {2}?'.format(random.choice(kw_off[:4]), dv, device_name))
                        try:
                            phan_hoi = inputimeout(prompt='>>', timeout=10)
                        except TimeoutOccurred:
                            print("Không nhận được phản hồi ")
                            list_word.clear()
                            break

                        if phan_hoi in YES:
                            device_type = dv_name[np.where(id_dv_name==id_map_dv_name)[0][0], 2]
                            data_cmd = data_command(setstatus, device_type, int(channel_data))
                            command = MCE + '|' + device_type + '|' + channel_data + '|' + "setstatus" + '|' + data_cmd
                            print("{0} đã được {1}".format(dv, random.choice(kw_off[:4])))
                            print(command)
                            list_word.clear()
                            return command
                        elif phan_hoi in NO:
                            command = None
                            list_word.clear()
                            break
            elif count >= 2:
                for i in ind_trung_lap:
                    id_name_devive = dv_channel[i, 2]
                    device_name = dv_name[np.where(id_dv_name==id_name_devive)[0][0], 1]
                    name_dv_trung_lap.append(device_name)
                print('Phát hiện sự trùng lặp trong danh sách thiết bị')
                print('Bạn muốn {0} ở {1} {2}?'.format(random.choice(kw_off[:4]), dv, " hay ".join(name_dv_trung_lap)))
                try:
                    phan_hoi = inputimeout(prompt='>>', timeout=10)
                except TimeoutOccurred:
                    print("không nhận được phản hồi")
                    list_word.clear()
                    break
                if phan_hoi in dv_name:
                    device_type = dv_name[np.where(dv_name==phan_hoi)[0][0], 2]
                    data_cmd = data_command(setstatus, device_type, int(channel_data))
                    command = MCE + '|' + device_type + '|' + channel_data + '|' + "setstatus" + '|' + data_cmd
                    print("{0} đã được {1}".format(dv, random.choice(kw_off[:4])))
                    print(command)
                    list_word.clear()
                    return command


def setting(words):
    
    pass

sentence = 'thiết lập RE4|1'
sentence = sentence.lower()
if len(sentence) > 0:
    words = sentence.split(" ")

mode_kw, list_word = search_kw_in_sentence(words)
# print(mode_kw)
if mode_kw == 'on':
    if len(list_word[1]) >= 1:
        cmd_data = on(list_word[1])

elif mode_kw == 'off':
    if len(list_word[1]) >= 1:
        cmd_data = off(list_word[1])

elif mode_kw == 'setting':
    setting()

elif mode_kw == 'on_media' or mode_kw == 'off_media':
    media()