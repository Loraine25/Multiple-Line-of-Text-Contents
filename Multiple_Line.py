#Anonuevo, Loraine N.
#BSCpE 1-4 
#Multiple Line Text Contents

#Header
print("\033[;33;1;3m\033[10m" * 65)
print("\033[;33;1;3mAyooo! It's a pleasure to have you here!\033[0m".center(81))
print("\033[;33;1;3mಠ\033[10m" * 65)

#Request about the user's name.
print("")
print("\033[1;3mMy name is \033[;45;1;3mLoraine\033[0m")
your_name = input("\033[1;3mWhat is your name?\033[0m")
print("\033[;1;3mI'm glad that you're here!\033[;34;1;3m" + your_name + "\033[0m \033[;1;3m, sit back and learn with me!\033[0m")

#To open the file "mylife.txt" If the file does not already exist, it will be created.
with open("mylife.txt", "w") as file:

    #Use loop to execute the block of code repeatedly.
    while True:
        #Request for a line of text from the user.
        line = input("\n\033[;34;1;3mInput line: \033[0m")
        #Insert the text line, followed by a new line character, into the file.
        file.write(f" {line}\n")

#Close the file
file.close()