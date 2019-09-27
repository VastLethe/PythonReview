import random
import sorting_class

# initializing a 2D list. The first number of a sublist is
#   the deadline, and the 2nd number is the profit of the job.
#   Each sublist is the info of the job.
#   Maximize the profit.

jobInfo = []

"""
#test

for x in range(10):
    jobInfo.append([random.randrange(1, 11)])
    jobInfo[x].append(random.randrange(50))

"""

jobInfo = [[9, 15], [2, 2], [5, 18], [7, 1], [4, 25], [2, 20], [5, 8], [7, 10], [4, 12], [3, 5]]

sorting_class.sort_2d(jobInfo, 0, 10, 0)
latestDeadline = jobInfo[-1][0]

sorting_class.sort_2d(jobInfo, 0, 10, 1)
jobInfo.reverse() # so that it starts from the biggest

greedyJobs = [[0, 0]] * latestDeadline

for i in range(len(jobInfo)):
    for a in range(jobInfo[i][0] - 1, -1, -1):
        if greedyJobs[a][0] == 0:
            greedyJobs[a] = jobInfo[i]
            break

profit = 0
for x in range(len(greedyJobs)):
    profit += greedyJobs[x][1]
print(profit)

# the maximized profit is 109 in this case


