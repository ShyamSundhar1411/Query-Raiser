from . models import Query,Profile,Department
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources

class DepartmentResource(resources.ModelResource):

    class Meta:
        model = Department
class DepartmentAdmin(ImportExportModelAdmin):
    resource_class = DepartmentResource

# Register your models here.
admin.site.register(Query)
admin.site.register(Profile)
admin.site.register(Department,DepartmentAdmin)