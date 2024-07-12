from django.contrib import admin

# Register your models here.
from form_en.models import form_enquirys
class formadmin(admin.ModelAdmin):
    lisst=('full_name', 'email', 'job_role', 'address', 'city', 'pincode')
    
admin.site.register(form_enquirys, formadmin)