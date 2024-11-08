#!/bin/bash

# Edit: sudo nano my_network_tool.sh
# chmod +x my_network_tool.sh
# Run: ./my_network_tool.sh
#
# https://patorjk.com/software/taag/#p=display&f=Digital&t=MENU

#
# The Variable - option-  is to store the decision coming from the user  (1-6)
# The ariable - host - is to store the host  
#
option=""
host=""

#
# 1. This function shows all network interfaces
#
info_network_inferface() {
    echo "Network Interface Information"
    ip addr show
}

#
#  2. This function is to print the TTL (time to live) of the host
#
ping_test() {
    read -p "Enter an IPv4 address: " host
    ping -c 10 "$host"
}

#
# 3. This function makes a scan using nmap
#
nmap_scan() {
    read -p "Enter an IPv4 address: " host
    nmap "$host"
}

#
# 4. This function to display the routing table
#
routing_table() {
    echo "Routing Table:"
    ip route
}

#
# 5. This function to perform a traceroute to a host
#
traceroute_test() {
    read -p "Enter an IPv4 address: " host
    traceroute "$host"
}




#
# 6. Main loop
#
while true; do

    echo " +-+-+-+-+ "
    echo " |M|E|N|U| "
    echo " --------- "
    echo ""
    echo "1) Check Network Interface Information"
    echo "2) Ping a Host"
    echo "3) Port Scan with Nmap"
    echo "4) Display Routing Table"
    echo "5) Traceroute to Host"
    echo "6) Exit"
    echo ""
    echo ""
    read -p "Enter your option: " option
    # Using if statements to handle menu options
    if [ "$option" -eq 1 ]; then
       info_network_inferface
    elif [ "$option" -eq 2 ]; then
       ping_test
    elif [ "$option" -eq 3 ]; then
       nmap_scan
    elif [ "$option" -eq 4 ]; then
       routing_table
    elif [ "$option" -eq 5 ]; then
       traceroute_test
    elif [ "$option" -eq 6 ]; then
       echo "Exit."
       exit 0
    else
        echo "Please repeat again. See you!"
    fi
done

