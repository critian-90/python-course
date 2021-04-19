demo_list = [1, 'hello', 1.34, True, [1, 2,3]]
colors = ['red', 'green', 'blue']

numbers_list = list((1, 2, 3, 4))
print (type(numbers_list))
rango = list(range(1, 11))
print (rango)
print (type(colors))
print (type(demo_list))
print (len(colors))
print (len(demo_list))
print (colors[2])
colors[0]  = 'white'
print (colors)
#print (dir(colors))
colors.append ("black")
print (colors)
colors.extend (["orange", "brown"])
print (colors)
colors.insert(0, "gray")
print (colors)
colors.pop() #quita el ultimo
print (colors)
colors.remove("blue") # remueve el que se digite
colors.sort()
print (colors)