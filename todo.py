import tkinter as tk
import datetime as dt


class ToDoApp:
    def __init__(self):
        self.app = tk.Tk()

        self.app.geometry('640x640')
        self.app.title('To Do list')

        self.todos = []
        self.index = 0

    def add_todo(self, item):
        self.todos.append([item, {'index': self.index}, {'checked': False}, {'added_time': dt.datetime.now()},
                           {'complete_by': ''}])
        # for complete by use wheel or other GUI included option to avoid formatting issues
        self.index += 1

    def remove_todo(self):
        # remove item based on index
        pass

    def remove_checked(self):
        # filter todos to remove checked items
        pass

    def sort_by_date_added(self):
        # when date button is clicked sort item by date added
        pass

    def sort_by_date_to_be_completed(self):
        # when date button is clicked sort item by date item needs to be completed by
        pass


if __name__ == '__main__':
    ToDoApp().app.mainloop()
