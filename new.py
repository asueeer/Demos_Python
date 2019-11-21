# 百钱百🐔问题

# 我国古代数学家张丘建在《算经》一书中提出的数学问题：鸡翁一值钱五，鸡母一值钱三，鸡雏三值钱一。百钱买百鸡，问鸡翁、鸡母、鸡雏各几何？
#
# 百钱百鸡问题:公鸡5元一只，母鸡3元一只，小鸡一元3只。 如何100元买100只鸡？

# 设公鸡x只，母鸡y只，小鸡z只

# for x in range(101):
# # #     for y in range(101):
# # #         for z in range(101):
# # #             if 5*x+3*y+1/3*z == 100:
# # #                 if x+y+z==100:
# # #                     print(str(x)+" "+ str(y)+ " " + str(z))


#
# 请实现一个函数，将一个字符串中的每个空格替换成“%20”。
# 例如，当字符串为We Are Happy.
# 则经过替换之后的字符串为We%20Are%20Happy。

# def replace(s):
#     temp = ""
#     for i in s:
#         if i==" ":
#             temp = temp+"%20"
#         else:
#             temp = temp + i
#     return temp
#
# print(replace("We Are Happy."))


# def LeftRotateString(s, n):
#     return s[n:] + s[0:n]
#
#
# # write code here
#
# print(LeftRotateString('abcdefg', 3))
# # 输出应为"cdefg ab"

def FirstNotRepeatingChar(s):
    for i in range(len(s)):
        if s.count(s[i])==1:
            return i

# write code here

# print(FirstNotRepeatingChar('google'))
# 输出应为"4"


# def ReverseSentence(s):


# write code here

# print(ReverseSentence('I am a student.'))
# 输出应为"student. a am I"


# s = 'I am a student.'
#
# lst = s[0:-1].split(" ")
#
# print(lst)
# lst.reverse()
# print(lst)
#
# temp = ""
# for i in lst:
#     temp = temp+i + " "
# print(temp)

def jiecheng(n):
    if n==1:
        return 1
    else:
        return n*jiecheng(n-1)


print(jiecheng(30))


# 30! = 30* 29!

