resx<-c(50,55,55,55,60,60,60,60,60,60,60,65,65,65,65,65,65,70,70,75)
resy<-c(80,85,85,85,90,90,90,90,90,90,90,90,90,95,95,95,95,100,100,110)
resa<-(-3.175/100*pnorm(7.575-0.122*res)+0.03075)*33.3

res<-resx
plot.ecdf(res, main = "ECDF of x", xlab = "x", ylab = "F'(x)")

smooth_ecd = function(adj = 1) {
  dens = density(dat$x, adjust = adj)
  dens = data.frame(x = dens$x, y = dens$y)
  ggplot(dat, aes(x)) + 
    geom_density(adjust = adj, colour = "blue", alpha = 0.7) +
    geom_line(data = dens, aes(x = x, y = cumsum(y)/sum(y)), size = 1,
              colour = 'red') +
    stat_ecdf(colour = "black", size = 0.6, alpha = 0.6) +
    theme_classic() + labs(title=paste0("adj=",adj))
}
library(ggplot2)
dat <- data.frame(x = res)
smooth_ecd(adj = 1.5)

library("actuar")
fendo.ln <- fitdist(res, "lnorm")
fendo.P <- fitdist(res, "pareto", start = list(shape = 1, scale = 500))
fendo.B <- fitdist(res, "burr", start = list(shape1 = 0.3, shape2 = 1, rate = 1))
cdfcomp(list(fendo.B, fendo.ln, fendo.P), lwd=2,
        datacol = "gray65",
        main = "Эмпирическая и теоретические CDF",
        xlab = "Частоты величины x",
        legendtext = c("Burr","Empir","lognormal"), panel.first=grid())

library("actuar")
fendo.B <- fitdist(res, "burr", start = list(shape1 = 0.3, shape2 = 1, rate = 1))
cdfcomp(fendo.B, lwd=2,
        datacol = "gray65",
        main = "Эмпирическая и теоретические CDF",
        xlab = "Частоты величины x",
        legendtext = "Burr", panel.first=grid())

approx.ksD <- function(n) {
  ## оценка критического значения статистики Колмогорова-
  ## Смирнова D для доверительного уровня 0.95.
  ## реализована по Bickel & Doksum, table IX,  p.483
  ## и Lienert G.A.(1975) 
  ifelse(n > 10, 1.358 /( sqrt(n) + .12 + .11/sqrt(n)),   ##B&D
         splinefun(c(1:9, 10, 15, 10 * 2:8),# from Lienert
                   c(.975,   .84189, .70760, .62394, .56328,  # 1:5
                     .51926, .48342, .45427, .43001, .40925,  # 6:10
                     .33760, .29408, .24170, .21012,     # 15,20,30,40
                     .18841, .17231, .15975, .14960)) (n))
}
approx.ksD(length(res)) 


