states = ["WA", "NT", "Q", "SA", "NSW", "V", "T"]

neighbors = {
    "WA": ["NT", "SA"],
    "NT": ["WA", "SA", "Q"],
    "Q": ["NT", "SA", "NSW"],
    "SA": ["WA", "NT", "Q", "NSW", "V"],
    "NSW": ["Q", "SA", "V"],
    "V": ["SA", "NSW"],
    "T": []
}

colors = ["Red", "Green", "Blue"]
solution = {}

def is_safe(state, color):
    for n in neighbors[state]:
        if n in solution and solution[n] == color:
            return False
    return True

def solve(index):
    if index == len(states):
        return True
    
    state = states[index]
    
    for color in colors:
        if is_safe(state, color):
            solution[state] = color
            
            if solve(index + 1):
                return True
            
            del solution[state]
    
    return False

solve(0)

print("Australia Map Coloring Solution:")
for s in solution:
    print(s, "->", solution[s])
