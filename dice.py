import matplotlib.pyplot as plt
import random as r

result = {}
fig, ax = plt.subplots()
for x in range(100000):
    x = r.randint(1, 6)
    if x in result:
        result[x] = result[x] + 1
    else:
        result[x] = 0
x = []
y = []
for k in result:
    x.append(k)
    y.append(result[k])
ax.plot(x, y)
ax.set_ylim(0, max(y) + 500)
plt.show()
