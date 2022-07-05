class TextMenuItem(object):
    description = "Описание по умолчанию"
    sub_menu = None
    todo = []
    
    def __init__(self, description=None, sub_menu=None, todo=None):
        self.description = str(description) or self.description
        self.sub_menu = sub_menu
        if todo:
            self.todo = list(todo)
        
    def on_click(self):
        if self.todo:
            self.todo[0](*self.todo[1])
        if self.sub_menu:
            return self.sub_menu.display()           