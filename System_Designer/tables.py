import django_tables2 as tables
from .models import *
from django_tables2.utils import A

def test(value):
    cell_value = value
    return cell_value

def test2(record):

    return record['count']

class TestColumn(tables.Column):
    attrs={'th': {'id': 'anotherTest'}, 'td':{'class': 'allTesting'}}
    def render(self, value, record):
        value = ( record.atrribute)
        return value.attribute


class AccessoryTable(tables.Table):
    ### edit column to link to an edit form. The form needs to load the accessory as an instance
    # edit = tables.LinkColumn('accessory_update', text='Edit', args=[A('pk')], orderable=False, empty_values=(), attrs={'td':{"class": "btn"}})
    voltage = tables.Column(accessor = 'accessory.draw_voltage', attrs={'th':{'class': 'allTesting'} , 'td':{'id': lambda value: test(value)}})#lambda value: test(value)}})
    amperage = tables.Column(accessor = 'accessory.draw_amperage')
    watts = tables.Column(accessor = 'accessory.draw_watts')
    is_Ac = tables.Column(accessor = 'accessory.is_Ac')
    remove = tables.LinkColumn('remove_accesory', text='Remove', args=[A('pk')], orderable=False, empty_values=(), attrs={'td':{"class": "btn"}})

    class Meta:
        model = LoadAccessory
        template_name = 'django_tables2/bootstrap-responsive.html'
        fields = ['accessory', 'estimated_usage', 'quantity']
        # table elements
        # attrs={'id': 'Super Test', 'class': 'Test'}
        # table body tr elements
        row_attrs = {'class':'test'}


class BatteryCountTable(tables.Table):
    """
    Table columns are dynmanically created in view based on model function output.
    """
    class Meta:
        template_name = 'django_tables2/bootstrap-responsive.html'
        # table element
        # attrs={'id': 'Super Test', 'class': 'Test', 'th': {'class': 'littleTest'}}
        # table body tr elements
        row_attrs = {'class':'test', 'id': lambda record: test2(record)}
