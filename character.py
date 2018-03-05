# Superclass (of Enemy): Has the common characteristics of a Character
class Character():

    # Create a character object
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    # Describe this character
    def describe(self):
        print( self.name + " is here!" )
        print( self.description )

    # Set what this character will say when talked to
    # (This is a Setter method that sets the conversation attribute)
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character (& let character talk back!)
    def talkedTo(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character - only picks fight with enemies-> msg returned backs off
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        #return True
        return False    #since in main.py fight occurs when True, set superclass
                        #... method to return False until overriden by base classes

class Enemy(Character):
    """Sub-class: Some objects will be friends others enemies => I smell INHERITANCE!
        If a function requires a character object as a parameter, we can give the
        function an Enemy object instead and the code will still work... coz Enemy IS A Character..
        ... as in it contains (all) what character has.
        However, this does not work the other way around : if the function requires an Enemy object
         we cannot give it a character object, because Enemy is a MORE SPECIALISED version of Character.
         
    # Enemy is a subclass (of Character) that adds more functionality specific to enemies
    # Enemy class will inherit ALL of the attributes and methods from Character

    # [Important] POLYMORPHISM: <Subclass> IS A <superclass> ==> an enemy IS A character
    # (An object of a subclass is also considered to be an object of its superclass.)"""
    

    enemies_defeated = 0 # CLASS variable: win only after a specific number of enemies defeated!!!!
    
    # Constructor of subclass - (no different from superclass....)
    def __init__(self, char_name, char_description):
        # To ensure that Enemy INHERITS from Character ==> call superclass constructor METHOD right HERE!
        super().__init__(char_name, char_description) # ==> FIRST instantiate Character object then WE'LL customise it

        self.weakness = None #To customise object, add new functionality --> a new attribute called weakness
                                # e.g. Superman would be vulnerable to Kryptonite

    # Setters and Getters
    def set_weakness(self, item_weakness):
        self.weakness = item_weakness

    def get_weakness(self):
        return self.weakness

    # implementation of fight() Overidden: Hostile characters will be fought!
    #If the combat_item the player uses to fight with the enemy is the enemys weakness
        #then Enemy Object will be defeated!
    # Fight with this character -> State what outcomes of the fight will be
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You fends " + self.name + " off with the " + combat_item )

            Enemy.enemies_defeated += 1
            return True
        else:
            print(self.name + "[the Enemy] crushes you, puny adventurer")
            return False

    #Getters/Setters for the enemies_defeated CLASS variable
    def set_defeated(self, number_defeated):
        Enemy.enemies_defeated = number_defeated

    def get_defeated(self):
        return Enemy.enemies_defeated

    ### You could add other methods here to interact with Enemy in other ways!!
        # e.g. steal from an enemy, bribe an enemy, or send it to sleep...etc
    def steal(self):
        print("You steal from " + self.name)  # Perhaps you could have added attribute in constructor "self.has_item" to steal :)
        # How will you decide what this character has to steal?


class Friend(Character):
  
    def __init__(self, char_name, char_description):
    
        super().__init__(char_name, char_description)
        self.feeling = None # custom attribute(s)

    ### Friend class with some custom methods
        # you could hug the friendly character, or offer them a gift.
    # To facilitate calling a hug method on a friend!!
    def hug(self):
        print(self.name + " hugs you back!")
    # What other methods could your Friend class have?


