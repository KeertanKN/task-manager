def addtask(k):
    with open("task.txt", "a") as tasks:
        k = k+1
        task = input("write a task to do:")
        tasks.write(str(k) + task+"Pnd\n")


def displaytask():
    with open("task.txt", "r") as tasks:
        task = tasks.read()
        print(task)
def markcomplete(k):
    with open("task.txt", "r") as tasks:
        lines = tasks.readlines()
    lines.pop(1)

def main():
    while True:
        k = 0
        print("\t------Task Manager------\t\t")
        print("\t\t1.Add Task\t\t")
        print("\t\t2.Display Task\t\t")
        print("\t\t2.Mark Complete\t\t")
        print("\t\t3.Delete Task\t\t")
        print("\t\t4.Modifie Task\t\t")
        print("\t\t5.exit\t\t")
        choice = int(input("Enter your choice: "))
        match choice:
            case 1:
                addtask(k)
            case 2:
                displaytask()
            case 3:
                markcomplete(k)
            case 4:
                modifytask()
            case 5:
                print("Exiting.....")
                break
            case _:
                print("Invalid choice enter between(1 <> 4)")
main()