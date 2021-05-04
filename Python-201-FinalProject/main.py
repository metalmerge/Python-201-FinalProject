import Approval, Plurality, Runoff
while (True):
    choice = int(
        input("""
	Pick what election type:
	1- Plurality
	2- Runoff
	3- Approval
	"""))
    if choice == 1:
        print(
            """In single-winner plurality voting, each voter is allowed to vote for only one candidate, and the winner of the election is the candidate who represents a plurality of voters or, in other words, received the largest number of votes."""
        )
        print("")
        Plurality.start_Plurality()
    elif choice == 2:
        print(
            """The two-round system is a voting method used to elect a single candidate, where voters cast a single vote for their preferred candidate. The election proceeds to a second round only if in the first round no candidate has received a simple majority of votes cast."""
        )
        print("")
        Runoff.start_Runoff()
    elif choice == 3:
        print(
            """Approval voting is a single-winner electoral system where each voter may select ("approve") any number of candidates."""
        )
        print("")
        Approval.start_Approval()

    again = input("Go again?\n")
    if again != "Yes" and again != "yes" and again != "Y" and again != "y":
        break
