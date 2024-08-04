library(ggplot2)
# set seed
set.seed(123)
#parameters
low <- 0
high <- 20
size <- 10000
#generate random uniform data in date.frame form
data <- data.frame(value = runif(size, min = low, max = high))
#create histogram
ggplot(data, aes(x = value)) +
  geom_histogram(binwidth = 0.5, fill = "blue", color = "black", alpha = 0.5) +
  labs (title = "Histogram of Uniform Distribution:low=0,high=20",
        x = "Value", 
        y = "Probability Density")
