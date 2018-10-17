# Python-challenge
Python homework for bootcamp

# PyBank

In this challenge, you are tasked with creating a Python script for analyzing the financial records of your company. You will be given two sets of revenue data (budget_data_1.csv and budget_data_2.csv). Each dataset is composed of two columns: Date and Revenue. (Thankfully, your company has rather lax standards for accounting so the records are simple.)

Your task is to create a Python script that analyzes the records to calculate each of the following:


The total number of months included in the dataset
The total amount of revenue gained over the entire period
The average change in revenue between months over the entire period
The greatest increase in revenue (date and amount) over the entire period
The greatest decrease in revenue (date and amount) over the entire period


As an example, your analysis should look similar to the one below:

Financial Analysis
----------------------------
Total Months: 25
Total Revenue: $1241412
Average Revenue Change: $216825
Greatest Increase in Revenue: Sep-16 ($815531)
Greatest Decrease in Revenue: Aug-12 ($-652794)
Your final script must be able to handle any such similarly structured dataset in the future (your boss is going to give you more of these -- so your script has to work for the ones to come). In addition, your final script should both print the analysis to the terminal and export a text file with the results.


# PyBoss

In this challenge, you get to be the boss. You oversee hundreds of employees across the country developing Tuna 2.0, a world-changing snack food based on canned tuna fish. Alas, being the boss isn't all fun, games, and self-adulation. The company recently decided to purchase a new HR system, and unfortunately for you, the new system requires employee records be stored completely differently.

Your task is to help bridge the gap by creating a Python script able to convert your employee records to the required format. Your script will need to do the following:


Import the employee_data1.csv and employee_data2.csv files, which currently holds employee records like the below:


Emp ID,Name,DOB,SSN,State
214,Sarah Simpson,1985-12-04,282-01-8166,Florida
15,Samantha Lara,1993-09-08,848-80-7526,Colorado
411,Stacy Charles,1957-12-20,658-75-8526,Pennsylvania

Then convert and export the data to use the following format instead:


Emp ID,First Name,Last Name,DOB,SSN,State
214,Sarah,Simpson,12/04/1985,***-**-8166,FL
15,Samantha,Lara,09/08/1993,***-**-7526,CO
411,Stacy,Charles,12/20/1957,***-**-8526,PA


In summary, the required conversions are as follows:


The Name column should be split into separate First Name and Last Name columns.
The DOB data should be re-written into MM/DD/YYYY format.
The SSN data should be re-written such that the first five numbers are hidden from view.
The State data should be re-written as simple two-letter abbreviations.


Special Hint: You may find this link to be helpful—Python Dictionary for State Abbreviations.

# PyPoll

In this challenge, you are tasked with helping a small, rural town modernize its vote-counting process. (Up until now, Uncle Cleetus had been trustfully tallying them one-by-one, but unfortunately, his concentration isn't what it used to be.)

You will be given two sets of poll data (election_data_1.csv and election_data_2.csv). Each dataset is composed of three columns: Voter ID, County, and Candidate. Your task is to create a Python script that analyzes the votes and calculates each of the following:


The total number of votes cast
A complete list of candidates who received votes
The percentage of votes each candidate won
The total number of votes each candidate won
The winner of the election based on popular vote.


As an example, your analysis should look similar to the one below:

Election Results
-------------------------
Total Votes: 620100
-------------------------
Rogers: 36.0% (223236)
Gomez: 54.0% (334854)
Brentwood: 4.0% (24804)
Higgins: 6.0% (37206)
-------------------------
Winner: Gomez
-------------------------
Your final script must be able to handle any such similarly-structured dataset in the future (i.e you have zero intentions of living in this hillbilly town -- so your script needs to work without massive re-writes). In addition, your final script should both print the analysis to the terminal and export a text file with the results.
