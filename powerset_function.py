# powerset generates binary of 1 to 2^input length (or, number of all possible unique subsets) and checks each bit
# sequentially. 1 results in the data indexed in the position of the bit being checked relative to the total bits
# present being added to the subset, and 0 results in nothing. Each subset is added to a list.
def powerset(x):
    powerset.powerlist = []
    temp = []
    for i in range(2 ** len(x)):
        s = list((bin(i).replace("0b", "")))
        if i > 0:
            powerset.powerlist.append(temp)
        temp = []
        for p in range(len(s)):
            if s[p] == '1':
                temp.append(x[len(s) - p - 1])
    powerset.powerlist.append(temp)


powerset([1, 2, 3, 4])
print(powerset.powerlist)
