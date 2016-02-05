temp <- read.csv("3779_advocacy.csv")
matrix_3779 <- matrix(0,57,57)

for (i in 1:nrow(temp)) {
  matrix_3779[temp$rater_id[i],temp$rated_id[i]] <- 1
}


temp <- read.csv("3780_popularity.csv")
matrix_3780 <- matrix(0,57,57)

for (i in 1:nrow(temp)) {
  matrix_3780[temp$rater_id[i],temp$rated_id[i]] <- 1
}


temp <- read.csv("3781_implementation.csv")
matrix_3781 <- matrix(0,57,57)

for (i in 1:nrow(temp)) {
  matrix_3781[temp$rater_id[i],temp$rated_id[i]] <- 1
}


temp <- read.csv("3782_design.csv")
matrix_3782 <- matrix(0,57,57)

for (i in 1:nrow(temp)) {
  matrix_3782[temp$rater_id[i],temp$rated_id[i]] <- 1
}

library(lsa)

cosine_3779_3780 <- vector(length=57)
cosine_3779_3781 <- vector(length=57)
cosine_3779_3782 <- vector(length=57)
cosine_3780_3781 <- vector(length=57)
cosine_3780_3782 <- vector(length=57)
cosine_3781_3782 <- vector(length=57)

for (i in 1:57) {
  cosine_3779_3780[i] <- cosine(matrix_3779[i,],matrix_3780[i,])
  cosine_3779_3781[i] <- cosine(matrix_3779[i,],matrix_3781[i,])
  cosine_3779_3782[i] <- cosine(matrix_3779[i,],matrix_3782[i,])
  cosine_3780_3781[i] <- cosine(matrix_3780[i,],matrix_3781[i,])
  cosine_3780_3782[i] <- cosine(matrix_3780[i,],matrix_3782[i,])
  cosine_3781_3782[i] <- cosine(matrix_3781[i,],matrix_3782[i,])
}

cosine_matrix <- data.frame(cosine_3779_3780, cosine_3779_3781, cosine_3779_3782, cosine_3780_3781, cosine_3780_3782,cosine_3781_3782)

flexibility_score <- rowSums(cosine_matrix)
flexibility_score <- cbind(1:57,flexibility_score)
colnames(flexibility_score) <- c("id","flexibility")
sorted_flexibility <- flexibility_score[order(flexibility_score[,2],decreasing=F,na.last=T),]
#head(sorted_flexibility,10)

#cleaned_flexibility_score <- flexibility_score[!is.na(flexibility_score)]
#z_score_flexibility <- (flexibility_score - mean(cleaned_flexibility_score))/sd(cleaned_flexibility_score)
library(R.basic)
z_score_flexibility <- zscore(flexibility_score[,2],na.rm=T)
z_score_flexibility <- cbind(1:57,z_score_flexibility)
colnames(z_score_flexibility) <- c("id","z-score")
sorted_flex_z <- z_score_flexibility[order(z_score_flexibility[,"z-score"],decreasing=F),]
sorted_flex_z

combined <- merge(sorted_flexibility,sorted_flex_z)
sorted_combined <- combined[order(combined[,"flexibility"],decreasing=F),]

########For in-degree centrality:
indegree <- read.csv(file ="regression_summary_s.csv",header = T)

##For implementation group leader:
implementation_indegree <- indegree[,c("id","implementation")]
sorted_implem_in <- implementation_indegree[order(implementation_indegree$implementation,decreasing=T),]

#find the candidates that are both flexible and have a high in-degree in implementation network:
candidates_implem <- merge(sorted_flex_z[1:30,],sorted_implem_in[1:20,])
#candidates_implem_both <- candidates_implem_all[sorted_implem_in[1:15,"id"] %in% sorted_flex_z[1:20,"id"],]
candidates_implem_top <- candidates_implem[order(candidates_implem[,"implementation"],
                                                      -candidates_implem[,"z-score"],decreasing=T),]
candidates_implem_top
##Promising candidate for implementation group leader: 40,44,55,52,49,36,6


##For design group leader:
design_indegree <- indegree[,c("id","design")]
sorted_design_in <- design_indegree[order(design_indegree$design,decreasing=T),]

#find the candidates that are both flexible and have a high in-degree in design network:
candidates_design <- merge(sorted_flex_z[1:30,],sorted_design_in[1:20,])
#candidates_design_both <- candidates_design_all[sorted_design_in[1:15,"id"] %in% sorted_flex_z[1:20,"id"],]
candidates_design_top <- candidates_design[order(candidates_design[,"design"],
                                                 -candidates_design[,"z-score"],decreasing=T),]
candidates_design_top
##Promising candidate for design group leader: 44,55,40,52,6,11


##For advocacy group leader:
advocacy_indegree <- indegree[,c("id","advocacy")]
sorted_advocacy_in <- advocacy_indegree[order(advocacy_indegree$advocacy,decreasing=T),]

#find the candidates that are both flexible and have a high in-degree in advocacy network:
candidates_advocacy <- merge(sorted_flex_z[1:30,],sorted_advocacy_in[1:20,])
#candidates_advocacy_both <- candidates_advocacy_all[sorted_advocacy_in[1:15,"id"] %in% sorted_flex_z[1:20,"id"],]
candidates_advocacy_top <- candidates_advocacy[order(candidates_advocacy[,"advocacy"],
                                                 -candidates_advocacy[,"z-score"],decreasing=T),]
candidates_advocacy_top
##Promising candidate for advocacy group leader: 40,52,6,55,29,8,11
