best <- function(state, outcome) {
        ## Read outcome data
        dataset <-read.csv("outcome-of-care-measures.csv", colClasses = "character")
       
        ## Check that state and outcome are valid
        State.List <- dataset[, "State"]
        Outcome.List <- list("heart attack", "heart failure", "pneumonia")
        if(!is.element(state, State.List)) {
                return("Error: invalid state")
        }
        
        if(! is.element(outcome, Outcome.List)) {
                return(Error: invalid outcome)
        }
        
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
                row <- data[i] # MAKE A LIST instead a normal variable
                if(row == min(data)) {
                        Hospital.Name <- dataset[i, "Hospital.Name"]
                        Hospital.List <- append(Hospital.List, Hospital.Name)
                }
        }
        
        print(min(data))
        print(Hospital.Name)
        output <- sort(unlist(Hospital.List))
        print(output)
        
        ## rate
}

best("AL", "heart attack")
best("TX", "heart attack")
best("BB", "heart attack")
best("NY", "hert attack")