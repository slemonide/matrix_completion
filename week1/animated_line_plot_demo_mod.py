import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

fig, ax = plt.subplots()

speed = np.pi/1000

s1 = np.array([0, 1, 0, -1, 0])
s2 = np.array([1, 0, -1, 0, 1])

plt.plot(s1,s2)

theta = 0

det = np.sqrt((s2-s1)**2 + 1 + 2*np.cos(2*theta)*(s2-s1))
t1 = 1/2*(s1 + s2 - 1 + det)
t2 = 1/2*(s1 + s2 - 1 - det)

plt.plot(t1,t2)

line, = ax.plot(t1, t2)

plt.xlabel("first singular value")
plt.ylabel("second singular value")
plt.legend(["X' singular values", "Y(0) singular values",
            "Y(angle) singular values"])

def init():  # only required for blitting to give a clean slate.
    line.set_ydata([np.nan] * len(t1))
    return line,


def animate(i):
    theta = i * speed
    
    #ttl.set_text("angle = " + str(theta))

    det = np.sqrt((s2-s1)**2 + 1 + 2*np.cos(2*theta)*(s2-s1))
    t1 = 1/2*(s1 + s2 - 1 + det)
    t2 = 1/2*(s1 + s2 - 1 - det)
    
    line.set_ydata(t2)  # update the data.
    line.set_xdata(t1)
    return line,


ani = animation.FuncAnimation(
    fig, animate, init_func=init, interval=2, blit=True, save_count=50)

# To save the animation, use e.g.
#
ani.save("movie.mp4")
#
# or
#
# from matplotlib.animation import FFMpegWriter
# writer = FFMpegWriter(fps=15, metadata=dict(artist='Me'), bitrate=1800)
# ani.save("movie.mp4", writer=writer)

plt.show()