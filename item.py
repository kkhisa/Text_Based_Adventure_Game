#item.py

class Item():
    """ The items you could find placed in Rooms of the Adventure Game"""
    def __init__(self, item_name):
        self.name = item_name
        self.description = None
        self.metal = ""


    #setters and getters
    def set_name(self, item_name):
        self.name = item_name

    def get_name(self):
        return self.name
        
    def set_description(self, item_description):
        self.description = item_description

    def get_description(self):
        return self.description

    #def set_metal(self, item_metal):
    #    self.metal = item_metal


    # Other methods
    def display(self):
        print("The [" + self.name + "] is here - " + self.description)

    """def display(self):
        #print(self.name)
        #print('===========')
        #print(self.description + ' and is made from ' + self.metal)"""
