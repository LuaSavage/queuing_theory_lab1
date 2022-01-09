from textmenu.item import TextMenuItem

class TextMenu(object):
    description = "Описание по умолчанию"
    items = []
    
    def __init__(self, description=None, items=None, default_exit=None):
        self.description = str(description) or self.description
        self.items = list(items)
        if default_exit:
            self.items.append(TextMenuItem(description="Выход"))
        
    def display(self):
        print("Menu.")
        print(self.description)
        for item in self.items:
            item_id = self.items.index(item)        
            print(item_id,". ",item.description,"")         
        
        while True:
            operation_id = int(input("Введите номер операции: "))
            if operation_id in range(len(self.items)):
                self.items[operation_id].on_click()
                return True
            else:
                print("Неверный номер операции ")

        