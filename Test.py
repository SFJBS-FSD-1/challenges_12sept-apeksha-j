#Challenge1 : Write a function that takes a natural number as input and outputs the number of digit in it. Conversion of number to string is not allowed
def challenge1(user_number):
    count=0
    while user_number != 0:
        user_number//= 10
        count = count+1
    return count
user_number = int(input("Enter a natural number"))
print("Number of digits are %d" % (challenge1(user_number)))

#Challenge2 : Write a function that takes a natural number as input and outputs the reverse of that number. Conversion of number to string is not allowed
def challenge2(user_number):
    reverse=0
    while user_number> 0:
        ans= user_number%10
        reverse = (reverse*10) + ans
        user_number = user_number//10
    return reverse
user_number = int(input("Enter a natural number"))
print("The reverse digit is %d" % (challenge2(user_number)))

#Challenge3 : Write a function where user will enter a natural number as input and output returns the number of zeroes in the end of the factorial of that number. Conversion of number to string is not allowed
def challenge3(user_number):
    count = 0
    while(user_number >= 5):
        user_number//= 5
        count =count+1
    return count
user_number = int(input("Enter a natural number"))
print("The count of zeros is %d" % (challenge3(user_number)))

#Challenge4 : list1 = ["India" , "England", "Spain"]
#
# list2 = ["Delhi","London","Madrid"]
#
# Write your own function that takes list1 and list2 as inputs and returns a dictionary like
#
#   dict1 = {“India” : “Delhi” , “England”:”London”, “Spain”:”Madrid”}
def challenge4():
    list1 = ["India", "England", "Spain"]
    list2 = ["Delhi", "London", "Madrid"]
    dict = {list1[i]: list2[i] for i in range(len(list1))}
    return dict
print (challenge4())

#Challenge5 : places = {(“19.07'53.2”, “72.54'51.0”): "Mumbai",

#                  (“28.33'34.1”, “77.06'16.6”): "Delhi"}
#
#
#
# Write code to create a new dictionary using given dictionary
#
#
#
# city = {"Mumbai": {“Latitude”: “19.07'53.2” , “Longitude”: “72.54'51.0”}}
#
#              {“Delhi” : {“Latitude”: “28.33'34.1” , “Longitude”: “77.06'16.6”} }
places = {("19.07'53.2", "72.54'51.0"): "Mumbai", ("28.33'34.1", "77.06'16.6"): "Delhi"}
dict1= {"Latitude": "19.07'53.2" , "Longitude": "72.54'51.0"}
dict2= {"Latitude": "28.33'34.1" , "Longitude": "77.06'16.6"}
for i in places:
  val= places[i]
  city= {val:dict1}
  dict1 = dict2
  print(city)

#Challenge6 : Given mylist  =  [3, 5 ,4 , 6, 9, 10 , 2 , 8, 7 ,1]

# Using for loop find the sum of all even numbers in mylist
mylist  =  [3, 5 ,4 , 6, 9, 10 , 2 , 8, 7 ,1]
sum=0
for i in mylist:
    if i%2==0:
        sum=sum+i
print(f"The sum of even numbers in {mylist} is {sum}")