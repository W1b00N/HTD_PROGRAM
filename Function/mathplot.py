import matplotlib.pyplot as pl

x = range(0, 20, 2)
y = []

def motion(ux, ax, t):
    S = (u * t) + 0.5 * (a * (t ** 2))
    return S

u = int(input('ป้อนความเร็วต้นของรถ : '))
a = int(input('ป้อนความเร่งของรถ : '))

for t in range(0, 20, 2):
    S = motion(u, a, t)
    y.append(S)
    print('S(', t, ') =', S)

pl.title('Motion')
pl.xlabel('S')
pl.ylabel('T')
pl.plot(x, y)
pl.show()
