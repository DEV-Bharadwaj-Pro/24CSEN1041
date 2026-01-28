passwords = ["password", "admin", "Gitam$$123", "Gvsp$$123", "Idk"]
correct_password = "Gitam$$123"

for attempt in passwords:
    print(f"Cracking password: {attempt}")
    if attempt == "Gitam$$123":
        print("Password found! Access granted.")
        break

# OUTPUT:
#Cracking password: password
#Cracking password: admin
#Cracking password: Gitam$$123
#Password found! Access granted.
