Id = 10
class student:
    Id = 0 
    Name = ""
    Marks = None
    Rank = 0
    
    def printMe(self):
        print("I am a student ID is: ",self.Id,self.Marks)
    def average(self):
        avg = 0
        for i in self.Marks:
            avg = avg + i 
        average = avg/len(self.Marks)
        return average
    def __init__(self,Id,Name,Marks):
        self.Id = Id
        self.Name = Name 
        self.Marks = Marks
        
        
s1 = student(1,"Rishi",[1,2,23])

#s1.Marks = [10,10,9]
s2 = student(2,"Sanket",[2,3,5])
s1.printMe()
s2.printMe()
print(s1.average())
print(s2.average())
sarr = []

for i in range(1,4):
    a = int(input("Please enter marks for sub 1 for student :"))
    b = int(input("Please enter marks for sub 2 for student :"))
    c = int(input("Please enter marks for sub 3 for student :"))
    sarr.append(student(i, "rishi"+str(i),[a,b,c]))
    
    

for s in sarr:
    s.printMe()
    print(s.average())
    