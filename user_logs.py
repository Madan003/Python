todays_users = [108,102,107,109,110,87,88,90,102,87,88,90,102]
yesterdays_users = {108,107,102}
login_count = {}
today_logins = set()
for user_id in todays_users:
    today_logins.add(user_id)

    if user_id in login_count:
        login_count[user_id] += 1
    else:
        login_count[user_id] = 1

print("The users who logged in more than once today: ")
for user_id, freq in login_count.items():
    if freq>1:
        print(f"User - {user_id}")

print(f"Users logged in today but not yesterday {today_logins.difference(yesterdays_users)}")