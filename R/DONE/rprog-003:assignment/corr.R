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