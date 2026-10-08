
def main():
    while True:
        print("------Task Manager------")
        print("\t\t1.Add Task\t\t")
        print("\t\t2.Display Task\t\t")
        print("\t\t2.Mark Complete\t\t")
        print("\t\t3.Delete Task\t\t")
        print("\t\t4.Modifie Task\t\t")
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
            case _:
                print("Invalid choice enter between(1 <> 4)")
