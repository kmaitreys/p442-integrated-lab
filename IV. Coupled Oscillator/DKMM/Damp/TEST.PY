import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import find_peaks


file1 = '/home/ws10/maitrey/p442-integrated-lab/IV. Coupled Oscillator/DKMM/DLL0002.CSV'
data = np.loadtxt(file1, delimiter=',')
t1 = data[:, 0] # first wave
y1 = data[:, 1] # first wave
t2 = data[:, 2] # second wave
y2 = data[:, 3] # second wave

y1_square = y1**2
peaks1, _ = find_peaks(y1_square, height=0.1, distance=50)
y2_square = y2**2
peaks2, _ = find_peaks(y2_square, height=0.1, distance=50)

# Plot the square of the amplitudes (peaks)

fig, (ax1, ax2) = plt.subplots(nrows=2, figsize=(12, 8), sharex=True, sharey=True)

ax1.plot(t1, y1_square, label='Recorded data')
ax1.plot(t1[peaks1], y1_square[peaks1], 'x', label='Peaks')
ax1.set_ylabel('Square of the amplitude of first oscillator')
ax1.legend()

ax2.plot(t2, y2_square, label='Recorded data')
ax2.plot(t2[peaks2], y2_square[peaks2], 'x', label='Peaks')
ax2.set_xlabel('time (s)')
ax2.set_ylabel('Square of the amplitude of second oscillator')
ax2.legend()

fig.align_ylabels()
plt.tight_layout()
# fig.legend(loc='upper center', bbox_to_anchor=(0.5, 1.05), ncol=2)
plt.savefig(f"{file1[-6:-4]}_square.png",dpi=600)
plt.show()

