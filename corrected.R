# corrected
# by Batagelj, V.; 11. December 2015
# Corrected network elements importance measures
# Comparison diagrams in R
# setwd("C:/Users/batagelj/Documents/papers/2015/CRoNoS/london/nets")
setwd("C:/Users/batagelj/Documents/manuscripts/corrected/corr")
f <- list("integer","numeric","numeric","integer","integer")
t <- read.table("overlapMax.csv",header=TRUE,dec=".",sep=";",colClasses=f)
head(t)
plot(t$over,t$cOver,pch=16,cex=0.7,main="Overlap weights",xlab="overlap",ylab="corrOverlap")
plot(t$Te,t$over,pch=16,cex=0.7,main="Overlap weights",xlab="#triangles",ylab="overlap")
plot(t$Te,t$cOver,pch=16,cex=0.7,main="Overlap weights",xlab="#triangles",ylab="corrOverlap")
plot(t$m/t$M,t$over,pch=16,cex=0.7,main="Overlap weights",xlab="minDeg/maxDeg",ylab="overlap")
plot(t$m/t$M,t$cOver,pch=16,cex=0.7,main="Overlap weights",xlab="minDeg/maxDeg",ylab="corrOverlap")
plot(t$M,t$over,pch=16,cex=0.7,main="Overlap weights",xlab="maxDeg",ylab="overlap")
plot(t$M,t$cOver,pch=16,cex=0.7,main="Overlap weights",xlab="maxDeg",ylab="corrOverlap")
plot(t$m,t$over,pch=16,cex=0.7,main="Overlap weights",xlab="minDeg",ylab="overlap")
plot(t$m,t$cOver,pch=16,cex=0.7,main="Overlap weights",xlab="minDeg",ylab="corrOverlap")
 
f <- list("integer","numeric","numeric","numeric")
t <- read.table("ccMax.csv",header=TRUE,dec=".",sep=";",colClasses=f)
head(t)
plot(t$Cc,t$cCc,pch=16,cex=0.7,main="Clustering coefficients",xlab="clusCoef",ylab="corrClusCoef")
plot(t$deg,t$Cc,pch=16,cex=0.7,main="Clustering coefficients",xlab="deg",ylab="clusCoef")
plot(t$deg,t$cCc,pch=16,cex=0.7,main="Clustering coefficients",xlab="deg",ylab="corrClusCoef")
plot(t$deg,t$E,pch=16,cex=0.7,main="Clustering coefficients",xlab="deg",ylab="#edges")

