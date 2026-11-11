def ttc(patientPreference,kidneyPreference):
    patientMatch = {} #patient id to kidney

    remaining = set(patientPreference)
    nextIndex = {p:0 for p in remaining}

    while remaining:
        points = {}
        for p in remaining:
            while patientPreference[p][nextIndex[p]] not in remaining:
                nextIndex[p] += 1
            points[p] = patientPreference[p][nextIndex[p]]

        path = []
        p = next(iter(remaining))
        while p not in path:
            path.append(p)
            p = points[p]                    
        cycle = path[path.index(p):]

        for q in cycle:
            patientMatch[q] = points[q]
        remaining -= set(cycle)

    return patientMatch
