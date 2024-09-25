# #Exercise 1
# def FactorialCalc(num):
#     factorial=1
#     counter=1
#     for i in range(num):

#         factorial*=counter
#         counter+=1
#     print( factorial)

# num= int(input("Enter a number: "))
# FactorialCalc(num)


# #Exercise 2

# def divisorFinder(num):
#     division_list=[]
#     division=1
#     while division<=num:
#          if num % division==0:
#              division_list.append(division)
        
#          division+=1
    
#     print(division_list)    
    
    
# divisorFinder(10)    



# #Exercise 3
# def reverseString(word):
#     result=""
#     count=len(word)-1
#     for i in word:
#         result=result+word[count]
#         count-=1
#     print( result)    
    
# word=input("Enter a string: ")
# reverseString(word)



# #Exercise 4 

# def oddNumRemover(num):
     
#      result=num
#      for i in num:
#          if i %2==1:
#              result.remove(i)
    
    
#      print(result)         
            
# num=input("Enter a list of integers separated by spaces") 
# numList = list(map(int, num.split()))

# oddNumRemover(numList)
  



 

# #Exercise 5
# def passChecker(password):
#     isUpper=False
#     isLower=False
#     isdigit=False
#     specialCharacters=['!','#','$','?']
#     containsSpecialCharacters=False
#     for i in password:
        
#         if i.isupper():
#             isUpper=True
#         if i.islower():  
#             isLower=True
#         if i in specialCharacters:
#             containsSpecialCharacters=True
#         if i.isdigit():
#             isdigit=True

#     if isUpper==True and isLower==True and containsSpecialCharacters==True and len(password)>=8 and isdigit==True:
#         print("Strong password")
#     else:print("weak password")    
    

# password=input("Enter a password: ")
# passChecker(password)

# #Exercise 6

# def ipv4Validator(ipaddress):
#     octets=ipaddress.split('.')
#     isValid=True

#     if len(octets)!=4:
#         isValid=False
#     for i in octets:
#         if not i.isdigit():
#             isValid=False
#             break
#         num= int(i)
#         if num<0 or num>255 or(i[0]=='0' and len(i)>1):
#             isValid=False
#             break
#     if isValid:
#         print("The ip address is valid")

#     else :
#         print("invalid ip address")            
# ipaddress=input("Enter an ip address :")
# ipv4Validator(ipaddress)       