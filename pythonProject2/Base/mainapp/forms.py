from django.core.exceptions import ValidationError
from django.forms import ModelForm, Select, ChoiceField
from .models import *


class TableFormLoiha41(ModelForm):
    class Meta:
        model = Loiha41
        fields = '__all__'
        exclude = ['district', 'is_published']


class TableFormLoiha52(ModelForm):
    class Meta:
        model = Loiha52
        fields = '__all__'
        exclude = ['district', 'is_published']


class TableFormLoiha14(ModelForm):
    class Meta:
        model = Loiha14
        fields = '__all__'
        exclude = ['district', 'is_published']


class TableFormLoiha131(ModelForm):
    class Meta:
        model = Loiha131
        fields = '__all__'
        exclude = ['district', 'is_published']


class TableFormLoiha122(ModelForm):
    class Meta:
        model = Loiha122
        fields = '__all__'
        exclude = ['district', 'is_published']


class TableFormLoiha121(ModelForm):
    class Meta:
        model = Loiha121
        fields = '__all__'
        exclude = ['district', 'is_published']


class TableFormLoiha12(ModelForm):
    class Meta:
        model = Loiha12
        fields = '__all__'
        exclude = ['district', 'is_published']


class TableFormLoiha10(ModelForm):
    class Meta:
        model = Loiha10
        fields = '__all__'
        exclude = ['district', 'is_published']


class TableFormLoiha6(ModelForm):
    class Meta:
        model = Loiha6
        fields = '__all__'
        exclude = ['district', 'is_published']


class TableFormLoiha13(ModelForm):
    class Meta:
        model = Loiha13
        fields = '__all__'
        exclude = ['district', 'is_published']


class TableFormSanoat(ModelForm):
    class Meta:
        model = Sanoat
        fields = '__all__'
        exclude = ['district', 'is_published']


class TableFormKX(ModelForm):
    class Meta:
        model = KH
        fields = '__all__'
        exclude = ['district', 'is_published']


class TableFirstForm(ModelForm):
    class Meta:
        model = FirstTable
        fields = '__all__'
        exclude = ['district', 'is_published']


class TableKunliuForm(ModelForm):
    class Meta:
        model = Kunliu
        fields = [
            'date_of_forecast',
            'overall',
            'sanoat',
            'meva_sabz',
        ]


class TableJamiForm(ModelForm):
    class Meta:
        model = JamiVault
        fields = '__all__'
        exclude = ['district', 'is_published']


class TableQuarterForm(ModelForm):
    class Meta:
        model = QuarterVault
        fields = '__all__'
        exclude = ['district', 'is_published']


class TableMonthForm(ModelForm):
    class Meta:
        model = MonthVault
        fields = '__all__'
        exclude = ['district', 'is_published']


class TableBankForm(ModelForm):
    class Meta:
        model = BankVault
        fields = '__all__'
        exclude = ['district', 'is_published']


class TableRejaForm(ModelForm):
    class Meta:
        model = RejaVault
        fields = '__all__'
        exclude = ['district', 'is_published']


class CustomChoiceField(ChoiceField):
    def __init__(self, choices, **kwargs):
        super().__init__(choices=choices, **kwargs)

    def to_python(self, value):
        # Override to_python to return the display value instead of the key
        if value in self.empty_values:
            return None
        for key, display in self.choices:
            if key == value:
                return display
        raise ValidationError(
            self.error_messages['invalid_choice'], code='invalid_choice',
            params={'value': value},
        )


class CustomSelect(Select):
    def __init__(self, *args, **kwargs):
        self.choices = kwargs.pop('choices', [])
        super().__init__(*args, **kwargs)

    def create_option(self, *args, **kwargs):
        option = super().create_option(*args, **kwargs)
        for opt in option:
            if opt['value']:
                opt['display_name'] = dict(self.choices).get(int(opt['value']))
        return option


class TableTarmokForm(ModelForm):
    # category = CustomChoiceField(choices=CATEGORY_CHOICES, widget=CustomSelect)
    # industry = CustomChoiceField(choices=INDUSTRY_CHOICES, widget=CustomSelect)
    class Meta:
        model = TarmokVault
        fields = '__all__'
        exclude = ['district', 'is_published']  # , 'category'
        # widgets = {
        #     'category': Select(choices=CATEGORY_CHOICES)
        # }
    category = CustomChoiceField(choices=CATEGORY_CHOICES, widget=Select(choices=CATEGORY_CHOICES))
    industry = CustomChoiceField(choices=INDUSTRY_CHOICES, widget=Select(choices=INDUSTRY_CHOICES))

    # category = ChoiceField(choices=CATEGORY_CHOICES)


class TableManzilForm(ModelForm):
    class Meta:
        model = Manzil
        fields = '__all__'
        exclude = ['district', 'is_published']


class TableSubtotalsForm(ModelForm):
    class Meta:
        model = Subtotals
        fields = '__all__'
        exclude = ['district', 'is_published']


class TableAddressedForm(ModelForm):
    class Meta:
        model = Addressed
        fields = '__all__'
        exclude = ['district', 'is_published']


class TableNetworkAdministrationsForm(ModelForm):
    class Meta:
        model = NetworkAdministrations
        fields = '__all__'
        exclude = ['district', 'is_published']


class TableTotalCleaningForm(ModelForm):
    class Meta:
        model = TotalCleaning
        fields = '__all__'
        exclude = ['district', 'is_published']


class TableTotalCleaningNetworkForm(ModelForm):
    class Meta:
        model = TotalCleaningNetwork
        fields = '__all__'
        exclude = ['district', 'is_published']


class TableTotalDoneForm(ModelForm):
    class Meta:
        model = TotalDone
        fields = '__all__'
        exclude = ['district', 'is_published']


class TableTotalCompletedNetworkForm(ModelForm):
    class Meta:
        model = TotalCompletedNetwork
        fields = '__all__'
        exclude = ['district', 'is_published']


class TableTotalProblemForm(ModelForm):
    class Meta:
        model = TotalProblem
        fields = '__all__'
        exclude = ['district', 'is_published']


class TablePerformanceIsAddressedForm(ModelForm):
    class Meta:
        model = PerformanceIsAddressed
        fields = '__all__'
        exclude = ['district', 'is_published']