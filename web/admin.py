from django.contrib import admin
from web.models import Category


class CategoryAdmin(admin.ModelAdmin):
    model = Category

    list_display = ('name', 'url', 'get_full_url')
    readonly_fields = ('get_full_url', )

    def get_queryset(self, request):
        return self.model.objects.all()


admin.site.register(Category, CategoryAdmin)
