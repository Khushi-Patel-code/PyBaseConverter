def validate_input (input_number , source_base , target_base):
    decimal_found = False
    negative_num = False
    if input_number.startswith('-'): #checks whether input starts with a negative sign
        negative_found = True
        input_number = input_number[1:] # removes the negative sign so we just deal with the actual number

    for c in input_number: #Iterate over each character in the input_number 
        if c=='.': # checks that the program has atmost one decimal point
            if decimal_found == True:
                print ("\nError! only one decimal point is allowed")
                return False
            else:
                decimal_found = True
                continue

        #validation for decimal_base (base 10)
        if (source_base == 10):
            if not ('0'<=c and c<='9'):
                print("\nError! Invalid characters(s) found in decimal base input")
                print("Allowed characters for decimal base input (0-9)")
                return False
        
        #validation for binary_base (base 2)
        elif source_base == 2:
            if c not in ['0', '1']:
                print("\nError! Invalid character(s) found in binary base input")
                print("Allowed characters for binary base input (0,1)")
                return False
        
        #validation for hexadecimal_base (base 16)
        elif source_base == 16:
            if not (('0' <= c <= '9') or ('A' <= c <= 'F') or ('a' <= c <= 'f')):
                print("\nError! Invalid character(s) found in hexadecimal base input")
                print("Allowed characters for hexadecimal base input (0-9 and A-F)")
                return False
        
        #validation for source_base (valid: 2 , 10 , 16)
        else:
            print("\nError! Invalid source base")
            print("Allowed source base inputs are : 2 (Binary) , 10 (Decimal) , 16 (Hexadecimal)")
            return False
        
    #validation for target_base (valid:
    if target_base not in [2,10,16]:
        print("\nError! Invalid target base")
        return False
    
    #if all validation pass
    return True


###=======================     Converting Functions     ==================###





###=======================     Decimal to Binary Function     ==================###

def decimal_to_binary(input_number): 
    negative_num = input_number.startswith('-')   #checks whether input starts with a negative sign
    if negative_num:
        input_number = input_number[1:]   # removes the negative sign so we just deal with the actual number

    if '.' in input_number:
        integer_part , fractional_part = input_number.split('.') #for fractional part
    else:
        integer_part , fractional_part = input_number, '0' #for no fractional part

    #converting the integer_part string into int

    integer_part=int(integer_part) 

    
    if integer_part == 0:
        return '0'
            
    #creating an empty string to store the converted binary integer part

    binary_integer= ""
    while integer_part > 0:
        rem = integer_part % 2 #getting remiander when divided by 2 (0 or 1)
        binary_integer = str(rem) + binary_integer #adding the string rem into the binary number string
        integer_part = integer_part //2  #floor dividing the number by 2



    # Converting the fractional part into float with preceding 0. as the integer
    fractional_part = float('0.' + fractional_part)  

    #creating an empty string to store the converted binary fractional part
    binary_fractional = "" 
    while fractional_part > 0 and len(binary_fractional) <20: #Giving a precision of 20 fractional binary digits
        fractional_part *= 2 #fracractional part = fractional part * 2 
        whole_number = int(fractional_part)  #Only gets us the whole number part i.e either 0 or 1
        binary_fractional += str(whole_number)
        fractional_part = fractional_part - whole_number #updtaing the fractional part for the while loop

    #combining the integer part and the fractional part

    if negative_num:
        sign= '-'
    else:
        sign = ''

    if binary_fractional :
        return f"{sign}{binary_integer}.{binary_fractional}"  # Returns the combined result
    else:
        return f"{sign}{binary_integer}" #Returns just the integer in case of no fractional part

###=======================     Decimal to Hexadecimal function     ==================###

def decimal_to_hex(input_number):
    negative_num = input_number.startswith('-')   #checks whether input starts with a negative sign
    if negative_num:
        input_number = input_number[1:]   # removes the negative sign so we just deal with the actual number

    if '.' in input_number:
        integer_part , fractional_part = input_number.split('.') #for fractional part
    else:
        integer_part , fractional_part = input_number, '0' #for no fractional part

    #converting the integer_part string into int
    integer_part=int(integer_part) 

   
    if integer_part == 0:
        return '0'
    else:
        hex_integer = "" #creating an empty string to store the converted hexadecimal integer part
        while integer_part > 0:
            rem=integer_part % 16   #getting remiander when divided by 16 (0 or 9)
            if rem < 10 :
                hex_digit= str(rem)   #it will convert the remianders 0-9 into strings
            elif rem==10:
                hex_digit = 'A'
            elif rem == 11:
                hex_digit = 'B'
            elif rem == 12:
                hex_digit = 'C'
            elif rem == 13:
                hex_digit = 'D'
            elif rem == 14:
                hex_digit = 'E'
            elif rem == 15:
                hex_digit = 'F'
            hex_integer = hex_digit + hex_integer  #adding the string hex_digit into the hex_integer string
            integer_part=integer_part//16 #floor dividing the number by 16

    #converting the fractional_part string into int 

    fractional_part = float('0.' + fractional_part) 

    #creating an empty string to store the converted hexadecimal fractional part
    hex_fractional = ""
    while fractional_part > 0 and len(hex_fractional) <20:
        fractional_part *= 16
        fractional_digit = int(fractional_part) #Only stores the whole number part
        if fractional_digit < 10:
            hex_fractional += str(fractional_digit) 
        elif fractional_digit == 10:
            hex_fractional += 'A'
        elif fractional_digit == 11:
            hex_fractional += 'B'
        elif fractional_digit == 12:
            hex_fractional += 'C'
        elif fractional_digit == 13:
            hex_fractional += 'D'
        elif fractional_digit == 14:
            hex_fractional += 'E'
        elif fractional_digit == 15:
            hex_fractional += 'F'

        fractional_part = fractional_part - fractional_digit #updtaing the fractional part for the while loop
    
    if negative_num:
        sign= '-'
    else:
        sign = ''

    if hex_fractional:
        return f"{sign}{hex_integer}.{hex_fractional}"
    else:
        return f"{sign}{hex_integer}"
    




###=======================     Binary to Decimal function     ==================###

def binary_to_decimal(input_number):

    negative_num = input_number.startswith('-')   #checks whether input starts with a negative sign
    if negative_num:
        input_number = input_number[1:]   # removes the negative sign so we just deal with the actual number

    if '.' in input_number:
        integer_part , fractional_part = input_number.split('.') # Split into integer and fractional parts
    else:
        integer_part , fractional_part = input_number, '0' #for no fractional part

    #Converting the integer part into Decimal

    decimal_integer = 0
    power = len(integer_part)-1  # As the power starts from 2 raised to power 0
    for i in integer_part:
        if i == '1':   #As anything multipled by zero is zero so makes no difference to the sum
            decimal_integer += 2**power   
        power -= 1 

    #Converting the fractional part into Decimal

    decimal_fractional = 0
    power = -1    #The first digit after the decimal is multiplied with 2 raised to -1
    for i in fractional_part:
        if i=='1': #As anything multipled by zero is zero so makes no difference to the sum
            decimal_fractional += 2**power
        power -=1

    #Combining the decimal_integer and the decimal_fractional as they are in numbers
    

    
    decimal_number = decimal_integer + decimal_fractional
    if negative_num:
        return -decimal_number
    else:
        return decimal_number 

###=======================     Binary to HexaDecimal function     ==================###     

def binary_to_hex(input_number):

    #First Converting the number from binary to decimal using the above mentioned functions
    decimal_number = binary_to_decimal(input_number)

    #second , Converting the number from decimal to hexadecimal using the above mentioned functions
    hex_number = decimal_to_hex (str(decimal_number)) #because binary_to_decimal function returns a number value 

    return  hex_number 
###=======================     Hexadecimal to Decimal function     ==================###
def hex_to_decimal(input_number):

    negative_num = input_number.startswith('-')   #checks whether input starts with a negative sign
    if negative_num:
        input_number = input_number[1:]   # removes the negative sign temporarily so we just deal with the actual number

    if '.' in input_number:
        integer_part, fractional_part = input_number.split('.')  # Split into integer and fractional parts
    else:
        integer_part, fractional_part = input_number, '0'  # For No fractional part
    
    # Converting the integer part into Decimal

    decimal_integer = 0 #initialize to 0 
    power = len (integer_part) -1  # As the power starts from 16 raised to power 0
    for i in integer_part:
        if '0' <= i <= '9':
            decimal_integer += int(i) * (16 ** power ) #converting string digits into integers

        #In case of upper_case decimal integer part
        elif 'A' <= i <= 'F':   #Changing the Alphabets into corresponing numbers
            if i == 'A':
                decimal_integer += 10 * (16 ** power)
            elif i == 'B':
                decimal_integer += 11 * (16 ** power)
            elif i == 'C':
                decimal_integer += 12 * (16 ** power)
            elif i == 'D':
                decimal_integer += 13 * (16 ** power)
            elif i == 'E':
                decimal_integer += 14 * (16 ** power)
            elif i == 'F':
                decimal_integer += 15 * (16 ** power)

        #In case of lower_case decimal integer part
        elif 'a' <= i <= 'f':
            if i == 'a':
                decimal_integer += 10 * (16 ** power)
            elif i == 'b':
                decimal_integer += 11 * (16 ** power)
            elif i == 'c':
                decimal_integer += 12 * (16 ** power)
            elif i == 'd':
                decimal_integer += 13 * (16 ** power)
            elif i == 'e':
                decimal_integer += 14 * (16 ** power)
            elif i == 'f':
                decimal_integer += 15 * (16 ** power)
        power -= 1

    #Converting the fractional part into Decimal

    decimal_fractional = 0
    power = -1  # The first digit after the decimal is multiplied with 16 raised to -1

    for i in fractional_part:
        if '0' <= i <= '9':
            decimal_fractional += int(i) * (16 ** power) #converting string digits into integers

        #In case of upper_case decimal integer part
        elif 'A' <= i <= 'F':  #Changing the Alphabets into corresponing numbers
            if i == 'A':
                decimal_fractional += 10 * (16 ** power)
            elif i == 'B':
                decimal_fractional += 11 * (16 ** power)
            elif i == 'C':
                decimal_fractional += 12 * (16 ** power)
            elif i == 'D':
                decimal_fractional += 13 * (16 ** power)
            elif i == 'E':
                decimal_fractional += 14 * (16 ** power)
            elif i == 'F':
                decimal_fractional += 15 * (16 ** power)

             #In case of lower_case decimal integer part
        elif 'a' <= i <= 'f':
            if i == 'a':
                decimal_fractional += 10 * (16 ** power)
            elif i == 'b':
                decimal_fractional += 11 * (16 ** power)
            elif i == 'c':
                decimal_fractional += 12 * (16 ** power)
            elif i == 'd':
                decimal_fractional += 13 * (16 ** power)
            elif i == 'e':
                decimal_fractional += 14 * (16 ** power)
            elif i == 'f':
                decimal_fractional += 15 * (16 ** power)
        power -= 1 #iterating through the string hex number by decreasing the power by 1 every time

    #Combining the decimal_integer and the decimal_fractional as they are in numbers

    decimal_number = decimal_integer + decimal_fractional

    if decimal_fractional == 0:
        if negative_num:
            return -decimal_integer
        else:
            decimal_integer
    else: 
        if negative_num:
            return -decimal_number
        else:
            return decimal_number


###=======================     Hexadecimal to Binary function     ==================###

def hex_to_binary(input_number):

    #First Converting the number from hexadecimal to decimal using the above mentioned functions
    decimal_number = hex_to_decimal(input_number)

    #second , Converting the number from decimal to binary using the above mentioned functions
    binary_number = decimal_to_binary(str(decimal_number)) #because hex_to_decimal function returns a number value 

    return binary_number

##=======================     converting the input_number from source_base to target_base    ==================###
def convert_number(input_number, source_base, target_base):

    #Converting from source base 10
    if source_base == 10:  
        if target_base == 2 :
            return decimal_to_binary(input_number)  # Returns the binary_number string from function decimal_to_binary
        elif target_base == 16 :
            return decimal_to_hex(input_number) # Returns the hexadecimal_number string from function decimal_to_hex
    
    
    #Converting from source base 2  
    if source_base == 2 :
        if target_base == 10 :
            return binary_to_decimal(input_number) # Returns the decimal_number string from function binary_to_decimal
        if target_base == 16 :
            return binary_to_hex(input_number) # Returns the hex_number string from function binary_to_hex


    #Converting from source base 16   
    if source_base == 16 : 
        if target_base == 10 :
            return hex_to_decimal(input_number)   # Returns the decimal_number string from function hex_to_decimal
        if target_base == 2 :
            return hex_to_binary(input_number) # Returns the binary_number string from function hex_to_binary
        

###=======================     Main Code      ==================###


while True:
    input_number= input("\nPlease enter the number to convert: ")
    source_base= int(input("The source base (i.e., the base to convert from): "))
    target_base= int(input("The target base (i.e., the base to convert to): "))

    if not validate_input(input_number, source_base, target_base):
        continue # continues to take another input if the validation fails under invalid inputs
    
    print(f"The result of converting the number {input_number} from base {source_base} to base {target_base} is: ")
    print(convert_number(input_number, source_base, target_base))

    while True:
        choice = input("Do you want to convert another number? \nEnter (Y) to Continue \nEnter (N) to Quit \n")
        
        if choice.upper() == "Y": # if it is a lower case n then changes and checks for upper case N
            break #exits the loop in case of y and continues the program:
        elif choice.upper() == "N":
            print("\nQuitting Calculator...")
            print("Thank You for using our Calculator!")
            exit()  #exits the whole program
        else:
            print("Invalid input. Please enter Y To Continue or N To Quit.\n")




        




