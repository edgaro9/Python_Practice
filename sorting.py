l = [5,8,2,9,17,43,25,10]
print(len)
l.insert(9, "shushrut")
len = len(l)
print(len)

class array():
    #remember to use push, pop , delete, insert, get
    
    # remember when creating our own array class we 
    #we have to bascially make it work just like built in python array function
    def _init_(self):
        self.length = 0
        self.data = {} # we use dictionary to combine the array index and the value asscioted with it even if its the same 
        
        