def complement(C):
    if "¬" in C:
        return C.replace("¬","")
    else:
        return "¬" + C

def verificare(C1, C2):
    for c1 in C1:
        if complement(c1) in C2:
            return True
    return False

def rezolvent(C1, C2):
    for c1 in C1:
        comp = complement(c1)
        if comp in C2:
            return (C1 - {c1}) | (C2 - {comp})

input = [
    {"A", "¬B"}, 
    {"A", "C"}, 
    {"¬B", "C"}, 
    {"¬A", "B"}, 
    {"B", "¬C"}, 
    {"¬A", "¬C"}
]

data_REZ = input[:]
data_DP = input[:]
data_DPLL = input[:]

def rezolutie(data):
    i = 0
    while i < len(data):
        j = i+1
        while j < len(data):
            if verificare(data[i], data[j]):
                rez = rezolvent(data[i], data[j])
                if rez not in data:
                    data.append(rez)

                    print("Din ({})({}) => {}".format(i+1, j+1, rez))

                    if len(rez) == 0:
                        return "Nesatisfiabil"
            j += 1
        i += 1

    return "Satisfiabil"

def rezolutie_DP(data):
    i = 0
    while i < len(data):
        j = i+1
        while j < len(data):
            if verificare(data[i], data[j]):
                rez = rezolvent(data[i], data[j])
                if rez not in data:
                    data.append(rez)

                    print("Din ({})({}) => {}".format(i+1, j+1, rez))

                    if len(rez) == 1:
                        return DP(data, rez)
            j += 1
        i += 1

def cautare_clauza_1lit(data):
    for i in data:
        if len(i) == 1:
            return DP(data, i)

    return rezolutie_DP(data)

def DP(data, C):
    for c in C:
        break

    comp = complement(c)

    print(data, c)

    i = 0
    n = len(data)
    while i < n:
        if c in data[i]:
            data.remove(data[i])

            if len(data) == 0:
                return "Satisfiabil"
            else:
                return DP(data, C)

        if comp in data[i]:
            rezolvent = data[i] - {comp}

            if len(rezolvent) == 0:
                data.remove(data[i])
                
                if len(data[i]) == 1:
                    return "Satisfiabil"
                else:
                    return DP(data, C)
            else:
                if rezolvent not in data:
                    data[i] = rezolvent

        i += 1
    
    return cautare_clauza_1lit(data)
    
print("===================================================================")
print("Rezolutie =>", rezolutie(data_REZ))
print("===================================================================")
print("DP =>", rezolutie_DP(data_DP))
#print("DPLL =>", rezolutie_DPLL(data_DPLL))
print("===================================================================")