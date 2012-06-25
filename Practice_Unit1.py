print max([3,4,5,0]),max([3,4,-5,2],key=abs)


hand = "6DR 7DT 8DG 9DH TDT".split()
#print ["--23456789TJQKA".index(r) for r,s,t in hand]
for r,s,t in hand:
	print r,s,t            #Separates one character each from List "hand"
	
reverse = [1,5,3,5,2,8]
print list(reversed(reverse)) #[8, 2, 5, 3, 5, 1]

def peter_flush(hand):
    suits = [s for r,s in hand]
    return len(set(suits))==1

def my_flush(hand):
    return hand[0][1]==hand[1][1]==hand[2][1]==hand[3][1]==hand[4][1]

def jason_flush(hand):
    "Return True if all the cards have the same suit."
    suits = [suit for r,suit in hand]
    return suits == [suits[0]]*5

def test(N):
    hand = ["6D 7C 8C 9C TC".split(), "6C 7C 8C 9C TC".split()]
    testprog = {0:peter_flush, 1:my_flush, 2:jason_flush}
    programname = {0:'peter_flush', 1:'my_flush', 2:'jason_flush'}
    import time
    for h in hand:
        print "--For hand ", h, "--"
        for p in range(len(testprog)):
            start = time.time()
            for i in range(N):
                a = testprog[p](h)
            elapsed = time.time() - start
            print "program ", programname[p], " for ", N, " = ", elapsed, " seconds"

test(1000000)
