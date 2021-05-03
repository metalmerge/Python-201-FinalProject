import universal_functions


def voter_recorder(candidate_count, candidate_coll, voter_coll, voter_approval,
                   current):
    for m in range(voter_approval):
        trueName = 0
        while (True):
            approval_vote = input("Please input vote: ")
            for c in range(candidate_count):
                if approval_vote == candidate_coll[c]["name"]:
                    trueName += 1
            if trueName == 1:
                break
            else:
                print("Invalid name.")

        voter_coll.append({"name": approval_vote})

    for elem in voter_coll:
        if voter_coll.count(elem) > 1 + current:
            return True
    return False


def start_Approval():
    Acandidates = []
    Avotes = []

    while (True):
        Acandidate_count = int(input("How many candiates? "))
        checker = universal_functions.candidate_finder(Acandidates,
                                                       Acandidate_count)
        if checker == True:
            print('Invalid, candidate names match.')
            Acandidates = Acandidates[:-Acandidate_count or None]
        else:
            break

    Avoter_count = universal_functions.vote_finder()

    for b in range(Avoter_count):

        while (True):
            Amount_Approved = int(
                input("How many candidates does Voter " + str(b + 1) +
                      " approve of? "))
            if Acandidate_count == 1:
                print(
                    "Well, you made a one party system, therefore the system breaks down."
                )
                break
            elif Amount_Approved < Acandidate_count:
                break
            elif Amount_Approved == Acandidate_count:
                print("Approving of all candidates is useless.")
            elif Amount_Approved > Acandidate_count:
                print("Invalid, that is more than the amount of candidates")

        while (True):
            dupiclate_check = voter_recorder(Acandidate_count, Acandidates,
                                             Avotes, Amount_Approved, b)
            if dupiclate_check == True:
                print("Invalid, can't vote for same candidate more than once.")
                Avotes = Avotes[:-Amount_Approved or None]
            else:
                break

    substitute = len(Avotes)
    for x in range(substitute):
        for b in range(Acandidate_count):
            if Acandidates[b]["name"] == Avotes[x]["name"]:
                Acandidates[b]["votes"] += 1

    max = universal_functions.find_max(Acandidates, Acandidate_count)

    universal_functions.print_winners(Acandidate_count, Acandidates, max)