#Problem 1
# Words = {
#     "Mota" : "fat",
#     "kala" : "Black",
#     "patala" : "Slim",
#     "Pehelwan" : "wrestler"
# }
# word = input("Enter a word to know its meaning: ")
# print(Words[word])

#Problem 2
# n = {set}
# for i in range(8):
#     n.add(int(input(f"Enter number  {i+1} : " )))
#     print(n)
#another solution to problem 2:
# e = {set}
# n = input("Enter a number: ")
# e.add(int(n))
# n = input("Enter a number: ")
# e.add(int(n))
# n = input("Enter a number: ")
# e.add(int(n))
# n = input("Enter a number: ")
# e.add(int(n))
# n = input("Enter a number: ")
# e.add(int(n))
# n = input("Enter a number: ")
# e.add(int(n))
# n = input("Enter a number: ")
# e.add(int(n))
# n = input("Enter a number: ")
# e.add(int(n))
# print(e)

#Problem 3
# g = {18,"18"}
# print(g)

#Problem 4
# h = set()
# h.add(20)
# h.add(20.0)
# h.add('20')
# print(h)

#Problem 6
# j = {}
# j[input("Enter your name: ")] = input("Enter your favourite language : ")
# j[input("Enter your name: ")] = input("Enter your favourite language : ")
# j[input("Enter your name: ")] = input("Enter your favourite language : ")
# j[input("Enter your name: ")] = input("Enter your favourite language : ")
# print(j)

#Another method for problem 6
# i = {}
# name = input("Enter your Name: ")
# lang = input("Enter your favourite language: ")
# i.update({name:lang})
# name = input("Enter your Name: ")
# lang = input("Enter your favourite language: ")
# i.update({name:lang})
# name = input("Enter your Name: ")
# lang = input("Enter your favourite language: ")
# i.update({name:lang})
# name = input("Enter your Name: ")
# lang = input("Enter your favourite language: ")
# i.update({name:lang})
# print(i)

#Problem 7 : what if names(keys) of the two friends are same?
#Answer : Language of "Harry" gets updated to C. (keys are Unique Identifiers & hence can't be same)

#Problem 8 : what if languages(values) of the two friends are same?
#Answer : Gets displayed as it is (values can be same)

#Problem 9 : 
# s = {8,7,12,"Harry",[1,2]}
#first of all, we can't add a list to a set and secondly, we can't change the elements in the list within set-s, as sets don't posses indexing.