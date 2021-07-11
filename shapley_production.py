import math
import numpy as np

num_factors = int(input("How many factors do you want to use? Enter a positive integer:"))
exps = []
vals = []
for i in range(num_factors):
    val = int(input("Value for Factor %s? Enter a positive integer:" % i))
    vals.append(val)
    exp = float(input("Exponent for Factor %s? Enter a decimal number:" % i))
    exps.append(exp)

shaps = []
n = np.sum(vals)
im1_vals = vals.copy()
im2_vals = vals.copy()
im2_vals = [x+1 for x in im2_vals]
im2_vals.pop()

# Looping over each factor and calculating shapley value
for shap_factor in range(num_factors):
    shap = 0

    # Here I am looping over all possible combinations of values of the production factors up to the actual factor value (given by user)
    # We know there are product(X_i + 1) possible combos, and so I have an index from 0 to that
    for i in range(np.prod([x+1 for x in vals])):
        im2_vals = vals.copy()
        im2_vals = [x+1 for x in im2_vals]
        im2_vals.pop()
        # From the index, I infer the particular combo of values we are at by using some int division
        # This is ugly but I couldnt easily find a better way to do this
        for j in range(num_factors):
            y = i // int(np.prod(im2_vals))
            im1_vals[num_factors - 1 - j] = y
            i -= y * np.prod(im2_vals)
            if len(im2_vals) != 0:
                im2_vals.pop()
        
        # Now we have calculated the combo of values we are at, and get the contribution to the shapley value
        # The formula for shapley values for production functions isnt obvious--calculated by hand
        func = [im1_vals[i]**exps[i] for i in range(num_factors)]
        del func[shap_factor]
        t = np.prod(func)
        t *= (im1_vals[shap_factor] + 1)**exps[shap_factor] - (im1_vals[shap_factor])**exps[shap_factor]
        t /= math.comb(n, np.sum(im1_vals))
        shap += t
    shaps.append(shap / n)
        


print("The Shapley values are %s" % shaps)
if sum(shaps) != 0:
    normed_shaps = [float(i)/sum(shaps) for i in shaps]
    print("The normalized Shapley values are %s" % normed_shaps)
    print(np.sum(normed_shaps))









# summing_arr = np.zeros(tuple([x+1 for x in vals]))

# print(summing_arr.shape)

# for i in np.nditer(summing_arr):
#     print(i.index)
    
