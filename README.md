# What are the Shapley values for factors in a production function?
I derived the formula and then wrote some code for computing the Shapley values for a user-specified production function.

![equation](https://latex.codecogs.com/gif.latex?%5Cvarphi_%7BX_i%7D%28f%29%20%3D%20%5Cfrac%7B1%7D%7BN%7D%20%5Csum_%7Bj_l%3D0%7D%5E%7BX_l%7D%20%5Ccdots%20%5Csum_%7Bj_1%3D0%7D%5E%7BX_1%7D%20%5Cfrac%7Bf%28j_1%2C%20%5Cdots%2C%20j_i%20&plus;%201%2C%20%5Cdots%2C%20j_l%29%20-%20f%28j_1%2C%20%5Cdots%2C%20j_i%2C%20%5Cdots%2C%20j_l%29%7D%7B%5Cbinom%7BN%7D%20%7B%5Csum_%7Bk%3D1%7D%5E%7Bl%7Dj_k%7D%7D)
