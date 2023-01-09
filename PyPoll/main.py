import os, csv

def pub_analysis(summary, votes, winner):
    #Print out the Election Results
    print("\nElection Results")
    print("---------------------------")
    print("Total Votes: " + str(len(votes)))
    print("---------------------------")
    for candid in summary:       
        print(candid + ": " + str( round(summary[candid] / len(votes) * 100,3)) + "%" +  " " + "("+ str(summary[candid]) + ")")
    print("---------------------------")
    print("Winner: " + str(list(summary.keys())[list(summary.values()).index(winner)]))
    print("---------------------------")


    #Set path for output file
    analysis_budg = os.path.join("Analysis", "election_analysis")

    #Open and write to the output file the election results
    with open(analysis_budg,'w') as elect_analysis:
        elect_analysis.write("\nElection Results\n")
        elect_analysis.write("---------------------------\n")
        elect_analysis.write("Total Votes: " + str(len(votes)) + "\n")
        elect_analysis.write("---------------------------\n")
        for candid in summary:       
            elect_analysis.write(candid + ": " + str( round(summary[candid] / len(votes) * 100,3)) + "%" +  " " + "("+ str(summary[candid]) + ")\n")
        elect_analysis.write("---------------------------\n")
        elect_analysis.write("Winner: " + str(list(summary.keys())[list(summary.values()).index(winner)])+"\n")
        elect_analysis.write("---------------------------\n")
    

#Declaring list that will store votes cast
votes_cast = []

#Declare a dictionary
summary_dict = {}

#Initializing variables
counter = 0
vote_count = 0

#Set path for election data csv file
elect_data = os.path.join("Resources","election_data.csv")

#Open the CSV file for reading
with open(elect_data) as elect_csv:
    election_reader = csv.reader(elect_csv, delimiter=",")
    header_row = next(election_reader)
    #Loop through the election results csv file
    for row in election_reader:

        #Collect candidate votes and place them into a dictionary
        if summary_dict.get(row[2]) == None: 
            summary_dict[row[2]] = 1
        else:
            vote_count = 0
            vote_count = summary_dict.get(row[2])
            vote_count = vote_count + 1
            summary_dict.update({row[2]:vote_count})
            

        #Number of Votes cast
        votes_cast.append(row[0])

#Getting the value for the winner
winner = max(summary_dict.values())
#Passing results to function
pub_analysis(summary_dict,votes_cast,winner)


