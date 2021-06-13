from django.forms import ModelChoiceField, ModelForm
from django.contrib import admin

from .models import *


class SportCarsAdminForm(ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        instance = kwargs.get('instance')
        if instance and not instance.sd:
            self.fields['max_speed'].widget.attrs.update({
                'readonly': True, 'style': 'background: lightgray;'
            })


    def clean(self):
        if not self.cleaned_data['max_speed']:
            self.cleaned_data['max_speed'] = None
        return self.cleaned_data


class FClassSedansAdmin(admin.ModelAdmin):

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='fclasssedans'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class SportCarsAdmin(admin.ModelAdmin):

    change_form_template = 'admin.html'
    form = SportCarsAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='sportcars'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(FClassSedans, FClassSedansAdmin)
admin.site.register(SportCars, SportCarsAdmin)
admin.site.register(CartProduct)
admin.site.register(Cart)
admin.site.register(Customer)
admin.site.register(Order)
