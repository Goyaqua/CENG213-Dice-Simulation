import numpy as np
import random
from matplotlib import pyplot as plt

# Experiment 1

ar_A = []
ar_B = []
ar_C = []
ar_X = []

av_A = []
av_B = []
av_C = []
av_X = []
vr_X = []

# Populate the given arrays.
#simulating A, B , C and X
iterations = 30000

for i in range(1, iterations + 1):

    #1 <= dice roll <= 6 
    #0 <= random < 1
    #0 <= random * 6 < 6
    #1 <= (random * 6) + 1 <= 6

    A = int(random.random() * 6) + 1

    #1 <= dice roll <= 4 
    #0 <= random < 1
    #0 <= random * 4 < 4
    #1 <= (random * 4) + 1 <= 4

    B = int(random.random() * 4) + 1

    #coin toss = 1 or -1, (1/2 probability)
    #0 <= random < 1
    #random / 2 = 0.5

    if random.random() > 0.5:
        C = 1 
    else:
        C = -1

    X = A + (B * C)

    ar_A.append(A)
    ar_B.append(B)
    ar_C.append(C)
    ar_X.append(X)

#calculating the averages of A, B, C and X
total_A = 0
total_B = 0
total_C = 0
total_X = 0

length = iterations

for j in range(length):

    total_A += ar_A[j]
    total_B += ar_B[j]
    total_C += ar_C[j]
    total_X += ar_X[j]

    average_A = total_A / (j+1)
    average_B = total_B / (j+1)
    average_C = total_C / (j+1)
    average_X = total_X / (j+1)

    av_A.append(average_A)
    av_B.append(average_B)
    av_C.append(average_C)
    av_X.append(average_X)

#calculating the variance of X
square_of_differences = 0
for j in range(1,length + 1):

    #by the formula:
    #var = (sum of (Xi - avXi)^2) / (n-1)
    square_of_differences += (ar_X[j-1] - av_X[j-1])**2

    var_X = square_of_differences / j
    vr_X.append(var_X)

#plots
plt.figure()
plt.hist(ar_A,6,range=(1,7),align='left',density=True, rwidth=0.8)
plt.figure()
plt.hist(ar_B,4,range=(1,5),align='left',density=True, rwidth=0.8)
plt.figure()
plt.hist(ar_C,3,range=(-1,2),align='left',density=True, rwidth=0.8)
plt.figure()
plt.hist(ar_X,14,range=(-3,11),align='left',density=True, rwidth=0.8)
plt.show()

# Plot the average and variance values.

#x-values with using range
x_values = range(length)

# Plotting Average A
plt.figure()
plt.plot(x_values, av_A, label='Average A')
plt.legend()
plt.grid()

# Plotting Average B
plt.figure()
plt.plot(x_values, av_B, label='Average B')
plt.legend()
plt.grid()

# Plotting Average C
plt.figure()
plt.plot(x_values, av_C, label='Average C')
plt.legend()
plt.grid()

# Plotting Average X
plt.figure()
plt.plot(x_values, av_X, label='Average X')
plt.legend()
plt.grid()

# Plotting variance of X
plt.figure()
plt.plot(x_values, vr_X, label='Variance of X')
plt.legend()e
plt.grid()

plt.show()