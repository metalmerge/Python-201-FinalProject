def eliminate_last(min, collection, candidate_amount):
	for g in range(candidate_amount):
		if collection[g]["votes"] == min:
			collection[g]["eliminated"] == True
def find_tie(min, collection, candidate_amount):
	stillIn = 0;
  for g in range(candidate_amount):
    if !collection[e]["eliminated"]:
      stillIn++;
  
  tied = 0;
  for t in range(stillIn):
    if candidates[t]["votes"] == min:
      tied++;
  if tied == stillIn:
    return true
  else:
    return false
def tabulate(collection, candidate_amount, voter_amount):
	for x in range(candidate_amount):
		collection[x]["votes"] = 0;

	for l in range(voter_amount)
def find_min(collection, candidate_amount):
	listing = []
	for g in range(candidate_amount):
		listing.append(collection[g]["votes"])
	
	minimum = min(listing)
	return minimum
def reset_votes(collection, candidate_amount):
	for x in range(candidate_amount):
		collection[x]["votes"] = 0;
def winner_found(collection, candidate_amount):
	sum = 0;
	for x in range(candidate_amount):
		sum += collection[x]["votes"]
	for y in range(candidate_amount):
		if collection[y]["votes"] > sum:
			print(collection[y]["name"])
			return True
		else:
			return False
def print_votes(collection, candidate_amount):
	for x in range(candidate_amount):
		print(collection[x]["votes"])
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
	collection.append({"name":"a", "votes":0,})
	collection.append({"name":"x", "votes":0,})
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
example = [
	{
	"name": "Dima",
	"rank#": "Dima",
	"votes": 0,
	"eliminated": False 
	}
]
#Potential bugs: one vote, invalid input for amount
choice = 2
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
	print("""The two-round system is a voting method used to elect a single candidate, where voters cast a single vote for their preferred candidate. The election proceeds to a second round only if in the first round no candidate has received a simple majority of votes cast.""")
	Rcandidate_count = candidate_finder(Rcandidates)
	
	Rvoter_count = vote_finder()

	for q in range(Rvoter_count):
		print("Voter " + str(q+1) + "'s rankings:")
		for u in range(Rcandidate_count):
			runoff_vote = input("Rank " + str(u + 1) + "-")
			Rvotes.append({"Rank": str(u+1), "name":runoff_vote, "eliminated":False})
	
	#sub = len(Rvotes)
	#for s in range(sub):
	#	if Rvotes[s]["Rank"] == "1":
	#		for d in range(Rcandidate_count):
	#			if Rcandidates[d]["name"] == Rvotes[s]["name"]:
	#				Rcandidates[d]["votes"] += 1
	
	while(True):
		tabulate(Rcandidates,Rcandidate_count, Rvoter_count)
		check = winner_found(Rcandidates,Rcandidate_count)
		if check == True:
			break
		minimum = find_min(Rcandidates,Rcandidate_count)
		bool_tie = find_tie(minimum,Rcandidates,Rcandidate_count)
		if bool_tie == True:
			for n in range(Rcandidate_count):
				if !Rcandidates[n]["eliminated"]:
					print(Rcandidates[n]["name"])
			break
			
		eliminate_last(minimum, Rcandidates,Rcandidate_count)

		reset_votes(Rcandidates,Rcandidate_count)
	

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
