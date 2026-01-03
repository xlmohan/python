# Read in the raw text data
rawData = open("SMSSpamCollection.tsv", "r").read()

# Print the raw data
# print(rawData[0:500])

parsedData = rawData.split("\n")

# Print the first 5 entries of the parsed data - it will take five lines and split them into a list
#print(parsedData[0:5])

parsedDataTab = rawData.replace("\t" , "\n").split("\n")

# Print the first 5 entries of the parsed data split by tab
print(parsedDataTab[0:5])