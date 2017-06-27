#!/usr/bin/env python3

import re


from .mapping import Mapping as mpg
from .processor.prcmap import PrcMap as Prm


class Sabdakosh():
    def __init__(self):
        self.prerex = mpg.getPreRex()
        self.postrex = mpg.getRexArray()
        self.rawunifile= './res/Chha.txt'
        self.unifile = './res/ChhaPr.txt'
        #self.outfile = './res/Out.txt'
        #self.infile  = './res/Page.txt'
        self.asciifile= './res/ChhaASCII.txt'
        #self.infile = '/home/pranphy/Desktop/Dictionarys.txt'

    def rexSub(self,line,rex):
        for rx in rex:
            line = re.sub(rx[0],rx[1],line)
        return line 


    def asciiToUnicode(self):
        dicmap = mpg.getMapping()
        rexarray = mpg.getRexArray()
        extmap = mpg.getExtraMap()
        with open (self.rawunifile,'w') as ofl:
            with open(self.asciifile,'r') as fil:
                content = fil.read()
                content = self.rexSub(content,self.prerex)
                cnt = ''
                for char in content:
                    try:
                        ucc = dicmap[char]
                        cnt += ucc
                    except KeyError:
                        try:
                            euc = extmap[char]
                            cnt += euc
                        except KeyError:
                            cnt += char
                
                cnt = self.rexSub(cnt,self.postrex)
                ofl.write(cnt)


    def postProcess(self):
        with open(self.rawunifile,'r') as inf:
            with open(self.unifile,'w') as otf:
                wholeFile = inf.read()
                for rex in self.prerex:
                    wholeFile = re.sub(rex[0],rex[1],wholeFile)

                otf.write(wholeFile)


    def doStuffs(self):
        self.asciiToUnicode()
        self.postProcess()

                            
if __name__ == '__main__':
    obj = Sabdakosh()
    obj.doStuffs()
