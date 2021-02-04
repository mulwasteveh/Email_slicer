# enter user email address
email = input("enter your email address: ")

# Slice out the user name
username = email[:email.index("@")]

# Slice the domain name
domain = email[email.index('@')+1:email.index('.')]

# Display output message
print("username: {} \n Domain: {}".format(username,domain))