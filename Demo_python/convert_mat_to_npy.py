import numpy as np
import matplotlib.pyplot as plt

from fonctions.io import read_data

from scipy.io import loadmat

fft_catbrain = loadmat("fonctions/data/IRM.mat")['IRM']
np.save('fonctions/data/IRM.npy', fft_catbrain)
IRM = read_data('IRM.npy')

plt.imshow(np.log(np.abs(np.real(fft_catbrain))))
plt.show()

plt.imshow(np.log(np.abs(np.real(IRM))))
plt.show()
