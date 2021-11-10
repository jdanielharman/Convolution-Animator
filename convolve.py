import scipy.integrate
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def showConvolution(t0, t, f1, f2):
    convolution = np.zeros(len(t))                          # Empty Array to Store Convolution Results
    for n, t_ in enumerate(t):                              # For Every Point in Time, Find the Convolution
        prod = lambda tau: f1(tau) * f2(t_-tau)             # Function of the Product of the two functions
        convolution[n] = scipy.integrate.simps(prod(t), t)  # Integral of the Product

    # Create the Shifted and Flipped Function
    f_shift = lambda t: f2(t0-t)                            # Flip and Shift Method for Showing the Process of Convolution
    prod    = lambda tau: f1(tau) * f2(t0-tau)              # Function of the Product of the two functions

    # Plot the curves
    plt.gcf().clear()                                                           # Clears Figure From Previous Animations
    plt.subplot(211)                                                            # 1st Subplot
    plt.plot(t, f1(t), label=r'$f_1(\tau)$')                                    # Plot the 1st Function
    plt.plot(t, f_shift(t), label=r'$f_2(t_0-\tau)$')                           # Plot the 2nd Function
    plt.fill(t, prod(t), color='r', alpha=0.5, edgecolor='black', hatch='//')   # Fill in the difference - The Part Where the Integral is Taken
    plt.plot(t, prod(t), 'r-', label=r'$f_1(\tau)f_2(t_0-\tau)$')               # Function Line for Product - Makes it More Clear 
    plt.grid(True); plt.xlabel(r'$\tau$'); plt.ylabel(r'$x(\tau)$')             # Figure Decorators
    plt.legend(fontsize=10, loc="center left")
    plt.text(-4, 0.6, '$t_0=%.2f$' % t0, bbox=dict(fc='white'))

    # plot the convolution curve
    plt.subplot(212)                                                            # 2nd Subplot 
    plt.plot(t, convolution, label='$(f_1*f_2)(t)$')                            # Plot Convolution

    # recalculate the value of the convolution integral at the current time-shift t0
    current_value = scipy.integrate.simps(prod(t), t)                           # Find Current Point of Convolution
    plt.plot(t0, current_value, 'ro')                                           # Plot Current Value of Convolution
    plt.grid(True); plt.xlabel('$t$'); plt.ylabel('$(f_1*f_2)(t)$')             # Figure Decorators
    plt.legend(fontsize=10) # il

def rect(start, stop):
    return lambda t: (t>start) * (t<stop) * np.ones(len(t))

def sin(start, amplitude=1):
    return lambda t: (t>start) * amplitude * np.sin(t)

def sinc(start, amplitude=1):
    return lambda t: (t>start) * amplitude * np.sin(t) / t

def cos(start, amplitude=1):
    return lambda t: (t>start) * amplitude * np.cos(t)

def triangle(width):
    return lambda t: np.maximum(0, width-abs(t))

def step(start, amplitude):
    return lambda t: (t>start) * amplitude * np.ones(len(t))

def ramp(start, stop):
    return lambda t: (t<stop) * (t>start) * t

def triangle_ramp():
    return lambda t: ( (t>0) * t * (t<1) ) + ( (t>1) * 1 )

def dual_step(start, start2, amp=1, amp2=1):
    return lambda t: ( (t>start) * amp ) + ((t>start2) * amp2)