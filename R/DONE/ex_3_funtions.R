best <- function(state, outcome) {
        ## Read outcome data
        dataset <-read.csv("outcome-of-care-measures.csv", colClasses = "character")
        
        ## Check that state and outcome are valid
        State.List <- dataset[, "State"]
        Outcome.List <- list("heart attack", "heart failure", "pneumonia")
        if(!is.element(state, State.List)) stop("invalid state")
        if(! is.element(outcome, Outcome.List)) stop("invalid outcome")
        
        ## rate
        dataset <- subset(dataset, State == state) # all entries reguarding a State
        if(outcome == "heart attack") {
                data <- dataset[, "Hospital.30.Day.Death..Mortality..Rates.from.Heart.Attack"]        
        }
        if(outcome == "heart failure") {
                data <- dataset[state, "Hospital.30.Day.Death..Mortality..Rates.from.Heart.Failure"]
        }
        if(outcome == "pneumonia") {
                data <- dataset[state, "Hospital.30.Day.Death..Mortality..Rates.from.Pneumonia"]
        }
        
        ## Return hospital name in that state with lowest 30-day death
        Hospital.List <- list()
        for(i in 1:nrow(dataset)) {
                row <- data[i]
                if(row == min(data)) {
                        Hospital.Name <- dataset[i, "Hospital.Name"]
                        Hospital.List <- append(Hospital.List, Hospital.Name)
                }
        }        
        #print(min(data))
        #print(Hospital.Name)
        output <- sort(unlist(Hospital.List))
        return(output)
}

## TEST best()
# best("AL", "heart attack")
# best("TX", "heart attack")
# best("BB", "heart attack")
# best("NY", "hert attack")


rankhospital <- function(state, outcome, num = "best") {
        ## Read outcome data
        dataset <-read.csv("outcome-of-care-measures.csv", colClasses = "character")
        
        ## Check that state and outcome are valid
        State.List <- dataset[, "State"]
        Outcome.List <- list("heart attack", "heart failure", "pneumonia")
        if(!is.element(state, State.List)) stop("invalid state")
        if(! is.element(outcome, Outcome.List)) stop("invalid outcome")
        
        ## Return hospital name in that state with the given rank
        ## 30-day death rate
        if(outcome == "heart attack") {
                col <- "Hospital.30.Day.Death..Mortality..Rates.from.Heart.Attack"        
        }
        if(outcome == "heart failure") {
                col <- "Hospital.30.Day.Death..Mortality..Rates.from.Heart.Failure"
        }
        if(outcome == "pneumonia") {
                col <- "Hospital.30.Day.Death..Mortality..Rates.from.Pneumonia"
        }
        
        dataset <- dataset[dataset$State == state, c("Hospital.Name", col)] # by State
        dataset[,2] <- suppressWarnings(as.numeric(dataset[,2])) # using suppressWarnings() to suppress "NAs introduced by coercion"
        ordered_dataset <- order(dataset[col], dataset$Hospital.Name, na.last=NA)
        
        if (num == "best") {
                as.character(dataset$Hospital.Name[ordered_dataset[1]])
        } else if (num == "worst") {
                as.character(dataset$Hospital.Name[ordered_dataset[length(ordered_dataset)]])
        } else if (is.numeric(num)) {
                as.character(dataset$Hospital.Name[ordered_dataset[num]])
        } else {
                stop("invalid num")
        }
}

## TEST rankhospital()
# rankhospital("TX", "heart failure", 4)
# rankhospital("MD", "heart attack", "worst")
# rankhospital("MN", "heart attack", 5000)


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

## TEST rankall()
head(rankall("heart attack", 20), 10)
tail(rankall("pneumonia", "worst"), 3)
