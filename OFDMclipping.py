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
batch_size = 5000
Nsubc = 64
modulation_level = 4
CR = 2
ber_clip =[]
ber = []
lin_space = np.arange(0,11,2)
for SNR in range(0,11,2):

    # Tx

    batch_ys = np.random.randint(modulation_level, size=(batch_size, Nsubc))
    batch_y = np.zeros((batch_size, Nsubc),dtype=complex)
    decoded_symbol = np.zeros((batch_size, Nsubc))
    decoded_symbol_clipped = np.zeros((batch_size, Nsubc))
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


    encoded_symbol = np.fft.ifft(batch_y)
    N0 = 1.0 / np.log2(modulation_level) / 1.0 * np.power(10.0, -SNR / 10.0)
    CL = CR * np.mean(np.abs(encoded_symbol))
    clipped_symbol = encoded_symbol
    idx1, idx2 = np.where(np.abs(encoded_symbol) > CL)
    print np.mean(np.abs(encoded_symbol))
    clipped_symbol[idx1,idx2] = np.divide(encoded_symbol[idx1,idx2],np.abs(encoded_symbol[idx1,idx2])) * CR
    print np.mean(np.abs(encoded_symbol))
    print np.mean(np.abs(clipped_symbol))
    # noise generation
    noise_batch_r = (np.sqrt(N0 / 2.0)) * np.random.normal(0.0, size=(batch_size, Nsubc))
    noise_batch_i = (np.sqrt(N0 / 2.0)) * np.random.normal(0.0, size=(batch_size, Nsubc))
    rly = np.random.rayleigh(1.0 / 2.0, (batch_size, Nsubc))
    corruption_r = np.divide(noise_batch_r, rly)
    corruption_i = np.divide(noise_batch_i, rly)
    #corruption_batch = corruption_r + 1j * corruption_i
    corruption_batch = noise_batch_r + 1j * noise_batch_i
    received_symbol = encoded_symbol/np.mean(np.abs(encoded_symbol))+corruption_batch
    received_symbol_clipped = clipped_symbol / np.mean(np.abs(encoded_symbol)) + corruption_batch
    ffted_symbol = np.fft.fft(received_symbol)
    ffted_symbol_clipped = np.fft.fft(received_symbol_clipped)
    for n in range(batch_size):
        for m in range(Nsubc):
            decoded_symbol[n,m] = np.argmin(np.abs([ffted_symbol[n,m]-1, ffted_symbol[n,m]+1, ffted_symbol[n,m]-1j, ffted_symbol[n,m]+1j]))

    BERarray = np.zeros((batch_size, Nsubc))
    idx1,idx2 = np.where(np.abs(decoded_symbol-batch_ys)==0)
    BERarray[idx1,idx2] = 0
    idx1, idx2 = np.where(np.abs(decoded_symbol - batch_ys) == 1)
    BERarray[idx1, idx2] = 1
    idx1, idx2 = np.where(np.abs(decoded_symbol - batch_ys) == 2)
    BERarray[idx1, idx2] = 2
    idx1, idx2 = np.where(np.abs(decoded_symbol - batch_ys) == 3)
    BERarray[idx1, idx2] = 1
    ber.append(np.mean(BERarray) / np.log2(modulation_level))

    for n in range(batch_size):
        for m in range(Nsubc):
            decoded_symbol_clipped[n,m] = np.argmin(np.abs([ffted_symbol_clipped[n,m]-1, ffted_symbol_clipped[n,m]+1, ffted_symbol_clipped[n,m]-1j, ffted_symbol_clipped[n,m]+1j]))

    BERarray = np.zeros((batch_size, Nsubc))
    idx1,idx2 = np.where(np.abs(decoded_symbol_clipped-batch_ys)==0)
    BERarray[idx1,idx2] = 0
    idx1, idx2 = np.where(np.abs(decoded_symbol_clipped - batch_ys) == 1)
    BERarray[idx1, idx2] = 1
    idx1, idx2 = np.where(np.abs(decoded_symbol_clipped - batch_ys) == 2)
    BERarray[idx1, idx2] = 2
    idx1, idx2 = np.where(np.abs(decoded_symbol_clipped - batch_ys) == 3)
    BERarray[idx1, idx2] = 1
    ber_clip.append(np.mean(BERarray) / np.log2(modulation_level))
print ber_clip

semilogy(lin_space, ber_clip, 'r', marker='^')
semilogy(lin_space, ber, 'b', ls='dashed',marker='o')
ylim(ymin=1e-4)
grid()
show()