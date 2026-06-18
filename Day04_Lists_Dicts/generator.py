first = input("enter your first name: ").strip().lower()
last = input("enter your last name: ").strip().lower()
company = "techno"

#email = f"{first}.{last}@{company}.com"
#username = f"{first[0:2]}{last}"

print(f"generated email:{first}.{last}@{company}.com")
print(f"user name:{first[0:3]}{last} NOC")
#print(f"generated email: {email}")
#print(f"user_name: {username}")
print(f"Temp password: {first.capitalize()}@123")