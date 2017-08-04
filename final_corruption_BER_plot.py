from pylab import *
import scipy.special as sc
import seaborn as sns
sns.set_context("paper")
sns.set_style("white")

lin_space = np.arange(0,13,2) + 10*np.log10(2)
lin_space2 = np.arange(0,13,2)
figure()
err2 = np.loadtxt("./result/OFDM_BER_trained_at_0dB SNR_L4_64_temp")
err3 = np.loadtxt("./result/OFDM_BER_trained_at_2dB SNR_L4_64_temp")
err4 = np.loadtxt("./result/OFDM_BER_trained_at_4dB SNR_L4_64_temp")
err5 = np.loadtxt("./result/OFDM_BER_trained_at_6dB SNR_L4_64_temp")
err6 = np.loadtxt("./result/OFDM_BER_trained_at_8dB SNR_L4_64_temp")
# semilogy(lin_space2, err1 ,color='r',  marker="o", markersize=5,linewidth=2,label="BER_trained_at_0dB SNR")
semilogy(lin_space2[0:5], err2[0:5] ,color='g',  marker="o", markersize=7,linewidth=1,label="Trained at $\eta =$0dB")
semilogy(lin_space2[0:5], err3[0:5] ,color='r',  ls='dashed', markersize=7,linewidth=1,label="Trained at $\eta =$-2dB")
semilogy(lin_space2[0:5], err4[0:5] ,color='blue',  marker="^", markersize=7,linewidth=1,label="Trained at $\eta =$-4dB")
#semilogy(lin_space2[0:5], err5[0:5] ,color='orange',  marker="*", markersize=5,linewidth=1,label="BER trained at -6dB corruption level")
semilogy(lin_space2[0:5], err6[0:5] ,color='black',  marker="s", markersize=7,linewidth=1,label="Trained at $\eta =$-8dB")
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
plt.savefig('final_corruption_BER_plot.eps', format='eps', dpi=300)
show()
