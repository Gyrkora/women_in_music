from tkinter import Label

class Utilities():
    def __init__(self, tree):
        self.tree = tree
    
    def update_treeview_GUI(self):
       for item in self.tree.get_children():
          self.tree.delete(item)

    def capitalized_doubled(artists_name):
        name_split = artists_name.split()
        if len(name_split) >= 2:
                name_split[0] = name_split[0].capitalize()
                name_split[1] = name_split[1].capitalize()
                name_capitalized = ' '.join(name_split)
                return name_capitalized
        else:
            return artists_name.capitalize()
        

    
    def advertencia(texto, colorfg, colorbg, row, col, root):
        global type_error
        type_error = Label(root, text=texto, fg=colorfg, bg=colorbg)
        type_error.grid(row=row, column=col)
        root.after(2000, lambda:type_error.destroy())  


    def clear_entries(val1, val2, val3, val4):
        entries = [val1, val2, val3, val4]
        for entry in entries:
            entry.delete(0, 'end')



