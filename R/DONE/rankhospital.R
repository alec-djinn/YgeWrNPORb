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