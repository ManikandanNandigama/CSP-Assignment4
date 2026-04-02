
districts = ["Adilabad", "Nizamabad", "Karimnagar", "Warangal", "Khammam"]

neighbors = {
    "Adilabad": ["Nizamabad"],
    "Nizamabad": ["Adilabad", "Karimnagar"],
    "Karimnagar": ["Nizamabad", "Warangal"],
    "Warangal": ["Karimnagar", "Khammam"],
    "Khammam": ["Warangal"]
}

colors = ["Red", "Green", "Blue", "Yellow"]
solution = {}

def is_safe(district, color):
    for n in neighbors[district]:
        if n in solution and solution[n] == color:
            return False
    return True

def solve(index):
    if index == len(districts):
        return True
    
    d = districts[index]
    
    for color in colors:
        if is_safe(d, color):
            solution[d] = color
            
            if solve(index + 1):
                return True
            
            del solution[d]
    
    return False

solve(0)

print("Telangana Map Coloring Solution:")
for d in solution:
    print(d, "->", solution[d])
