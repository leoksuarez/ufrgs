import numpy as np
import matplotlib.pyplot as plt
from matplotlib.ticker import MultipleLocator, FuncFormatter

def f_1(x):
    return np.cos(x)

def f_2(x, k):
    return k*x

def fp(x, k):
    return -np.sin(x) - k

xx = np.linspace(0, 3*np.pi)

fig, (ax1, ax2) = plt.subplots(2, 1)

ax1.plot(xx, f_1(xx), label=r"$\cos(x)$")

for k in np.linspace(0.1, 0.2, 3):
    ax1.plot(xx, f_2(xx, k), label=fr"${k}x$")
    ax2.plot(xx, fp(xx, k), label=fr"k={k}")


def format_func(value, tick_number):
    # Find the nearest multiple of pi/2
    N = int(np.round(2 * value / np.pi))
    if N == 0: return "0"
    if N == 1: return r"$\pi/2$"
    if N == 2: return r"$\pi$"
    if N % 2 > 0:
        return r"${0}\pi/2$".format(N)
    return r"${0}\pi$".format(N // 2)

ax1.xaxis.set_major_locator(MultipleLocator(np.pi / 2))
ax1.xaxis.set_major_formatter(FuncFormatter(format_func))
ax2.xaxis.set_major_locator(MultipleLocator(np.pi / 2))
ax2.xaxis.set_major_formatter(FuncFormatter(format_func))

plt.tight_layout()
ax1.grid(); ax2.grid()
ax1.legend(); ax2.legend()
ax2.set_ylabel(r"$f'(x) = -\sin(x)-k$")
plt.show()