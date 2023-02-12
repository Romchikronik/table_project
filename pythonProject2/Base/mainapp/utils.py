from django.core.paginator import Paginator
from datetime import timedelta
from django.utils import timezone
# from django.contrib.auth.models import Group, Permission
# from django.contrib.contenttypes.models import ContentType
# from django.contrib.auth.models import User

from .models import *

projects_department = [
    {'table_name': 'Илова-4.1', 'url_form': 'form_loiha4.1', 'url_data_table': 'table_loiha4.1'},
    {'table_name': 'Илова-5.2', 'url_form': 'form_loiha5.2', 'url_data_table': 'table_loiha5.2'},
    {'table_name': 'Илова-14', 'url_form': 'form_loiha14', 'url_data_table': 'table_loiha14'},
    {'table_name': 'Илова-13.1', 'url_form': 'form_loiha13.1', 'url_data_table': 'table_loiha13.1'},
    {'table_name': 'Илова-12.2', 'url_form': 'form_loiha12.2', 'url_data_table': 'table_loiha12.2'},
    {'table_name': 'Илова-12.1', 'url_form': 'form_loiha12.1', 'url_data_table': 'table_loiha12.1'},
    {'table_name': 'Илова-12', 'url_form': 'form_loiha12', 'url_data_table': 'table_loiha12'},
    {'table_name': 'Илова-10', 'url_form': 'form_loiha10', 'url_data_table': 'table_loiha10'},
    {'table_name': 'Илова-6', 'url_form': 'form_loiha6', 'url_data_table': 'table_loiha6'},
    {'table_name': 'Илова-13', 'url_form': 'form_loiha13', 'url_data_table': 'table_loiha13'},
]

# url Таблиц и форм отдела-2
second_department_tables_menu = [
    {'table_name': 'Sanoat', 'url_form': 'form_sanoat', 'url_data_table': 'table_sanoat'},
    {'table_name': 'KX', 'url_form': 'form_kx', 'url_data_table': 'table_kx'},
    {'table_name': 'Таблица 1', 'url_form': 'form_first_table', 'url_data_table': 'table_first'},
    {'table_name': 'кунлиу', 'url_form': 'form_kunliu', 'url_data_table': 'table_kunliu'},
]
# url Таблиц и форм отдела 3
third_department_tables_menu = [
    {'table_name': 'Жами свод', 'url_form': 'form_jami', 'url_data_table': 'table_jami'},
    {'table_name': 'Cвод чорак', 'url_form': 'form_quarter', 'url_data_table': 'table_quarter'},
    {'table_name': 'Cвод ойлар', 'url_form': 'form_monthly', 'url_data_table': 'table_monthly'},
    {'table_name': 'Cвод банк', 'url_form': 'form_bank', 'url_data_table': 'table_bank'},
    {'table_name': 'Cвод режа', 'url_form': 'form_reja', 'url_data_table': 'table_reja'},
    {'table_name': 'Cвод тармок', 'url_form': 'form_tarmok', 'url_data_table': 'table_tarmok'},
]
# url Таблиц и форм отдела 4
fourth_department_tables_menu = [
    {'table_name': 'Отдел-4.1', },
    {'table_name': 'Отдел-4.1', },
    {'table_name': 'Отдел-4.1', },
    {'table_name': 'Отдел-4.1', }
]
# url Таблиц и форм отдела 5
fifth_department_tables_menu = [
    {'table_name': 'Отдел-5.1', },
    {'table_name': 'Отдел-5.1', },
    {'table_name': 'Отдел-5.1', },
    {'table_name': 'Отдел-5.1', }
]


loiha_models = {
    'loiha41': Loiha41,
    'loiha52': Loiha52,
    'loiha14': Loiha14,
    'loiha131': Loiha131,
    'loiha122': Loiha122,
    'loiha121': Loiha121,
    'loiha12': Loiha12,
    'loiha10': Loiha10,
    'loiha6': Loiha6,
    'loiha13': Loiha13,
    # Add other models here
}

second_department_models_dict = {
    'sanoat': Sanoat,
    'kx': KH,
    'table_1': FirstTable,
    'kunliu': Kunliu,
}

third_department_models_dict = {
    'jami': JamiVault,
    'quarter': QuarterVault,
    'monthly': MonthVault,
    'bank': BankVault,
    'reja': RejaVault,
    'tarmok': TarmokVault,
}


projects_department_models = [
    Loiha41,
    Loiha52,
    Loiha6,
    Loiha10,
    Loiha12,
    Loiha121,
    Loiha122,
    Loiha13,
    Loiha131,
    Loiha14
]
# templates
src = {
    'login': 'mainapp/login.html',
    'loiha41': 'mainapp/data_table/table_Loiha41.html',
    'loiha52': 'mainapp/data_table/table_Loiha52.html',
    'loiha6': 'mainapp/data_table/table_Loiha6.html',
    'loiha10': 'mainapp/data_table/table_Loiha10.html',
    'loiha12': 'mainapp/data_table/table_Loiha12.html',
    'loiha121': 'mainapp/data_table/table_Loiha121.html',
    'loiha122': 'mainapp/data_table/table_Loiha122.html',
    'loiha13': 'mainapp/data_table/table_Loiha13.html',
    'loiha131': 'mainapp/data_table/table_Loiha131.html',
    'loiha14': 'mainapp/data_table/table_Loiha14.html',
    'sanoat': 'mainapp/data_table/second_departament/sanoat.html',
    'kx': 'mainapp/data_table/second_departament/kh.html',
    'table_1': 'mainapp/data_table/second_departament/first_table.html',
    'kunliu': 'mainapp/data_table/second_departament/kunliu.html',
    'jami': 'mainapp/data_table/third_departament/table_jami.html',
    'quarter': 'mainapp/data_table/third_departament/quarter.html',
    'monthly': 'mainapp/data_table/third_departament/month.html',
    'bank': 'mainapp/data_table/third_departament/bank.html',
    'reja': 'mainapp/data_table/third_departament/reja.html',
    'tarmok': 'mainapp/data_table/third_departament/tarmok.html',
}

# список моделей отдела -2
second_department_models = [
    Sanoat,
    KH,
    FirstTable,
    Kunliu
]
# список моделей отдела -3
third_department_models = [
    JamiVault,
    QuarterVault,
    MonthVault,
    BankVault,
    RejaVault,
    TarmokVault
]
# список моделей отдела -4
fourth_department_models = []
# список моделей отдела -5
fifth_department_models = []


def show_data_table(request, model):
    model = model.objects.filter(district=request.user.district)
    return model


def show_data_table_to_departament(model):
    model = model.objects.all()
    return model


def create_data(request, model, form):
    model = model.objects.create(**form.cleaned_data, district=request.user.district)
    return model


def get_context_data(page_obj, title, menu, table_data):
    context = {
        'page_obj': page_obj,
        'title': title,
        'projects_department': menu,
        'table_data': table_data
    }
    return context


# def get_context(*args, **kwargs):
#     args = list(args)
#     context = {str(arg): arg for arg in args}
#     return {**context, **kwargs}

# Group id

def get_group_loiha_id(request):
    return request.user.groups.filter(id=3).exists() and request.user.groups.filter(id=1)


def del_group_loiha_id(request):
    return request.user.groups.filter(id=3).exists() and not request.user.groups.filter(id=1)


def get_group_export_id(request):
    return request.user.groups.filter(id=3).exists() and request.user.groups.filter(id=2)


def del_group_export_id(request):
    return request.user.groups.filter(id=3).exists() and not request.user.groups.filter(id=2)


def get_group_vault_id(request):
    return request.user.groups.filter(id=3).exists() and request.user.groups.filter(id=4)


def del_group_vault_id(request):
    return request.user.groups.filter(id=3).exists() and not request.user.groups.filter(id=4)


def make_context_by_form(data, form, menu, page_obj):
    context = {
        'title': data,
        'form': form,
        'projects_department': menu,
        'page_obj': page_obj
    }
    return context


def paginate_page(request, table_data):
    paginator = Paginator(table_data, 3)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return page_obj


def filter_tables(filter_slug, table_p):
    if filter_slug == 'week':
        now = timezone.now() - timedelta(minutes=60 * 24 * 7)
        table = table_p.filter(time_create__gte=now)
    elif filter_slug == 'month':
        now = timezone.now() - timedelta(minutes=60 * 24 * 30)
        table = table_p.filter(time_create__gte=now)

    return table




