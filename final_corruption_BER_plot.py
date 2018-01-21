from pylab import *
import scipy.special as sc
import seaborn as sns
sns.set_context("paper")
sns.set_style("white")

lin_space2 = np.arange(0,31,5)
figure()
err2 = np.loadtxt("./result/OFDM_BER_trained_at_0dB SNR_L4_64_rly_corr")
err3 = np.loadtxt("./result/OFDM_BER_trained_at_5dB SNR_L4_64_rly_corr")
err4 = np.loadtxt("./result/OFDM_BER_trained_at_10dB SNR_L4_64_rly_corr")
err5 = np.loadtxt("./result/OFDM_BER_trained_at_15dB SNR_L4_64_rly_corr")
err6 = np.loadtxt("./result/OFDM_BER_trained_at_20dB SNR_L4_64_rly_corr")
err7 = np.loadtxt("./result/OFDM_BER_trained_at_25dB SNR_L4_64_rly_corr")
err8 = np.loadtxt("./result/OFDM_BER_trained_at_30dB SNR_L4_64_rly_corr")
err9 = np.loadtxt("./result/OFDM_BER_trained_at_15dB SNR_L4_64_rly_mixed")
# semilogy(lin_space2, err1 ,color='r',  marker="o", markersize=5,linewidth=2,label="BER_trained_at_0dB SNR")
semilogy(lin_space2[0:7], err2[0:7] ,color='g',  marker="o", markersize=7,linewidth=1,label="Trained at $\eta =$0dB")
semilogy(lin_space2[0:7], err3[0:7] ,color='r',  ls='dashed', markersize=7,linewidth=1,label="Trained at $\eta =$-5dB")
semilogy(lin_space2[0:7], err4[0:7] ,color='blue',  marker="^", markersize=7,linewidth=1,label="Trained at $\eta =$-10dB")
semilogy(lin_space2[0:7], err5[0:7] ,color='orange',  marker="*", markersize=7,linewidth=1,label="trained at $\eta =$-15dB")
semilogy(lin_space2[0:7], err6[0:7] ,color='black',  marker="s", markersize=7,linewidth=1,label="Trained at $\eta =$-20dB")
semilogy(lin_space2[0:7], err7[0:7] ,color='r',  marker="s", markersize=7,linewidth=1,label="Trained at $\eta =$-25dB")
semilogy(lin_space2[0:7], err8[0:7] ,color='g', ls='dashed', marker="s", markersize=7,linewidth=1,label="Trained at $\eta =$-30dB")
semilogy(lin_space2[0:7], err9[0:7] ,color='purple', marker="s", markersize=7,linewidth=1,label="Trained at $\eta =$mixed")
# semilogy(lin_space2, err3 ,color='gray',  marker="o", markersize=5,linewidth=2,label="BER_trained_at_4dB SNR")
EbNodB=lin_space2
EbNo= np.power(10.0, (EbNodB/10.0))
k=2.0;
M=np.power(2.0,k)
x=np.sqrt(3*k*EbNo/(M-1))
Pb=(4/k)*(1-1/np.sqrt(M))*(1/2.0)*sc.erfc(x/np.sqrt(2))

print Pb
#semilogy(EbNodB,Pb,color='b',  marker="*", markersize=5,linewidth=2,label="theoretical 4 QAM BER")

legend = legend(frameon=True,fontsize=12)
frame = legend.get_frame()
frame.set_facecolor('white')
xlabel('Eb/N0', fontsize=14)
ylabel('BER', fontsize=14)
ylim(ymin=np.power(10,-4.5))
#xlim(xmax=9)
tick_params(labelsize=10)
grid(which='minor')
grid(which='major')
# plt.savefig('final_corruption_BER_plot_rly.eps', format='eps', dpi=300)
show()
