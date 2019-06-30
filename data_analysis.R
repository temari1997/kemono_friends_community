data <- read.csv("kemofure_data.csv", header = FALSE, row.names=1)

summary(data[,1])
summary(data[,2])
summary(data[,3])
cor(data[, c(1:3)])
plot(data[, c(1:3)])

km <- kmeans(data,4)
result <- km$cluster
result
library(cluster)
plot(pam(data[, 3], 4), ask=TRUE)

hc <- hclust(dist(data), "ward.D2")
plot(hc)
result <- cutree(hc, h=1300)
result["usXgamqvFdb0GSh"]
result["ookami0756"]

user_wo_dummy <- data.frame(result[result != 97])
write.table(rownames(user_wo_dummy), "kemofure_wo_ghost.csv", append = F, quote=F, col.names = F)