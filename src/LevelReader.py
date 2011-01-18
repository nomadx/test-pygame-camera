'''
Created on 2011 1 18

@author: nomadx
'''
from someNome import SomeNode

class LevelReader():
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        
        pass
    def read_map_info(self):
        self.list = []
        
        f = open('data/map/map.txt','r')
        n = f.readline()
        print n
        self.nodes = []
        for iter in range(1,n):
            line = f.readline()
            type = line.split()[2]
            conCount = line.split()[1]
            coord = line.split()[3]             
            for ism in range(line.split()[1]):
                list.append(f.readline())
            self.nodes.append(SomeNode(type,conCount, list, coord))
        print self.nodes[1]
        f.close()
        pass