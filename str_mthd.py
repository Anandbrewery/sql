name=input()
print(len(name))
res=name.find("a") #first occ of the character/string presnt returns -1 if char not fnd
res2=name.rfind("o") # finds last occ of the char or string specified -1 if char not fnd
res3=name.capitalize() # captitalize 1st letter
res4=name.upper()# make all char uppercase
res5=name.lower()# make all char lower
resBool=name.isdigit() # returns if only digits are present
resBool=name.isalpha() # returns true iff only char present and no white space
ph_no=123-456-789
cnt=ph.count("-") # cnts no of dashes in the variable
res=ph_no.replace("-"," ") # replaces - with ph no with dashes
print(res)