from pylab import *
import scipy.special as sc
import seaborn as sns
import matplotlib as mpl
sns.set_context("paper")
sns.set_style("white")
lin_space = np.arange(0,31,5)
lin_space2 = np.arange(0,11,2)




figure()
ber_NN = np.loadtxt("./result/OFDM_BER_trained_at_15dB SNR_L4_64_rly")
ber_clipped = np.array([0.385656875000000,	0.281966250000000,	0.138218437500000,	0.0375418750000000,	0.00875703125000000,	0.00233562500000000,	0.000752031250000000])
ber_pts = np.array([0.420379122807018,	0.294000701754386,	0.129699122807018,	0.0311117543859649,	0.00750456140350877,	0.00210491228070175,	0.000687719298245614])
print ber_clipped
# semilogy(lin_space2, err3 ,color='gray',  marker="o", markersize=5,linewidth=2,label="BER_trained_at_4dB SNR")
EbNodB=lin_space2
EbNo= np.power(10.0, (EbNodB/10.0))
k=2.0;
M=np.power(2.0,k)
x=np.sqrt(3*k*EbNo/(M-1))
ber_4qam_uncoded=(4/k)*(1-1/np.sqrt(M))*(1/2.0)*sc.erfc(x/np.sqrt(2))

#semilogy(EbNodB[0:5],ber_4qam_uncoded[0:5],color='black',  ls='dashed', markersize=5,linewidth=1,label="uncoded 4 QAM BER")
semilogy(lin_space, ber_NN ,color='r',  marker="o", markersize=7,linewidth=1,label="PRnet")
semilogy(lin_space, ber_clipped ,color='g',  marker="^", markersize=7,linewidth=1,label="Clipping scheme")
semilogy(lin_space, ber_pts ,color='b',  marker="s", markersize=7,linewidth=1,label="PTS scheme")

legend = legend(frameon=True, fontsize=12)
frame = legend.get_frame()
frame.set_facecolor('white')
xlabel('Eb/N0 [dB]', fontsize=14)
ylabel('BER', fontsize=14)
ylim(ymax=1,ymin=np.power(10,-4.0))
#xlim(xmax=9)
tick_params(labelsize=10)
grid(which='minor')
grid(which='major')
plt.savefig('final_BER_plot_rly.eps', format='eps', dpi=300)
show()