from django import template
from django.utils.safestring import mark_safe

from mainapp.models import SportCars


register = template.Library()


TABLE_HEAD = """
                <table class="table">
                  <tbody>
             """

TABLE_TAIL = """
                  </tbody>
                </table>
             """

TABLE_CONTENT = """
                    <tr>
                      <td>{name}</td>
                      <td>{value}</td>
                    </tr>
                """

PRODUCT_SPEC = {
    'fclasssedans': {
        'Длинна автомобиля': 'lenght_car',
        'Производитель': 'car_brend',
        'Мощность двигателя': 'hs_power',
        'Крутящий момент двигателя': 'n_power',
        'Расход топлива': 'fuel_consumption'
    },
    'sportcars': {
        'Производитель': 'car_brend',
        'Мощность двигателя': 'hs_power',
        'Крутящий момент двигателя': 'n_power',
        'Разгон 0-100': 'zero_hundred',
        'Вес автомобиля': 'weight',
        'Максимальная скорость': 'max_speed'
    }
}


def get_product_spec(product, model_name):
    table_content = ''
    for name, value in PRODUCT_SPEC[model_name].items():
        table_content += TABLE_CONTENT.format(name=name, value=getattr(product, value))
    return table_content


@register.filter
def product_spec(product):
    model_name = product.__class__._meta.model_name
    if isinstance(product, SportCars):
        if not product.sd:
            PRODUCT_SPEC['sportcars'].pop('Максимальная скорость', None)
        else:
            PRODUCT_SPEC['sportcars']['Максимальная скорость'] = 'max_speed'
    return mark_safe(TABLE_HEAD + get_product_spec(product, model_name) + TABLE_TAIL)

