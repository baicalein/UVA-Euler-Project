library(ggplot2)
# set seed
set.speed(123)
# parameters
df <- 5
size <- 10000
# generate random chi-squared random data in data.frame form
data <- data.frame(value = rchisq(size, df))
# create histogram
ggplot(data, aes(x = value)) +
  geom_histogram(binwidth = 0.7, fill = "yellow", color = "black", alpha = 0.5) +
  labs(title = "Histogram of Chi-squared Distribution:degree of feedom=3",
       x = "value",
       y = "Probability Density")
