from pylab import *
import scipy.special as sc

lin_space = np.arange(0,100000,10)



figure()
err0 = np.loadtxt("./result/cost_at_learning_rate1e-05")
err1 = np.loadtxt("./result/cost_at_learning_rate0.0001")
err2 = np.loadtxt("./result/cost_at_learning_rate0.001")
err3 = np.loadtxt("./result/cost_at_learning_rate0.01")
semilogy(lin_space[0::100], err0[0::100],color='black',  ls='dashed', markersize=5,linewidth=1,label="learning rate 0.00001")
semilogy(lin_space[0::100], err1[0::100] ,color='r', marker='*',  markersize=5,linewidth=1,label="learning rate 0.0001")
semilogy(lin_space[0::100], err2[0::100] ,color='g', marker='o',  markersize=5,linewidth=1,label="learning rate 0.001")
semilogy(lin_space[0::100], err3[0::100] ,color='b', marker='^',  markersize=5,linewidth=1,label="learning rate 0.01")

legend()
xlabel('Training iteration [batch]', fontsize=12)
ylabel('Cost', fontsize=12)
ylim(ymax=1, ymin=np.power(10,-1.5))
grid(which='minor')
grid(which='major')

show()
