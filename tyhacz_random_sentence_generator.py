import random
import string

a_deter = ["The","A","Those"]
a_nouns = ["lion","fox","car","program","dog","banana","book"]
a_verbs = ["are","were","is"]
a_adv_adj = ["very","not so","ultra","a little","not"]
a_adj = ["scary","red","weird","cool","lame","yellow"]

rand_d = 0
rand_n = 0
rand_v = 0
rand_adv = 0
rand_adj = 0

s_sentence = ""

def Search():
	global s_sentence
	loc_string = ""
	locations = []
	user_in = raw_input("Search a word or character in the sentence: ")
	loc = s_sentence.find(user_in,0)
	if(s_sentence.count(user_in) > 0):
		while (len(locations) < s_sentence.count(user_in)):
			#print "locations found",len(locations)
			#print "count",s_sentence.count(user_in)
			if( s_sentence.find(user_in,loc) == -1 or s_sentence.find(user_in,loc) == 0):
				print "Not Found"
				GenSent()
			else:
				loc = s_sentence.find(user_in,loc) + 1
				locations.append(loc)
				#print "found",user_in,"at ",loc
		#print "Location:", s_sentence.find(user_in), s_sentence.rfind(user_in)
		for item in locations:
			loc_string += str(item)+", "
		print
		print "Locations:",loc_string
		print "Occurances:", s_sentence.count(user_in)
		print
		GenSent()
	
def GenSent():
	global a_deter, a_nouns, a_verbs, rand_d, rand_n, rand_v, s_sentence
	bPlural = 0 # 0 is not plural, 1 is plural
	
	s_sentence = ""
	rand_d = random.randint(0,2)
	rand_n = random.randint(0,6)
	rand_v = random.randint(0,1)
	rand_adv = random.randint(0,4)
	rand_adj = random.randint(0,5)
	
	s_sentence += a_deter[rand_d] + " "
	
	if(rand_d == 2):
		bPlural = 1
	elif(rand_d == 0 and 2+rand_n > 4): # just a random factor to make it plural for ' the '
		bPlural = 1
	else: bPlural = 0
	
	s_sentence += a_nouns[rand_n]
	if(bPlural == 1):
		if(rand_n == 1):
			s_sentence += "es"
		else:
			s_sentence += "s"
		
		s_sentence += " " + a_verbs[rand_v] + " "
	else:
		s_sentence += " " + a_verbs[2] + " "
	
	s_sentence += a_adv_adj[rand_adv] + " " + a_adj[rand_adj] + "."
	print s_sentence
	Search()

GenSent()