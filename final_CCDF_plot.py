from pylab import *
import matplotlib.pyplot as plt
import seaborn as sns
sns.set_context("paper")
sns.set_style("white")
lin_space = np.arange(0,16.2,0.2)


fig = figure()

CCDF_NN = np.append(np.loadtxt("./result/CCDF_trained_at_15dB SNR_L4_64_rly"), np.zeros(51))
CCDF_original = np.loadtxt("./result/64_subc_4qam_original_CCDF.txt")
CCDF_PTS = np.loadtxt("./result/64_subc_4qam_PTS_CCDF.txt")
CCDF_clipped = np.loadtxt("./result/64_subc_4qam_clipped_CCDF.txt")
semilogy(lin_space, CCDF_original ,color='black', ls='dashed', markersize=7,linewidth=1,label="Original OFDM")
semilogy(lin_space, CCDF_NN ,color='r',  marker="o", markersize=7,linewidth=1,label="PRnet")
semilogy(lin_space, CCDF_clipped ,color='g',  marker="^", markersize=7,linewidth=1,label="Clipping scheme")
semilogy(lin_space, CCDF_PTS ,color='b',  marker="s", markersize=7,linewidth=1,label="PTS scheme")


legend = legend(frameon=True,fontsize=12)
frame = legend.get_frame()
frame.set_facecolor('white')
xlabel('PAPR0 [dB]', fontsize=14)
ylabel('CCDF (PAPR<PAPR0)', fontsize=14)
ylim(ymin=np.power(10,-3.5))
xlim(xmax=14)
tick_params(labelsize=10)
grid(which='minor')
grid(which='major')
#plt.savefig('final_CCDF_plot.eps', format='eps', dpi=300)
show()
