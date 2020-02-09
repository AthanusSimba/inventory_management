from django.contrib import admin
from .models import Desktop, Laptop, Mobile
from import_export.admin import ImportExportModelAdmin

# Register your models here.
'''admin.site.register(Desktop)
admin.site.register(Laptop)
admin.site.register(Mobile)'''


@admin.register(Desktop, Laptop, Mobile)
class ViewAdmin(ImportExportModelAdmin):
    pass
