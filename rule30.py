# This program attempts the Rule 30 cellular automata by
# Stephen Wolfram

width = 80
vnew = [0] * width
vold = [0] * width
vold[width>>1] = 1

for rows in range(100):
    for i in range(width):
        if i >= 1 and i < width-2:
            left = vold[i-1]
            central = vold[i]
            right = vold[i+1]
            
            vnew[i] = left ^ (central | right)
    vold = vnew.copy()
    for c in vnew:
        x = 'A' if c else ' '
        print(x, end='')
    print()
