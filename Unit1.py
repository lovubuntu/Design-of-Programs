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
	#Returns the value indicating the rank of a hand
	
	ranks = card_ranks(hand)  #Orders the hand in descending order of rank
	
	if straight(ranks) and flush(hand):
		return (8,max(ranks))		
	elif kind(4,ranks):
		return (7,kind(4,ranks),kind(1,ranks))		
	elif kind(3,ranks) and kind(2,ranks):
		return (6,kind(3,ranks),kind(2,ranks))	
	elif flush(hand):
		return (5,ranks)		
	elif straight(ranks):
		return (4,max(ranks))	
	elif kind(3,ranks):
		return (3,kind(3,ranks),ranks)	
	elif two_pair(ranks):
		return (2,two_pair(ranks),kind(1,ranks))	
	elif kind(2,ranks):
		return (1,kind(2,ranks),ranks)	
	else:
		return (0,ranks)
		
def straight(ranks):
	return (max(ranks) - min(ranks)) == 4 and len(set(ranks)) == 5
	
def flush(hand):
	suits = [s for r,s in hand]
	return len(set(suits)) == 1 and len(suits) == 5

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

def card_ranks(hand):
	ranks = ["--23456789TJQKA".index(r) for r,s in hand]
	ranks.sort(reverse=True)
#	return [5,4,3,2,1] if ranks == [14,5,4,3,2] else ranks "Syntax will work"
	if ranks == [14,5,4,3,2]:
		return [5,4,3,2,1]
	return ranks
	
mydeck = [r+s for r in '23456789TJQKA' for s in 'SCDH']

def deal(numhands,n=5,deck = mydeck):
	"Shuffles the deck of cards"
	random.shuffle(deck)
	return [deck[n*i:n*(i+1)] for i in range(numhands)]
#	result = []
#	for i in range(numhands):
#		result.append(deck[i*n:(i+1)*n])
#	return result


input = deal(11)
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

	#Test cases for card_ranks(hand)
	assert card_ranks(sf) == [10,9,8,7,6]
	assert card_ranks(fk) == [9,9,9,9,3]
	assert card_ranks(fh) == [6,6,3,3,3]

	#Test for flush(hand)
	assert flush(sf) == True
	assert flush(fk) == False
	assert flush(fh) == False
	
	#Test for straight(ranks)
	assert straight([1,2,3,4,5]) == True
	assert straight([9,10,11,12,13]) == True
	assert straight([9,10,11,12,14]) == False
	
	#Test for kind
	fk_kind = card_ranks(fk)
	fh_kind = card_ranks(fh)
	tp_kind = card_ranks(tp)
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
	
test()
ip_error1 = [['5H', 'QH', 'AS', '8S', 'AH'], ['QS', 'TC', '6S', 'TD', '9C'], ['4C', 'JC', 'KC', 'KH', '5S'], ['9H', 'KD', '6D', '3D', 'QC'], ['TH', '7S', 'JH', '5D', 'QD'], ['JS', '8H', '6C', '4S', '7H'], ['2C', '3S', 'TS', '2S', '6H'], ['AD', 'KS', '3C', '4D', '2H'], ['5C', '2D', 'AC', '7D', '4H'], ['9D', '9S', '8D', '3H', 'JD'], ['7C', '8C']]
ip_error2 = [['5C', '9C', '4C', '8C', '9H'], ['QH', '9S', 'QS', 'KS', 'JS'], ['7H', 'AC', '2S', 'TD', '4H'], ['6H', '8H', '4D', 'JD', '3D'], ['3C', 'KH', 'AD', '5H', 'KC'], ['2D', '7D', '8D', '5D', 'KD'], ['7S', '8S', 'TS', '6C', 'AH'], ['9D', '7C', 'QC', '3S', '2C'], ['3H', '5S', '4S', 'TH', '6S'], ['TC', 'AS', 'JC', '6D', 'QD']]
print poker(ip_error1)
print poker(ip_error2)
