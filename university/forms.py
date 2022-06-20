from django.forms import ModelForm
from .models import Uni

class UniversityForm(ModelForm):
    class Meta:
        model = Uni
        fields =(
            'kod',
            'type',
            'name',
            'faculty',
            'department',
            'point_type',
            'quota',
            'accepted',
            'min_point',
            'max_point'
        )