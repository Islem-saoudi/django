from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User
from .models import Clients



class ClientInline(admin.StackedInline):
    model = Clients
    can_delete = False
    verbose_name_plural = 'Clients'
    fk_name = 'user'

class ClientUserAdmin(UserAdmin):
    inlines = (ClientInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(ClientUserAdmin, self).get_inline_instances(request, obj)


admin.site.unregister(User)
admin.site.register(User, ClientUserAdmin)