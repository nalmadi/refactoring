'''
John Connors 
Lab 8 
Draws som better colorful 
trees with the L system class. 
Creates the L system class.  
4/11/19 
Version 2 of lsystem.py
''' 

import sys

#Creates the Lsystem class
class Lsystem: 
    def __init__(self, filename = None):

        self.base = '' #Creates an empty string for base 
        self.rule = [] #Creates a list called rules that is empty 

        if filename != None: 
            self.read(filename) # reads the name of the file 

    def setBase(self, newbase): 
        self.base = newbase #Sets the base of the string  

    def getBase(self):
        return self.base #Returns the value of base 

    def getRule(self, index): #Indexes to a part of the rules list
        return self.rule[index]

    def addRule(self, newrule): #Adds a new rule to the rules list 
        self.rule.append(newrule)
    
    def numRules(self): #Gets the value of the number of rules in the rules list 
        return len(self.rule)

    def read(self, filename): #Reads the string in the file and skips over the words base and rule 
        fp = open(filename, 'r')
        for line in fp: 
            words = line.split()
            if words[0] == 'base': 
                self.setBase(words[1])
            elif words[0] == 'rule': 
                self.addRule(words[1:])
        fp.close()

    def replace(self, istring): #Replaces parts of the string with other characters 
        tstring = ''
        for c in istring: 
            found = False

            for rule in self.rule: 
                if rule[0] == c : 
                    tstring += rule[1]
                    found = True
                    break
            if found != True:
                tstring += c 
        return tstring

    def buildString(self, iterations): #Reads over the string a certain number of times 
        nstring = self.base 
        for i in range(iterations):
            nstring = self.replace(nstring)
        return nstring

def main(argv): #tests to see in Lsystem class works by printing what is in a file 

    if len(argv) < 2:
      print('Usage: lsystem.py <filename>')
      exit()

    filename = argv[1]
    iterations = 2

    lsys = Lsystem()

    lsys.read( filename )

    print( lsys )
    print( lsys.getBase() )
    for i in range( lsys.numRules() ):
      rule = lsys.getRule(i)
      print( rule[0] + ' -> ' + rule[1] )

    lstr = lsys.buildString( iterations )
    print( lstr )

    return

#This is the main code 
if __name__ == "__main__":
    main(sys.argv)
						