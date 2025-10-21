#Conditionals
# The value of 10*4 (40) is greater than 14+23 (37), therefore this 
# comparison expression will return the Boolean value of True.
print(10*4 > 14+23) # Should print True
print("tall" < "short")  # Should print False



# This function accepts one variable as a parameter
def translate_error_code(error_code):
    if error_code == "401 Unauthorized":  
        translation = "Server received an unauthenticated request"
    elif error_code == "404 Not Found":
        translation = "Requested web page not found on server"
    elif error_code == "408 Request Timeout":
        translation = "Server request to close unused connection"
    else:
        translation = "Unknown error code"
    return translation
print(translate_error_code("404 Not Found"))
print(translate_error_code("500 Internal Server Error"))


#Use if-elif statements with comparisonan operators
# Sets value of the "number" variable
number = 50 
if number <= 5: 
   print("The number is 5 or smaller.")
elif number == 33:
   print("The number is 33.")
elif number < 32 and number >= 6:
   print("The number is less than 32 and greater than 6.")
 
else:
   print("The number is " + str(number))



# Identify IP addresses
def identify_IP(IP_address):
    if IP_address == "192.168.1.1":
        IP_description = "Network router"
    elif IP_address == "8.8.8.8" or IP_address == "8.8.4.4":
        IP_description = "Google DNS server"
    elif IP_address == "142.250.191.46":
        IP_description = "Google.com"
    else:
        IP_description = "unknown"
    return IP_description


print(identify_IP("8.8.4.4")) # Should print 'Google DNS server'
print(identify_IP("142.250.191.46")) # Should print 'Google.com'
print(identify_IP("192.168.1.1")) # Should print 'Network router'
print(identify_IP("8.8.8.8")) # Should print 'Google DNS server'
print(identify_IP("10.10.10.10")) # Should print 'unknown'
print(identify_IP("")) # Should Should print 'unknown'

