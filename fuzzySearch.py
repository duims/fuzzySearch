#the mock one we know works slowly (to get unit tests done)
def lev(w1, w2):
	if not w1:
		return len(w2)
	if not w2:
		return len(w1)
	return min(lev(w1[1:], w2[1:])+(w1[0] != w2[0]), lev(w1[1:], w2)+1, lev(w1, w2[1:])+1)

#
def leven(w1, w2, errMax):
	#w2 smaller pls:
	if len(w1) < len(w2):
		return leven(w2, w1, errMax)
	errCount=0
	if w1==w2:
		return True
		
	#hamming
	if len(w1)==len(w2):
		for i in range(len(w1)):
			if w1[i]!= w2[i]:
				errCount+=1
	

	#if the length difference is too big, we aren't even bothering to calculate
	if len(w1)-len(w2)- errMax > 0:
		return False
	
	#let's cheat using the terrible recursive version for now so we can get test done
	errCount=lev(w1, w2)
	
	if errCount<=errMax:
		return True
	else:
		return False
		
		

def main():
	pass
