# Importamos las librerías necesarias.
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parámetros generales
m = 1.0
g = 9.8

# Parámetros de integración
tini = 0.0
tfin = 20.0
dt = 0.1

# Condiciones iniciales
t0 = 0.0
x0 = 0.0
v0 = 100.0
y0 = np.array([x0, v0])

time = []
x = []
v = []

def derivs(t,y):
  u = y[1]
  v = -g
  return np.array([u,v])

def integrar(tini,tfin,dt,y0,derivs):
  t = tini
  y = y0
  while t <= tfin:
    y += derivs(t,y)*dt
    t += dt
    time.append(t)
    x.append(y[0])
    v.append(y[1])

integrar(tini,tfin,dt,y0,derivs)

xa = x0+v0*(np.array(time)-t0)-0.5*g*(np.array(time)-t0)**2

fig, ax = plt.subplots()
plt.title("Posición vs. tiempo")
plt.xlabel("Tiempo [s]")
plt.ylabel("Posición [m]")
ax.scatter(time, x,label="Solución numérica", s=10, c="orange", marker='x')
ax.plot(time,xa,label="Solución analítica")
plt.legend()
plt.show()

fig, ax = plt.subplots()
plt.title("Velocidad vs. tiempo")
plt.xlabel("Tiempo [s]")
plt.ylabel("Velocidad [m/s]")
ax.plot(time, v)
plt.show()

fig, ax = plt.subplots()
line, = ax.plot(time, x)

def update(num, x, y, line):
    line.set_data(x[:num], y[:num])
    return line,

ani = animation.FuncAnimation(fig, update, len(x), interval=0, 
                              fargs=[time, xa, line], blit=True)
ani.save('animacion.gif', writer='imagemagick', fps=120)