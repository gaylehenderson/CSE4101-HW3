def studentMatching(studentPreferences, advisorPreferences, quota):
    studentAssignment = {}  # applicant id to advisor
    advisorAssignment = {a: [] for a in list(advisorPreferences)}  # advisor id to list of students

    freeAdvisors = list(advisorPreferences)
    nextIndex = {a: 0 for a in freeAdvisors}
    remainingSlots = {a: quota[a] for a in freeAdvisors}  # how many slots does each advisor have left?

    while freeAdvisors:
        a = freeAdvisors.pop()
        s = advisorPreferences[a][nextIndex[a]]
        nextIndex[a] += 1

        if a not in studentPreferences[s]: #student does not list this advisor as a preference
            pass 
        elif s not in studentAssignment: #if this student is not already assinged an advisor
            # match them, update both dictionaries
            studentAssignment[s] = a 
            advisorAssignment[a].append(s)
            remainingSlots[a] = remainingSlots[a] - 1 
        else: #if they have been assigned an advisor but there is a better option
            current = studentAssignment[s]  
            if studentPreferences[s].index(a) < studentPreferences[s].index(current): # prefers smaller index in studentPreferences[s]
                studentAssignment[s] = a
                advisorAssignment[a].append(s)
                remainingSlots[a] = remainingSlots[a] - 1
                advisorAssignment[current].remove(s) #remove current student from advisor assignment
                remainingSlots[current] += 1
                if current not in freeAdvisors and nextIndex[current] < len(advisorPreferences[current]):  #are they already in the queue, and do they still have someone on their list left to propose to
                    freeAdvisors.append(current) #add the current advisor back to the free advisor pool
        if remainingSlots[a] > 0 and nextIndex[a] < len(advisorPreferences[a]): #if they have unfilled capacity and there is still unproposed candidates add back to free advisors
            freeAdvisors.append(a)

    return [studentAssignment, advisorAssignment]