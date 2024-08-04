# Visually Demonstrate (use histograms) to show that the Binomial and 
# Normal distributions converge in the large N limit.
library(ggplot2)
# set seed
set.seed(123)
# parameters
size <- 10000 # sample size
n <- 100 # number of trials
prob <- 0.5 # probability of success for binomial distribution
# generate binomila data in data.frame form
binomial_data <- data.frame(value = rbinom(n, size, prob)
# binomial histogram
ggplot(binomial_data, aes(x = value)) +
  geom_histogram(binwidth = 1, fill = "blue", color = "black", alpha = 0.5) +
  labs(title = "Histogram of binomial distribution to compare",
       x = "value",
       y = "frequency")
  ggsave("binomial_histogram_compare.png")

#generate normal data
mean <- size * prob
sd <- sqrt(n * prob * (1-prob))
# generate normal date in data.frame form
normal_data <- data.frame(value = rnorm(size,mean, sd))
#normal histogram
ggplot(normal_data, aes(x = value)) +
  geom_histogram(binwidth = 1, fill = "green", color = "black", alpha = 0.5) +
  labs(title = "Histogram of normal distribution to compare",
       x = "value", 
       y = "frequency")
 ggsave("normal_histogram_compare.png")
 