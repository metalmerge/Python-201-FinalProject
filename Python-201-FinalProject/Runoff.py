import universal_functions


def preference_check(preferences, current):
    for elem in preferences[current]:
        if preferences[current].count(elem) > 1 and elem != []:
            return True
    return False


def vote(candidates, candidate_amount, preference, voter_amount):
    for i in range(voter_amount):

        while (True):
            print("Voter " + str(i + 1) + "'s rankings")
            for j in range(candidate_amount):
                trueName = 0
                while (True):
                    name = input("Rank " + str(j + 1) + "-")
                    for c in range(candidate_amount):
                        if name == candidates[c]["name"]:
                            trueName += 1
                    if trueName == 1:
                        break
                    else:
                        print("Invalid Name")
                preference[i][j] = name
            print("")

            checker = preference_check(preference, i)

            if checker == True:
                print('Invalid, candidate names match.')
                preference[i] = [[], [], [], [], [], [], [], []]
            else:
                break

    for b in range(voter_amount):
        for x in range(candidate_amount):
            if preference[b][0] == candidates[x]["name"]:
                candidates[x]["votes"] += 1


def eliminate_last(min, collection, candidate_amount):

    for g in range(candidate_amount):
        if collection[g]["votes"] == min:
            collection[g]["eliminated"] = True


def find_tie(min, collection, candidate_amount, voter_amount):
    remaining_amount = 0
    for g in range(candidate_amount):
        if collection[g]["eliminated"] == False:
            remaining_amount += 1

    maximum = 0
    for y in range(candidate_amount):
        if collection[y]["votes"] > maximum:
            maximum = collection[y]["votes"]
    print(maximum)
    tied = 0
    for t in range(candidate_amount):
        #if collection[t]["eliminated"] = False:
        if collection[t]["votes"] == maximum:
            tied += 1
    for m in range(candidate_amount):
        print(str(collection[m]["votes"]) + str(collection[m]["name"]))

    if tied == remaining_amount:
        print("It is a tie, the winners are:")
        for a in range(candidate_amount):
            if collection[a]["votes"] == maximum:
                print(collection[a]["name"])
        return True
    else:
        return False


def find_min(collection, candidate_amount):
    minimum = 100
    for x in range(candidate_amount):
        if collection[x]["eliminated"] == False:
            if collection[x]["votes"] < minimum:
                minimum = collection[x]["votes"]
    return minimum


def reset_votes(collection, candidate_amount):
    for x in range(candidate_amount):
        collection[x]["votes"] = 0


def winner_found(collection, candidate_amount, voter_amount, percentage_coll):
    yes = 0
    sum = 0
    for y in range(candidate_amount):
        if collection[y]["votes"] > voter_amount / 2:
            print("The winner is: " + collection[y]["name"])
            yes = 1
            for p in range(candidate_amount):
                sum += percentage_coll[p]["votes"]
            percentage = round(percentage_coll[y]["votes"] / sum * 100)

            print("Won with " + str(percentage) + "% of the vote")
    if yes == 1:
        return True
    else:
        return False


def tabulate(collection, candidate_amount, voter_amount, preference):

    for x in range(candidate_amount):
        collection[x]["votes"] = 0

    for l in range(voter_amount):
        first = preference[l][0]
        second = preference[l][1]
        third = preference[l][2]
        fourth = preference[l][3]
        fifth = preference[l][4]
        sixth = preference[l][5]
        seventh = preference[l][6]

        for r in range(candidate_amount):
            if collection[r]["eliminated"] == True:
                if collection[r]["name"] == first:
                    preference[l][0] = preference[l][1]
                elif collection[r]["name"] == second:
                    preference[l][1] = preference[l][2]
                elif collection[r]["name"] == third:
                    preference[l][2] = preference[l][3]
                elif collection[r]["name"] == fourth:
                    preference[l][3] = preference[l][4]
                elif collection[r]["name"] == fifth:
                    preference[l][4] = preference[l][5]
                elif collection[r]["name"] == sixth:
                    preference[l][5] = preference[l][6]
                elif collection[r]["name"] == seventh:
                    preference[l][6] = preference[l][7]

    for d in range(voter_amount):
        for v in range(candidate_amount):
            if collection[v]["eliminated"] == False:
                if collection[v]["name"] == preference[d][0]:
                    collection[v]["votes"] += 1


def vote_finder():
    while (True):
        voters = int(
            input(
                "How many voters? (10 is maximum allowed because too much typing)\n"
            ))
        if voters < 11 and voters > 0:
            break
        else:
            print("Invalid, not within allowed amount")
    return voters


def candidate_finder(collection, temp_count):

    for t in range(temp_count):
        candidate = input("Candidate name: ")
        collection.append({"name": candidate, "votes": 0, "eliminated": False})

    check = universal_functions.candidate_checker(collection)

    return check


def start_Runoff():
    candidates = []
    percentage_data = []
    preferences = []
    for i in range(0, 10):
        preferences.append([])
    for v in range(0, 10):
        for t in range(0, 8):
            preferences[v].append([])

    while (True):
        candidate_count = int(
            input(
                "How many candiates? (8 is maximum allowed because too much typing)\n"
            ))
        if candidate_count < 9 and candidate_count > 1:
            break
        else:
            print("Invalid, not within allowed amount")

    while (True):
        checker = candidate_finder(candidates, candidate_count)
        if checker == True:
            print('Invalid, candidate names match.')
            candidates = candidates[:-candidate_count or None]
        else:
            break

    voter_count = vote_finder()

    vote(candidates, candidate_count, preferences, voter_count)

    for z in range(candidate_count):
        percentage_data.append({
            "name": candidates[z]["name"],
            "votes": candidates[z]["votes"]
        })

    while (True):

        tabulate(candidates, candidate_count, voter_count, preferences)
        #print(preferences)

        check = winner_found(candidates, candidate_count, voter_count,
                             percentage_data)
        if check == True:
            break

        minimum = find_min(candidates, candidate_count)

        bool_tie = find_tie(minimum, candidates, candidate_count, voter_count)
        if bool_tie == True:

            #	for n in range(candidate_count):
            #			if candidates[n]["votes"] == voter_count / 2:
            #				print(candidates[n]["name"])
            break
        #for b in range(candidate_count):
        #	print(str(candidates[b]["votes"]) + str(candidates[b]["name"] + str(candidates[b]["eliminated"])))

        eliminate_last(minimum, candidates, candidate_count)

        reset_votes(candidates, candidate_count)
