import json
import os

DATA_FILE = "todo_list.json"

class Task:
    def __init__(self, title, completed=False):
        self.title = title
        self.completed = completed
        
    def mark_done(self):
        self.completed = True
        
    def to_dict(self):
        return {"title" : self.title, "completed": self.completed}
    
    @classmethod
    def from_dict(cls, data):
        return cls(data['title'], data['completed'])
    
    def __str__(self):
        # FIXED: spelling of 'completed'
        status = "[x]" if self.completed else "[ ]"
        return f"{status} {self.title}"
    
class ToDoList:
    # FIXED: __init__ (was __ini__)
    def __init__(self, filename="todo_oop.json"):
        self.filename = filename
        self.tasks = self.load_tasks()
        
    # FIXED: load_tasks (was load_tasts)
    def load_tasks(self):
        if not os.path.exists(self.filename):
            return []
        
        try:
            with open(self.filename, 'r') as file:
                # FIXED: json.load (was json.loading)
                data = json.load(file)
                return [Task.from_dict(item) for item in data]
            
        except (json.JSONDecodeError, IOError):
            return []
        
    def save_tasks(self):
        try:
            # FIXED: to_dict (was do_dict)
            data = [task.to_dict() for task in self.tasks]
            with open(self.filename, 'w') as file:
                json.dump(data, file, indent=4)
                
        except IOError as e:
            print(f"Error saving: {e}")
            
    def add_task(self, title):
        new_task = Task(title)
        self.tasks.append(new_task)
        self.save_tasks()
        print(f"Added: {title}")
        
    def delete_task(self, index):
        if 0 <= index < len(self.tasks):
            removed = self.tasks.pop(index)
            self.save_tasks()
            print(f"Deleted: {removed.title}")
        else:
            print("Invalid task number")

    # ADDED: This function was missing in your code!
    def mark_task_done(self, index):
        if 0 <= index < len(self.tasks):
            self.tasks[index].mark_done()
            self.save_tasks()
            print("Task marked as done.")
        else:
            print("Invalid task number")
            
    # FIXED: renamed to list_tasks (was list_task singular)
    def list_tasks(self):
        print("\n--- TO-DO LIST ---")
        if not self.tasks:
            print("No tasks found")
            
        else:
            # FIXED: enumerate(self.tasks) (was enumerate(self))
            for i, task in enumerate(self.tasks, start=1):
                print(f"{i}. {task}")
        print("-------------------------")
        
        
def main():
    my_list = ToDoList()
    
    while True:
        print("\n1. Add 2. View 3. Complete 4. Delete 5. Exit")
        choice = input("Enter your choice: ")
        
        if choice == '1':
            title = input("Task name: ").strip()
            if title: my_list.add_task(title)
            
        elif choice == '2':
            my_list.list_tasks()
            
        elif choice == '3':
            my_list.list_tasks()
            try:
                idx = int(input("Task # to complete: ")) - 1
                my_list.mark_task_done(idx)
                
            except ValueError:
                print("Please enter a number.")
                
        elif choice == '4':
            my_list.list_tasks()
            try:
                idx = int(input("Task # to delete: ")) - 1
                my_list.delete_task(idx)
                
            except ValueError:
                print("Please enter a number.")
                
        elif choice == '5':
            print("Goodbye!")
            break
        else:
            print("Invalid option.")
            
            
if __name__ == "__main__":
    main()