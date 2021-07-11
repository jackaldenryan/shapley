# What are the Shapley values of the factors in a production function?
I derived the formula and then wrote code for computing the Shapley values for a user-specified production function. For now, the production function must fit the following form:

<img src="images/generalized_production_func.png" alt="Production Function" width="300"/>

The user specifies the number of factors <img src="https://latex.codecogs.com/gif.latex?l" /> 
, the current values of each factor $X_k$, and each exponent $\alpha_k$. The Shapley value for factor $X_i$ is then:

<img src="images/shapley_production_formula.png" alt="Production Function" width="800"/>



