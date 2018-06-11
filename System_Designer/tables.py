import django_tables2 as tables
from .models import *
from django_tables2.utils import A

# def test(value):
#     if value <1:
#         return "table-grad-green-1"
#     elif value < 2:
#         return "table-grad-green-2"
#     elif value < 3:
#         return "table-grad-green-3"
#     elif value < 4:
#         return "table-grad-green-4"
#     elif value < 5:
#         return "table-grad-green-5"
#     elif value < 6:
#         return "table-grad-green-6"
#     elif value < 7:
#         return "table-grad-green-7"
#     elif value < 8:
#         return "table-grad-green-8"
#     elif value < 9:
#         return "table-grad-green-9"
#     else:
#         return "table-grad-green-10"


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
    remove = tables.LinkColumn('remove_accesory', text='Remove', args=[A('pk')], orderable=False, empty_values=(), attrs={'td':{"class": "btn"}})

    class Meta:
        model = LoadAccessory
        template_name = 'django_tables2/bootstrap-responsive.html'
        fields = ['accessory', 'estimated_usage', 'quantity']


class BatteryCountTable(tables.Table):
    """
    Table columns are dynmanically created in view based on model function output.
    """
    class Meta:
        template_name = 'django_tables2/bootstrap-responsive.html'
#        attrs={'class': ''}
