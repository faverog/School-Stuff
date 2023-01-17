from scipy import signal as sig
import numpy as np
import matplotlib.pyplot as plt
import sympy as sym

def expand_expression():
    s = sym.Symbol("s")
    numerator = sym.Poly(0*s+1, s)
    denominator = sym.Poly((1+0.25*s)*(1+3*s), s)
    num = [float(x) for x in numerator.rep.rep]
    den = [float(x) for x in denominator.rep.rep]
    return num, den

def bodePlot():
    num, den = expand_expression() 
    H = sig.lti(num, den)
    w, mag, phase = sig.bode(H)

    fig, a = plt.subplots(2, 1, squeeze = False)
    a[0][0].set_title("Bode Diagram")
    a[0][0].semilogx(w, mag)
    a[0][0].set_ylabel("Magnitude (dB)")
    a[0][0].grid(True, which = "both")

    a[1][0].semilogx(w, phase)
    a[1][0].set_ylabel("Phase (deg)")
    plt.yticks([-180, -90, -45, 0, 45, 90], labels = ["-180", "-90", "-45", "0", "45", "90"])
    a[1][0].grid(True, which = "both")

    plt.xlabel("Frequency (rad/s)")

    plt.show()

# Calculates the numerical values of the magnitude and phase of specified TF
def calcMagPhase():
    freqs = [0.01, 0.1, 1, 10, 100, 1000]
    for w in freqs:
        # Input transfer function here
        z = (1000*(1j*w))/((1j*w+10)*((1j*w)+100))
        mag = 20*np.log10(abs(z))
        phase = (180/np.pi)*np.angle(z)
        print(f"w = {w}, mag = {mag:.4f}, phase = {phase:0.4f}")


if __name__ == "__main__":
    bodePlot()
    calcMagPhase()