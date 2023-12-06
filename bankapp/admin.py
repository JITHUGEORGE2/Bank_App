# from django.contrib import admin
# from .models import PersonalInformation, District, Branch

# class PersonalInformationAdmin(admin.ModelAdmin):
#     list_display = ('name', 'dob', 'age', 'gender', 'phone', 'email', 'district', 'branch', 'account_type')
#     search_fields = ('name', 'email')
#     list_filter = ('gender', 'district', 'branch', 'account_type')
#     ordering = ('name',)

#     def formfield_for_foreignkey(self, db_field, request, **kwargs):
#         if db_field.name == 'district':
#             kwargs['queryset'] = District.objects.all()
#         elif db_field.name == 'branch':
#             kwargs['queryset'] = Branch.objects.all()
#         return super().formfield_for_foreignkey(db_field, request, **kwargs)

# admin.site.register(PersonalInformation, PersonalInformationAdmin)
# admin.site.register(District)
# admin.site.register(Branch)
from django.contrib import admin
from .models import PersonalInformation, District, Branch

class PersonalInformationAdmin(admin.ModelAdmin):
    list_display = ('name', 'dob', 'age', 'gender', 'phone', 'email', 'district', 'branch', 'account_type')
    search_fields = ('name', 'email')
    list_filter = ('gender', 'district', 'branch', 'account_type')
    ordering = ('name',)

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'district':
            kwargs['queryset'] = District.objects.all()
        elif db_field.name == 'branch':
            # Check if this is an add form or change form
            if request.resolver_match.url_name == 'add':
                # For add form, display all branches
                kwargs['queryset'] = Branch.objects.all()
            elif request.resolver_match.url_name == 'change':
                # For change form, filter branches based on the selected district
                selected_district_id = request.POST.get('district') or self.model.objects.get(pk=request.resolver_match.kwargs['object_id']).district_id
                kwargs['queryset'] = Branch.objects.filter(district_id=selected_district_id)
            else:
                kwargs['queryset'] = Branch.objects.none()
        return super().formfield_for_foreignkey(db_field, request, **kwargs)

admin.site.register(PersonalInformation, PersonalInformationAdmin)
admin.site.register(District)
admin.site.register(Branch)
