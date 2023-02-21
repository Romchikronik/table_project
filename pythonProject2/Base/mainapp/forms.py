from django.forms import ModelForm
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
        fields = '__all__'
        exclude = ['district', 'is_published']


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


class TableTarmokForm(ModelForm):
    class Meta:
        model = TarmokVault
        fields = '__all__'
        exclude = ['district', 'is_published']


class TableManzilForm(ModelForm):
    class Meta:
        model = Manzil
        fields = '__all__'
        exclude = ['district', 'is_published']
