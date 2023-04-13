from django import template

from web.models import Category

register = template.Library()


@register.inclusion_tag('categories.html', takes_context=True)
def draw_menu(context, id=None, open_cats=None):
    path_list = []
    try:
        path = context['request'].path
        if path != '/':
            path_list = path.split('/')[1:]
    except:
        pass
    if id is None:
        cats = Category.tops.all()
    else:
        cats = Category.objects.filter(id=id)
    dct = {'cats': cats}
    if path_list:
        dct['open_cats'] = path_list
    elif open_cats:
        dct['open_cats'] = open_cats
    return dct
