import django_tables2 as tables
from .models import *
from django_tables2.utils import A


class NumberFormatColumn(tables.Column):
    def render(self, value, record):
        value = ( record.atrribute)
        return value.attribute


class AccessoryTable(tables.Table):
    ### edit column to link to an edit form. The form needs to load the accessory as an instance
    # edit = tables.LinkColumn('accessory_update', text='Edit', args=[A('pk')], orderable=False, empty_values=(), attrs={'td':{"class": "btn"}})
    voltage = tables.Column(accessor = 'accessory.draw_voltage')
    amperage = tables.Column(accessor = 'accessory.draw_amperage')
    watts = tables.Column(accessor = 'accessory.draw_watts')
    is_Ac = tables.Column(accessor = 'accessory.is_Ac')
    selection = tables.CheckBoxColumn(accessor='pk', orderable = True) # allow the removal of an accessory

    class Meta:
        model = LoadAccessory
        template_name = 'django_tables2/bootstrap-responsive.html'
        fields = ['accessory', 'estimated_usage', 'quantity']
