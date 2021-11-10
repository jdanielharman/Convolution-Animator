'''
Original Source Code: https://stackoverflow.com/questions/56095788/convolution-integral-export-as-animation
'''
import numpy as np
from convolve import *

Fs = 50                             # Sampling Frequency for Plotting
T = np.pi * 6                       # Looking at Times from -T to T
t  = np.arange(-T, T, 1/Fs)         # Time Samples
t0 = np.arange(-10, T-2, 10/Fs)      # Time Samples for Time Reversal - Shorter to Account Artifacts near the Edges

# Stationary Function
f1 = sinc(-20)
# Time Shifted Function   
f2 = triangle(1)

fig = plt.figure(figsize=(8,3)) # Create Figure
fig.canvas.mpl_connect('close_event', lambda event: exit()) # Necessary to end program because of some bugs in matplotlib 
anim = animation.FuncAnimation(fig, showConvolution, frames=t0, fargs=(t, f1,f2), interval=50) # Create Animation Object

# Uncomment to Save Animation as a Gif - Fast Moving / Movie Writer is really slow. 
anim.save('sinc_tri.gif', writer="Pillow", fps=30)

# Uncomment to Show Plot Live - Slower moving
# plt.show()