import random

def allmax(iterable,key=None):
	result,max_val = [],None
	key = key or (lambda y: y)
	for x in iterable:
		xval = key(x)
#		print x,xval
		if not result or xval > max_val:
			result = [x]
			max_val = xval
		elif xval == max_val:
			result.append(x)
	return result

def poker(hands):
	#Returns the best hand:poker([hand,...])=>[hand]
	return allmax(hands,key=hand_rank)
	
def hand_rank(hand):
	#Return a value indicating the rank of a hand
	#counts is the count of each rank; ranks lists corresponding ranks
	#for eg: group('7H','TD','7D','3C','7S') => counts=(3,1,1), ranks=(7,10,3)
	
#	ranks = card_ranks(hand)  #Orders the hand in descending order of rank
	groups = group(["--23456789TJQKA".index(r) for r,s in hand])
	counts,ranks = unzip(groups)
	if ranks == [14,5,4,3,2]:
		ranks = [5,4,3,2,1]
	straight = max(ranks)-min(ranks)==4 and len(ranks) == 5
	flush = len(set([s for r,s in hand])) == 1 and len(s) == 5
	return (9 if (5,)== counts else
			8 if straight and flush else
			7 if (4,1) == counts else
			6 if (3,2) == counts else
			5 if flush else
			4 if straight else
			3 if (3,1,1) == counts else
			2 if (2,2,1) == counts else
			1 if (2,1,1,1) == counts else
			0),ranks

def group(items):
	"Return a list of [(counts,x)...] with highest count first,then highest x first"
	groups = [(items.count(x),x) for x in set(items)]
	return sorted(groups,reverse=True)
			
def unzip(pairs):
	return zip(*pairs)
	
def kind(n,ranks):
	for r in ranks:
		if ranks.count(r) == n:
			return r
	return None
			
def two_pair(ranks):
	highpair = kind(2,ranks)
	ranks.sort()
	lowpair = kind(2,ranks)
	if highpair and lowpair and highpair != lowpair:
		return (highpair,lowpair)
	return None

mydeck = [r+s for r in '23456789TJQKA' for s in 'SCDH']

def deal(numhands,n=5,deck = mydeck):
	"Shuffles the deck of cards"
	random.shuffle(deck)
	return [deck[n*i:n*(i+1)] for i in range(numhands)]
#	result = []
#	for i in range(numhands):
#		result.append(deck[i*n:(i+1)*n])
#	return result


input = deal(5)
print input
print '--------------'
print 'winning hand is:',poker(input)

def test():
	#Test cases for Poker
	sf = "6D 7D 8D 9D TD".split()
	fk = "9S 9D 9C 9H 3D".split()
	fh = "3S 3D 3H 6D 6S".split()
	tp = "3D 4S 3S 7H 7C".split()
	assert poker([sf,fk,fh]) == [sf]
	assert poker([fk,fh]) == [fk]
	assert poker([fh,fh]) == [fh,fh]
	assert poker([fh,90*tp]) == [fh]
	#Extreme values testing for Poker
	assert poker([fh]) == [fh]
	#Test cases for hand_rank(hand)
	assert hand_rank(sf) == (8,10)
	assert hand_rank(fk) == (7,9,3)
	assert hand_rank(fh) == (6,3,6)

	#Test for flush(hand)
	assert flush(sf) == True
	assert flush(fk) == False
	assert flush(fh) == False
	
	#Test for straight(ranks)
	assert straight([1,2,3,4,5]) == True
	assert straight([9,10,11,12,13]) == True
	assert straight([9,10,11,12,14]) == False
		
	assert kind(4,fk_kind) == 9
	assert kind(3,fh_kind) == 3
	assert kind(3,fk_kind) == None
	assert kind(1,fk_kind) == 3
	assert kind(2,tp_kind) == 7
	
	#Test for two pair
	assert two_pair(tp_kind) == (7,3)
	assert two_pair(fh_kind) == None
	
	#Test for Tie and Ace as first card
	s1 = '2D 3S 4H 5C AS'.split()  		#Ranks = [1,2,3,4,5]
	s2 = '2D 3S 4H 5S 6H'.split()  
	ah = 'AD 2S 3H 4C 6S'.split()  		#A high
	sh = '2D 3S 4H 6H 7D'.split()  		#7 high
	sh2 = '2D 3D 4S 6D 7H'.split()  	#7 high with suits different
	assert poker([s1,ah,sh]) == [s1]
	assert poker([s1,s2,ah,sh]) == [s2]
	assert poker([sf,s2,ah,sh,s1]) == [sf]
	assert poker([sh,sh2]) == [sh,sh2]
	
	assert poker([ah,sh]) == [ah]
	print 'Tests Pass'
	
#test()
