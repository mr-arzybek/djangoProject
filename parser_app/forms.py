from django import forms
from . import models, parser


class ParserForm(forms.Form):
    MEDIA_CHOISCES = (
        ('cars.kg', 'cars.kg'),
    )
    media_type = forms.ChoiceField(choices=MEDIA_CHOISCES)



    class Meta:
        fields = [
            'media_type',
        ]

    def parser_data(self):
        if self.data['media_type'] == 'cars.kg':
            film_parser = parser.parser()
            for i in film_parser:
                models.FilmsKg.objects.create(**i)
