#!/usr/bin/env python
# -*-  coding: utf-8  -*-
import sys
import os


# give input folder name here, containing text files
path = "/mnt/mydisk/Manipuri MT/WebScrap/Newspaper to text /mn newspaper 2023- text raw"
print(path)
# give output folder name here, output text files will be generated here
path_op = "/mnt/mydisk/Manipuri MT/WebScrap/Newspaper to text /newspaper corpus"
dir_count = 0
subdir_count = 0
files = os.listdir(path)
print(len(files))
for name in files:
    try:
        print("printing names")
        print(name)
        if name=='.DS_Store':
            continue
        # d = path + "/" + name
        # print("printing d")
        # print(d)
        # do = path_op + "/" + name
        # print("Printing do")
        # print(do)
        # if not os.path.exists(do):
        #     print("inside")
        #     os.makedirs(do)
        # dir_count += 1
        #sub_files = os.listdir(d)
        i=0
        for i in range(0,1):
            # subdir_count += 1
            # print d + "/" + sub
            dir_ip = path+'/'+name
            #dir_ip = d + "/" + sub
            #dir_op = do + "/" + sub
            dir_op = path_op+"/"+name
            fo = open(dir_op, "w")
            with open(dir_ip) as f:
                lines = f.readlines()
                for sen in lines:
                    print(sen)
                    text = sen
                    word_list = text.split()
                    # sangai express
                    dict = {'Òü': 'ই', 'l¡ü': 'উ', 'B¡': 'ক্ক', 'E': 'ক্ৱ', 'A¡': 'ক', 'A': 'ক', 'ÑH': 'স্ক', '{': 'ি',
                            'Ê¡': 'ষ্ট', 'ü': '', 'þ': 'ক', '•': 'ন', 'I': 'ক্র', 'B': 'ক্ক', 'T': 'ঙ্খ',  'j': 'ট্ট',
                            'yû¡': 'ক্র', 'œ¡': 'প্ত', 'A¢¡': 'র্ক', 'G': 'ক্স', 'â«': 'ত্ব', 'x': 'ত্থ', 'Ð': 'স্ট', '¼': 'ল্গ',
                            'r': 'ণ্ড', 'û': 'ণ', 'Â': 'ল্', 'ê': 'ূ', '”': 'ন্', '$': 'ঊ', '`': 'জ্ঞ', 'u': 'ত্ম', ']' : '',
                            'U': 'ঙ্গ', 'k': 'ঠ', 'ö': 'র', '«': '্ব', '”z': 'ন্ত', '¶': 'ম', '¸': '্য', 'æ': 'ু', 'a': 'জ্ব',
                            '”‚': 'ন্থ', 'H': '', '‚': 'থ', '‘': '"', '’': '"', 'Q': 'ঘ', 'õ': 'ৃ', 'S': 'ঙ্ক', ' ': ' ',
                            '¤Ã': 'ব্ল', 'Ç¡': 'শু', 'v¡û¡': 'ক্ত', '³¢': 'র্ম', '‹': 'ধ', 'Û¡': 'ক্ষ', 'v¡û': 'ক্ত', 'b': 'জ্র',
                            '¾': 'ল্ব', 'Á': 'ল্ড', 'F': 'ক্ম', 'ò': 'ঁ', '+': 'ঔ', 'f': 'ন্স', '¿': 'ল্', 'ˆ': 'দ্ম', 'Ç': 'শু',
                            '´š': 'ম্প', '‰': 'দ্র', '»': 'ল্ক', 'Á¡': 'ল্ড', 'Ñ|': 'স্ত্র', '™': 'য', 'Ÿ': 'প্', 'ÒÇü': 'ইশু',
                            '–i¡': 'ন্ট', 'ð': 'জ্জ', '„': 'দ্দ', 'ß': 'প্র', 'y': 'ত্র', 'â': 'ত্',  'L': 'গ্গ', '“': 'ন্ড',
                            'Ñ': 'স্', 'Ñš': 'স্প', 'e': 'ঞ্চ', 'v': 'ত্ত', 'Ø': 'ড়', 'W': 'চ', 'á': 'ছ', '#': 'ঈ', '%': '%',
                            'z': 'ও', 'Õ': 'ক্ষ', 'ô': '', '|': 'ত্র', 'ý': 'ধ', 'Þ': 'ন্', 'V': 'ঙ্', '/': 'ব্', '­': '',
                            'W¡': 'চ', 'R¡': 'ঙ', 'i¡': 'ট', 'i': 'ট', 't¡': 'ত', 'C¡': 'ক্ট', 'v¡': 'ত্ত', 'ø': '্র',
                            'Ì': 'ষ্ণ', 'C': 'ক্ট', 'ç': 'ু', 'c': 'ঝ', 'Z': 'চ্', 'ÿ': '', '÷': 'র', '‡': 'দ্ব', 'd': 'ঞ',
                            '£¡': 'ফ', '£': 'ফ', 'ó¡': 'ফ', 'ó': 'ফ', 'ç¡': 'ু', 'óø¡': 'ফ্র', 'N': 'গ', '‡ý': 'দ্ধ',
                            '"': 'অ', 'à': 'া', '[': 'ি', 'ã': 'ী', 'å': 'ু', 'è¡': 'ূ', 'è': 'ূ', 'Ô': 'হ্ব', 'n': 'ঢ',
                            '&': 'এ', 'ë': 'ে', 'ì': 'ে', "'": 'ঐ', 'í': 'ৈ', 'î': 'ৈ', '*': 'ও', ';': 'ৎ', '}': 'ং',
                            'J': 'খ', 'K': 'গ', 't': 'ত', 'Æµ': 'শ্ম', 'µ': 'ম', '¢': 'র্', '¢¡': 'র্', '¯': 'ৱ', '¡': '',
                            'o': 'ণ', '>': 'ন', '=': 'থ', '>': 'ন', 'g': 'ঞ্জ', 'Þê': 'ন্ধ', 'é': '', 'œ': 'প্ত', 'ñ': 'ও',
                            'š': 'প', 'Ù': 'প্প', '¤': 'ব', '¬': 'ব', '®': 'ভ', 'Øn': 'ঢ়', '›': 'প্স', '¦': 'ব্দ', '˜': 'ঋ',
                            '³': 'ম', '´': 'ম্', 'Ú': 'য়', '¹': 'র', 'Å': 'শ', 'ï': '', 'R': 'ঙ', 'Ý': 'ক্ষ্ণ', 'Æ': 'শ',
                            'Î': 'স', 'Ê': 'স্', 'Ò': 'হ', '@': 'ঃ', 'È': 'ষ', 'ƒ': 'দ', 'º': 'ল', '\\': 'জ', 'É': 'ষ্ব',
                            'À': 'ল্ল', 'Ã¡': 'ল', 'Ã': 'ল', '–': 'ন্', '—¡': 'ন', '—': 'ন', 'Ä': 'ন্ন', 'X': 'ন্স',
                            'P': 'গু', '×': 'হু', 'M': 'গ্ব', 'Ë': 'ষ্ঠ', 'Ü': 'ক্ষ্ম', 'sn': 'ণ্ঢ', '±': 'ম্ভ', 'Ó': 'হ্ল',
                            'ìà': 'ো', 'ëà': 'ো', 'ìï': 'ৌ', 'ëï': 'ৌ', 'l': 'ড', 'l¡': 'ড', 'Øl¡': 'ড়', 'Š':'দ্ভ',
                            '0': '০', '1': '১', '2': '২', '3': '৩', '4': '৪', '5': '৫', '6': '৬', '7': '৭', '8': '৮','O':'O','q':'q','Í':'ৈ',
                            '9': '৯', 'ú': ' ।', ',': ',','¡³':'ম', 'X':'ন্স','':'','Y':'Y','o':'o',
                            '-': '-', '(': '(', ')': ')', '.': '.', '?': '?', ':': ':','':'','D':'D','¶':'ম', '':' ', '!': '!','¥':'্ন','x':'ত্থ','e':'e','h':'h','w':'w','m':'m','s':'s','a':'a','i':'i','l':'l','p':'p','r':'r','o':'o','t':'t','c':'c','d':'d'}
                
                    post_sym = ['ি', 'ে', 'ৈ']

                    pre_sym = ['র্']

                    comp_sym = ['ক্ক', 'ক্ৱ', 'স্ক', 'দ্ম', 'ষ্ঠ', 'ষ্ট', 'ক্র', 'ক্ক', 'ঙ্খ', 'ট্ট', 'ত্ম', 'গ্ব', 'ক্র','দ্ভ',
                                'প্ত', 'র্ক', 'ক্স', 'ত্ব',
                                'ত্থ', 'ত্র', 'ক্ষ্ম', 'ল্গ', 'ণ্ড', 'জ্ঞ', 'ল্ড', 'প্র', 'গ্গ', 'জ্ব', 'ঙ্গ', 'ন্ত', 'ত্র',
                                'ন্ড', 'ন্থ', 'ঙ্ক', 'ণ্ঢ',
                                'ব্ল', 'ক্ত', 'র্ম', 'ক্ষ', 'ক্ত', 'ল্ব', 'স্ট', 'ম্প', 'দ্র', 'ল্ক', 'ল্ড', 'স্ত্র', 'ন্ট',
                                'জ্জ', 'দ্দ', 'স্প', 'ঞ্চ',
                                'ত্ত', 'ক্ষ', 'ক্ট', 'ষ্ণ', 'ক্ট', 'ষ্ব', 'ফ্র', 'দ্ধ', 'ম্ভ', 'হ্ব', 'শ্ম', 'ক্ষ্ণ', 'ঞ্জ',
                                'ন্ধ', 'ক্ম', 'ন্স', 'প্প',
                                'প্স', 'দ্ব', 'প্ত', 'হ্ল', 'ব্দ', 'ল্ল', 'ন্ন', 'ন্স', 'জ্র']
                    text_op = ""
                    for word in word_list:
                        translate = ""
                        if "www." in word or ".in" in word:
                            text_op = text_op + word
                            continue
                        word = word.decode('utf-8')
                        print("Printing word")
                        print(word)
                        print("Printing file name")
                        print(name)
                        # if '[email protected]' in word:
                        #     print("&&&&&&&&&&&&&&&")
                        #     word=word.replace("[email protected]", " ") 

                        w = list(word)
                        i = 0
                        t = -1
                        c = ""
                        temp = ""
                        flag = 0
                        flag1 = 0
                        while i < len(w):
                            if flag1 == 1 and (
                                    w[i] == "à".decode('utf-8') or w[i] == "ï".decode('utf-8')):  # for okara and aukara
                                c = w[i].encode('utf-8')
                                print(c)
                                # print(dict[c])
                                translate = translate + temp
                                temp = ""
                                flag1 = 0
                                i = i + 1
                            elif ((i + 2) < len(w)) and (
                                    (w[i] == "ì".decode('utf-8') and w[i + 2] == "à".decode('utf-8')) or (
                                    w[i] == "ë".decode('utf-8') and w[i + 2] == "à".decode('utf-8'))):  # for okara
                                c = w[i] + w[i + 2]
                                c = c.encode('utf-8')
                                print(c)
                                #print(dict[c])
                                temp = dict[c]
                                flag1 = 1
                                i = i + 1
                            elif ((i + 3) < len(w)) and ((w[i] == "ì".decode('utf-8') and w[i + 2] == "¡".decode(
                                    'utf-8') and w[i + 3] == "à".decode('utf-8')) or (
                                                                w[i] == "ë".decode('utf-8') and w[i + 2] == "¡".decode(
                                                                'utf-8') and w[i + 3] == "à".decode(
                                                                'utf-8'))):  # for okara
                                c = w[i] + w[i + 3]  # between is a multi symbol
                                c = c.encode('utf-8')
                                print(c)
                                #print(dict[c])
                                temp = dict[c]
                                flag1 = 1
                                i = i + 1
                            elif ((i + 2) < len(w)) and ((
                                    w[i] == "ì".decode('utf-8') and w[i + 2] == "ï".decode('utf-8')) or (
                                    w[i] == "ë".decode('utf-8') and w[i + 2] == "ï".decode('utf-8'))):  # for aukara
                                c = w[i] + w[i + 2]
                                c = c.encode('utf-8')
                                print(c)
                                #print(dict[c])
                                temp = dict[c]
                                flag1 = 1
                                i = i + 1
                            elif ((i + 3) < len(w)) and (
                                    w[i] == "ì".decode('utf-8') and w[i + 2] == "¡".decode('utf-8') and w[
                                i + 3] == "ï".decode('utf-8') or (
                                            w[i] == "ë".decode('utf-8') and w[i + 2] == "¡".decode('utf-8') and w[
                                        i + 3] == "ï".decode('utf-8'))):  # for aukara
                                c = w[i] + w[i + 3]  # between is a multi symbol
                                c = c.encode('utf-8')
                                print(c)
                                #print(dict[c])
                                temp = dict[c]
                                flag1 = 1
                                i = i + 1
                            elif ((i + 3) < len(w)) and w[i] == "v".decode('utf-8') and w[i + 1] == "¡".decode('utf-8') and \
                                    w[i + 2] == "û".decode('utf-8') and w[i + 3] == '¡'.decode('utf-8'):
                                c = w[i] + w[i + 1] + w[i + 2] + w[i + 3]
                                c = c.encode('utf-8')
                                print(c)
                                #print(dict[c])
                                if flag == 1:
                                    translate = translate + dict[c] + temp
                                    temp = ""
                                    flag = 0
                                else:
                                    translate = translate + dict[c]
                                c = ""
                                i = i + 4
                            # Single and double characters
                            elif ((i + 1) < len(w)) and (w[i] == "Ò".decode('utf-8') and w[i + 1] == "ü".decode('utf-8')):
                                c = w[i] + w[i + 1]
                                c = c.encode('utf-8')
                                print(c)
                                #print(dict[c])
                                if flag == 1:
                                    translate = translate + dict[c] + temp
                                    temp = ""
                                    flag = 0
                                else:
                                    translate = translate + dict[c]
                                c = ""
                                i = i + 2
                            elif ((i + 1) < len(w)) and (w[i] == "s".decode('utf-8') and w[i + 1] == "n".decode('utf-8')):
                                c = w[i] + w[i + 1]
                                c = c.encode('utf-8')
                                print(c)
                                print(dict[c])
                                if flag == 1:
                                    translate = translate + dict[c] + temp
                                    temp = ""
                                    flag = 0
                                else:
                                    translate = translate + dict[c]
                                c = ""
                                i = i + 2
                            elif ((i + 1) < len(w)) and (w[i] == "Þ".decode('utf-8') and w[i + 1] == "ê".decode('utf-8')):
                                c = w[i] + w[i + 1]
                                c = c.encode('utf-8')
                                print(c)
                                print(dict[c])
                                if flag == 1:
                                    translate = translate + dict[c] + temp
                                    temp = ""
                                    flag = 0
                                else:
                                    translate = translate + dict[c]
                                c = ""
                                i = i + 2
                            elif ((i + 1) < len(w)) and (w[i] == "Ø".decode('utf-8') and w[i + 1] == "n".decode('utf-8')):
                                c = w[i] + w[i + 1]
                                c = c.encode('utf-8')
                                print(c)
                                #print(dict[c])
                                if flag == 1:
                                    translate = translate + dict[c] + temp
                                    temp = ""
                                    flag = 0
                                else:
                                    translate = translate + dict[c]
                                c = ""
                                i = i + 2
                            elif ((i + 1) < len(w)) and (w[i] == "‡".decode('utf-8') and w[i + 1] == "ý".decode('utf-8')):
                                c = w[i] + w[i + 1]
                                c = c.encode('utf-8')
                                print(c)
                                #print(dict[c])
                                if flag == 1:
                                    translate = translate + dict[c] + temp
                                    temp = ""
                                    flag = 0
                                else:
                                    translate = translate + dict[c]
                                c = ""
                                i = i + 2
                            elif ((i + 2) < len(w)) and (
                                    w[i] == "l".decode('utf-8') and w[i + 1] == "¡".decode('utf-8') and w[
                                i + 2] == "ü".decode('utf-8')):
                                c = w[i] + w[i + 1] + w[i + 2]
                                c = c.encode('utf-8')
                                print(c)
                                print(dict[c])
                                if flag == 1:
                                    translate = translate + dict[c] + temp
                                    temp = ""
                                    flag = 0
                                else:
                                    translate = translate + dict[c]
                                c = ""
                                i = i + 3
                            elif ((i + 1) < len(w)) and (w[i] == "l".decode('utf-8') and w[i + 1] == "¡".decode('utf-8')):
                                c = w[i] + w[i + 1]
                                c = c.encode('utf-8')
                                print(c)
                                #print(dict[c])
                                if flag == 1:
                                    translate = translate + dict[c] + temp
                                    temp = ""
                                    flag = 0
                                else:
                                    translate = translate + dict[c]
                                c = ""
                                i = i + 2
                            elif ((i + 1) < len(w)) and (w[i] == "Ñ".decode('utf-8') and w[i + 1] == "š".decode('utf-8')):
                                c = w[i] + w[i + 1]
                                c = c.encode('utf-8')
                                print(c)
                                #print(dict[c])
                                if flag == 1:
                                    translate = translate + dict[c] + temp
                                    temp = ""
                                    flag = 0
                                else:
                                    translate = translate + dict[c]
                                c = ""
                                i = i + 2
                            elif ((i + 2) < len(w)) and (
                                    w[i] == "–".decode('utf-8') and w[i + 1] == "i".decode('utf-8') and w[
                                i + 2] == "¡".decode('utf-8')):
                                c = w[i] + w[i + 1] + w[i + 2]
                                c = c.encode('utf-8')
                                print(c)
                                #print(dict[c])
                                if flag == 1:
                                    translate = translate + dict[c] + temp
                                    temp = ""
                                    flag = 0
                                else:
                                    translate = translate + dict[c]
                                c = ""
                                i = i + 3
                            elif ((i + 2) < len(w)) and w[i] == "v".decode('utf-8') and w[i + 1] == "¡".decode('utf-8') and \
                                    w[i + 2] == "û".decode('utf-8'):
                                c = w[i] + w[i + 1] + w[i + 2]
                                c = c.encode('utf-8')
                                print(c)
                                #print(dict[c])
                                if flag == 1:
                                    translate = translate + dict[c] + temp
                                    temp = ""
                                    flag = 0
                                else:
                                    translate = translate + dict[c]
                                c = ""
                                i = i + 3
                            elif ((i + 1) < len(w)) and (w[i] == "Ñ".decode('utf-8') and w[i + 1] == "|".decode('utf-8')):
                                c = w[i] + w[i + 1]
                                c = c.encode('utf-8')
                                print(c)
                                #print(dict[c])
                                if flag == 1:
                                    translate = translate + dict[c] + temp
                                    temp = ""
                                    flag = 0
                                else:
                                    translate = translate + dict[c]
                                c = ""
                                i = i + 2
                            elif ((i + 1) < len(w)) and (w[i] == "”".decode('utf-8') and w[i + 1] == "z".decode('utf-8')):
                                c = w[i] + w[i + 1]
                                c = c.encode('utf-8')
                                print(c)
                                #print(dict[c])
                                if flag == 1:
                                    translate = translate + dict[c] + temp
                                    temp = ""
                                    flag = 0
                                else:
                                    translate = translate + dict[c]
                                c = ""
                                i = i + 2
                            elif ((i + 1) < len(w)) and (w[i] == "Æ".decode('utf-8') and w[i + 1] == "µ".decode('utf-8')):
                                c = w[i] + w[i + 1]
                                c = c.encode('utf-8')
                                print(c)
                                #print(dict[c])
                                if flag == 1:
                                    translate = translate + dict[c] + temp
                                    temp = ""
                                    flag = 0
                                else:
                                    translate = translate + dict[c]
                                c = ""
                                i = i + 2
                            elif ((i + 1) < len(w)) and (w[i] == "Á".decode('utf-8') and w[i + 1] == "¡".decode('utf-8')):
                                c = w[i] + w[i + 1]
                                c = c.encode('utf-8')
                                print(c)
                                #print(dict[c])
                                if flag == 1:
                                    translate = translate + dict[c] + temp
                                    temp = ""
                                    flag = 0
                                else:
                                    translate = translate + dict[c]
                                c = ""
                                i = i + 2
                            elif ((i + 2) < len(w)) and (
                                    w[i] == "l".decode('utf-8') and w[i + 1] == "¡".decode('utf-8') and w[
                                i + 2] == "ü".decode('utf-8')):
                                c = w[i] + w[i + 1] + w[i + 2]
                                c = c.encode('utf-8')
                                print(c)
                                #print(dict[c])
                                if flag == 1:
                                    translate = translate + dict[c] + temp
                                    temp = ""
                                    flag = 0
                                else:
                                    translate = translate + dict[c]
                                c = ""
                                i = i + 3
                            elif ((i + 1) < len(w)) and (w[i] == "B".decode('utf-8') and w[i + 1] == "¡".decode('utf-8')):
                                c = w[i] + w[i + 1]
                                c = c.encode('utf-8')
                                print(c)
                                #print(dict[c])
                                if flag == 1:
                                    translate = translate + dict[c] + temp
                                    temp = ""
                                    flag = 0
                                else:
                                    translate = translate + dict[c]
                                c = ""
                                i = i + 2
                            elif ((i + 1) < len(w)) and (w[i] == "¡".decode('utf-8') and w[i + 1] == "³".decode('utf-8')):
                                c = w[i] + w[i + 1]
                                c = c.encode('utf-8')
                                print(c)
                                #print(dict[c])
                                if flag == 1:
                                    translate = translate + dict[c] + temp
                                    temp = ""
                                    flag = 0
                                else:
                                    translate = translate + dict[c]
                                c = ""
                                i = i + 2
                            elif ((i + 1) < len(w)) and (w[i] == "Ñ".decode('utf-8') and w[i + 1] == "H".decode('utf-8')):
                                c = w[i] + w[i + 1]
                                c = c.encode('utf-8')
                                print(c)
                                #print(dict[c])
                                if flag == 1:
                                    translate = translate + dict[c] + temp
                                    temp = ""
                                    flag = 0
                                else:
                                    translate = translate + dict[c]
                                c = ""
                                i = i + 2
                            elif ((i + 1) < len(w)) and (w[i] == "Ê".decode('utf-8') and w[i + 1] == "¡".decode('utf-8')):
                                c = w[i] + w[i + 1]
                                c = c.encode('utf-8')
                                print(c)
                                #print(dict[c])
                                if flag == 1:
                                    translate = translate + dict[c] + temp
                                    temp = ""
                                    flag = 0
                                else:
                                    translate = translate + dict[c]
                                c = ""
                                i = i + 2
                            elif ((i + 1) < len(w)) and (w[i] == "”".decode('utf-8') and w[i + 1] == "‚".decode('utf-8')):
                                c = w[i] + w[i + 1]
                                c = c.encode('utf-8')
                                print(c)
                                #print(dict[c])
                                if flag == 1:
                                    translate = translate + dict[c] + temp
                                    temp = ""
                                    flag = 0
                                else:
                                    translate = translate + dict[c]
                                c = ""
                                i = i + 2
                            elif ((i + 2) < len(w)) and (
                                    w[i] == "y".decode('utf-8') and w[i + 1] == "û".decode('utf-8') and w[
                                i + 2] == "¡".decode('utf-8')):
                                c = w[i] + w[i + 1] + w[i + 2]
                                c = c.encode('utf-8')
                                print(c)
                                #print(dict[c])
                                if flag == 1:
                                    translate = translate + dict[c] + temp
                                    temp = ""
                                    flag = 0
                                else:
                                    translate = translate + dict[c]
                                c = ""
                                i = i + 3
                            elif ((i + 1) < len(w)) and (w[i] == "œ".decode('utf-8') and w[i + 1] == "¡".decode('utf-8')):
                                c = w[i] + w[i + 1]
                                c = c.encode('utf-8')
                                print(c)
                                #print(dict[c])
                                if flag == 1:
                                    translate = translate + dict[c] + temp
                                    temp = ""
                                    flag = 0
                                else:
                                    translate = translate + dict[c]
                                c = ""
                                i = i + 2
                            elif ((i + 1) < len(w)) and (w[i] == "Ç".decode('utf-8') and w[i + 1] == "¡".decode('utf-8')):
                                c = w[i] + w[i + 1]
                                c = c.encode('utf-8')
                                print(c)
                                #print(dict[c])
                                if flag == 1:
                                    translate = translate + dict[c] + temp
                                    temp = ""
                                    flag = 0
                                else:
                                    translate = translate + dict[c]
                                c = ""
                                i = i + 2
                            elif ((i + 1) < len(w)) and (w[i] == "³".decode('utf-8') and w[i + 1] == "¢".decode('utf-8')):
                                c = w[i] + w[i + 1]
                                c = c.encode('utf-8')
                                print(c)
                                #print(dict[c])
                                if flag == 1:
                                    translate = translate + dict[c] + temp
                                    temp = ""
                                    flag = 0
                                else:
                                    translate = translate + dict[c]
                                c = ""
                                i = i + 2
                            elif ((i + 2) < len(w)) and (
                                    w[i] == "A".decode('utf-8') and w[i + 1] == "¢".decode('utf-8') and w[
                                i + 2] == "¡".decode('utf-8')):
                                c = w[i] + w[i + 1] + w[i + 2]
                                c = c.encode('utf-8')
                                print(c)
                                #print(dict[c])
                                if flag == 1:
                                    translate = translate + dict[c] + temp
                                    temp = ""
                                    flag = 0
                                else:
                                    translate = translate + dict[c]
                                c = ""
                                i = i + 3
                            elif ((i + 2) < len(w)) and (
                                    w[i] == "Ò".decode('utf-8') and w[i + 1] == "Ç".decode('utf-8') and w[
                                i + 2] == "ü".decode('utf-8')):
                                c = w[i] + w[i + 1] + w[i + 2]
                                c = c.encode('utf-8')
                                print(c)
                                print(dict[c])
                                if flag == 1:
                                    translate = translate + dict[c] + temp
                                    temp = ""
                                    flag = 0
                                else:
                                    translate = translate + dict[c]
                                c = ""
                                i = i + 3
                            elif ((i + 1) < len(w)) and (w[i] == "A".decode('utf-8') and w[i + 1] == "¡".decode('utf-8')):
                                c = w[i] + w[i + 1]
                                c = c.encode('utf-8')
                                print(c)
                                #print(dict[c])
                                if flag == 1:
                                    translate = translate + dict[c] + temp
                                    temp = ""
                                    flag = 0
                                else:
                                    translate = translate + dict[c]
                                c = ""
                                i = i + 2
                            elif ((i + 1) < len(w)) and (w[i] == "â".decode('utf-8') and w[i + 1] == "«".decode('utf-8')):
                                c = w[i] + w[i + 1]
                                c = c.encode('utf-8')
                                print(c)
                                #print(dict[c])
                                if flag == 1:
                                    translate = translate + dict[c] + temp
                                    temp = ""
                                    flag = 0
                                else:
                                    translate = translate + dict[c]
                                c = ""
                                i = i + 2
                            elif ((i + 1) < len(w)) and (w[i] == "W".decode('utf-8') and w[i + 1] == "¡".decode('utf-8')):
                                c = w[i] + w[i + 1]
                                c = c.encode('utf-8')
                                print(c)
                                #print(dict[c])
                                if flag == 1:
                                    translate = translate + dict[c] + temp
                                    temp = ""
                                    flag = 0
                                else:
                                    translate = translate + dict[c]
                                c = ""
                                i = i + 2
                            elif ((i + 1) < len(w)) and (w[i] == "R".decode('utf-8') and w[i + 1] == "¡".decode('utf-8')):
                                c = w[i] + w[i + 1]
                                c = c.encode('utf-8')
                                print(c)
                                #print(dict[c])
                                if flag == 1:
                                    translate = translate + dict[c] + temp
                                    temp = ""
                                    flag = 0
                                else:
                                    translate = translate + dict[c]
                                c = ""
                                i = i + 2
                            elif ((i + 1) < len(w)) and (w[i] == "i".decode('utf-8') and w[i + 1] == "¡".decode('utf-8')):
                                c = w[i] + w[i + 1]
                                c = c.encode('utf-8')
                                print(c)
                                #print(dict[c])
                                if flag == 1:
                                    translate = translate + dict[c] + temp
                                    temp = ""
                                    flag = 0
                                else:
                                    translate = translate + dict[c]
                                c = ""
                                i = i + 2
                            elif ((i + 1) < len(w)) and (w[i] == "t".decode('utf-8') and w[i + 1] == "¡".decode('utf-8')):
                                c = w[i] + w[i + 1]
                                c = c.encode('utf-8')
                                print(c)
                                #print(dict[c])
                                if flag == 1:
                                    translate = translate + dict[c] + temp
                                    temp = ""
                                    flag = 0
                                else:
                                    translate = translate + dict[c]
                                c = ""
                                i = i + 2
                            elif ((i + 1) < len(w)) and (w[i] == "C".decode('utf-8') and w[i + 1] == "¡".decode('utf-8')):
                                c = w[i] + w[i + 1]
                                c = c.encode('utf-8')
                                print(c)
                                #print(dict[c])
                                if flag == 1:
                                    translate = translate + dict[c] + temp
                                    temp = ""
                                    flag = 0
                                else:
                                    translate = translate + dict[c]
                                c = ""
                                i = i + 2
                            elif ((i + 1) < len(w)) and (w[i] == "v".decode('utf-8') and w[i + 1] == "¡".decode('utf-8')):
                                c = w[i] + w[i + 1]
                                c = c.encode('utf-8')
                                print(c)
                                #print(dict[c])
                                if flag == 1:
                                    translate = translate + dict[c] + temp
                                    temp = ""
                                    flag = 0
                                else:
                                    translate = translate + dict[c]
                                c = ""
                                i = i + 2
                            elif ((i + 1) < len(w)) and (w[i] == "ó".decode('utf-8') and w[i + 1] == "¡".decode('utf-8')):
                                c = w[i] + w[i + 1]
                                c = c.encode('utf-8')
                                print(c)
                                #print(dict[c])
                                if flag == 1:
                                    translate = translate + dict[c] + temp
                                    temp = ""
                                    flag = 0
                                else:
                                    translate = translate + dict[c]
                                c = ""
                                i = i + 2
                            elif ((i + 1) < len(w)) and (w[i] == "ç".decode('utf-8') and w[i + 1] == "¡".decode('utf-8')):
                                c = w[i] + w[i + 1]
                                c = c.encode('utf-8')
                                print(c)
                                #print(dict[c])
                                if flag == 1:
                                    translate = translate + dict[c] + temp
                                    temp = ""
                                    flag = 0
                                else:
                                    translate = translate + dict[c]
                                c = ""
                                i = i + 2
                            elif ((i + 1) < len(w)) and (w[i] == "¤".decode('utf-8') and w[i + 1] == "Ã".decode('utf-8')):
                                c = w[i] + w[i + 1]
                                c = c.encode('utf-8')
                                print(c)
                                #print(dict[c])
                                if flag == 1:
                                    translate = translate + dict[c] + temp
                                    temp = ""
                                    flag = 0
                                else:
                                    translate = translate + dict[c]
                                c = ""
                                i = i + 2
                            elif ((i + 2) < len(w)) and (
                                    w[i] == "ó".decode('utf-8') and w[i + 1] == "ø".decode('utf-8') and w[
                                i + 2] == "¡".decode('utf-8')):
                                c = w[i] + w[i + 1] + w[i + 2]
                                c = c.encode('utf-8')
                                print(c)
                                #print(dict[c])
                                if flag == 1:
                                    translate = translate + dict[c] + temp
                                    temp = ""
                                    flag = 0
                                else:
                                    translate = translate + dict[c]
                                c = ""
                                i = i + 3
                            elif ((i + 1) < len(w)) and (w[i] == "è".decode('utf-8') and w[i + 1] == "¡".decode('utf-8')):
                                c = w[i] + w[i + 1]
                                c = c.encode('utf-8')
                                print(c)
                                #print(dict[c])
                                if flag == 1:
                                    translate = translate + dict[c] + temp
                                    temp = ""
                                    flag = 0
                                else:
                                    translate = translate + dict[c]
                                c = ""
                                i = i + 2
                            elif ((i + 1) < len(w)) and (w[i] == "Û".decode('utf-8') and w[i + 1] == "¡".decode('utf-8')):
                                c = w[i] + w[i + 1]
                                c = c.encode('utf-8')
                                print(c)
                                #print(dict[c])
                                if flag == 1:
                                    translate = translate + dict[c] + temp
                                    temp = ""
                                    flag = 0
                                else:
                                    translate = translate + dict[c]
                                c = ""
                                i = i + 2
                            elif ((i + 1) < len(w)) and (w[i] == "´".decode('utf-8') and w[i + 1] == "š".decode('utf-8')):
                                c = w[i] + w[i + 1]
                                c = c.encode('utf-8')
                                print(c)
                                #print(dict[c])
                                if flag == 1:
                                    translate = translate + dict[c] + temp
                                    temp = ""
                                    flag = 0
                                else:
                                    translate = translate + dict[c]
                                c = ""
                                i = i + 2
                            ########################
                            elif ((i + 1) < len(w)) and (w[i] == "—".decode('utf-8') and w[i + 1] == "¡".decode('utf-8')):
                                c = w[i] + w[i + 1]
                                c = c.encode('utf-8')
                                print(c)
                                #print(dict[c])
                                if flag == 1:
                                    translate = translate + dict[c] + temp
                                    temp = ""
                                    flag = 0
                                else:
                                    translate = translate + dict[c]
                                c = ""
                                i = i + 2
                            elif ((i + 1) < len(w)) and (w[i] == "Ã".decode('utf-8') and w[i + 1] == "¡".decode('utf-8')):
                                c = w[i] + w[i + 1]
                                c = c.encode('utf-8')
                                print(c)
                                #print(dict[c])
                                if flag == 1:
                                    translate = translate + dict[c] + temp
                                    temp = ""
                                    flag = 0
                                else:
                                    translate = translate + dict[c]
                                c = ""
                                i = i + 2
                            elif ((i + 2) < len(w)) and (
                                    w[i] == "l".decode('utf-8') and w[i + 1] == "¡".decode('utf-8') and w[
                                i + 2] == "ü".decode('utf-8')):
                                c = w[i] + w[i + 1] + w[i + 2]
                                c = c.encode('utf-8')
                                print(c)
                                #print(dict[c])
                                if flag == 1:
                                    translate = translate + dict[c] + temp
                                    temp = ""
                                    flag = 0
                                else:
                                    translate = translate + dict[c]
                                c = ""
                                i = i + 3
                            else:
                                c = w[i].encode('utf-8')
                                print(c)
                                #print(dict[c])
                                if dict[c] in post_sym:
                                    temp = dict[c]
                                    flag = 1
                                elif flag == 1:
                                    if '্' not in dict[c] or dict[c] in comp_sym:  # if post symbol is followed by a compound symbol
                                        translate = translate + dict[c] + temp
                                        temp = ""
                                        flag = 0
                                    else:
                                        translate = translate + dict[c]
                                elif dict[c] in pre_sym:
                                    trans = translate.decode('utf-8')
                                    temp1 = list(trans)
                                    if len(temp1) > 1:
                                        c1 = temp1[-1]
                                        if len(temp1) > 3:
                                            c2 = temp1[-2]
                                            c3 = temp1[-3]
                                            c4 = c3 + c2 + c1
                                            c4 = c4.encode('utf-8')
                                            if c4 in comp_sym:  # compound_word_followed_by_pre-symbol
                                                temp1[-3] = dict[c].decode('utf-8')
                                                temp1[-2] = c3
                                                temp1[-1] = c2
                                                temp1.append(c1)
                                        else:
                                            temp1[-1] = dict[c].decode('utf-8')
                                            temp1.append(c1)
                                        temp2 = ""
                                        for x in temp1:
                                            temp2 = temp2 + x
                                        translate = temp2.encode('utf-8')
                                else:
                                    translate = translate + dict[c]
                                c = ""
                                i = i + 1
                        print(translate)
                        text_op = text_op + " " + translate
                    print(text_op)
                    fo.write(text_op)
                    fo.write('\n')
            fo.close()
    except Exception as e:
        print("Error in file: " + name)
        print(e)
        pass
print(dir_count)
print(subdir_count)

