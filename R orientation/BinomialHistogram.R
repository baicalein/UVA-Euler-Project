library(ggplot2)
library(dplyr)
# set seed
set.seed(123)
# set parameter for binomal distribution, 1000 trials and 
# 10000 times of experiments
n <- 1000
size <- 10000
# generate random binomial data with probability 0.5 in data.frame form
data <- data.frame(value = rbinom(n, size, 0.5))
# make histogram in ggplot2
ggplot(data, aes(x = value)) + 
  geom_histogram(binwidth = 1, fill = "blue", color = "black", alpha = 0.5) +
  labs(title = "Histogram of Binomial Distribution:n=1,000,p=0.5,size=10,000", 
       x = "Number of Successes",
       y = "Probability Density")
