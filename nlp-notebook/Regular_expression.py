import re

test1 = "The rain in Spain"
test2_specialchars = "The  rain  in   Sp@in!"
test3_multiple_specialchars = "Th#e r@ain in Sp@in!!"


# split the text in to list which are having whitespaces
print(re.split(r'\s', test1))

# split the text in to list which are have one or more whitespaces
print(re.findall(r'\S+', test2_specialchars))

# split the text that are having special characters
print(re.split(r'\W+', test3_multiple_specialchars))

# find all the characters which are not having special characters
print(re.findall(r'\w+', test3_multiple_specialchars))

# find all the characters which are not having one or more special characters
print(re.findall(r'\W+', test3_multiple_specialchars)) 

# find text which contains numbers and some text mixing with numbers
test4_numbers = "The rain in Spain 1234 and 5678"

print(re.split(r'\d+', test4_numbers)) # it will split the text at the position where number is found
print(re.findall(r'\d+', test4_numbers)) # it will find all the text which does not contain numbers

# find the text which is have numbers between 0 to 9, a to z and A to Z
test5_mixed = "The rain in Spain 1234 and 5678 with symbols #$% and letters ABC xyz"
print(re.split(r'[0-9a-zA-Z]+', test5_mixed))

# find the text if any upper and numbers like this format PEP338 compliant
test6_pep338 = "This is PEP338 KAB2 compliant 1234 text With UPPERCASE and lowercase Letters 5678"
print(re.findall('[A-Z]+[0-9]', test6_pep338))

# find the text which is PEP338 compliant and having one or more spaces after full stop
print(re.split(r'\.\s+', test6_pep338))

# find the text which is have uppercase with number characters
print(re.findall(r'[A-Z0-9]+', test6_pep338))

# find the text which is having only uppercase with number characters
print(re.findall(r'[^a-z\s]+', test6_pep338))

