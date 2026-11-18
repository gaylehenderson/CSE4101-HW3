def ttc(patientPreference,kidneyPreference):
    patientMatch = {} #patient id to kidney

    remaining = set(patientPreference) #set instead of list because we dont want duplicates and can be unordered
    nextIndex = {p:0 for p in remaining}

    while remaining: #while we still have unmatched patients remaining in the set
        points = {} #making points a list because each patient will "point" to their preferred kidney, we can have duplicates
        for p in remaining: #each patient in remaining
            while patientPreference[p][nextIndex[p]] not in remaining:
                nextIndex[p] += 1
            points[p] = patientPreference[p][nextIndex[p]] #each patient in points points to the kidney they most prefer, where next index is the next one that hasnt been ruled out yet

        path = [] #tracing arrows from patient A to patient B that has their preferred kidney
        current_p = next(iter(remaining)) #one at a time, hand out a new patient p, does not matter who we start with
        while current_p not in path:
            path.append(current_p) #add p to the path
            current_p = points[current_p] #p becomes the one that old p was pointing to                  
        cycle = path[path.index(current_p):] #cut out the patient that leads to the cycle
        #for example, if A -> B, B -> C, C -> B, we cut out A to give the cycle B -> C and C -> B

        for q in cycle:
            patientMatch[q] = points[q] #add cycle to patientMatch
        remaining -= set(cycle) #remove cycle from the set

    return patientMatch


