class Checklist:
    def __init__(self): # constructor
        self.checklist = [] # list to store tasks
        self.completed_tasks = [] # list to store completed tasks
        self.incomplete_tasks = [] # list to store incomplete tasks

    def add_task(self, task):  # method to add task
        self.checklist.append(task)

    def mark_task(self, task, completed=True): # method to mark task as completed or incomplete
        if task in self.checklist: # check if task is in checklist
            self.checklist.remove(task)
            if completed:  # check if task is completed
                self.completed_tasks.append(task)
            else:
                self.incomplete_tasks.append(task)
        else:
            print(f"Task '{task}' not found in checklist.")

    def review_tasks(self): # method to review tasks
        print("\nCompleted Tasks:")
        for task in self.completed_tasks:
            print(f"{task}")

        print("\nIncomplete Tasks:")
        for task in self.incomplete_tasks:
            print(f"{task}")


checklist_obj = Checklist() # create object of Checklist class
checklist_obj.add_task("Finish day_01 task") # add task to checklist
checklist_obj.add_task("Finish day_02 task")
checklist_obj.add_task("Finish day_13 task")
checklist_obj.add_task("Finish day_03 task")
checklist_obj.add_task("Finish day_15 task")

checklist_obj.mark_task("Finish day_01 task") # mark task as completed
checklist_obj.mark_task("Finish day_02 task", completed=True)
checklist_obj.mark_task("Finish day_13 task", completed=False)
checklist_obj.mark_task("Finish day_03 task", completed=True)
checklist_obj.mark_task("Finish day_15 task", completed=False)

checklist_obj.review_tasks() # review tasks
