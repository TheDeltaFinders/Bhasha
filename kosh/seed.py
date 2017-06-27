#!/usr/bin/env python3

#import os

#os.environ.setdefault('DJANGO_SETTINGS_MODULE','nepali.settings')



from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

from .processor.indexmaper import IndexMaper as IdMap
from .models import Pos 



class Seed():
    def __init__(self):
        self.idxmap = IdMap().getIndexMap()

    def seedNow(self):
        print('the index amp is ')
        print(self.idxmap)
        for k in self.idxmap:
            curpos = Pos(partname = self.idxmap[k],abbr=k,is_active=True)
            curpos.save()

    def showNow(self):
        for pos in Pos.objects.all():
            print('key {} and value {}'.format(pos.abbr,pos.partname))

    def doStuffs(self):
        #self.seedNow()
        self.showNow()



if __name__ == '__main__':
    a = Seed()
    a.doStuffs()

