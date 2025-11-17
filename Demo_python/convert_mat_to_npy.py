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

lena = np.array(loadmat('fonctions/data/lena.mat')['lena'], dtype=float)
mand = np.array(loadmat('fonctions/data/mandrill.mat')['mandrill'], dtype=float)
phan = np.array(loadmat('fonctions/data/phantom.mat')['phantom'], dtype=float)
regu = np.array(loadmat('fonctions/data/regular.mat')['regular'], dtype=float)

np.save('fonctions/data/phantom.npy', phan)
np.save('fonctions/data/regular.npy', regu)
np.save('fonctions/data/lena.npy', lena)
np.save('fonctions/data/mandrill.npy', mand)

