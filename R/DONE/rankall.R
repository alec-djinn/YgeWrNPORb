rankall <- function(outcome, num = "best") {
        ## Read outcome data
        dataset <- read.csv("outcome-of-care-measures.csv", colClasses = "character")
        
        ## Check if outcome is valid
        Outcome.List <- list("heart attack", "heart failure", "pneumonia")
        if(! is.element(outcome, Outcome.List)) stop("invalid outcome")
        
        ## convert outcome to column index
        if (outcome == "heart attack") {
                col <- 11
        } else if (outcome == "heart failure") {
                col <- 17
        } else if (outcome == "pneumonia") {
                col <- 23
        }
        
        States <- dataset$State
        Hospitals <- dataset$Hospital.Name
        Outcome <- dataset[,col]
        new_data <- cbind(States, Hospitals, Outcome) # bind columns      
        new_dataset <- subset(new_data, new_data[,3] != "Not Available")        
        df <- new_dataset[order(new_dataset[,2]),] # order by name
        new_data <- df[order(as.numeric(df[,3])),] # order by mortality rate        
        States <- sort(unique(new_data[,1])) # sort
        hospitals <- vector()
        
        ## For each state, find the hospital of the given rank
        for (state in States) {
                df <- subset(new_data, new_data[,1] == state)
                
                if (num != "best" && num != "worst" && num > nrow(df)) {
                        Hospital.Name <- "<NA>"
                } else {
                        if (num == "best") {
                                Hospital.Name <- df[[1,2]]
                        } else if (num == "worst") {
                                Hospital.Name <- df[[nrow(df),2]]
                        } else {
                                Hospital.Name <- df[[num,2]]
                        }
                }
                hospitals <- append(hospitals, Hospital.Name)
        }
        
        ## Return a data frame with the hospital names and the
        ## (abbreviated) state name
        return(data.frame(hospital=hospitals, state=States))        
}