# go to r/eyebleach bcz this code fucking sucks and is written in hurry.
# but I hope it gets you a job/interview :p

total_sem = 5

# your credits here. This is an example showing 5 semester credit scores.
# write them like this only.

credits = {
    1: [4,4,4,4,4,3,1,1,1,2],
    2: [4,4,4,4,3,3,1,1,1,1,2],
    3: [4,4,4,4,4,1,2,1,1],
    4: [4,4,4,4,4,1,2,1,1],
    5: [4,4,4,4,4,3,2,1,1,1]
}

# do the same with your marks.

marks = {
    1: [61,60,60,65,83,64,91,81,87,77],
    2: [59,82,75,63,79,66,84,81,67,81,78],
    3: [76,77,63,92,70,86,75,81,91],
    4: [68,73,58,85,79,87,76,84,76],
    5: [77,86,77,75,68,84,94,77,85,85]
}


def with_credit_cpi(credits, marks, total_sem):
    total = 0
    total_list = []

    for x in range(1,total_sem+1):
        total = 0
        for credit,mark in zip(credits[x], marks[x]):
            total += (mark*credit)
        print("----------")
        total_list.append(total/sum(credits[x]))
        
    return sum(total_list)/total_sem

# uncomment to print cpi
# print(with_credit_cpi(credits,marks,total_sem))

def without_credit_percentage(marks, total_sem):
    # total = 0
    def_total = 0
    for mark in marks.values():
        def_total += sum(mark) / len(mark)

    return def_total / total_sem

# uncomment to print percentage without credits
# print(without_credit_percentage(marks, total_sem))
