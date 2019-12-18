class Spell:
    def __init__(self, incantation, name):
        self.name = name
        self.incantation = incantation
    def __str__(self):
        return self.name + ' ' + self.incantation + '\n' + self.get_description()
    def get_description(self):
        return 'No description' #can be changed to ‘This charm summons an object to the caster, potentially over a significant distance’ for Accio description
    def execute(self):
        print(self.incantation) #add parantheses in self.incanatation
class Accio(Spell):
    def __init__(self):
        Spell.__init__(self, 'Accio', 'Summoning Charm')
    def get_description(self):
        return 'This charm summons an object to the caster, potentially over a significant distance'
    #added get_description using return for the study_spell(spell)
#fix class indentation
class Confundo(Spell):
    def __init__(self):
        Spell.__init__(self, 'Confundo', 'Confundus Charm')
    def get_description(self):
        return 'Causes the victim to become confused and befuddled.'
#put def study_spell out from Confundo class
def study_spell(spell):
        print(spell)
spell = Accio()
spell2 = Confundo()
spell.execute()
study_spell(spell)
study_spell(Confundo())

#print(spell.get_description()) #for Accio description but not needed because there already study_spell(spell)


#ANSWER:
#a. Parent class = Spell, child class = Accio & Confundo
#
#b. spell.execute : print : Accio
#   study_spell(spell) : print : Accio , Summoning Charm Accio, No description
#   study_spell(Confundo()) : print : Confundo, Confundus Charm Confundo, Causes the victim to become confused and befuddled.
#
#c. the one in the confundo class: 
# def get_description(self):
#       return 'Causes the victim to become confused and befuddled.'
#
#d. you can either change the description from the parent class from the 'No description' to ‘This charm summons an object to the caster, potentially over a significant distance’
#   or you can add 1 more function at the Accio class by adding: 
# def getDescription(self):
#       return ‘This charm summons an object to the caster, potentially over a significant distance’
