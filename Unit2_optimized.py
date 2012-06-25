import itertools
import time
import RunningTime
timed_call = RunningTime.timed_calls


def zebra_puzzle():
    "Returns a tuple(WATER,ZEBRA) indicating their house numbers"
    houses = first,_,middle,_,_ = [1,2,3,4,5]
    orderings = list(itertools.permutations(houses))
    return next((WATER,ZEBRA)
                for red,green,ivory,yellow,blue in orderings
                for englishman,spaniard,norwegian,ukranian,japanese in orderings
                for dog,snails,ZEBRA,horse,fox in orderings
                for coffee,tea,milk,oj,WATER in orderings
                for OldGold,Kools,ChesterFields,LuckyStrike,Parliaments in orderings
                if englishman is red
                if spaniard is dog
                if coffee is green
                if ukranian is tea
                if imright(green,ivory)
                if OldGold is snails
                if Kools is yellow
                if milk is middle
                if norwegian is first
                if nextto(ChesterFields,fox)
                if nextto(Kools,horse)
                if LuckyStrike is oj
                if japanese is Parliaments
                if nextto(norwegian,blue)
                )   

def zebra_puzzle2():
    "Returns a tuple(WATER,ZEBRA) indicating their house numbers"
    houses = first,_,middle,_,_ = [1,2,3,4,5]
    orderings = list(itertools.permutations(houses))
    return next((WATER,ZEBRA)
                for red,green,ivory,yellow,blue in orderings
                if imright(green,ivory)
                for englishman,spaniard,norwegian,ukranian,japanese in orderings
                for dog,snails,ZEBRA,horse,fox in orderings
                for coffee,tea,milk,oj,WATER in orderings
                for OldGold,Kools,ChesterFields,LuckyStrike,Parliaments in orderings
                if englishman is red
                if spaniard is dog
                if coffee is green
                if ukranian is tea
                if OldGold is snails
                if Kools is yellow
                if milk is middle
                if norwegian is first
                if nextto(ChesterFields,fox)
                if nextto(Kools,horse)
                if LuckyStrike is oj
                if japanese is Parliaments
                if nextto(norwegian,blue)
                )   


def zebra_puzzle3():
    "Returns a tuple(WATER,ZEBRA) indicating their house numbers"
    houses = first,_,middle,_,_ = [1,2,3,4,5]
    orderings = list(itertools.permutations(houses))
    return next((WATER,ZEBRA)
                for red,green,ivory,yellow,blue in orderings
                if imright(green,ivory)
                for englishman,spaniard,norwegian,ukranian,japanese in orderings
                if norwegian is first
                if nextto(norwegian,blue)
                if englishman is red
                for coffee,tea,milk,oj,WATER in orderings
                if coffee is green
                if ukranian is tea
                if milk is middle
                for OldGold,Kools,ChesterFields,LuckyStrike,Parliaments in orderings
                if Kools is yellow
                if LuckyStrike is oj
                if japanese is Parliaments
                for dog,snails,ZEBRA,horse,fox in orderings
                if spaniard is dog
                if OldGold is snails
                if nextto(ChesterFields,fox)
                if nextto(Kools,horse)
                )

def imright(h1,h2):
    "House h1 is immediately to the right of h2 if h1 - h2 == 1"
    return h1 - h2 == 1
    
def nextto(h1,h2):
    "House h1 and h2 are next to each other if the difference is 1"
    return abs(h1-h2) == 1

def timed_run(function,*args):
    "Calls the function with arguments *args and returns time and result"
    start = time.time()
    result = function(*args)
    end = time.time()
    return end - start, result
    
def timed_calls(n,fn,*args):
    """calls fn repeatedly: n times if n is an int or upto n seconds if n is 
    a float; returns the min,average,max times respectively"""
    if isinstance(n,int):
        times = [timed_run(fn,*args)[0] for _ in range(n)]
    else:
        times = []
        while(sum(times) < n):
            times.append(timed_run(fn,*args)[0])
    return min(times),average(times),max(times)
    
def average(numbers):
    return sum(numbers)/float(len(numbers))

print 'Duration = ',timed_calls(10,zebra_puzzle3)


def zebra_puzzle_debug():
    "This is the replica of zebra_puzzle() used for debugging purpose"
    "Returns a tuple(WATER,ZEBRA) indicating their house numbers"
    houses = first,_,middle,_,_ = [1,2,3,4,5]
    orderings = list(itertools.permutations(houses))
    return next((WATER,ZEBRA)
                for red,green,ivory,yellow,blue in debug(orderings)
                if imright(green,ivory)
                for englishman,spaniard,norwegian,ukranian,japanese in debug(orderings)
                if norwegian is first
                if nextto(norwegian,blue)
                if englishman is red
                for coffee,tea,milk,oj,WATER in debug(orderings)
                if coffee is green
                if ukranian is tea
                if milk is middle
                for OldGold,Kools,ChesterFields,LuckyStrike,Parliaments in debug(orderings)
                if Kools is yellow
                if LuckyStrike is oj
                if japanese is Parliaments
                for dog,snails,ZEBRA,horse,fox in debug(orderings)
                if spaniard is dog
                if OldGold is snails
                if nextto(ChesterFields,fox)
                if nextto(Kools,horse)
                )

def instrument_fn(fn,*args):
    debug.starts,debug.items = 0,0
    result = fn(*args)
    print "%s got %s with %5d iters over %7d items" %(
            fn.__name__,result,debug.starts,debug.items)
            
def debug(sequence):
    """Generates item in sequence;keeps counts as we go;debug.starts holds 
    the no.of sequence we started;debug.items holds the no.of items generated"""
    debug.starts += 1
    for item in sequence:
        debug.items += 1
        yield item
print timed_call(10.0,zebra_puzzle3)
instrument_fn(zebra_puzzle_debug,)
instrument_fn(zebra_puzzle3,)
