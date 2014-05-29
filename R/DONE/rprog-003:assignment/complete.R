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