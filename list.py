# Python Collection (Arrays)
# List : it is a collection which is ordered, changable, allow duplicate elements
# Tuple : it is collection ordered, unchangeable, allow duplicate elements
# Set: It is collection unordered(unindexed), unchangeable and no duplicates elements
# Directory: It is collection ordered/indexed, changeable and no duplicates elements

# append, clear, copy, count, extend, index, insert, pop, remove, reverse, del, sort, join(+ sign with two list)
fruit = ["apple","mengo","banana","cherry","blueberry"]

fruit2 = list(("apple","mengo","banana","apple")) # list()

num= [2,4,6,8,10]
boollist = [True,False,True]
mixlist = ["xyz",23,False,56,"qas"]

fruit[3] = 'cherry'
print(type(fruit))
print(type(num))
print(type(boollist))
print(type(mixlist))
print(len(fruit))
print(fruit2)
print(fruit[-4])
print(fruit[0:4]) # print(fruit[:4]) both equals
print(fruit[2:])
print(fruit[-4:-1])
print(fruit[-4:]) 


if "mengo" in fruit:
   print("Yes, mengo is in the list!")

#fruit = ["apple","mengo","banana","cherry","blueberry"]
fruit[1:3] = ["watermelon","dragonfruit"]

#['apple', 'watermelon', 'dragonfruit', 'cherry', 'blueberry']
print(fruit)

fruit.insert(2,"kiwi")
fruit.append("Orange")


mytuple = ("bmw","audi")

fruit.extend(mytuple)

print(fruit)

fruit.remove("audi")

fruit.pop()   

del fruit[0]

#del fruit #working or not

fruit3 = ["apple","mengo","banana"]


#fruit3.clear()

print(fruit3)

fruit3.sort()
print(fruit3)

numB = [233,34,76,89,7,44,12]

numB.sort()

numB.sort(reverse= True)

print(numB)

def mysort(n):
    return abs(n - 50)

numC = [200,100,50,25,1]

numC.sort(key = mysort)

print(numC)

fruit3.sort(reverse= True)
print(fruit3)

#copy list
#fruitq = fruit3.copy() #working or not

fruitq = list(fruit3)

fruitw = fruit3 #working or not


fruit3[2] = 'kiwi'
fruitw[0] = 'coconut'
print(fruitq)
print(fruit3)


combolist = fruit3  +  numC

print(combolist)

for y in numC:
    fruit3.append(y)

print(fruit3)
