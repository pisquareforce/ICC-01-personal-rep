# Run: python3 first_python_script.py 

inputfile:str
inputfile = "names.txt"

#
# function to add a new name to the file
#
def addname(name: str):
    with open(inputfile, 'a') as file:  #  append mode
        file.write(name + '\n')
    return
#
# function to read amd display names
#
def read_display(filename: str):

    with open(filename, 'r') as file:
            for line in file:
                print(line.strip())  
    return

#
# menu funtcion
#
def menu ():
    option:int
    while True:
        print("1) Read and display names;")
        print("2) Add a new name;")
        print("3) Exit;")
        option = int(input("Please choose an option: "))
        if option == 3:
            print("Exiting ...") 
            break
        elif option == 1:
           read_display(inputfile)
        elif option == 2:
            name = input("Enter a name to add: ")
            addname(name)
#
# main fucntion
#
def main(): 
    menu()


if __name__ == "__main__":

    main()
