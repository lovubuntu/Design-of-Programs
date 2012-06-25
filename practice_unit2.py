import math
#print [s for r,s in ['AB','CD','EF','GH']]
#lis = []
#for r,s in ['AB','CD','EF','GH']:
#    lis.append(s)
#print lis

#di = {}
#try:
#    print di[2]
#except:
#    print 'Exception'
#    
#di[2] = 34
#for i in range(10):
#    di[i] = i+5
#j = 19
#while(j>9):
#    di[j] = j
#    j-=1
#    
#print di

#def return_check():
#    "checks if more than one return values then it is returned as a tuple"
#    return 2,3
#print return_check()

#def sq(x):
#    print 'Inside Square Root',x ; return x*x
#    
#"Generator Expression"
#g = (sq(x) for x in range(10) if x%2 == 0)

#for x2 in g: #=>"Prints Inside Square Root" message
#    pass # do nothing inside the loop 

##prints square root value
#for x2 in (sq(x) for x in range(10) if x%2 == 0):pass; print x2 

##Forms a list of square root that is divisible by 2
#print list(x2 for x2 in (sq(x) for x in range(10) if x%2 == 0)) 

#import collections
#dictionary = collections.defaultdict(int)
#print dictionary[1]

#### Yield checking ####
def check_yield(start,end):
    "Checks the working of a generator fn"
    print '\n'
    print '====================='
    print 'Inside Yield function'
    print '====================='
    i = start
    while(i <= end):
        print 'before yield command'
        yield i       #yield converts the fn to generator fn
        i = i + 1
        print 'inside while loop',i
    print 'Value of i after while loop',i
    
y_gen = check_yield(1,5)
print y_gen
print 'normal call to next',next(y_gen)
for i in y_gen:
    pass
check_yield(4,14)
#### Yield checking ####

#### More Yield ####
#def all_ints():
#    yield 0
#    i = 1
#    while True:
#        yield +i
#        yield -i
#        i += 1
#        
#gen_int = all_ints()
#for i in range(11):
#    print next(gen_int)
##### More Yield ####

#####    

#### For loop working ###
#salary = [10000,20000,300000,42315,53142]
#item = iter(salary)
#try:
#    while True:
#        res = next(item)
#        print res
#except StopIteration:
#    pass
#    
####In built form of eval###
f = lambda a,b,c,d,e:a*b*c*d*e
print f(1,2,3,4,5)
sum = 0
for i in range(10):
    g = lambda a,b,c:a**2+b**2+c**2
    sum += g(i,i+1,i+2)
print sum
"""what this line does is word[startposition:endposition:
    {'+'sign to move forward,'-' sign to traverse backward} value to step]"""
word = '123456789'
print word[3:7:1]
"""Outputs 4567 (starting from position 3 till 6 incrementing the step by 1)"""

print word[3:7:-1]
"""Outputs nothing since range 3-7 has values to its right from position 3 to 7.
    but since reverse direction is mentioned it will travel to the left of 3.
    so there will be no values to print"""
    
print word[3:0:-1]
"""Prints values from 3 to 0 in reverse direction"""
word = 'YOU ARE HERE'
for i,char in enumerate(word[::-1]):
    print i,char
    
def compile_word(word):
    if word.isupper():
        expr_list = ['%s*%s'%(10**d,char) 
                        for d,char in enumerate(word[::-1])]
        return ' + '.join(expr_list)
import re            
x = 'HELLO HI'
print "re.split('([A-Z]+)','HELLO') = ",re.split('([A-Z]+)',x)
print x
print compile_word("HELLO + HI")


