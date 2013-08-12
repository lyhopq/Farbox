# coding=utf-8

import matplotlib.pyplot as plt
import numpy as np
#import matplotlib
#zhfont1 = matplotlib.font_manager.FontProperties(fname='/home/lyh/.fonts/simsun.ttc')

x = np.arange(120.0)
N = len(x)
mu = 1.0/N*sum(x)

c = np.zeros(N)
for k in range(N):
    c[k] = sum((x[:N-k]-mu)*(x[k:]-mu))/sum((x-mu)**2)

plt.figure(figsize=(8,3))
plt.plot(x, c)
#plt.ylabel(u'Correlation相关函数', fontproperties=zhfont1)
plt.ylabel(u'Correlation')
plt.savefig('correlation.png')
