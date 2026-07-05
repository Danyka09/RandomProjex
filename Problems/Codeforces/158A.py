# okay this is a confusing as hell assignment but basically 1st number is number of participants, 2nd numbers is which places score we need to equal to or be larger to continue to the next round. next line is scores of each participant starting with first place. so if there are 8 peaple and 2nd number is 5, the 5th places score is the divider which is 7 so anyone with 7 or more goes so we count how many people that is, in the case 6.

line_1 = list(map(int, input().split()))
line_2 = scores = list(map(int, input().split()))

n = line_1[0] # this aint even neccesary
k = line_1[1]

passed = 0

for i in scores:
    if 0 < i >= scores[k-1]: # almost had it right. but not k but k-1 since python starts at 0. claude helped me with this one thign cause i couldnt figure it out.
        passed += 1

print(passed)