def studentMatching(studentPreferences, advisorPreferences, quota):
    studentAssignment = {}  # applicant id to advisor
    advisorAssignment = {a: [] for a in list(advisorPreferences)}  # advisor id to ***list*** of students

    freeAdvisors = list(advisorPreferences)
    nextIndex = {a: 0 for a in freeAdvisors}
    remainingSlots = {a: quota[a] for a in freeAdvisors}  # how many slots does each advisor have left?

    while freeAdvisors:
        a = freeAdvisors.pop()
        s = advisorPreferences[a][nextIndex[a]]
        nextIndex[a] += 1

        if a not in studentPreferences[s]: 
            pass
        elif s not in studentAssignment: 
            # match them, update both dictionaries
            studentAssignment[s] = a
            advisorAssignment[a].append(s)
            remainingSlots[a] = remainingSlots[a] - 1
        else:
            current = studentAssignment[s]  # prefers smaller index in studentPreferences[s]
            if studentPreferences[s].index(a) < studentPreferences[s].index(current):
                studentAssignment[s] = a
                advisorAssignment[a].append(s)
                remainingSlots[a] = remainingSlots[a] - 1
                advisorAssignment[current].remove(s)
                remainingSlots[current] += 1
                if current not in freeAdvisors and nextIndex[current] < len(advisorPreferences[current]):  
                    freeAdvisors.append(current)
        if remainingSlots[a] > 0 and nextIndex[a] < len(advisorPreferences[a]):
            freeAdvisors.append(a)

    return [studentAssignment, advisorAssignment]