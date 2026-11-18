

def stableMatching(advisorPreferences,studentPreferences):
    advisorAssignment = {} #advisor id to student
    studentAssignment = {} #student id to advisor

    freeAdvisors = list(advisorPreferences)
    nextIndex = {a: 0 for a in freeAdvisors}

    while freeAdvisors:
        a = freeAdvisors.pop()
        s = advisorPreferences[a][nextIndex[a]]
        nextIndex[a] += 1

        if s not in studentAssignment: #student is not yet assigned an advisor
            studentAssignment[s] = a #match them, update both dictionaires
            advisorAssignment[a] = s
        else:
            current = studentAssignment[s] #look at this current student in student assignment
            if studentPreferences[s].index(a) < studentPreferences[s].index(current):  #if the next index is a better matching than this one
                studentAssignment[s] = a #match these two up instead
                advisorAssignment[a] = s
                del advisorAssignment[current]
                freeAdvisors.append(current) #put this advisor back in free advisors
            else: 
                freeAdvisors.append(a)

    return [advisorAssignment, studentAssignment]
