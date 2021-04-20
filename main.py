def candidate_Amount(collection):
	temp_count = 2
	#int(input("How many candiates? "))
	#for t in range(temp_count):
		#candidate = input("Candidate name: ")
		#collection.append({"name":candidate, "votes":0,})
	collection.append({"name":"Dima", "votes":0,})
	collection.append({"name":"Jason", "votes":0,})
	return temp_count
# doesn't check in runoff ranking input
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
	
	Pcandidate_count = candidate_Amount(Pcandidates)
	
	voter_count = int(input("How many voters? "))
	for i in range(voter_count):
		trueName = 0
		while (True):
			pluraility_vote = input("Voter " + str(i+1) + "'s vote:")
			for c in range(Pcandidate_count):			
				if pluraility_vote == Pcandidates[c]["name"]:
					trueName += 1
			if trueName == 1:
				break;
			else: 
					print("Invalid Name")
		Pvotes.append({"name":pluraility_vote})
		
			
	for x in range(Pcandidate_count):
		for b in range(voter_count):
			if Pcandidates[x]["name"] == Pvotes[b]["name"]:
				Pcandidates[x]["votes"] += 1

	max = 0
	for y in range(Pcandidate_count):
		
		if Pcandidates[y]["votes"] > max:
			max = Pcandidates[y]["votes"]
			
	print("Winner(s):")
	for z in range(Pcandidate_count):
		if Pcandidates[z]["votes"] == max:
			print(Pcandidates[z]["name"])
			sum = 0;
			for p in range(Pcandidate_count):
				sum += Pcandidates[p]["votes"]

			percentage = round(Pcandidates[z]["votes"] / sum * 100)

	print(str(percentage) + "% of the vote")
	
elif choice == 2:
	print("""The two-round system is a voting method used to elect a single candidate, where voters cast a single vote for their preferred candidate. The election proceeds to a second round only if in the first round no candidate has received a simple majority of votes cast, or at least some other prescribed percentage.""")
	Rcandidate_count = candidate_Amount(Rcandidates)
	
	# Rvoter_count = int(input("How many voters? "))
	Rvoter_count = 2

	for q in range(Rvoter_count):
		print("Voter " + str(q+1) + "'s rankings:")
		for u in range(Rcandidate_count):
			runoff_vote = input("Rank " + str(u + 1) + "-")
			Rvotes.append({"Rank" + str(u+1):runoff_vote})
	print(Rvotes)	
		
elif choice == 3:
	print("""Approval voting is a single-winner electoral system where each voter may select ("approve") any number of candidates.""")
	Acandidate_count = candidate_Amount(Acandidates)
	
	# Avoter_count = int(input("How many voters? "))
	Avoter_count = 1
	print("Please type each candidate's name that you are voting for with a , seperating each name.")
	for b in range(Avoter_count):
		print("Voter " + str(b+1) + "'s approvals:")