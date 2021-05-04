import universal_functions


def vote(candidate_coll, voter_amount, candidate_amount, vote_coll):
    for x in range(candidate_amount):
        for b in range(voter_amount):
            if candidate_coll[x]["name"] == vote_coll[b]["name"]:
                candidate_coll[x]["votes"] += 1


def start_Plurality():
    votes = []
    candidates = []

    while (True):
        candidate_count = int(input("How many candiates? "))
        checker = universal_functions.candidate_finder(candidates,
                                                       candidate_count)
        if checker == True:
            print('Invalid, candidate names match.')
            candidates = candidates[:-candidate_count or None]
        else:
            break

    voter_count = universal_functions.vote_finder()

    for i in range(voter_count):
        trueName = 0
        while (True):
            pluraility_vote = input("Voter " + str(i + 1) + "'s vote: ")
            for c in range(candidate_count):
                if pluraility_vote == candidates[c]["name"]:
                    trueName += 1
            if trueName == 1:
                break
            else:
                print("Invalid Name")
        votes.append({"name": pluraility_vote})
        if candidate_count == 1:
            print(
                "Well, you made a one party system, therefore the system breaks down."
            )
            break

    vote(candidates, voter_count, candidate_count, votes)

    max = universal_functions.find_max(candidates, candidate_count)

    universal_functions.print_winners(candidate_count, candidates, max)