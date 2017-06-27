from django.contrib import admin

from .models import BaseWord
from .models import Pos
from .models import SubWord
from .models import Meaning

admin.site.register(Pos)
admin.site.register(BaseWord)
admin.site.register(SubWord)
admin.site.register(Meaning)
