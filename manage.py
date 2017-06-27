#!/usr/bin/env python3

import os
import sys

if __name__ == "__main__":
   os.environ.setdefault("DJANGO_SETTINGS_MODULE", "nepali.settings")
   from django.core.management import execute_from_command_line
   custOpt = sys.argv[1]
   if custOpt == 'seed':
       from kosh.seed import Seed
       a = Seed()
       a.doStuffs()
   elif custOpt == 'prepare':
       from kosh.prepare import Sabdakosh
       sk = Sabdakosh() 
       sk.doStuffs()
   else:
       execute_from_command_line(sys.argv)
