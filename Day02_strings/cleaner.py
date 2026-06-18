full_name = input("enter your full name:")

#strip = removes extra space
name = full_name.strip()
#print staetment type 1  ......
print(f"original : {full_name}")
print(f"upper case : {full_name.upper()}")
print(f"lowercase : {full_name.lower()}")
print(f"title case : {full_name.title()}")
#print statement type 2........
print(full_name.upper())
print(full_name.lower())
print(full_name.title())


#split into first and last
names = full_name.split()
if len(names) >= 2:
    print(f"first name : {names[0]}")
    print(f"last name : {names[-1]}")
    print(f"initial : {names[0][0]}.{names[-1][0]}")
else:
    print("enter your full name:")
