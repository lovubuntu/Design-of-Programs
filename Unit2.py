import itertools
import time
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

def imright(h1,h2):
    "House h1 is immediately to the right of h2 if h1 - h2 == 1"
    return h1 - h2 == 1
    
def nextto(h1,h2):
    "House h1 and h2 are next to each other if the difference is 1"
    return abs(h1-h2) == 1
    
print time.time()
start = time.time()    
print zebra_puzzle()
end = time.time()
print start,end,'Duration = ',end - start
