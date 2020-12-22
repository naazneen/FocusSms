from django.contrib import admin

# Register your models here.
from django.contrib import admin
from django.contrib.auth.models import Group
# Register your models here.
from .models import Patient
from import_export.admin import ImportExportModelAdmin

admin.site.unregister(Group)


class PatientAdmin(ImportExportModelAdmin):
    list_display_links = ('firstname',)
    list_display = ('firstname', 'lastname','gender', 'date_of_birth', 'email', 'phone_number')
    #list_editable = ('email',)
    list_filter = ('gender',)
    search_fields = ('firstname', 'lastname','gender', 'date_of_birth', 'email', 'phone_number')


admin.site.register(Patient, PatientAdmin)
