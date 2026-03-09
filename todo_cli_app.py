#this is a todo list app we add task and delet that tasks is done
file="todo_list.txt"
#opening file 
with open(file) as f:
# fetching current todo list
    data=f.read()
    print("your current todo list is:")
    print(data)
#getting user input
print("what you want to do add or delete tasks ")
user_choice=input("please enter:").lower()
# evaluating user choice
# adding task to  the list
if user_choice=="add":
    user_task=input("input task that you want to add:")
    with open(file,"a") as f:
        f.write("\n"+user_task)
        print("update list successfully")
# deleting tasks from the list
elif user_choice=="delete":
    comp_task=input("enter the completed task:")
    if comp_task in data:
        updated=data.replace(comp_task,"").strip()
        with open(file,"w") as f:
           f.write(updated)
           print (updated)
    # in case user enter the task that is not present in list
    else:
        print("invalid task")
# if user enter anthing except add or delete it show error
else:
    print("error invalid choice")
