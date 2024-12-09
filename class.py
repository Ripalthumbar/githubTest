class Mydemo:
    dw1 =  45

print(Mydemo)

print(Mydemo.dw1)#45


d1 = Mydemo() # create object of the class
print(d1.dw1)#45


class Human:
    # def __init__(yourname, fname, age):
    #     yourname.name = fname
    #     yourname.age =  age


    def __str__(self):
        return f"Result : {self.name}{self.age}"
        print( "{self.name}({self.age})")

#h1 =  Human('jay',29)
h1 =  Human() 
h1.name = 'Urmi'
h1.age = '32'
#del h1.age
print(h1.name)
#print(h1.age)
print(h1)#jay(29)


class Animal:
    def __str__(self):
        return f"Result : {self.name}{self.size}"
        print("{self.name}({self.size})")
        
#   def __init__(self, name, color):
#     self.name = name
#     self.color = color

a1 = Animal("Elephant", 'gray')
print(a1)
print(a1)
    
            
#a1 = Animal()
#a1.name = 'Elephant'
#a1.size = 'big'
#print(a1)

