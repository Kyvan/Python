# Libraries needed
import subprocess
import sys
import getpass

# User creation funtion
def createUser():
    
    # Get the username
    username = input("What's the username? ")

    # Get the password
    password = getpass.getpass()

    try:
        # Excute useradd command using subprocess
        subprocess.run(['useradd', '-p', password, username])

    except:
        print ("Failed to add user")
        sys.exit(1)

createUser()