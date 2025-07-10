def analyze_log(file_name): #defining a function
    log_levels = {"INFO": 0, "WARNING": 0, "ERROR": 0, "DEBUG": 0} #creating a dictionary to keep track of log levels

    try:
        with open(file_name, "r") as f: #open log file as read-only (f)
            for line in f:
                for level in log_levels: #check each log level
                    if f"[{level}]" in line: #check if the log level is in the line
                        log_levels[level] += 1 #increment the count

        with open("report.txt", "w") as report: #open report file as write-only
            for level, count in log_levels.items(): #write each log level and its count
                report.write(f"{level}: {count}\n") #write each log level and its count

        print("Log analysis complete. See report.txt") 

    except FileNotFoundError: #catch file not found error
        print("Log file not found.")
    except IOError as e: #catch I/O error
        print("An I/O error occurred:", e)

analyze_log("server.log")