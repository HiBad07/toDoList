# TO DO LIST PROGRAM

#im very proud of this

# Description:
# The program uses a .json file called "todolist.json" to remember the todolist between runs.
# The program uses two classes, Task and ToDoList, where each task is represented as an 
# object with title, description, and completion status attributes. 

# Users interact with the program through a CLI in the main function, selecting various actions.
# Additionally, the program saves and loads the to-do list data to/from a JSON file, 
# ensuring that the to-do list state is preserved across different runs of the program. 
# This enables users to manage their to-do list over multiple runs.


import json

class Task:
    #instantiate class
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.completed = False

    #method to mark a task as complete
    def mark_as_completed(self):
        self.completed = True

class ToDoList:
    #instantiate task
    def __init__(self):
        self.tasks = []

    #method to add task object to list
    def add_task(self, task):
        #add task to the self.tasks list
        self.tasks.append(task)

    #method to view the full list from the json file
    def view_tasks(self):
        #iterate through all the tasks stored in self.tasks using enumerate to get the index and the task object in each iteration
        for index, task in enumerate(self.tasks, start=1):
            #mark the status of the task
            status = "Completed" if task.completed else "Incomplete"
            #print each task to console
            print(f"{index}. Title: {task.title}, Description: {task.description}, Status: {status}")

    #method to update the details of a task when given the index of the task
    def update_task(self, task_index, new_title, new_description):
        #make sure the correct task is being getted
        task = self.tasks[task_index - 1]
        #update the title
        task.title = new_title
        #update the description
        task.description = new_description

    #methdo to mark a task as completed
    def mark_task_completed(self, task_index):
        task = self.tasks[task_index - 1]
        task.mark_as_completed()

    #method to remove a task from the list
    def remove_task(self, task_index):
        del self.tasks[task_index - 1]

    #method to convert the state of a todolist object into a dictionary format
    def to_dict(self):
        #create a list of all the tasks using the three properties of the task by iterating through each task in the self.tasks list
        #resulting list will contain dictionaries for each task with all 3 properties
        task_list = [{'title': task.title, 'description': task.description, 'completed': task.completed} for task in self.tasks]
        #return the dictionary ready to convert to json form
        return {'tasks': task_list}

    #creates a new list object by grabbing data from the dictionary format
    #and reconstructs the list based on the information from the json file
    @classmethod
    def from_dict(cls, data):
        #creates empty instance of the class
        todo_list = cls()
        #iterate through the data dictionary
        for task_data in data['tasks']:
            #extract the title and description from the data and use it to create a task object
            task = Task(task_data['title'], task_data['description'])
            #If the task is completed, mark the object as completed
            if task_data['completed']:
                task.mark_as_completed()
            #add the task to the todolist object
            todo_list.add_task(task)
        #return the list which now contains data from the json file
        return todo_list

#subroutine to save the file as a json
def save_to_file(todo_list, filename):
    #open the json file in write mode
    with open(filename, 'w') as file:
        #serialize the contents of the list using json.dump and write to the file 
        json.dump(todo_list.to_dict(), file)

#function to grab the contents of the json file and returns the ToDoList object based on the contents of the file
def load_from_file(filename):
    try:
        #open the json file in read only mode
        with open(filename, 'r') as file:
            #parse the json data from the file
            data = json.load(file)
            #returns the reconstructed list using the from_dict function above
            return ToDoList.from_dict(data)
        #If the file doesnt exist, the program returns an empty object to provide a default value
    except FileNotFoundError:
        return ToDoList()

#main function for program
#i dont have enough time to explain what all the lines do like i have done with the methods and procedures above
def main():
    filename = "todolist.json"
    my_todo_list = load_from_file(filename)

    
    while True:
        print("")
        print("To-Do List Menu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Update Task")
        print("4. Mark Task as Completed")
        print("5. Remove Task")
        print("6. Save and Exit")

        choice = input("Enter your choice: ")

        #TO DO: CHANGE THIS TO SWITCH CASE RATHER THAN WHILE TRUE
        if choice == "1":
            title = input("Enter task title: ")
            description = input("Enter task description: ")
            task = Task(title, description)
            my_todo_list.add_task(task)
            print("Task added successfully")

        elif choice == "2":
            print("\nTasks:")
            my_todo_list.view_tasks()

        elif choice == "3":
            task_index = int(input("Enter the task to update: "))
            new_title = input("Enter the new task title: ")
            new_description = input("Enter the new task description: ")
            my_todo_list.update_task(task_index, new_title, new_description)
            print("Task updated successfully")

        elif choice == "4":
            task_index = int(input("Enter the task to mark as completed: "))
            my_todo_list.mark_task_completed(task_index)
            print("Task marked as completed")

        elif choice == "5":
            task_index = int(input("Enter the task to remove: "))
            my_todo_list.remove_task(task_index)
            print("Task removed successfully")

        elif choice == "6":
            save_to_file(my_todo_list, filename)
            break
        else:
            print("Invalid choice")


main()


