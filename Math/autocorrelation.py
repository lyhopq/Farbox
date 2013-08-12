# coding=utf-8

import matplotlib.pyplot as plt
import numpy as np
#import matplotlib
#zhfont1 = matplotlib.font_manager.FontProperties(fname='/home/lyh/.fonts/simsun.ttc')

t = np.arange(0, 20*np.pi, 0.1)
x = np.sin(t)
N = len(x)
mu = 1.0/N*sum(x)

c = np.zeros(N)
for k in range(N):
    c[k] = sum((x[:N-k]-mu)*(x[k:]-mu))/sum((x-mu)**2)

plt.figure(figsize=(8,3))
plt.plot(t, c, label=u'$sin(x)$ auto correlation')
#plt.ylabel(u'Correlation相关函数', fontproperties=zhfont1)
plt.legend()
plt.savefig('autocorrelation.png')

