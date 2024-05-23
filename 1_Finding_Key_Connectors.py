from __future__ import division  # apparently, integer division is lame lol

# list of users, detail of each user stored as dict allowing easy modification later
users = [
    {"id": 0, "name": "Hero"},
    {"id": 1, "name": "Dunn"},
    {"id": 2, "name": "Sue"},
    {"id": 3, "name": "Chi"},
    {"id": 4, "name": "Thor"},
    {"id": 5, "name": "Clive"},
    {"id": 6, "name": "Hicks"},
    {"id": 7, "name": "Devin"},
    {"id": 8, "name": "Kate"},
    {"id": 9, "name": "Klein"}
]

# list of connections
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# each user has a list to store their friends
for user in users:
    user["friends"] = []

# note each user's connection
for i, j in friendships:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])


# what's the average number of connections?
def number_of_friends(user):  # find total number of connections by summing lengths of all friends list
    return len(user["friends"])  # how many friends does user have?


total_connections = sum(number_of_friends(user) for user in users)

# the average is simply total connections divided by number of users
num_users = len(users)
avg_connections = total_connections / num_users

print(avg_connections)

# who are the most connected people?
num_friends_by_id = [(user["id"], number_of_friends(user)) for user in users]  # list user_id, number_of_friends

# since there aren't many users, we'll sort them from most to the least friends
num_friends_by_id = sorted(num_friends_by_id, key=lambda user_id_num_friends: user_id_num_friends[1], reverse=True)

highest_connection = num_friends_by_id[0][1]
users_with_hc = ""

for i, user_connection in enumerate(num_friends_by_id):
    next_user_connection = num_friends_by_id[i+1]
    user_name = ""
    for user in users:
        if user["id"] == user_connection[0]:
            user_name = user["name"]
            break
    if user_connection[1] == highest_connection:
        if next_user_connection[1] < highest_connection or i+1 > len(num_friends_by_id):
            users_with_hc += "and " + user_name + "."
        else:
            users_with_hc += user_name + ", "
    else:
        break

print(f"The users with the highest number of connections are {users_with_hc}")
