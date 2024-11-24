#!/bin/bash

# Turn it executable file: chmod +x Logger.sh

# References: 
#    https://stackoverflow.com/questions/1401482/yyyy-mm-dd-format-date-in-shell-script
#    https://www.cyberciti.biz/faq/unix-linux-getting-current-date-in-bash-ksh-shell-script/
#    https://serverfault.com/questions/196734/bash-difference-between-and-operator

#
# 1. Current date time
#
c_datetime=""

#
# 2. Get the user
#
user=$USER

#
# 3. Get the current time
#
c_datetime=$(date "+%Y-%m-%d %H:%M:%S")


#
# 4. Message
#
message="The software executed successfully!"


#
# 5.Append the log to the file Activity.log
#

echo "[$c_datetime] User: $user - $message" >> Activity.log
