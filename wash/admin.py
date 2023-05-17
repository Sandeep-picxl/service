from django.contrib import admin

from .models import Message
from .models import *

# Register your models here.


admin.site.register(Service)
admin.site.register(Message)
