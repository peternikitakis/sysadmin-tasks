# sysadmin-tasks
A repo dedicated towards scripts for system administration

# rhel.ipscripty py:
In this script, I imported two modules: 1. ipaddress 2. subprocess. The ipaddress module is used to validate the user's input for IPv4 and IPv6. The subprocess module is used to interact with other external applications or programs and integrate within our script. I prompted the user for two inputs: 1. IP address 2. Network Interface ID. I stored both of these values as their respective variables. I defined two functions: 1. ip_address_validation 2. ip_change. ip_address_validation is called to pass through the user's input, pass it through the ip.address function, and store it as an object if valid. ip_change is called to pass through the validated ip address and run a series of Linux commands to pull up the network manager cli, identify the network interface ID, modify the ip address, and bring the network interface back up. 
