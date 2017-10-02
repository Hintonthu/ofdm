# Lab 10 MNIST and Dropout
#import tensorflow as tf
import random
import numpy as np
import time
from pylab import *
# import matplotlib.pyplot as plt
import shutil
import os
import keras

from tensorflow.examples.tutorials.mnist import input_data

#tf.set_random_seed(777)  # reproducibility
tic = time.time()
learning_rate = 0.0001
batch_size = 50000
Nsubc = 64
modulation_level = 4
CR = 1.6
ber_clip =[]
lin_space = np.arange(0,31,5)
for SNR in range(0,31,5):

    # Tx
    N0 = 1 / np.log2(modulation_level) / 1.0 * np.power(10.0, -SNR / 10.0)
    batch_ys = np.random.randint(modulation_level, size=(batch_size, Nsubc))
    batch_y = np.zeros((batch_size, Nsubc),dtype=complex)
    decoded_symbol = np.zeros((batch_size, Nsubc))
    for n in range(batch_size):
        for m in range(Nsubc):
            if batch_ys[n,m] == 0:
                batch_y[n, m] = 1
            elif batch_ys[n,m] == 1:
                batch_y[n, m] = -1
            elif batch_ys[n,m] == 2:
                batch_y[n, m] = 1j
            elif batch_ys[n,m] == 3:
                batch_y[n, m] = -1j

    # noise generation
    noise_batch_r = (np.sqrt(N0 / 2.0)) * np.random.normal(0.0, size=(batch_size, Nsubc))
    noise_batch_i = (np.sqrt(N0 / 2.0)) * np.random.normal(0.0, size=(batch_size, Nsubc))
    rly = np.random.rayleigh(1/2.0, (batch_size, Nsubc))
    corruption_r = np.divide(noise_batch_r, rly)
    corruption_i = np.divide(noise_batch_i, rly)
    corruption_batch = corruption_r+ 1j*corruption_i
    corruption_batch = noise_batch_r + 1j * noise_batch_i

    encoded_symbol = np.fft.ifft(batch_y)
    encoded_symbol = batch_y
    clipped_symbol = np.clip(encoded_symbol,-CR,CR)
    clipped_symbol = np.clip(clipped_symbol, -CR*1j, CR*1j)

    received_symbol = encoded_symbol+corruption_batch
    ffted_symbol = np.fft.fft(received_symbol)
    ffted_symbol = received_symbol
    for n in range(batch_size):
        for m in range(Nsubc):
            decoded_symbol[n,m] = np.argmin(np.abs([ffted_symbol[n,m]-1, ffted_symbol[n,m]+1, ffted_symbol[n,m]-1j, ffted_symbol[n,m]+1j]))
    ber_clip.append(np.mean(np.equal(decoded_symbol,batch_y)+np.zeros((batch_size, Nsubc))))

print ber_clip

semilogy(lin_space, ber_clip)
ylim(ymin=1e-4)
grid()
show()