class Checklist:
    def __init__(self):
        self.checklist = []
        self.completed_tasks = []
        self.incomplete_tasks = []

    def add_task(self, task):
        self.checklist.append(task)

    def mark_task(self, task, completed=True):
        if task in self.checklist:
            self.checklist.remove(task)
            if completed:
                self.completed_tasks.append(task)
            else:
                self.incomplete_tasks.append(task)
        else:
            print(f"Task '{task}' not found in checklist.")

    def review_tasks(self):
        print("\nCompleted Tasks:")
        for task in self.completed_tasks:
            print(f"{task}")

        print("\nIncomplete Tasks:")
        for task in self.incomplete_tasks:
            print(f"{task}")


checklist_obj = Checklist()
checklist_obj.add_task("Finish day_01 task")
checklist_obj.add_task("Finish day_02 task")
checklist_obj.add_task("Finish day_13 task")
checklist_obj.add_task("Finish day_03 task")
checklist_obj.add_task("Finish day_15 task")

checklist_obj.mark_task("Finish day_01 task")
checklist_obj.mark_task("Finish day_02 task", completed=True)
checklist_obj.mark_task("Finish day_13 task", completed=False)
checklist_obj.mark_task("Finish day_03 task", completed=True)
checklist_obj.mark_task("Finish day_15 task", completed=False)

checklist_obj.review_tasks()
