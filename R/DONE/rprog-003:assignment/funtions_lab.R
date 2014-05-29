pollutantmean <- function(directory, pollutant, id = 1:332) {
        # get the list of the files in directory
        wd <- getwd()
        wd <- paste(wd,'/',directory, sep = '')
        files <- list.files(directory)
        files <- files[id]
        result <- c() # initialize result
        # iterate over each file and get the data from pollutant column
        for(file in files) {
                filename <- paste(wd, '/', file, sep = '')
                data <- read.csv(filename, header = TRUE)
                temp <- data[pollutant]
                temp <- temp[!is.na(temp)] # clean the data from NA values
                result <- append(result, temp) # accumulate the data into results 
        }  
        result <- mean(result) # calculate the mean value
        return(result)
}

# test cases
setwd('/Users/alec_djinn/Desktop/YgeWrNPORb/R/rprog-003:assignment') # set the working directory
pollutantmean("specdata", "sulfate", 1:10)
pollutantmean("specdata", "nitrate", 70:72)
pollutantmean("specdata", "nitrate", 23)




complete <- function(directory, id = 1:332) {
        # get the list of the files in directory
        wd <- getwd()
        wd <- paste(wd,'/',directory, sep = '')
        files <- list.files(wd)
        files <- files[id]
        col_id <- c()
        col_nobs <- c()
        # iterate over each file and get the data from column "sulfate", "nitrate" and "ID"
        for(file in files) {
                filename <- paste(wd, '/', file, sep = '')
                data <- read.csv(filename, header = TRUE)
                id <- data[1,4]
                nobs <- 0
                for(x in 1:nrow(data)) {
                        if(!is.na(data[x, 2]) && !is.na(data[x, 3])) {
                                nobs <- nobs + 1    
                        }
                        
                }
                # append the data    
                col_id <- append(col_id, id)
                col_nobs <- append(col_nobs, nobs)
        } 
        # make a dataframe
        result <- cbind(col_id, col_nobs)
        result <- data.frame(result)
        colnames(result) <- c("id", "nobs")
        return(result)
}

# test cases
setwd('/Users/alec_djinn/Desktop/YgeWrNPORb/R/rprog-003:assignment') # set the working directory
complete("specdata", 1)
complete("specdata", c(2, 4, 8, 10, 12))
complete("specdata", 30:25)
complete("specdata", 3)



corr <- function(directory, threshold = 0) {
        #files <- list.files(directory)        
        cr <- c() 
        wd <- getwd()
        wd <- paste(wd,'/',directory, sep = '')
        files <- list.files(wd)
        # iterate over each file
        for(file in files) {
                filename <- paste(wd, '/', file, sep = '')
                data <- read.csv(filename, header = TRUE)
                data <- data[complete.cases(data),]
                if ( nrow(data) > threshold ) {
                        cr <- c(cr, cor(data$sulfate, data$nitrate) ) # append corralations
                }
        }
        
        return(cr)
}

# test cases
setwd('/Users/alec_djinn/Desktop/YgeWrNPORb/R/rprog-003:assignment')
cr <- corr("specdata")
summary(cr)
