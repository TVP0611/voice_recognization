import numpy as np
import collections
from numpy.core.defchararray import index
from numpy.core.numeric import count_nonzero
from inputimeout import inputimeout, TimeoutOccurred
import random

dv_name = np.loadtxt('phan_tich_ngon_ngu\code_seach_KW\key_word_devices_list.txt', dtype=np.object, encoding="utf-8", delimiter = ":")
dv_channel = np.loadtxt('phan_tich_ngon_ngu\code_seach_KW\device_channel.txt', dtype=np.object, encoding="utf-8", delimiter = ":")


words = 'van tưới 1'

# for dv in dv_channel[:16, 0]:
#     if dv in words:
dv_c = dv_channel[:16, 0]
ind_dv = np.where(dv_c==words)[0][0]
id_map_dv_name = dv_channel[ind_dv][2]
id_dv_name = dv_name[:, 0]
device_name = dv_name[np.where(id_dv_name==id_map_dv_name)[0][0], 1]

ind = np.where(words == dv_channel)[0]
for i in ind:
    id_name_devive = dv_channel[i, 2]
    device_name = dv_name[np.where(id_dv_name==id_name_devive)[0][0], 1]
    print(device_name)
# if ind > 0:
        #     print(ind)
    # save_value