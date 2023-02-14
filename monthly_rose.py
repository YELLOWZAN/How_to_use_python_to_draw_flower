from matplotlib import cm, pyplot as plt
import numpy as np

def monthly_rose():
    fig = plt.figure(figsize=(10,7),facecolor='black',clear=True)
    ax = fig.gca(projection='3d')
    [x, t] = np.meshgrid(np.array(range(25)) / 24.0, np.arange(0, 575.5, 0.5) / 575 * 30 * np.pi - 4 * np.pi)
    p = (np.pi / 2) * np.exp(-t / (8 * np.pi))
    change = np.sin(20 * t) / 50
    u = 1 - (1 - np.mod(3.3 * t, 2 * np.pi) / np.pi) ** 4 / 2 + change
    y = 2 * (x ** 2 - x) ** 2 * np.sin(p)
    r = u * (x * np.sin(p) + y * np.cos(p)) * 1.5
    h = u * (x * np.cos(p) - y * np.sin(p))
    c = cm.get_cmap('magma')
    surf = ax.plot_surface(r * np.cos(t), r * np.sin(t), h, rstride=1, cstride=1,
                           cmap=c, linewidth=0, antialiased=True)

monthly_rose()