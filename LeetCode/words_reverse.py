"""
给定一个句子（只包含字母和空格）， 将句子中的单词位置反转，单词用空格分割, 单词之间只有一个空格，前后没有空格。
比如： （1） “hello xiao mi”-> “mi xiao hello”


"""


list_number = list(input().split(' ')) #由于reverse无法对字符串进行操作，故对输入字符串以空格为单位分割，然后转为列表

list_number.reverse()
 
# list to string : " ".join(list)
print(" ".join(list_number)) #以" "为单位对列表中的单词进行组合为字符串