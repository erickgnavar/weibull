from django import forms
# from crispy_forms.helper import FormHelper


class WeibullForm(forms.Form):

    TYPE_CHOICES = (
        ('DENSITY', 'Probabilidad de Densidad'),
        ('UPPER_CUMULATIVE', 'Distribucion Acumulada Superior'),
        ('LOWER_CUMULATIVE', 'Distribucion Acumulada Inferior')
    )

    function = forms.ChoiceField(
        label='Seleccione funcion',
        choices=TYPE_CHOICES,
        widget=forms.RadioSelect(),
    )
    alpha = forms.FloatField(
        label='Alfa'
    )
    beta = forms.FloatField(
        label='Beta'
    )
    increment = forms.FloatField(
        label='Incremento'
    )
    initial = forms.FloatField(
        label='Percentil Inicial'
    )
    repetitions = forms.IntegerField(
        label='Repeticiones'
    )

    # def __init__(self, *args, **kwargs):
    #     self.helper = FormHelper()
    #     self.helper.form_show_errors = True
    #     self.helper.form_tag = False
    #     super(WeibullForm, self).__init__(*args, **kwargs)
