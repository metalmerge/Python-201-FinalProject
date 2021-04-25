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
Pvotes = []
Pcandidates = []

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