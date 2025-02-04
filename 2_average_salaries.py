# Question: How much does a data scientist earn?

salaries_and_tenures = [(83000, 8.7), (88000, 8.1),
                        (48000, 0.7), (76000, 6),
                        (69000, 6.5), (76000, 7.5),
                        (60000, 2.5), (83000, 10),
                        (48000, 1.9), (63000, 4.2)]

# The natural first step is to import the data
import numpy as np
import matplotlib.pyplot as plt
from collections import  defaultdict

y_points = np.array([value[0] for value in salaries_and_tenures])
x_points = np.array([value[1] for value in salaries_and_tenures])

plt.scatter(x_points, y_points)
plt.xlim(0, 12)
plt.ylim(40000, 100000)
plt.show()

# Graph shows people with more experience tend to earn more.
# How to turn this into a fun fact?

# Let's look at average salary for each tenure:
salary_by_tenure = defaultdict(list)
for salary, tenure in salaries_and_tenures:
    salary_by_tenure[tenure].append(salary)  # keys = years, value = list of salaries of each tenure

# keys = years, value = average salary for that tenure
average_salary_by_tenure = {
    tenure: sum(salaries) / len(salaries) for tenure, salaries in salary_by_tenure.items()
}

print(average_salary_by_tenure)  # this is not very helpful since none of the users have the same tenure.

# Let's try putting the tenures into buckets


def tenure_bucket(tenure):
    if tenure < 2:
        return "less than two"
    elif tenure < 5:
        return "between two and five"
    else:
        return "more than five"


# Group salaries into buckets:
salary_by_tenure_bucket = defaultdict(list)
for salary, tenure in salaries_and_tenures:  # keys = tenure buckets, values = salary list for that buckex
    bucket = tenure_bucket(tenure)
    salary_by_tenure_bucket[bucket].append(salary)

# Now compute average salary for each group
average_salary_by_bucket = {
    tenure_bucket: sum(salaries) / len(salaries) for tenure_bucket, salaries in salary_by_tenure_bucket.items()
}

print(average_salary_by_bucket)

# The latter is more interesting and comes with the cool soundbite:
"""Data scientists with more than five years experience earn 65% more than 
data scientists with little or no experience"""

# But we chose the buckets pretty arbitrarily.
# End goal would be making some statement about salary effect - on average - of having an additional year of experience.
