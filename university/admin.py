from pyexpat import model
from django.contrib import admin

from .models import Uni


class UniAdmin(admin.ModelAdmin):

    list_display=["department", "name", "point_type", "min_point" ]
    list_display_links = ["department"]

    list_filter = ["department",  'name']

    search_fields = ["department", "name"]

    list_editable = []

    class Meta:
        model = Uni



admin.site.register(Uni, UniAdmin)