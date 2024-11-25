class Door:
    def __init__(self, is_opened=False):
        self.is_opened = is_opened

    def open_door(self):
        self.is_opened = True
        print("The door is open.")

    def close_door(self):
        self.is_opened = False
        print("The door is closed.")

class Blocked_Door(Door):
    def open_door(self):
        super().open_door() 
        print("This door is blocked and cannot be opened.")

    def close_door(self):
        super().close_door()  
        print("This door is blocked and cannot be closed.")

