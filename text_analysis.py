# -*- coding: utf-8 -*-
"""
Created on Fri Mar  1 21:54:11 2019

@author: Alexey
"""

import pymorphy2
import re
import matplotlib.pyplot as plt
import numpy as np

morph = pymorphy2.MorphAnalyzer()
p = morph.parse('пиву')[0]
print(p.normal_form)

REPLACE_BY_SPACE_RE = re.compile('[/(){}\[\]\|*@,;:...?!]')
BAD_SYMBOLS_RE = re.compile('[^0-9a-z #+_]')

file_object = open('t_don.txt', 'r') 
counter = 0
num_lines = 1000
km = 0

# split txt file

file_part = open('0.txt', 'w')
for i in file_object:
    if (i != '\n'):
        new_text = re.sub(REPLACE_BY_SPACE_RE, ' ', i)
        counter+=1;
        print(km, ": ", counter)
        file_part.write(new_text)
        if (counter > num_lines):
            file_part.close()
            km+=1
            print(km)
            file_part = open(str(km) + '.txt', 'w')
            counter = 0       
file_object.close()
    
dict_full_list = []
for ft in range(0,20):
    file_object  = open(str(ft) + '.txt', 'r') 
    part = []
    counter = 0
    words_type = []
    result_dict = {}
    for i in file_object:
        if (counter < num_lines) and (i != '\n'):
            new_text = re.sub(REPLACE_BY_SPACE_RE, ' ', i)
            counter+=1;
            print(counter)
            for k in new_text:
                p2 = morph.parse(k)[0].tag.POS
                if (p2 != None):
                    if (p2 in result_dict.keys()):
                        result_dict[p2]+=1
                    else:
                        result_dict[p2] = 1
    dict_full_list.append(result_dict)
    file_object.close()


#result_dict = {i:words_type.count(i) for i in words_type}
freq_list = []
for k in range(0,20):
    result_dict = dict_full_list[k]
    pos_list = []
    freq_pos = []
    for key, value in result_dict.items():
        pos_list.append(key)
        freq_pos.append(value)
    freq_list.append(freq_pos)

# DISPLAY RESULTS

f = plt.figure(1)
positions = np.arange(len(pos_list))
plt.bar(positions, freq_pos, align='center', alpha=0.5)
plt.xticks(positions, pos_list)
plt.ylabel('Usage')
plt.title('Programming language usage')
f.show()



#plt.show()