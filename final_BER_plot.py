from pylab import *
import scipy.special as sc
import seaborn as sns
import matplotlib as mpl
sns.set_context("paper")
sns.set_style("white")
lin_space = np.arange(0,13,2) + 10*np.log10(2)
lin_space2 = np.arange(0,11,2)



figure()
err0 = np.loadtxt("./result/OFDM_SER_trained_at_2dB SNR_L4_64")
ser_4qam = np.loadtxt("./result/4qam")
# semilogy(lin_space, err_1[1:] ,color='r',  marker="^", markersize=5,linewidth=2, label="SER_trained_at_-2dB SNR")
semilogy(lin_space, err0 ,color='y',  marker="o", markersize=5,linewidth=2,label="SER_trained_at_2dB SNR")
semilogy(lin_space, ser_4qam ,color='c',  marker="*", markersize=8,linewidth=2,ls='dashed',label="SER_4QAM")
# semilogy(lin_space, err2[0:7] ,color='blue',  marker="^", markersize=5,linewidth=2,label="SER_trained_at_10dB SNR")
# semilogy(lin_space, err8 ,color='y',  marker="o", markersize=5,linewidth=2,label="SER_trained_at_8dB SNR_200000")
# semilogy(lin_space, err3[0:7] ,color='g',  marker="^", markersize=5,linewidth=2,label="SER_trained_at_12dB SNR")
# semilogy(lin_space, err4[0:7] ,color='purple',  marker="^", markersize=5,linewidth=2,label="SER_trained_at_14dB SNR")
legend()
xlabel('Es/N0', fontsize=12)
ylabel('SER', fontsize=12)
grid(which='minor')
grid(which='major')

figure()
ber_NN = np.loadtxt("./result/OFDM_BER_trained_at_2dB SNR_L4_64")
ber_clipped = np.array([0.100859523809524,	0.0612825396825397,	0.0328087301587302,	0.0157000000000000,	0.00706984126984127,	0.00313333333333333,	0.00155634920634921])
ber_pts = np.array([0.181585385122442,	0.0584408311077144,	0.0156014874467276,	0.00277642854133844,	0.000237129209655346,	6.50549031421613e-06,	0])
print ber_clipped
# semilogy(lin_space2, err3 ,color='gray',  marker="o", markersize=5,linewidth=2,label="BER_trained_at_4dB SNR")
EbNodB=lin_space2
EbNo= np.power(10.0, (EbNodB/10.0))
k=2.0;
M=np.power(2.0,k)
x=np.sqrt(3*k*EbNo/(M-1))
ber_4qam_uncoded=(4/k)*(1-1/np.sqrt(M))*(1/2.0)*sc.erfc(x/np.sqrt(2))

#semilogy(EbNodB[0:5],ber_4qam_uncoded[0:5],color='black',  ls='dashed', markersize=5,linewidth=1,label="uncoded 4 QAM BER")
semilogy(lin_space2[0:5], ber_NN[0:5] ,color='r',  marker="o", markersize=7,linewidth=1,label="PRnet")
semilogy(lin_space2[0:5], ber_clipped[0:5] ,color='g',  marker="^", markersize=7,linewidth=1,label="Clipping scheme")
semilogy(lin_space2[0:5], ber_pts[0:5] ,color='b',  marker="s", markersize=7,linewidth=1,label="PTS scheme")
legend = legend(frameon=True, fontsize=12)
frame = legend.get_frame()
frame.set_facecolor('white')
xlabel('Eb/N0', fontsize=14)
ylabel('BER', fontsize=14)
ylim(ymax=1,ymin=np.power(10,-4.5))
xlim(xmax=9)
tick_params(labelsize=10)
grid(which='minor')
grid(which='major')
plt.savefig('final_BER_plot.eps', format='eps', dpi=300)
show()