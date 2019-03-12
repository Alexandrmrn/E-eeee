my_string = "Пусть дана строка, состоящая из слов, пробелов и знаков препинания. На основании этой строки создайте новую (и выведите ее на консоль)"
ov_string = list(filter(lambda x : x[-2:] == 'ов' , my_string.split()))
os_string = list(filter(lambda x : x[-3:] == 'ов,' , my_string.split()))
print (ov_string + os_string)