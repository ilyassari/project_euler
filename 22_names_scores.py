'''
Problem 22 Names scores

Using names.txt (right click and 'Save Link/Target As...'), a 46K text file containing over five-thousand first names, begin by sorting it into alphabetical order. Then working out the alphabetical value for each name, multiply this value by its alphabetical position in the list to obtain a name score.

For example, when the list is sorted into alphabetical order, COLIN, which is worth 3 + 15 + 12 + 9 + 14 = 53, is the 938th name in the list. So, COLIN would obtain a score of 938 × 53 = 49714.

What is the total of all the name scores in the file?
'''
import os

def get_file(file_name):
    """ take file name; return file content"""
    txt_path = os.getcwd()
    txt_file = txt_path + "//" + file_name
    active_file = open(txt_file, mode="r")
    return active_file.read()

def make_list(names):
    """ take list as string; give as list"""
    names = names.split(',') #list of names
    for i in range(len(names)):
        names[i] = names[i].replace('"','')
    names.sort()
    return names

def letter_point(name):
    """ take a name; return sum of letter index in alphabet """
    alphabet = ('', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z')
    letters = list(name.lower()) #name as list
    letter_point = 0
    for letter in letters:
        letter_point += alphabet.index(letter)
    return letter_point

def name_point(name, names):
    """ take name and name list; return multiple of letter point and name index in list.
        name index starts with 1 """
    return letter_point(name) * (names.index(name) + 1)

def names_scores(file_name):
    """ take file name; return points """
    names = make_list(get_file(file_name))
    score = 0
    for name in names:
        score += name_point(name, names)
    return score

print(names_scores("p022_names.txt")) # 871198282
