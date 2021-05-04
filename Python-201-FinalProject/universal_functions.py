def candidate_checker(collection):
    for elem in collection:
        if collection.count(elem) > 1:
            return True
    return False


def vote_finder():
    while (True):
        voters = int(input("How many voters? "))
        if voters <= 0:
            print("Sorry no, invalid.")
        else:
            break
    return voters


def find_max(collection, candidate_amount):
    maximum = 0
    for y in range(candidate_amount):
        if collection[y]["votes"] > maximum:
            maximum = collection[y]["votes"]
    return maximum


def print_winners(candidate_amount, candidate_coll, max):
    print("Winner(s):")
    for z in range(candidate_amount):
        if candidate_coll[z]["votes"] == max:
            print(candidate_coll[z]["name"])
            sum = 0
            for p in range(candidate_amount):
                sum += candidate_coll[p]["votes"]

            percentage = round(candidate_coll[z]["votes"] / sum * 100)

    print("Won with " + str(percentage) + "% of the vote")


def candidate_finder(collection, temp_count):
    for t in range(temp_count):
        candidate = input("Candidate name: ")
        collection.append({
            "name": candidate,
            "votes": 0,
        })

    check = candidate_checker(collection)

    return check
