# file = open('suifeng.txt')
# # text = file.read()
# # print(text)
# # file.close()

# with open('suifeng.txt') as f:
#     print(f.read())


newList=[]
for i in range(11):
    newList.append(i*2)
print(newList)

newList2=[i*2 for i in range(11)]
print(newList2)


list = ["小米","王银龙","王思"]
emptyList=[]
for name in list:
    if name.startswith('王'):
        emptyList.append(name)
print(emptyList)

print([name for name in list if name.startswith('王')])