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