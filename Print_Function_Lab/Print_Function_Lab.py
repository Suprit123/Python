# In the below Print Function Lab, you will be using the print function to display various types of data.
print(
    "Hello, my name is Suprit"
)  # The content inside the parentheses is what will be printed to the console and its type is a string.

# This line has been added to demonstrate the use of single quotes within a string.
print("Welcome to the 'Python Print' Function Lab")

# The above print function can also be done in reverse manner. We have used double quotes within a string
print('Welcome to the "Python Print" Function Lab')

# In below print function we will look into escape characters using backslash (\)
print('Welcome to the "CCNA" Training')

# In below print function we will look into how to print multiple lines one after other by using backslash n (\n)
print("router ospf 10 \n router-id 1.1.1.1 \n network 192.168.1.0 0.0.0.255")

# The alternative for the above print function when we want to print multiple lines is use tripple quotes("""). We can use triple single quotes as well (''').
print(
    """ router bgp 100 
      neighbor 1.1.1.1 remote-as 100 
      network 192.168.1.0 mask 255.255.255.0 """
)
