user_input = input("Enter the server ID:")
print(f"you entered :{user_input}")

#string slicing:
log_line = "ERROR 2026-06-11 08:15:32 failed login for user id"
print(log_line.lower())
print(log_line.upper())
print(log_line.count("ERROR"))
print(log_line.startswith("ERROR"))

#string slicing : cuts the message
alert = log_line[0:5]
date = log_line[6:16]
time = log_line[17:25]
message = log_line[26:]
print(f"Alert : {alert},DATE : {date} ,TIME: {time} MESSAGE: {message}")
