import numpy as np
import skfuzzy as fuzz
import matplotlib.pyplot as plt

# 定義輸入範圍
x = np.linspace(-10, 10, 1000)

# 高斯隸屬函數
# mean: 均值, sigma: 標準差
gauss = fuzz.gaussmf(x, mean=0, sigma=2)

# 雙高斯隸屬函數
# mean1: 第一個高斯函數的均值, sigma1: 第一個高斯函數的標準差
# mean2: 第二個高斯函數的均值, sigma2: 第二個高斯函數的標準差
gauss2 = fuzz.gauss2mf(x, mean1=-5, sigma1=1.5, mean2=5, sigma2=1.5)

# 一般化貝爾隸屬函數
# a: 控制曲線的寬度, b: 控制曲線的形狀, c: 控制曲線的中心
gbell = fuzz.gbellmf(x, a=2, b=4, c=0)

# S型隸屬函數
# a: 曲線開始上升的點, b: 曲線達到最高點的點
s = fuzz.smf(x, a=-5, b=5)

# Z型隸屬函數
# a: 曲線開始下降的點, b: 曲線達到最低點的點
z = fuzz.zmf(x, a=-5, b=5)

# Pi型隸屬函數
# a: 曲線開始上升的點, b: 曲線達到最高點的第一個點
# c: 曲線開始下降的點, d: 曲線達到最低點的點
pi = fuzz.pimf(x, a=-8, b=-2, c=2, d=8)

# 三角形隸屬函數
# abc: 三角形的三個頂點
tri = fuzz.trimf(x, abc=[-5, 0, 5])

# 梯形隸屬函數
# abcd: 梯形的四個頂點
trap = fuzz.trapmf(x, abcd=[-7, -3, 3, 7])

# 差異Sigmoid隸屬函數
# b1: 第一個Sigmoid函數的斜率, c1: 第一個Sigmoid函數的中心
# b2: 第二個Sigmoid函數的斜率, c2: 第二個Sigmoid函數的中心
dsig = fuzz.dsigmf(x, b1=-2, c1=-5, b2=2, c2=5)

# 乘積Sigmoid隸屬函數
# b1: 第一個Sigmoid函數的斜率, c1: 第一個Sigmoid函數的中心
# b2: 第二個Sigmoid函數的斜率, c2: 第二個Sigmoid函數的中心
psig = fuzz.psigmf(x, b1=-2, c1=-5, b2=2, c2=5)

# 繪製所有隸屬函數
plt.figure(figsize=(15, 10))

plt.subplot(3, 3, 1)
plt.plot(x, gauss)
plt.title('Gaussian Membership Function')

plt.subplot(3, 3, 2)
plt.plot(x, gauss2)
plt.title('Double Gaussian Membership Function')

plt.subplot(3, 3, 3)
plt.plot(x, gbell)
plt.title('Generalized Bell Membership Function')

plt.subplot(3, 3, 4)
plt.plot(x, s)
plt.title('S-shaped Membership Function')

plt.subplot(3, 3, 5)
plt.plot(x, z)
plt.title('Z-shaped Membership Function')

plt.subplot(3, 3, 6)
plt.plot(x, pi)
plt.title('Pi-shaped Membership Function')

plt.subplot(3, 3, 7)
plt.plot(x, tri)
plt.title('Triangular Membership Function')

plt.subplot(3, 3, 8)
plt.plot(x, trap)
plt.title('Trapezoidal Membership Function')

plt.subplot(3, 3, 9)
plt.plot(x, dsig)
plt.title('Difference Sigmoid Membership Function')

plt.tight_layout()
plt.show()
