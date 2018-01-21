from pylab import *
import scipy.special as sc
import seaborn as sns
sns.set_context("paper")
sns.set_style("white")
lin_space = [0.1, 0.05, 0.01, 0.001]
BER =[]
figure()
BER.append(np.loadtxt("./result/OFDM_BER_trained_at_15dB SNR_L4_64_rly_0.1")[4])
BER.append(np.loadtxt("./result/OFDM_BER_trained_at_15dB SNR_L4_64_rly_0.05")[4])
#BER.append(np.loadtxt("./result/OFDM_BER_trained_at_2dB SNR_L4_64_lmbd_0.03")[3])
BER.append(np.loadtxt("./result/OFDM_BER_trained_at_15dB SNR_L4_64_rly_0.01")[4])
BER.append(np.loadtxt("./result/OFDM_BER_trained_at_15dB SNR_L4_64_rly_0.001")[4])

PAPR =[]
# PAPR.append(np.mean(np.loadtxt("./result/CCDF_trained_at_2dB SNR_L4_64_lmbd_0.1")) )
# PAPR.append(np.mean(np.loadtxt("./result/CCDF_trained_at_2dB SNR_L4_64_lmbd_0.01")) )
# PAPR.append(np.mean(np.loadtxt("./result/CCDF_trained_at_2dB SNR_L4_64_lmbd_0.001")) )
# PAPR.append(np.mean(np.loadtxt("./result/CCDF_trained_at_2dB SNR_L4_64_lmbd_0.0001")) )
PAPR.append(np.mean(np.loadtxt("./result/PAPR_at_15dB SNR_L4_64_0.1")) )
PAPR.append(np.mean(np.loadtxt("./result/PAPR_at_15dB SNR_L4_64_0.05")) )
#PAPR.append(np.mean(np.loadtxt("./result/PAPR_at_2dB SNR_L4_64_lmbd_0.03")) )
PAPR.append((np.mean(np.loadtxt("./result/PAPR_at_15dB SNR_L4_64_0.01"))))
PAPR.append(np.mean(np.loadtxt("./result/PAPR_at_15dB SNR_L4_64_0.001")) )
PAPR=10*np.log10(PAPR)

semilogy(PAPR[0], BER[0],color='black',  marker="o", markersize=8,linewidth=1,label="$\lambda =$ 0.1")
semilogy(PAPR[1], BER[1],color='black',  marker="^", markersize=8,linewidth=1,label="$\lambda =$ 0.05")
#semilogy(PAPR[2], BER[2],color='black',  marker=".", markersize=7,linewidth=1,label="Lambda 0.03")
semilogy(PAPR[2], BER[2],color='black',  marker="*", markersize=8,linewidth=1,label="$\lambda =$ 0.01")
semilogy(PAPR[3], BER[3],color='black',  marker="s", markersize=8,linewidth=1,label="$\lambda =$ 0.001")
semilogy(PAPR,BER, color='black', ls='dashed', markersize=5,linewidth=1)
print PAPR
print BER
#ylim(ymin=0.005, ymax=0.05)
legend = legend(frameon=True,fontsize=12)
frame = legend.get_frame()
frame.set_facecolor('white')
xlabel('Average PAPR [dB]', fontsize=14)
ylabel('BER', fontsize=14)
tick_params(labelsize=10)
grid(which='minor')
grid(which='major')
plt.savefig('final_lambda_plot_rly.eps', format='eps', dpi=300)
show()
