name = "Bro"

print('The length of name is', len(name)) #technically this is a function
print("The position of 'o' is", name.find("o"))
print('Can capitalize and get:', name.capitalize())
print('Can transform into uppercase and get:', name.upper())
print('Can transform into lowercase and get:', name.lower())
print('Is name a digit? Answer:', name.isdigit())
print('Is name alphabetic? Answer:', name.isalpha())
print("How many 'o's in name? Answer:", name.count("o"))
print("Let's replace 'o's with 'a's and get:", name.replace("o","a"))
print("Let's multiply name with 3 and get:", name*3)