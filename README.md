# CENG222-Dice-Simulation
A fair 6-face and a fair 4-face dice are rolled, alongside a fair coin toss. The random variables A and B represent the outcomes of the dice rolls, with A ranging from 1 to 6 and B from 1 to 4. Variable C is determined by the result of the coin toss, assigned +1 for heads and -1 for tails. Another random variable X is formulated as A+(B*C).

Simulated and iterated through this experiment 30000 times. For each iteration, stored the updated average value for all four random variables and the variance
of X in the given lists.

Plotted the average values of all four variables calculated throughout the experiment and the variance of X calculated throughout the experiment.

Figure 4: Shows the possibilities of X which is X= A + BC. Due to X's calculation it's graph is not uniformly distributed. X's probability is higher on the middle and lower on the edges of the interval [-3, 10] which are values of X can get.

Figure 3: Shows the possibilities of 2 sided fair coin toss. Outcomes are -1 (tail), 1 (head) with possibility of 1/2. When we toss the coin 30 .000 times our possibilities are near 1/2 which is very close to our theoretical possibility.

Figure 2: Shows the possibilities for the outcomes of the 4-faced dice (B), ranging from 1 to 4. Like Figure 1, this graph is also uniformly distributed, with each outcome having a probability of approximately 1/4. The experimental probabilities closely match the theoretical values.

Figure 1: This graph shows the possibilities for the outcomes of the 6-faced dice (A), ranging from 1 to 6. The graph is uniformly distributed, meaning that each outcome is equally likely, which is approximately 1/6 or 0.1667.

Figure 8: Shows the experimental average values of X. The average stabilizes near 3.5, which is very close to our theoretical mean M = 3.5. We can conclude that our theoretical mean is correct.

Figure 9: Shows the experimental values of variance of X. The variance stabilizes near 10.5 after several iterations, which is close to our theoretical value of Variance Var(x)=10.416. We can conclude that our theoretical variance is accurate.
