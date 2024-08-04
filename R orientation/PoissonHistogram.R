library(ggplot2)
# Poisson Distribution Histogram
# set seed
set.seed(123)
# parameter
lambda <- 5
size <- 10000
# generate random poissonn data in data.frame form
data <- data.frame(value = rpois(size, lambda))
# create historam
ggplot(data, aes(x = value)) +
  geom_histogram(binwidth = 0.5, fill = "red", color = "black", alpha = 0.8) +
  labs(title = "Histogram of Poisson Distribution:lambda=5",
       x = "Number of Events",
       y = "Probability Density")
