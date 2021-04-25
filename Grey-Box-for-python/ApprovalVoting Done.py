#one weakness input canidate multiple times
def print_winners(candidate_amount, candidate_coll):
	print("Winner(s):")
	for z in range(candidate_amount):
		if candidate_coll[z]["votes"] == max:
			print(candidate_coll[z]["name"])
			sum = 0;
			for p in range(candidate_amount):
				sum += candidate_coll[p]["votes"]
			percentage = round(candidate_coll[z]["votes"] / sum * 100)

	print("Won with " + str(percentage) + "% of the vote")
def find_max(collection, candidate_amount):
	maximum = 0
	for y in range(candidate_amount):
		if collection[y]["votes"] > maximum:
			maximum = collection[y]["votes"]
	return maximum
def vote_finder():
	voters = int(input("How many voters? "))
	return voters
def candidate_finder(collection):
	temp_count = int(input("How many candiates? "))
	for t in range(temp_count):
		candidate = input("Candidate name: ")
		collection.append({"name":candidate, "votes":0,})
	return temp_count
Acandidates = []
Avotes = []
print("""Approval voting is a single-winner electoral system where each voter may select ("approve") any number of candidates.""")
Acandidate_count = candidate_finder(Acandidates)
	
Avoter_count = vote_finder()
	
for b in range(Avoter_count):
	while(True):
		Amount_Approved = int(input("How many candidates does Voter " + str(b+1) + " approve of? "))
		if Amount_Approved < Acandidate_count:
			break
		elif Amount_Approved == Acandidate_count:
			print("Approving of all candidates is useless.")
		elif Amount_Approved > Acandidate_count:
			print("Invalid")	
	
	for m in range(Amount_Approved):
		trueName = 0
		while (True):
			approval_vote = input("Please input vote: ")
			for c in range(Acandidate_count):
				if approval_vote == Acandidates[c]["name"]:
					trueName += 1
			if trueName == 1:
				break;
			else: 
				print("Invalid Name")
			
		Avotes.append({"name":approval_vote})
	
			 
substitute = len(Avotes)
for x in range(substitute):
	for b in range(Acandidate_count):
		if Acandidates[b]["name"] == Avotes[x]["name"]:
			Acandidates[b]["votes"] += 1
				
max = find_max(Acandidates, Acandidate_count)

print_winners(Acandidate_count, Acandidates)