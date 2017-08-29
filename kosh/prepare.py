#!/usr/bin/env python3

import re

from .processor.mapping import Mapping as mpg
from .processor.prcmap import PrcMap as Prm


class Sabdakosh():
    def __init__(self):
        self.unirex = Prm.getPreRex()
        self.prerex = mpg.getPreRex()
        self.postrex = mpg.getRexArray()
        self.rawunifile= './res/Chha.txt'
        self.unifile = './res/ChhaPr.txt'
        self.sepfile = './res/ChhaSep.txt'
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
                
                print('doing a post process')
                cnt = self.rexSub(cnt,self.postrex)
                ofl.write(cnt)


    def postProcess(self):
        with open(self.rawunifile,'r') as inf:
            with open(self.unifile,'w') as otf:
                wholeFile = inf.read()
                for rex in self.unirex:
                    wholeFile = re.sub(rex[0],rex[1],wholeFile)

                otf.write(wholeFile)


    def doStuffs(self):
        self.asciiToUnicode()
        self.postProcess()
        self.separateWords()

    def separateWords(self):
        seprex = r'[^\x00-\x7F]*[/~]*([^\x00-\x7F]+—)'
        comprex = re.compile(seprex)
        cnt = 0
        lastPos = 0
        curPos  = 0
        with open(self.unifile,'r') as inf:
            with open(self.sepfile,'w') as otf:
                wholeFile = inf.read()
                for m in comprex.finditer(wholeFile):
                    lastPos = curPos
                    curPos = m.start()
                    otf.write('\n >> \n'+wholeFile[lastPos:curPos]+'\n << \n')
                    otf.write(m.group()+'\n')
                    print(cnt,' ',m.start(),' ' , m.group())
                    cnt += 1



                            
if __name__ == '__main__':
    obj = Sabdakosh()
    obj.doStuffs()
