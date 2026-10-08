def addtask():
    with open("task.txt", "a") as tasks:
        task = input("write a task to do:")
        tasks.write(task+"\n")

def displaytask():
    with open("task.txt", "r") as tasks:
        task = tasks.read()
        print(task)

def main():
    while True:
        print("\t\t------Task Manager------\t\t")
        print("\t\t1.Add Task\t\t")
        print("\t\t2.Display Task\t\t")
        print("\t\t2.Mark Complete\t\t")
        print("\t\t3.Delete Task\t\t")
        print("\t\t4.Modifie Task\t\t")
        print("\t\t5.exit\t\t")
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                addtask()
            case 2:
                displaytask()
            case 3:
                markcomplete()
            case 4:
                modifytask()
            case 5:
                print("Exiting.....")
                break
            case _:
                print("Invalid choice enter between(1 <> 4)")
main()