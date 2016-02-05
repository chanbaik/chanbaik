rm(list=ls())
setwd("C:/Users/Dino-PC/Desktop/Introduction to Data (Business) Analytics/Group Project")


## load data
data = read.csv(file ="regression_summary.csv",header = T)


pop_model1=lm(troubleshoot~Popularity.royal.albert.hall.  ,data)
pop_model2=lm(implementation~Popularity.royal.albert.hall.,data)
pop_model3=lm(design~Popularity.royal.albert.hall.,data)
              
summary(pop_model1) # trouble
summary(pop_model2) # implement
summary(pop_model3) # design


#################################################################
#########---------------OLS MODEL RESULTS---------------#########
#################################################################

        #Troubleshooting as a function of popularity
# Popularity explains 18.7% of the variance
# Coefficient  = 0.4

#---------

        #Implementation as a function of popularity
# Popularity explains 33.8% of the variance
# Coefficient  = 0.7
# This is the team that is going to meet regularly. Perhaps not surprising that popularity is an important
# factor in picking implementation team members?

#---------

        #Design as a function of popularity
# Popularity explains 21.5% of the variance
# Coefficient  = 0.38
# Similar in outcome to the troubleshooting team

#################################################################


## poisson regression models
## recall that interpretation of the coefficients is similar to a log OLS model.
      ## % change in y = 100*[exp(Bixi)-1]
pois_model1 = glm(troubleshoot ~ Popularity.royal.albert.hall.,data = data, family = "poisson")
pois_model2 = glm(implementation ~ Popularity.royal.albert.hall.,data = data, family = "poisson")
pois_model3 = glm(design ~ Popularity.royal.albert.hall.,data = data, family = "poisson")

summary(pois_model1) # trouble
summary(pois_model2) # implement
summary(pois_model3) # design

#################################################################
#########-------------POISSON MODEL RESULTS-------------#########
#################################################################

          #Troubleshooting as a function of popularity
# Popularity explains ??? of the variance
# Coefficient  = 0.08 == 0.8% increase in troubleshooting in-degrees centrality

#---------

          #Implementation as a function of popularity
# Popularity explains ??? of the variance
# Coefficient  = 0.12 == 12% increase
# This is the team that is going to meet regularly. Perhaps not surprising that popularity is an important
# factor in picking implementation team members?

#---------

          #Design as a function of popularity
# Popularity explains ??? of the variance
# Coefficient  = 0.07 == 7% of the variance
# Similar in outcome to the troubleshooting team


## The Poisson models tell the same story as the OLS really - popularity is important for
## the implementation team, where people will be spending a lot of time together, 
## but less so for the design and troubleshooting teams who meet less regularly.
#################################################################

#################################################################
##--------------NEGATIVE BINOMIAL REGRESSION-------------------##
#################################################################
# The negative binomial distribution is for modelling count variables which are said to be
# over dispersed. This means that the conditional variance exceeds the conditional mean.

# So, let's test to see what the mean and variance are of our data:
m = vector()
v = vector()

for (i in 2:5)
        {
          m[i-1] = mean(data[,i],na.rm = T)
          v[i-1] = var(data[,i],na.rm = T)
        }
data.frame(mean = m, variance = v, row.names = names(data[,2:5]))

## so our data are over dispersed, making this a candidate for a negative binomial model.
## However, the small sample size is a problem, due to the Poisson and Negative binomial estimation method.
## P and NB models estimate using Maximum Likelihood, which due to the small sample behaviour of ML being unknown
## is risky to use with samples <100. Recommended size is >= 500.


library(MASS)

nb_model1 = glm.nb(troubleshoot ~ Popularity.royal.albert.hall.,data = data )
nb_model2 = glm.nb(implementation ~ Popularity.royal.albert.hall.,data)
nb_model3 = glm.nb(design ~ Popularity.royal.albert.hall.,data )

summary(nb_model1)
summary(nb_model2)
summary(nb_model3)


#################################################################



readNet <- function(file){
  require(xlsx)
  dt1 <- read.xlsx(file, 3, stringsAsFactors=FALSE)
  dt2 <- read.xlsx(file, 4, stringsAsFactors=FALSE)
  dt3 <- read.xlsx(file, 5, stringsAsFactors=FALSE)
  dt4 <- read.xlsx(file, 6, stringsAsFactors=FALSE)
  
  dt1 <- apply(dt1, 2, function(x){ as.integer(as.character(x))})
  dt2 <- apply(dt2, 2, function(x){ as.integer(as.character(x))})
  dt3 <- apply(dt3, 2, function(x){ as.integer(as.character(x))})
  dt4 <- apply(dt4, 2, function(x){ as.integer(as.character(x))})
  
  tmp <- list(dt1, dt2, dt3, dt4)
  names(tmp) <- c("twoDayWorkshop", "WeeklyMeeting", "Concert", "urgentMeet")
  # before uncommenting the line above, you should check that the networks appear in that order in the excel file
  return(tmp)
}

# Reads in from the excel file
net <- readNet("BA_Anonymised.xlsx")


library(igraph)
# # Turns your network in igraph networks. --- COULDNT GET TO WORK
# for (i in 1:length(net)){
#   net <- graph_from_edgelist(net[[i]][,1:2])
# }

## generate the networks individually. 
net1 <- graph_from_edgelist(net[[1]][,1:2])
net2 <- graph_from_edgelist(net[[2]][,1:2])
net3 <- graph_from_edgelist(net[[3]][,1:2])
net4 <- graph_from_edgelist(net[[4]][,1:2])

net1.df = data.frame(in_deg = degree(net1,mode="in"), close = closeness(net1,mode="in"), between = betweenness(net1),eig =eigen_centrality(net1) )
net2.df = data.frame(in_deg = degree(net2,mode="in"), close = closeness(net2,mode="in"), between = betweenness(net2),eig =eigen_centrality(net2))
net3.df = data.frame(in_deg = degree(net3,mode="in"), close = closeness(net3,mode="in"), between = betweenness(net3),eig =eigen_centrality(net3))
net4.df = data.frame(in_deg = degree(net4,mode="in"), close = closeness(net4,mode="in"), between = betweenness(net4),eig =eigen_centrality(net4))


# # In-degree centrality of the first of the 4 networks
# deg <- degree(net[[1]], mode="in")
# 
# # Closeness centrality of the first of the 4 networks
# clo <- closeness(net[[1]], mode="in")
# 
# # Betweenness centrality of the first of the 4 networks
# btw <- betweenness(net[[1]])
# 
# # Eigenvector centrality of the first of the 4 networks
# eig <- eigen_centrality(net[[1]])
 

### print the data to csv for Excel interpretation.

# write.csv(net1.df,file = "design analysis.csv")
# write.csv(net2.df,file = "implementation analysis.csv")
# write.csv(net3.df,file = "popularity analysis.csv")
# write.csv(net4.df,file = "troubleshoot analysis.csv")
#   
  