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
for km in range(1,5):
    new_file = open(str(km) + '.txt', 'w')
    for i in file_object:
        if (counter < 1500) and (i != '\n'):
            new_text = re.sub(REPLACE_BY_SPACE_RE, ' ', i)
            counter+=1;
            print(km, ": ", counter)
            new_file.write(new_text)
    new_file.close()
        


file_object  = open('t_don.txt', 'r') 
part = []
counter = 0
words_type = []
result_dict = {}
for i in file_object:
    if (counter < 500) and (i != '\n'):
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

markers = ['* ЧАСТЬ ПЕРВАЯ *', '* ЧАСТЬ ВТОРАЯ *', '* ЧАСТЬ ТРЕТЬЯ *']
#result_dict = {i:words_type.count(i) for i in words_type}

pos_list = []
freq_pos = []
for key, value in result_dict.items():
    pos_list.append(key)
    freq_pos.append(value)

# DISPLAY RESULTS

f = plt.figure(1)
positions = np.arange(len(pos_list))
plt.bar(positions, freq_pos, align='center', alpha=0.5)
plt.xticks(positions, pos_list)
plt.ylabel('Usage')
plt.title('Programming language usage')
f.show()



#plt.show()