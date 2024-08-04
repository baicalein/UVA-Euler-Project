library(ggplot2)
# Normal Distribution historam
#set seed
set.seed(123)
# parameters
mean <- 0
sd <- 2
size <- 10000
# generate random normal data in data.frame form
data <- data.frame(value = rnorm(size, mean, sd))
#create histogram
ggplot(data, aes(x = value)) +
  geom_histogram(binwidth = 0.5, fill = "green", color = "black", alpha = 0.5) +
  labs(title = "Histogram of Normal Distribution:mean=0,standard deviation=2",
       x = 'value',
       y = "Probability Density")
