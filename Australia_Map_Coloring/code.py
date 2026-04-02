import itertools

letters = "TWOFUR"
digits = range(10)

for perm in itertools.permutations(digits, len(letters)):
    t, w, o, f, u, r = perm
    
    if t == 0 or f == 0:
        continue
    
    two = 100*t + 10*w + o
    four = 1000*f + 100*o + 10*u + r
    
    if two + two == four:
        print("Solution Found:")
        print("T =", t, "W =", w, "O =", o)
        print("F =", f, "U =", u, "R =", r)
        print("TWO =", two)
        print("FOUR =", four)
        break
