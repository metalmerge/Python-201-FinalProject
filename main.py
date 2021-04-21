def vote_finder():
	#voters = int(input("How many voters? "))
	voters = 3
	return voters
def print_winners(candidate_amount, candidate_collection):
	print("Winner(s):")
	for z in range(candidate_amount):
		if candidate_collection[z]["votes"] == max:
			print(candidate_collection[z]["name"])
			sum = 0;
			for p in range(candidate_amount):
				sum += candidate_collection[p]["votes"]

			percentage = round(candidate_collection[z]["votes"] / sum * 100)

	print("Won with " + str(percentage) + "% of the vote")
def vote(candidate_collection, voter_amount, candidate_amount, vote_collection):
	for x in range(candidate_amount):
		for b in range(voter_amount):
			if candidate_collection[x]["name"] == vote_collection[b]["name"]:
				candidate_collection[x]["votes"] += 1
				
def candidate_finder(collection):
	temp_count = 2
	#int(input("How many candiates? "))
	#for t in range(temp_count):
		#candidate = input("Candidate name: ")
		#collection.append({"name":candidate, "votes":0,})
	collection.append({"name":"Dima", "votes":0,})
	collection.append({"name":"Jason", "votes":0,})
	return temp_count
def find_max(collection, candidate_amount):
	maximum = 0
	for y in range(candidate_amount):
		if collection[y]["votes"] > maximum:
			maximum = collection[y]["votes"]
	return maximum
# doesn't check in runoff and approval
Pvotes = []
Pcandidates = []
Rvotes = []
Rcandidates = []
Avotes = []
Acandidates = []
#Potential bugs: one vote, invalid input for amount
choice = 1
#choice = int(input("""
#Pick what election type:
#1- Plurality
#2- Runoff
#3- Approval
#"""))
if choice == 1:
	print("""In single-winner plurality voting, each voter is allowed to vote for only one candidate, and the winner of the election is the candidate who represents a plurality of voters or, in other words, received the largest number of votes.""")
	
	Pcandidate_count = candidate_finder(Pcandidates)
	
	Pvoter_count = vote_finder()
	for i in range(Pvoter_count):
		trueName = 0
		while (True):
			pluraility_vote = input("Voter " + str(i+1) + "'s vote: ")
			for c in range(Pcandidate_count):			
				if pluraility_vote == Pcandidates[c]["name"]:
					trueName += 1
			if trueName == 1:
				break;
			else: 
					print("Invalid Name")
		Pvotes.append({"name":pluraility_vote})
		
			
	vote(Pcandidates, Pvoter_count, Pcandidate_count, Pvotes)

	max = find_max(Pcandidates, Pcandidate_count)
	
	print_winners(Pcandidate_count, Pcandidates)
	
elif choice == 2:
	print("""The two-round system is a voting method used to elect a single candidate, where voters cast a single vote for their preferred candidate. The election proceeds to a second round only if in the first round no candidate has received a simple majority of votes cast, or at least some other prescribed percentage.""")
	Rcandidate_count = candidate_finder(Rcandidates)
	
	Rvoter_count = vote_finder()

	for q in range(Rvoter_count):
		print("Voter " + str(q+1) + "'s rankings:")
		for u in range(Rcandidate_count):
			runoff_vote = input("Rank " + str(u + 1) + "-")
			Rvotes.append({"Rank" + str(u+1):runoff_vote})
	#print(Rvotes)	
		
elif choice == 3:
	print("""Approval voting is a single-winner electoral system where each voter may select ("approve") any number of candidates.""")
	Acandidate_count = candidate_finder(Acandidates)
	
	Avoter_count = vote_finder()
	
	for b in range(Avoter_count):
		Amount_Approved = int(input("How many candidates does Voter " + str(b+1) + " approve of? "))
		for m in range(Amount_Approved):
			approval_vote = input("Please input vote: ")
			Avotes.append({"name":approval_vote})

			 
	substitute = len(Avotes)
	for x in range(substitute):
		for b in range(Acandidate_count):
			if Acandidates[b]["name"] == Avotes[x]["name"]:
				Acandidates[b]["votes"] += 1
				

	max = find_max(Acandidates, Acandidate_count)

	print_winners(Acandidate_count, Acandidates)
