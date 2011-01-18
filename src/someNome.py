'''
Created on 2011 1 18

@author: nomadx
'''

class SomeNode:
    '''
    classdocs
    '''


    def __init__(self, type, conCount, cons, coord):
        '''
        Constructor
        '''
        self.type = type
        self.count = conCount
        self.coord = coord
        self.cons = cons[conCount]
        pass
    def node_info(self):
        print 'is "%s" type, connect count "%s", coordinate "%s"' % (self.type, self.cons, self.coord)
        for iter in range(0,self.count):
            print self.cons[iter]            