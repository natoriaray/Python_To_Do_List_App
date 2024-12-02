open_app = input("Hello would you like to add or delete a task? (Type 'add' or 'delete')").lower()
if open_app == "add":
  with open("todolistapp.txt", "a") as list:
    while True:
      task = input("Type in a task: ")
      list.write(task + "\n")

      end_task = input("would you like to add another task to your To-Do list? (y or n): ").lower()
      if end_task == "n":
        print("Thanks for adding tasks to your To-Do list. See you again next time")
        break
elif open_app == "delete":
  while True:
    to_delete = input("Type in the task you would like to delete: ").lower()
    to_delete_final = to_delete + "\n"
    with open("todolistapp.txt", "r") as list:
      task_list = list.readlines()
      task_list = [line.lower() for line in task_list]
      task_list.remove(to_delete_final)
    with open("todolistapp.txt", "w") as list:
      list.writelines(task_list)
      print("The task has been deleted. Way to be productive.")

    end_delete = input("Would you like to delete another task? y or n").lower()
    if end_delete == "n":
      print("See you next time!")
      break
else:
  print("You entered an invalid input. Please try again")
