import ipaddress  # ipaddress module which is used to validate ipv4, ipv6 input
import subprocess # subprocess module is used to interact with other programs or applications through a python script.  

userIP = input("Enter in new IPv4 Address: ")

def ip_address_validation(ip):  # defining a function (ip_address_validation) and passing through an argument "ip". 
    try:                      
        ip_obj = ipaddress.ip_address(ip) 
        print(f"The IP address {ip_obj} is valid.")
        return ip_obj

    except ValueError: # handling any errors
        print("Please input a valid IP Address")  
        exit()

validatedIP = ip_address_validation(userIP) # calling ip validation function and passing through ipv4 

print(f"Validating IP Address: {validatedIP}")
interfaceID = input("Enter in interface ID: ")

def ip_change(newip):    # defining a function that will pass through a new ip address as the argument
    try: # attempting to test a block of code  
        subprocess.run('nmcli', shell=True )
        subprocess.run(f'sudo nmcli connection modify {interfaceID} ipv4.addresses {validatedIP}', shell=True) # adding ip address the user entered in
        subprocess.run(f'sudo nmcli connection up {interfaceID} ', shell=True) # bringing interface back up

    except ValueError: # handling any errors
        print("Please input a valid IP Address")

ip_change(validatedIP)