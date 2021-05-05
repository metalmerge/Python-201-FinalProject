def find_max(collection, candidate_amount):
	maximum = 0
	for y in range(candidate_amount):
		if collection[y]["votes"] > maximum:
			maximum = collection[y]["votes"]
	return maximum
def vote(candidate_coll, voter_amount, candidate_amount, vote_coll):
	for x in range(candidate_amount):
		for b in range(voter_amount):
			if candidate_coll[x]["name"] == vote_coll[b]["name"]:
				candidate_coll[x]["votes"] += 1	
				
def vote_finder():
	voters = int(input("How many voters? "))
	return voters
def candidate_finder(collection):
	temp_count = int(input("How many candiates? "))
	for t in range(temp_count):
		candidate = input("Candidate name: ")
		collection.append({"name":candidate, "votes":0,})
	return temp_count
def print_winners(candidate_amount, candidate_coll, max):
	sum = 0;
	for p in range(candidate_amount):
		sum += candidate_coll[p]["votes"]
	for z in range(candidate_amount):
		
		if candidate_coll[z]["votes"] == max:
			
			percentage = round(candidate_coll[z]["votes"] / sum * 100)
			result = []
			result.append(candidate_coll[z]["name"])
			result.append(percentage)
			
	return result
		
def Start_Pluraility(CandidateOne, CandidateTwo, VoterOne,VoterTwo,VoterThree):

	Pvotes = []
	Pcandidates = []
	
	Pvoter_count = 3
	Pcandidate_count = 2
	#candidate_finder(Pcandidates, CandidateOne, CandidateTwo)
	
	#vote_finder(VoterOne,VoterTwo,VoterThree)
	Pcandidates.append({"name":CandidateOne, "votes":0,})
	Pcandidates.append({"name":CandidateTwo, "votes":0,})

	
	Pvotes.append({"name":VoterOne})
	Pvotes.append({"name":VoterTwo})
	Pvotes.append({"name":VoterThree})

	vote(Pcandidates, Pvoter_count, Pcandidate_count, Pvotes)
	max = find_max(Pcandidates, Pcandidate_count)
	
	winner = print_winners(Pcandidate_count, Pcandidates, max)
	#for r in range(Pcandidate_count):
		#print(Pcandidates[r]["votes"])
	
	return winner

#def test(CandidateOne):
#, CandidateTwo,VoterOne,VoterTwo,VoterThree):
#	x = CandidateOne
#	return x