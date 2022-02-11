from django.contrib import admin, messages
from django.utils.safestring import mark_safe

from store.models import History


@admin.register(History)
class HistoryAdmin(admin.ModelAdmin):
    actions = ['do_calc']
    readonly_fields = ['enter_to_polygon', 'can_ship_to_store', 'parse_coordinates']
    list_display = [
        'store', 'cargo',
        'tipper_number', 'tipper_model', 'max_mass', 'current_mass',
        'has_overload', 'overload', 'coordinates',
        'enter_to_polygon',
        'characteristics',
    ]
    list_editable = ['coordinates']
    list_display_links = ['store', 'cargo']
    list_filter = ['store', 'cargo', 'created']

    def tipper_number(self, instance):
        if instance.cargo.tipper:
            return instance.cargo.tipper.number
    tipper_number.short_description = 'Бортовой номер'

    def tipper_model(self, instance):
        if instance.cargo.tipper and instance.cargo.tipper.tmodel:
            return instance.cargo.tipper.tmodel.code
    tipper_model.short_description = 'Модель'

    def max_mass(self, instance):
        return instance.cargo.max_mass
    max_mass.short_description = 'Макс.груз'

    def current_mass(self, instance):
        return instance.cargo.mass
    current_mass.short_description = 'Текущий вес'

    def has_overload(self, instance):
        if instance.cargo:
            return instance.cargo.has_overload
    has_overload.boolean = True
    has_overload.short_description = 'Перегруз'

    def overload(self, instance):
        return '{} %'.format(instance.cargo.overload)
    overload.short_description = '%'

    def characteristics(self, instance):
        return 'SiO2: {} %, Fe: {} %'.format(instance.cargo.sio2, instance.cargo.fe)
    characteristics.short_description = 'Хар-ки'

    def enter_to_polygon(self, instance):
        return instance.enter_to_polygon
    enter_to_polygon.boolean = True
    enter_to_polygon.short_description = '!'

    # actions

    def do_calc(self, request, queryset):
        for q in queryset:
            if q.can_ship_to_store:
                calc = q.calc()

                html = mark_safe('''
                <i>Груз {cargo} успешно может быть доставлен на склад!</i><br>
                Название склада: <b>{store}</b><br> 
                Объем до разгрузки, т: <b>{current_mass}</b><br>
                Объем после разгрузки, т: <b>{new_mass}</b><br>
                Качественные характеристики после разгрузки: <b>{after_characteristics}</b>
                <small>{before_characteristics}</small>'''.format(
                    cargo=q.cargo,
                    store=calc.get('store', ''),
                    current_mass=calc.get('before_mass', ''),
                    new_mass=calc.get('after_mass', ''),
                    after_characteristics=calc.get('after_characteristics', ''),
                    before_characteristics=calc.get('before_characteristics', '')
                ))
                messages.success(request, html)
            else:
                html = mark_safe('''
                <i>Груз {cargo} не может быть доставлен на склад!</i><br>
                Название склада: <b>{store}</b><br>
                Полигон склада: {polygon}<br>
                Координаты: {coordinates}'''.format(
                    cargo=q.cargo,
                    store=q.store.title,
                    polygon=q.store.parse_polygon,
                    coordinates=q.coordinates,
                ))
                messages.warning(request, html)
    do_calc.short_description = 'Расчитать и показать результат'
