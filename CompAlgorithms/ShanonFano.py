class Char:
    
    #__init__. It's what we use to define the initialisation of an object.
    def __init__(self, name, freq):
        self._name = name
        self._freq = freq
        self._code = ""
     
    #__lt__(self, other) Defines the behaviour of the less-than operator <
    def __lt__(self, other):
        return True if self._freq < other.get_freq() else False
    
    #Defines the behaviour of the equality operator ==
    def __eq__(self, other):
        return True if self._name == other.get_name() and self._freq == other.get_freq() else False


    #The __str__ method in Python represents the class objects as a string – it can be used for classes.
    #The __str__ method should be defined in a way that is easy to read and outputs all the members of the class.
    def __str__(self):
        return "{0}\t {1}\t {2}".format(self._name, str(self._freq), self._code)
    
    #we can say that class Char is an iterable object because we implemented it with __iter__.
    #Method __iter__ returns an iterator.
    def __iter__(self):
        return self
    
    #to get the name of current object
    def get_name(self):
        return self._name
    
    #to get frequency of current object
    def get_freq(self):
        return self._freq
    
    #to get the code of current object
    def get_code(self):
        return self._code
    
    #to append current code to previous codes of current object
    def append_code(self, code):
        self._code += str(code)

#calculate the mid index of sample
def find_middle(lst):
    
    #if list contain only one element return none
    if len(lst) == 1: return None
    
    s = k = b = 0
    
    #sum all frequency for all symbols
    for p in lst: s += p.get_freq()
    s /= 2 #diving sum of freq /2
      
    for p in range(len(lst)):
        #append freq of p to k while k<s
        k += lst[p].get_freq()
        
    
        if k == s: return p #which p is index
        
        elif k > s:
            
            j = len(lst) - 1
            
            while b < s:
                #append freq of j to b while b<s
                b += lst[j].get_freq()
                
                j -= 1 #Note:decrement j before checking           
                #using abs() to ignore the sign 
            return p if abs(s - k) < abs(s - b) else j
 
           
  

#calculate shanon_fano codes
class ShannonFanoClass:
    def __init__(self, lst):
        self.shanonFanoCheck(lst)
        
    def shanonFanoCheck(self, list):
        mid = find_middle(list)
        if mid == None: return None

        for i in list[: mid + 1]:
            i.append_code(0)
        self.shanonFanoCheck(list[: mid + 1])
        for i in list[mid + 1:]: #range(middle+1,the end)
            i.append_code(1)  #append 0 to the specific symbols in range
        self.shanonFanoCheck(list[mid + 1:])


# def output():

#         lst=list()
#         lst.append(Char('A', 0.22))
#         lst.append(Char('B', 0.28))
#         lst.append(Char('C', 0.15))
#         lst.append(Char('D', 0.30))
#         lst.append(Char('E', 0.05))
        

        
#         lst.sort(reverse=True) #sorting DC
#         shannon_fano(lst) #CALL shanon_fano() fun 
#         print('char','freq','code')
#         for c in lst: #for loop to print all objects of list with codes
#          print(c)


