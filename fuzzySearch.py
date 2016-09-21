#the mock one we know works slowly (to get unit tests done)

#A more efficient method would never repeat the same distance calculation.
#For example, the Levenshtein distance of all possible prefixes might be stored in an array d[][]
#where d[i][j] is the distance between the first i characters of string s and the first j characters of string t. The table is easy to construct one row at a time starting with row 0. When the entire table has been built, the desired distance is d[len_s][len_t].
def lev(w1, w2):
	#Calculates the distance between 2 words
	#TODO: rewrite as a dynamic programming algorithm (curently shitty + recursive)
	if not w1:
		return len(w2)
	if not w2:
		return len(w1)
	return min(lev(w1[1:], w2[1:])+(w1[0] != w2[0]), lev(w1[1:], w2)+1, lev(w1, w2[1:])+1)

	
def leven(w1, w2, errMax):
	#calculates if 2 words are within the error bound wrt distance.
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
	

def search(w1, maxDiff):
	#Returns a list of the words that match the upper bound. 
	pass


def read_saved_index(fileName):
	with open(fileName, 'r') as file:
		index=json.load(file)
	return index


def dump_index(index, fileName):
	with open(fileName,"w") as file:
		json.dump(index, file)
	return


def index_read_file(fileName):
	#create a word index: {"cat":[1, 6, 100], 'mat':[2, 105, 238]}
	lineCount=1
	index={}
	with open(fileName, "r") as data:
		for line in data:
			words=line.split()
			for x in words:
				if x not in index:
					index[x]=[linecount]
				else:
					index[x].append(lineCount)

			lineCount+=1
	return index
					

 
def write_stats(word, maxDiff, numMatches):
	#adds data point to end of file of word, errMax, number of levenshtein matches.
	with open("searchRecord.txt", "a") as statsFile:
		statsFile.write("{0},{1},{2}".format(word, maxDiff, numMatches))
	return