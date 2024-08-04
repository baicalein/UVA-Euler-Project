#!/usr/bin/env python
# coding: utf-8

# ## UVA orientation: problem1 from Project Euler
# ## Find the sum of all the multiples of 3 or 5 below 1000

# In[7]:


def problem_1():
    sum_multiples = 0
    for i in range(1000):
        if i % 3 == 0 or i % 5 == 0:
            sum_multiples += i
    return sum_multiples

print(problem_1())


# # UVA orientation: problem2 from Project Euler

# ## Find the sum of the even-valued terms in the Fibonacci sequence whose values do not exceed four million

# In[8]:


def problem_2():
    sum_even_fibonacci = 0
    a, b = 1, 2
    while a <= 4000000:
        if a % 2 == 0:
            sum_even_fibonacci += a
        a, b = b, a + b
    return sum_even_fibonacci

print(problem_2())


# ## UVA orientation: problem3 from Project Euler
# ## Find the largest prime factor of the number 

# ## 600851475143

# In[9]:


def problem_3():
    num = 600851475143
    i = 2
    while i * i <= num:
        if num % i == 0:
            num //= i
        else:
            i += 1
    return num

print(problem_3())


# ## UVA orientation: use a random number generator to make histograms of popular probability distributions. 
# ## Use the numpy and matplotlib packages
# ## Binomial

# In[38]:


import numpy as np
import matplotlib.pyplot as plt

# Set parameters for the binomial distribution
n = 1000  # Number of trials
p = 0.5   # Probability of success

# Generate binomial distributed data
binomial_data = np.random.binomial(n, p, size=10000)

# Plot histogram
plt.hist(binomial_data, bins=50, density=True, alpha=0.5, color='b', edgecolor='black')

# Add labels and title
plt.xlabel('Number of Successes')
plt.ylabel('Probability Density')
plt.title('Histogram of Binomial Distribution:n=1,000,p=0.5,size=10,000')

plt.grid()
plt.show()


# ## Poisson

# In[39]:


import numpy as np
import matplotlib.pyplot as plt

# Set parameter for the Poisson distribution
lambda_test = 5  # Lambda parameter (mean number of events)

# Generate Poisson distributed data
poisson_data = np.random.poisson(lambda_test, size=10000)

# Plot histogram
plt.hist(poisson_data, bins=30, density=True, alpha=1, color='r', edgecolor='gold')

# Add labels and title
plt.xlabel('Number of Events')
plt.ylabel('Probability Density')
plt.title('Histogram of Poisson Distribution:lambda=5')

# Show plot
plt.grid()
plt.show()


# ## Normal

# In[49]:


import numpy as np
import matplotlib.pyplot as plt

# Set parameters for the Normal distribution
mu = 0     # Mean of the distribution
sigma = 2  # Standard deviation of the distribution

# Generate Normal distributed data
normal_data = np.random.normal(mu, sigma, size=10000)

# Plot histogram
plt.hist(normal_data, bins=50, density=True, alpha=1, color='g', edgecolor='red')

# Add labels and title
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.title('Histogram of Normal Distribution:mean=0,standard deviation=2')

# Show plot
plt.grid()
plt.show()


# ## Uniform

# In[52]:


import numpy as np
import matplotlib.pyplot as plt

# Set parameters for the Uniform distribution
low = 0    # Lower bound of the distribution
high = 20  # Upper bound of the distribution

# Generate Uniform distributed data
uniform_data = np.random.uniform(low, high, size=10000)

# Plot histogram
plt.hist(uniform_data, bins=50, density=True, alpha=0.2, color='b', edgecolor='black')

# Add labels and title
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.title('Histogram of Uniform Distribution:low=0,high=20')

# Show plot
plt.grid()
plt.show()


# ## Chi-Squared
# 

# In[62]:


import numpy as np
import matplotlib.pyplot as plt

# Set parameter (degrees of freedom) 
df = 4  # Degrees of freedom

# Generate Chi-squared distributed data
chi_squared_data = np.random.chisquare(df, size=10000)

# Plot histogram
plt.hist(chi_squared_data, bins=50, density=True, alpha=0.5, color='y', edgecolor='black')

# Add labels and title
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.title('Histogram of Chi-squared Distribution:degree of feedom=3')

# Show plot
plt.grid()
plt.show()


# ## Visually Demonstrate (use histograms) to show that the Binomial and Normal distributions converge in the large N limit. Store the resulting histograms in your github repo. Make a mini-presentation using a markdown file in your github repo explaining the proof.

# In[65]:


import numpy as np
import matplotlib.pyplot as plt

# Parameters
N = 10000  # Number of trials
p = 0.5   # Probability of success

# Generate Binomial distributed data
binomial_data = np.random.binomial(N, p, size=10000)

# Generate Normal distributed data
mu = N * p  # Mean of Normal distribution
sigma = np.sqrt(N * p * (1 - p))  # Standard deviation of Normal distribution
normal_data = np.random.normal(mu, sigma, size=10000)

# Plot histograms
plt.figure(figsize=(14, 7))

# Binomial distribution histogram
plt.subplot(1, 2, 1)
plt.hist(binomial_data, bins=30, density=True, alpha=0.5, color='g', edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.title('Histogram of Binomial Distribution n=10000,p=0.5)')
plt.grid()

# Normal distribution histogram
plt.subplot(1, 2, 2)
plt.hist(normal_data, bins=30, density=True, alpha=0.5, color='r', edgecolor='black')
plt.xlabel('Value')
plt.ylabel('Probability Density')
plt.title('Histogram of Normal Distribution:mean=np,sigma=sqrt(np(1-p))')
plt.grid()

# Show plots
plt.tight_layout()
plt.show()


# 1. Number of trials for the Binomial distribution: N=10000
# 2. Probability of success for each trial: p=0.5
# 3. Generates 10,000 samples from a Binomial distribution with parameters 𝑁 and p
# 4. In Binomial Ddistribution: mean 𝜇 = 𝑁𝑝 and variance 𝜎2=𝑁𝑝(1−𝑝)
# 5. Generates 10,000 samples from a Normal distribution with mean 𝜇 and standard deviation 𝜎
# 6. Create histogram for each distribution to compare
# 7. Observe the Binomial distribution resembles the Normal distribution as N becomes large by comparing two histogram.
# 

# ## Load the data from the class hardware survey into memory using pandas, manipulate that data into a binnable form, and make exploratory histographs of the features of the dataset. For the features you couldn't address with a histogram provide a qualitative description.

# ### Prepare for presentation your findings from the class hardware data using a markdown file in your repo. Share your mini presentation with another member of your cohort.

# In[ ]:




