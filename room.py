#room.py

# A text-based adventure game
# The constructor will initialize an Object with default values/attributes
class Room():          # A blueprint for the rooms  
    #def __init__(self):
        #self.name = None
        #self.description = None    # refers to a piece of data within the object
                                    # self means 'this object'
                                    # Setting the attribute values to 'None' means
                                    #     that they will start off with no value

    # Pass values if You want users of class to set the values of these parameters
    def __init__(self, room_name):  
        self.name = room_name
        self.description = None
        self.linked_rooms = {}  # "a dictionary data structure" form of associative list. Where each element has a key. Dictionaries are indexed by keys, 
                                # e.g think of a dictionary as an unordered set of key: value pairs (keys are unique WITHIN one dictionary)
                                # The main operations on a dictionary (1) storing a value with some key and (2) extracting the value given the key.
                                # It is also possible to delete a key:value pair with del
                                ###### which is the room in a particular direction?
        # Add this attribute to Room class constructor to know when room has a character inside it!!
        # Aggregation: objects within objects!
        self.character = None   # Aggregation: A OBJECT (room) has an OBJECT (character) INSIDE IT!!! 
                                # Rooms with no character have their character attributer set to None
                                #### IMPORTANT: THIS IS HOW a room (object) gets the capability to contain a character (object).

        self.item = None   # Add item to Room so Room can store an item
        
    # getters and setters
    

    # SETTERS: Method to set the description of the room:

    def set_description(self, room_description):
        """ For every method within a class, the first parameter specified must be self
         the object itself : followed by any data you wish to pass in just as we did with the constructor """
        self.description = room_description

    def set_name(self, room_name):
        self.name = room_name

    # GETTERS: Here is a method to get the description of the room:

    def get_description(self):
        return self.description

    def get_name(self):
        return self.name

    ###----setter/getter methods to put character inside a room
    def set_character(self, new_character):
        self.character = new_character

    def get_character(self):
        return self.character

    ###----setter/getter methods to put item inside a room
    def set_item(self, item_name):
        self.item = item_name

    def get_item(self):
        return self.item

    # OTHER methods: You need a print method/statement!
    def describe(self): 
        print( self.description )

    # method to allow us to link rooms together
    def link_room(self, room_to_link, direction):   
        self.linked_rooms[direction] = room_to_link  # STORAGE: room_to_link is the room in a particular direction...
	# to see what’s inside the dictionary BUT COMMENTED FOR NOW COZ OUT OF SCOPE
        #print( self.name + ' linked rooms ' + repr(self.linked_rooms) )
        

    def display(self):
        """Display method to report the room name, description, and the directions of all the rooms connected to it
        The above method loops through the dictionary self.linked_rooms and, for every defined
        direction, prints out that direction and the name of the room in that direction."""
        print( "The " + self.get_name())
        print( "----------------")
        print(self.get_description())
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]  # EXTRACT: room_to_link is the room in 
            print( "The " + room.get_name() + " is " + direction)


    #Move between rooms
    #Pass parameter for the direction in which the player would like to move
    def move(self, direction):
        if direction in self.linked_rooms:  #To check whether a single key is in the dictionary, use the 'in' keyword  
            return self.linked_rooms[direction] # Extract
        else:
            print("You can't go that way")
            return self


    

    




    



    
