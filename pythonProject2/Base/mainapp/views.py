import xlwt

# import xlsxwriter
# from djqscsv import write_csv, render_to_csv_response
from datetime import datetime, timedelta
from django.utils import timezone

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout, get_user
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, response
from django.shortcuts import render, redirect

from .forms import *
from .utils import *


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # try:
        #     User.objects.get(usernama=username)
        # except:
        #     messages.error(request, 'Попробуйте снова!')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('main')
        else:
            messages.error(request, 'Имя пользователя или пароль не существует')
    context = {'title': 'Авторизация'}
    return render(request, 'mainapp/login.html', context)


@login_required
def mainPage(request):
    context = {'title': 'Главная старница'}
    return render(request, 'mainapp/index.html', context)


# def departament_view(request):
#     user = User
# request.user.has_perm('mainapp.departament_group'):
#     if user.groups.filter(name='department_group').exists():

# if user in


@login_required
def get_department_projects(request):
    if del_group_loiha_id(request):
        # raise Exception('У вас нету доступа к этому департаменту')
        messages.error(request, 'У вас нету доступа к этому департаменту')
        return redirect('/')
    else:
        context = {
            'title': 'Отдел - Лоиха',
            'projects_department': projects_department
        }
        return render(request, 'mainapp/departments/projects_department.html', context)


@login_required
def get_department_exports(request):
    if del_group_export_id(request):
        # raise Exception('У вас нету доступа к этому департаменту')
        messages.error(request, 'У вас нету доступа к этому департаменту')
        return redirect('/')
    else:
        context = {
            'title': 'Отдел - 2',
            'second_department_tables_menu': second_department_tables_menu
        }
        return render(request, 'mainapp/departments/exports_department.html', context)


@login_required
def get_department_3(request):
    if del_group_vault_id(request):
        # raise Exception('У вас нету доступа к этому департаменту')
        messages.error(request, 'У вас нету доступа к этому департаменту')
        return redirect('/')
    else:
        context = {
            'title': 'Отдел - 3',
            'third_department_tables_menu': third_department_tables_menu
        }
        return render(request, 'mainapp/departments/department_3.html', context)


@login_required
def get_department_4(request):
    context = {
        'title': 'Отдел - 4',
        'fourth_department_tables_menu': fourth_department_tables_menu
    }
    return render(request, 'mainapp/departments/department_4.html', context)


@login_required
def get_department_5(request):
    context = {
        'title': 'Отдел - 5',
        'fifth_department_tables_menu': fifth_department_tables_menu
    }
    return render(request, 'mainapp/departments/department_5.html', context)



def export_excel(request, filter_slug):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=table' + \
                                      str(datetime.now()) + '.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('table', cell_overwrite_ok=True)
    row_num = 2  # с какой строки начинается наша таблица
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    cell_style = xlwt.easyxf("font: bold on; align: vert center, horiz center")
    cell_title = xlwt.easyxf("font: bold on, height 280; align: vert center, horiz left")
    # cell_style = xlwt.easyxf("align: vert centre, horiz center")

    # ws.title = 'Илова-4.1' Поменять на один если добавлять столбик в начале
    if not get_group_loiha_id(request):
        ws.write_merge(0, 0, 0, 25, 'Чирчик тумани, Илова-4.1', cell_title)
        ws.write_merge(1, 1, 0, 3, 'SANOAT', cell_style)
        ws.write_merge(1, 1, 4, 7, 'QISHLOQ', cell_style)
        ws.write_merge(1, 1, 8, 11, 'QURILISH', cell_style)
        ws.write_merge(1, 1, 12, 15, 'XIZMATLAR', cell_style)
        ws.write_merge(1, 1, 16, 19, 'CHAKANA SAVDO', cell_style)
        ws.write_merge(1, 1, 20, 21, 'TASHQI SAVDO AYLANMASI', cell_style)
        ws.write_merge(1, 1, 22, 23, 'EKSPORT', cell_style)
        ws.write_merge(1, 1, 24, 25, 'IMPORT', cell_style)
    else:
        ws.write_merge(0, 0, 0, 26, 'Илова-4.1', cell_title)
        # ws.write_merge(1, 2, 0, 1, 'Район', cell_style)
        ws.write_merge(1, 1, 1, 4, 'SANOAT', cell_style)
        ws.write_merge(1, 1, 5, 8, 'QISHLOQ', cell_style)
        ws.write_merge(1, 1, 9, 12, 'QURILISH', cell_style)
        ws.write_merge(1, 1, 13, 16, 'XIZMATLAR', cell_style)
        ws.write_merge(1, 1, 17, 20, 'CHAKANA SAVDO', cell_style)
        ws.write_merge(1, 1, 21, 22, 'TASHQI SAVDO AYLANMASI', cell_style)
        ws.write_merge(1, 1, 23, 24, 'EKSPORT', cell_style)
        ws.write_merge(1, 1, 25, 26, 'IMPORT', cell_style)

    # ws.col(0).width = 4500
    # ws.col(21).width = 5000

    # "Район",
    columns_list = ["mlrd. so'm",
                    "o'shish sur'ti %",
                    "prognoz",
                    "farqi (-;+)",
                    "mlrd. so'm",
                    "o'shish sur'ti %",
                    "prognoz",
                    "farqi (-;+)",
                    "mlrd. so'm",
                    "o'shish sur'ti%",
                    "prognoz",
                    "farqi (-;+)",
                    "mlrd. so'm",
                    "o'shish sur'ti%",
                    "prognoz",
                    "farqi (-;+)",
                    "mlrd. so'm",
                    "o'shish sur'ti%",
                    "prognoz",
                    "farqi (-;+)",
                    "ming. AQSh doll",
                    "o'shish sur'ti%",
                    "ming. AQSh doll",
                    "o'shish sur'ti%",
                    "ming. AQSh doll",
                    "o'shish sur'ti%"
                    ]

    if not get_group_loiha_id(request):
        columns = [
            *columns_list
        ]
    else:
        columns = [
            "Район",
            *columns_list
        ]

    for col_num in range(len(columns)):
        ws.col(col_num).width = 3800
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    # date_style = xlwt.XFStyle()
    # time_create = datetime.strftime('time_create', '%d/%m/%y %h:%m:%s')
    fields = [
        # 'district__district',
        'bill_sum_industry',
        'picture_of_growth_industry',
        'forecast_industry',
        'difference_industry',
        'bill_sum_locality',
        'picture_of_growth_locality',
        'forecast_locality',
        'difference_locality',
        'bill_sum_construction',
        'picture_of_growth_construction',
        'forecast_construction',
        'difference_construction',
        'bill_sum_services',
        'picture_of_growth_services',
        'forecast_services',
        'difference_services',
        'bill_sum_retail',
        'picture_of_growth_retail',
        'forecast_retail',
        'difference_retail',
        'thousand_dollar_international_trade',
        'picture_of_growth_international_trade',
        'thousand_dollar_export',
        'picture_of_growth_export',
        'thousand_dollar_import',
        'picture_of_growth_import',
        # 'time_create'
    ]

    department_fields = [
        'district__district',
        *fields
    ]

    if filter_slug == 'week':
        now = timezone.now() - timedelta(minutes=60 * 24 * 7)
        if not get_group_loiha_id(request):
            rows = show_data_table(request, Loiha41).filter(time_create__gte=now).values_list(*fields)
        else:
            rows = show_data_table_to_departament(Loiha41).filter(time_create__gte=now).values_list(*department_fields)
    elif filter_slug == 'month':
        now = timezone.now() - timedelta(minutes=60 * 24 * 30)
        if not get_group_loiha_id(request):
            rows = show_data_table(request, Loiha41).filter(time_create__gte=now).values_list(*fields)
        else:
            rows = show_data_table_to_departament(Loiha41).filter(time_create__gte=now).values_list(*department_fields)
    else:
        if not get_group_loiha_id(request):
            rows = show_data_table(request, Loiha41).values_list(*fields)
        else:
            rows = show_data_table_to_departament(Loiha41).values_list(*department_fields)

    for row in rows:
        row_num += 1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)
    return response


def export_excel_loiha52(request, filter_slug):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = 'attachment; filename=table' + \
                                      str(datetime.now()) + '.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('table', cell_overwrite_ok=True)
    row_num = 2  # с какой строки начинается наша таблица
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    cell_style = xlwt.easyxf("font: bold on; align: vert center, horiz center")
    cell_title = xlwt.easyxf("font: bold on, height 280; align: vert center, horiz left")
    # cell_style = xlwt.easyxf("align: vert centre, horiz center")

    # ws.title = 'Илова-4.1' Поменять на один если добавлять столбик в начале
    if not get_group_loiha_id(request):
        ws.write_merge(0, 0, 0, 12, 'Чирчик тумани, Илова-5.2', cell_title)
        ws.write_merge(1, 1, 4, 5, 'Состояние запасов на 01.01.2019', cell_style)
        ws.write_merge(1, 1, 6, 7, 'Оперативная информация', cell_style)
    else:
        ws.write_merge(0, 0, 0, 13, 'Илова-5.2', cell_title)
        # ws.write_merge(1, 2, 0, 1, 'Район', cell_style)
        ws.write_merge(1, 1, 5, 6, 'Состояние запасов на 01.01.2019', cell_style)
        ws.write_merge(1, 1, 7, 8, 'Оперативная информация', cell_style)

    # ws.col(0).width = 4500
    # ws.col(21).width = 5000

    # "Район",
    columns_list = ["Название места, где расположены природные ресурсы(Объекты геологоразведки)",
                    "Участки геологических образований",
                    "Наименование месторождений геологических формаций (сырых)",
                    "Единица измерения",
                    "A+B+C1 категории",
                    "С2 категория",
                    "Уровень развития",
                    "Дата и номер лицензии",
                    "Объем добычи в 2017 г.",
                    "Соответствующее министерство и ведомство",
                    "Подтвержденный отчет о запасах и его дата",
                    "Комментарий",
                    ]

    if not get_group_loiha_id(request):
        columns = [
            *columns_list
        ]
    else:
        columns = [
            "Район",
            *columns_list
        ]

    for col_num in range(len(columns)):
        ws.col(col_num).width = 3800
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    # date_style = xlwt.XFStyle()
    # time_create = datetime.strftime('time_create', '%d/%m/%y %h:%m:%s')
    fields = [
        # 'district__district',
        'places_of_exploration',
        'sites_of_geo_formations',
        'name_of_formations',
        'unit',
        'abc_categories',
        'c2_category',
        'lvl_development_operational_information',
        'date_license_operational_information',
        'volume_of_production_2017',
        'ministry_and_department',
        'confirmed_stock_and_date',
        'comment'
        # 'time_create'
    ]

    department_fields = [
        'district__district',
        *fields
    ]

    if filter_slug == 'week':
        now = timezone.now() - timedelta(minutes=60 * 24 * 7)
        if not get_group_loiha_id(request):
            rows = show_data_table(request, Loiha52).filter(time_create__gte=now).values_list(*fields)
        else:
            rows = show_data_table_to_departament(Loiha52).filter(time_create__gte=now).values_list(*department_fields)
    elif filter_slug == 'month':
        now = timezone.now() - timedelta(minutes=60 * 24 * 30)
        if not get_group_loiha_id(request):
            rows = show_data_table(request, Loiha52).filter(time_create__gte=now).values_list(*fields)
        else:
            rows = show_data_table_to_departament(Loiha52).filter(time_create__gte=now).values_list(*department_fields)
    else:
        if not get_group_loiha_id(request):
            rows = show_data_table(request, Loiha52).values_list(*fields)
        else:
            rows = show_data_table_to_departament(Loiha52).values_list(*department_fields)

    for row in rows:
        row_num += 1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)
    return response



def get_data_table(request, model_name, page_title):
    model = loiha_models.get(model_name, None)
    if not model:
        # Handle invalid model name
        raise ValueError("Invalid model name: %s" % model_name)

    if get_group_loiha_id(request):
        table_data = show_data_table_to_departament(model)
    else:
        table_data = show_data_table(request, model)

    page_obj = paginate_page(request, table_data)
    context = get_context_data(page_obj, page_title, projects_department, table_data)
    return render(request, src[model_name], context)


def get_data_table_Loiha41(request):
    return get_data_table(request, 'loiha41', 'Илова-4.1')


def get_data_table_Loiha52(request):
    return get_data_table(request, 'loiha52', 'Илова-5.2')


def get_data_table_Loiha14(request):
    return get_data_table(request, 'loiha14', 'Илова-14')


def get_data_table_Loiha131(request):
    return get_data_table(request, 'loiha131', 'Илова-13.1')


def get_data_table_Loiha122(request):
    return get_data_table(request, 'loiha122', 'Илова-12.2')


def get_data_table_Loiha121(request):
    return get_data_table(request, 'loiha121', 'Илова-12.1')


def get_data_table_Loiha12(request):
    return get_data_table(request, 'loiha12', 'Илова-12')


def get_data_table_Loiha10(request):
    return get_data_table(request, 'loiha10', 'Илова-10')


def get_data_table_Loiha6(request):
    return get_data_table(request, 'loiha6', 'Илова-6')


def get_data_table_Loiha13(request):
    return get_data_table(request, 'loiha13', 'Илова-13')

# All copied elements located in tests.py


def get_data_table_filter(request, model_name, page_title, filter_slug):
    model = loiha_models.get(model_name, None)
    if not model:
        # Handle invalid model name
        raise ValueError("Invalid model name: %s" % model_name)

    if not get_group_loiha_id(request):
        table_data = show_data_table(request, model)
    else:
        table_data = show_data_table_to_departament(model)

    table_data = filter_tables(filter_slug, table_data)

    page_obj = paginate_page(request, table_data)
    context = get_context_data(page_obj, page_title, projects_department, table_data)
    return render(request, src[model_name], context)


def table_filter_loiha41(request, filter_slug):
    return get_data_table_filter(request, 'loiha41', 'Илова-4.1', filter_slug)


def table_filter_loiha52(request, filter_slug):
    return get_data_table_filter(request, 'loiha52', 'Илова-5.2', filter_slug)


def table_filter_loiha14(request, filter_slug):
    return get_data_table_filter(request, 'loiha14', 'Илова-14', filter_slug)


def table_filter_loiha131(request, filter_slug):
    return get_data_table_filter(request, 'loiha131', 'Илова-13.1', filter_slug)


def table_filter_loiha122(request, filter_slug):
    return get_data_table_filter(request, 'loiha122', 'Илова-12.2', filter_slug)


def table_filter_loiha121(request, filter_slug):
    return get_data_table_filter(request, 'loiha121', 'Илова-12.1', filter_slug)


def table_filter_loiha12(request, filter_slug):
    return get_data_table_filter(request, 'loiha12', 'Илова-12', filter_slug)


def table_filter_loiha10(request, filter_slug):
    return get_data_table_filter(request, 'loiha10', 'Илова-10', filter_slug)


def table_filter_loiha6(request, filter_slug):
    return get_data_table_filter(request, 'loiha6', 'Илова-6', filter_slug)


def table_filter_loiha13(request, filter_slug):
    return get_data_table_filter(request, 'loiha13', 'Илова-13', filter_slug)


def logoutUser(request):
    logout(request)
    return render(request, 'mainapp/logout.html')


# TODO прочитать статью Django про итеграцию с телеграм ботом. Костамизация админкиз


@login_required
def add_data_table(request, model_name, model_form, redirect_url, page_title):
    model = loiha_models.get(model_name, None)
    table_data = show_data_table(request, model)
    page_obj = paginate_page(request, table_data)
    if request.method == 'POST':
        form = model_form(request.POST)
        if form.is_valid():
            try:
                model.objects.create(**form.cleaned_data, district=request.user.district)
                return redirect(redirect_url)
            except:
                form.add_error(None, 'Ошибка добавления данных')
    else:
        form = model_form()
    context = make_context_by_form(page_title, form, projects_department, page_obj)
    return render(request, f'mainapp/forms/form_{model_name}.html', context)


# @login_required
def add_data_table_Loiha41(request):
    return add_data_table(request, 'loiha41', TableFormLoiha41, 'table_loiha4.1', 'Илова-4.1')


def add_data_table_Loiha52(request):
    return add_data_table(request, 'loiha52', TableFormLoiha52, 'table_loiha5.2', 'Илова-5.2')


def add_data_table_Loiha14(request):
    return add_data_table(request, 'loiha14', TableFormLoiha14, 'table_loiha14', 'Илова-14')


def add_data_table_Loiha131(request):
    return add_data_table(request, 'loiha131', TableFormLoiha131, 'table_loiha13.1', 'Илова-13.1')


def add_data_table_Loiha122(request):
    return add_data_table(request, 'loiha122', TableFormLoiha122, 'table_loiha12.2', 'Илова-12.2')


def add_data_table_Loiha121(request):
    return add_data_table(request, 'loiha121', TableFormLoiha121, 'table_loiha12.1', 'Илова-12.1')


def add_data_table_Loiha12(request):
    return add_data_table(request, 'loiha12', TableFormLoiha12, 'table_loiha12', 'Илова-12')


def add_data_table_Loiha10(request):
    return add_data_table(request, 'loiha10', TableFormLoiha10, 'table_loiha10', 'Илова-10')


def add_data_table_Loiha6(request):
    return add_data_table(request, 'loiha6', TableFormLoiha6, 'table_loiha6', 'Илова-6')


def add_data_table_Loiha13(request):
    return add_data_table(request, 'loiha13', TableFormLoiha13, 'table_loiha13', 'Илова-13')


# Второй отдел

def get_data_table_2(request, model_name, page_title):
    model = second_department_models_dict.get(model_name, None)
    if not model:
        # Handle invalid model name
        raise ValueError("Invalid model name: %s" % model_name)

    if get_group_export_id(request):
        table_data = show_data_table_to_departament(model)
    else:
        table_data = show_data_table(request, model)

    page_obj = paginate_page(request, table_data)
    context = get_context_data(page_obj, page_title, second_department_tables_menu, table_data)
    return render(request, src[model_name], context)


def get_data_table_sanoat(request):
    return get_data_table_2(request, 'sanoat', 'Sanoat')


def get_data_table_kh(request):
    return get_data_table_2(request, 'kx', 'KX')


def get_data_table_first_table(request):
    return get_data_table_2(request, 'table_1', 'Таблица 1')


def get_data_table_kunliu(request):
    return get_data_table_2(request, 'kunliu', 'кунлиу')


def get_data_table_filter_second_departament(request, model_name, page_title, filter_slug):
    model = second_department_models_dict.get(model_name, None)
    if not model:
        # Handle invalid model name
        raise ValueError("Invalid model name: %s" % model_name)

    if not get_group_export_id(request):
        table_data = show_data_table(request, model)
    else:
        table_data = show_data_table_to_departament(model)

    table_data = filter_tables(filter_slug, table_data)

    page_obj = paginate_page(request, table_data)
    context = get_context_data(page_obj, page_title, second_department_tables_menu, table_data)
    return render(request, src[model_name], context)


def table_filter_sanoat(request, filter_slug):
    return get_data_table_filter_second_departament(request, 'sanoat', 'Sanoat', filter_slug)


def table_filter_kx(request, filter_slug):
    return get_data_table_filter_second_departament(request, 'kx', 'KX', filter_slug)


def table_filter_first_table(request, filter_slug):
    return get_data_table_filter_second_departament(request, 'table_1', 'Таблица 1', filter_slug)


def table_filter_kunliu(request, filter_slug):
    return get_data_table_filter_second_departament(request, 'kunliu', 'кунлиу', filter_slug)


@login_required
def add_data_table_second_department(request, model_name, model_form, redirect_url, page_title):
    model = second_department_models_dict.get(model_name, None)
    table_data = show_data_table(request, model)
    page_obj = paginate_page(request, table_data)
    if request.method == 'POST':
        form = model_form(request.POST)
        if form.is_valid():
            try:
                model.objects.create(**form.cleaned_data, district=request.user.district)
                return redirect(redirect_url)
            except:
                form.add_error(None, 'Ошибка добавления данных')
    else:
        form = model_form()
    context = make_context_by_form(page_title, form, second_department_tables_menu, page_obj)
    return render(request, f'mainapp/forms/second_departament/form_{model_name}.html', context)


def add_data_table_sanoat(request):
    return add_data_table_second_department(request, 'sanoat', TableFormSanoat, 'table_sanoat', 'Sanoat')


def add_data_table_kx(request):
    return add_data_table_second_department(request, 'kx', TableFormKX, 'table_kx', 'KX')


def add_data_table_1(request):
    return add_data_table_second_department(request, 'table_1', TableFirstForm, 'table_first', 'Таблица 1')


def add_data_table_kunliu(request):
    return add_data_table_second_department(request, 'kunliu', TableKunliuForm, 'table_kunliu', 'кунлиу')


# 3 Сводный отдел
def get_data_table_3(request, model_name, page_title):
    model = third_department_models_dict.get(model_name, None)
    if not model:
        # Handle invalid model name
        raise ValueError("Invalid model name: %s" % model_name)

    if get_group_vault_id(request):
        table_data = show_data_table_to_departament(model)
    else:
        table_data = show_data_table(request, model)

    page_obj = paginate_page(request, table_data)
    context = get_context_data(page_obj, page_title, third_department_tables_menu, table_data)
    return render(request, src[model_name], context)


def get_data_table_jami(request):
    return get_data_table_3(request, 'jami', 'Жами свод')


def get_data_table_quarter(request):
    return get_data_table_3(request, 'quarter', 'Cвод чорак')


def get_data_table_month(request):
    return get_data_table_3(request, 'monthly', 'Cвод ойлар')


def get_data_table_bank(request):
    return get_data_table_3(request, 'bank', 'Cвод банк')


def get_data_table_reja(request):
    return get_data_table_3(request, 'reja', 'Cвод режа')


def get_data_table_tarmok(request):
    return get_data_table_3(request, 'tarmok', 'Cвод тармок')

# Жами Свод


def get_data_table_filter_third_departament(request, model_name, page_title, filter_slug):
    model = third_department_models_dict.get(model_name, None)
    if not model:
        # Handle invalid model name
        raise ValueError("Invalid model name: %s" % model_name)

    if not get_group_vault_id(request):
        table_data = show_data_table(request, model)
    else:
        table_data = show_data_table_to_departament(model)

    table_data = filter_tables(filter_slug, table_data)
    page_obj = paginate_page(request, table_data)
    context = get_context_data(page_obj, page_title, third_department_tables_menu, table_data)
    return render(request, src[model_name], context)


def table_filter_table_jami(request, filter_slug):
    return get_data_table_filter_third_departament(request, 'jami', 'Жами свод', filter_slug)


def table_filter_table_quarter(request, filter_slug):
    return get_data_table_filter_third_departament(request, 'quarter', 'Cвод чорак', filter_slug)


def table_filter_table_month(request, filter_slug):
    return get_data_table_filter_third_departament(request, 'monthly', 'Cвод ойлар', filter_slug)


def table_filter_table_bank(request, filter_slug):
    return get_data_table_filter_third_departament(request, 'bank', 'Cвод банк', filter_slug)


def table_filter_table_reja(request, filter_slug):
    return get_data_table_filter_third_departament(request, 'reja', 'Cвод режа', filter_slug)


def table_filter_table_tarmok(request, filter_slug):
    return get_data_table_filter_third_departament(request, 'tarmok', 'Cвод тармок', filter_slug)


@login_required
def add_data_table_third_department(request, model_name, model_form, redirect_url, page_title):
    model = third_department_models_dict.get(model_name, None)
    table_data = show_data_table(request, model)
    page_obj = paginate_page(request, table_data)
    if request.method == 'POST':
        form = model_form(request.POST)
        if form.is_valid():
            try:
                model.objects.create(**form.cleaned_data, district=request.user.district)
                return redirect(redirect_url)
            except:
                form.add_error(None, 'Ошибка добавления данных')
    else:
        form = model_form()
    context = make_context_by_form(page_title, form, third_department_tables_menu, page_obj)
    return render(request, f'mainapp/forms/third_departament/form_{model_name}.html', context)


def add_data_table_jami(request):
    return add_data_table_third_department(request, 'jami', TableJamiForm, 'table_jami', 'Жами свод')


def add_data_table_quarter(request):
    return add_data_table_third_department(request, 'quarter', TableQuarterForm, 'table_quarter', 'Cвод чорак')


def add_data_table_month(request):
    return add_data_table_third_department(request, 'monthly', TableMonthForm, 'table_monthly', 'Cвод ойлар')


def add_data_table_bank(request):
    return add_data_table_third_department(request, 'bank', TableBankForm, 'table_bank', 'Cвод банк')


def add_data_table_reja(request):
    return add_data_table_third_department(request, 'reja', TableRejaForm, 'table_reja', 'Cвод режа')


def add_data_table_tarmok(request):
    return add_data_table_third_department(request, 'tarmok', TableTarmokForm, 'table_tarmok', 'Cвод тармок')
