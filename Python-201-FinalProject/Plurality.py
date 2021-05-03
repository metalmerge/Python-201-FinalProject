import universal_functions


def vote(candidate_coll, voter_amount, candidate_amount, vote_coll):
    for x in range(candidate_amount):
        for b in range(voter_amount):
            if candidate_coll[x]["name"] == vote_coll[b]["name"]:
                candidate_coll[x]["votes"] += 1


def start_Plurality():
    Pvotes = []
    Pcandidates = []

    while (True):
        Pcandidate_count = int(input("How many candiates? "))
        checker = universal_functions.candidate_finder(Pcandidates,
                                                       Pcandidate_count)
        if checker == True:
            print('Invalid, candidate names match.')
            Pcandidates = Pcandidates[:-Pcandidate_count or None]
        else:
            break

    Pvoter_count = universal_functions.vote_finder()

    for i in range(Pvoter_count):
        trueName = 0
        while (True):
            pluraility_vote = input("Voter " + str(i + 1) + "'s vote: ")
            for c in range(Pcandidate_count):
                if pluraility_vote == Pcandidates[c]["name"]:
                    trueName += 1
            if trueName == 1:
                break
            else:
                print("Invalid Name")
        Pvotes.append({"name": pluraility_vote})
        if Pcandidate_count == 1:
            print(
                "Well, you made a one party system, therefore the system breaks down."
            )
            break

    vote(Pcandidates, Pvoter_count, Pcandidate_count, Pvotes)

    max = universal_functions.find_max(Pcandidates, Pcandidate_count)

    universal_functions.print_winners(Pcandidate_count, Pcandidates, max)