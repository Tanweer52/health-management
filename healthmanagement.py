
def getdate():
    import datetime
    return datetime.datetime.now()

def client_name(client):
    info = True
    while (info):
        print("What do you want to log \n Press \n (1) Excercise\n (2) Diet")
        option = int(input())
        if option == 1:
            with open(client+"_excercise.txt","a") as f:
                print("Enter the type of excercise done")
                food = input()
                f.write("["+str(date)+"]"+"\t"+food+"\n")
                info = False

        elif option == 2:
            with open(client + "_diet.txt", "a") as f:
                print("Enter the type of diet done")
                excercise = input()
                f.write("[" + str(date) + "]" + "\t" + excercise+"\n")
                info = False
        else:
            print("Please enter a valid input\n")
            # while loop is used to avoid invalid inputfrom user othrwise it can be done without while loop


date = getdate()
print("Please enter the client name : \n (1) harry \n (2) rohan \n (3) hammad ")
clients = ["harry","rohan","hammad"]
i = int(input())
cl = clients[i-1]
client = client_name(cl)