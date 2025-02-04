from __future__ import division  # apparently, integer division is lame lol
from collections import Counter, defaultdict

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

interests = [
    (0, "Hadoop"), (0, "Big Data"), (0, "HBase"), (0, "Java"),
    (0, "Spark"), (0, "Storm"), (0, "Cassandra"),
    (1, "NoSQL"), (1, "MongoDB"), (1, "Cassandra"), (1, "HBase"),
    (1, "Postgres"), (2, "Python"), (2, "scikit-learn"), (2, "scipy"),
    (2, "numpy"), (2, "statsmodels"), (2, "pandas"), (3, "R"), (3, "Python"),
    (3, "statistics"), (3, "regression"), (3, "probability"),
    (4, "machine learning"), (4, "regression"), (4, "decision trees"),
    (4, "libsvm"), (5, "Python"), (5, "R"), (5, "Java"), (5, "C++"),
    (5, "Haskell"), (5, "programming languages"), (6, "statistics"),
    (6, "probability"), (6, "mathematics"), (6, "theory"),
    (7, "machine learning"), (7, "scikit-learn"), (7, "Mahout"),
    (7, "neural networks"), (8, "neural networks"), (8, "deep learning"),
    (8, "Big Data"), (8, "artificial intelligence"), (9, "Hadoop"),
    (9, "Java"), (9, "MapReduce"), (9, "Big Data")
]


# list of connections
friendships = [(0, 1), (0, 2), (1, 2), (1, 3), (2, 3), (3, 4),
               (4, 5), (5, 6), (5, 7), (6, 8), (7, 8), (8, 9)]

# each user has a list to store their friends
for user in users:
    user["friends"] = []

# note each user's connection and populate their friendship list
for i, j in friendships:
    users[i]["friends"].append(users[j])
    users[j]["friends"].append(users[i])


# Question: What's the average number of connections?
def number_of_friends(user):  # find total number of connections by summing lengths of all friends list
    return len(user["friends"])  # how many friends does user have?


# average is sum of elements divided by number of elements
total_connections = sum(number_of_friends(user) for user in users)  # find sum of connections

# the average is simply total connections divided by number of users
num_users = len(users)
avg_connections = total_connections / num_users

print(f"Average number of connections is {avg_connections}")

# Question: who are the most connected people?
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

# Feature: "Data Scientists You May Know" suggester.
# a user might know the friends of friends.


def friends_of_friends_ids_bad(user):
    # for each user's friends, iterate over the person's friends and compile results.
    # "foaf" is short for "friend of a friend"
    return [foaf["id"]
            for friend in user["friends"]  # for each of user's friends
            for foaf in friend["friends"]]  # get each of _their_ friends


def not_the_same(user, other_user):
    # two users are not the same if they have different ids
    return user["id"] != other_user["id"]


def not_friends(user, other_user):
    # other_user is not a friend if they're not in user["friends"]
    # i.e, if they're not_the_same as all the people in user["friends"]
    return all(not_the_same(friend, other_user)
               for friend in user["friends"])


def friends_of_friend_ids(user):
    return Counter(foaf["id"]
                   for friend in user["friends"]  # for each of my friends
                   for foaf in friend["friends"]  # count *their* friends
                   if not_the_same(user, foaf)  # who aren't me
                   and not_friends(user, foaf))  # and aren't my friends


print(friends_of_friend_ids(users[3]))


# Function to find users with certain interests
def data_scientists_who_like(target_interest):
    return[user_id
           for user_id, user_interest in interests
           if user_interest == target_interest]


# ↑ works. But has to examine the whole list of interests, for every search.
# Building an index from users to interest and interest to users is better if we want to do more searches

# keys are interests, values are lists of user_ids with that interest
user_ids_by_interest = defaultdict(list)

for user_id, interest in interests:
    user_ids_by_interest[interest].append(user_id)

# keys are user_ids, values are lists of interests, for that user_id
interests_by_user_id = defaultdict(list)

for user_id, interest in interests:
    interests_by_user_id[user_id].append(interest)

# Question: Who has the most interests in common with a given user?

def most_common_interest_with(user):
    return Counter(interested_user_id  # keep count of how many times we see each user
                   for interest in interests_by_user_id[user["id"]]  # iterate over the user's interests
                   for interested_user_id in user_ids_by_interest[interest]  # for each interest, iterate over the users with the same interest
                   if interested_user_id != user["id"])
