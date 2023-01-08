import os, csv


def create_data_lists(budget):
    
    #Declaring lists
    profit_loss = []
    num_months = []
    changes_in_pl = []

    #Initializing variables
    previous_pl = 0
    counter = 0
    avg_change_pl = 0
    avg_change_pl_total = 0

    #For loop to traverse through the csv file.
    for row in budget:
        
        #Collecting number of months and place them in a list
        num_months.append(row[0])
        
        #Collecting the profit loss
        profit_loss.append(int(row[1]))

        #This statement helps to exclude the first value of the profit loss list because 
        # we don't know the previous months profit or loss value
        if previous_pl != 0:
            #Collecting Profit and Losses and storing it in a list
            changes_in_pl.append(int(row[1]) - previous_pl)
            #Assigning the average of the profit and loss for each month and creating a total average.
            avg_change_pl = avg_change_pl + changes_in_pl[len(changes_in_pl)-1]
            avg_change_pl_total = avg_change_pl/len(changes_in_pl)
        
        #Used to refer to the previous profit/loss item
        previous_pl = int(row[1])
        #Moving counter along
        counter += 1
    
    #setting values to return to then push to the publishing function
    num_of_months = len(num_months)
    max_month = num_months[changes_in_pl.index(max(changes_in_pl))+1]
    max_increase = max(changes_in_pl)
    min_month = num_months[changes_in_pl.index(min(changes_in_pl))+1]
    min_decrease = min(changes_in_pl)
    total = sum(profit_loss)
    avg_total = round(avg_change_pl_total,2)
    
   
    '''print("What is going on :", total)
    print(f"This is the number of months: {len(num_months)}")
    print("The Average should be maybe this: " , round(avg_change_pl_total,2))
    print("The Average should be maybe this: " , num_months[changes_in_pl.index(max(changes_in_pl))+1] , max(changes_in_pl))
    print("The Average should be maybe this: " , num_months[changes_in_pl.index(min(changes_in_pl))+1] , min(changes_in_pl))
    '''

    return num_of_months, avg_total, total, max_month, max_increase, min_month, min_decrease

def pub_analysis(number_of_months, avg_total, total_pl, m_increase, g_increase, m_decrease, g_decrease):
    #print(number_of_months, avg_total, total_pl, m_increase, g_increase, m_decrease, g_decrease)

    print("\nFinancial Analysis")
    print("---------------------------")
    print("Total Months: " + str(number_of_months))
    print("Total: " + "$" + str(total_pl))
    print("Average Change: " + "$" + str(avg_total))
    print("Greatest Increase In Profits: " + str(m_increase) + " ($"+ str(g_increase)+")")
    print("Greatest Decrease In Profits: " + str(m_decrease) + " ($"+ str(g_decrease)+")\n")

    #Set path for output file
    analysis_budg = os.path.join("Analysis", "fin_analysis")

    #Open the output file
    with open(analysis_budg,'w') as fin_analysis:

        fin_analysis.write("Financial Analysis\n")
        fin_analysis.write("---------------------------\n")
        fin_analysis.write("Total Months: " + str(number_of_months) + "\n")
        fin_analysis.write("Total: " + "$" + str(total_pl) + "\n")
        fin_analysis.write("Average Change: " + "$" + str(avg_total) + "\n")
        fin_analysis.write("Greatest Increase In Profits: " + str(m_increase) + " ($"+ str(g_increase)+ ")\n")
        fin_analysis.write("Greatest Decrease In Profits: " + str(m_decrease) + " ($"+ str(g_decrease)+ ")\n")



#Set path for file
budget_file_path = os.path.join("Resources", "budget_data.csv")

#Opening the CSV file
with open(budget_file_path, encoding="utf-8") as budget_file:
    read_budget = csv.reader(budget_file, delimiter=",")
    header_row = next(read_budget)
    
    #Calling the total_months function to calclulate the total months
    number_of_months, avg_total, total_pl, m_increase, g_increase, m_decrease, g_decrease = create_data_lists(read_budget)

    #Using an publishing analysis function
    pub_analysis(number_of_months, avg_total, total_pl, m_increase, g_increase, m_decrease, g_decrease)





