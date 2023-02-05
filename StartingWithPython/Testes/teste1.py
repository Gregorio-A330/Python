print("Testando código da primeira aula")

# pais = "Brasil"
# quantidade = 5      ##tipagem dinamica 

# print(pais, "ganhou", quantidade, "titulos mundiais", end="!")



class TestDat():          # leave this empty
    def __init__(self):   # constructor function using self
        self.Dat1 = None  # variable using self.
        self.Dat2 = None  # variable using self
    
TestArray = [] #empty array

Test1 = TestDat() #this is an object
Test2 = TestDat() #this is another object
        
Test1.Dat1 = 0 #assigning value to object 1 
Test1.Dat2 = 1 #assigning value to object 1 
    
Test2.Dat1 = 3 #assigning value to object 2 
Test2.Dat2 = 4 #assigning value to object 2

TestArray.append(Test1) #append object 1
TestArray.append(Test2) #append object 2 
    
print ("aaaaa", TestArray[0]) # this is Test1
# print (TestArray[0].Dat1) # this is Test1
# print (TestArray[1].Dat1) # this is Test2
