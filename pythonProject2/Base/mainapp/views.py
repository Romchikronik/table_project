import xlwt

# import xlsxwriter
# from djqscsv import write_csv, render_to_csv_response
from datetime import datetime, timedelta
from django.utils import timezone

from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
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


# @login_required
# def get_department_projects(request, departament_slug):
#     context = {
#         'title': 'Отдел - Лоиха',
#         'projects_department': projects_department
#     }
#     return render(request, 'mainapp/departments/projects_department.html', context)

@login_required
def get_department_projects(request):
    context = {
        'title': 'Отдел - Лоиха',
        'projects_department': projects_department
    }
    return render(request, 'mainapp/departments/projects_department.html', context)


@login_required
def get_department_exports(request):
    context = {
        'title': 'Отдел - 2',
        'second_department_tables_menu': second_department_tables_menu
    }
    return render(request, 'mainapp/departments/exports_department.html', context)


@login_required
def get_department_3(request):
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


# def export_csv(request):
#     response = HttpResponse(
#         content_type='text/csv',
#         headers={'Content-Disposition': 'attachment; filename="table.csv"'},
#     )
#     writer = csv.writer(response)
#     writer.writerow(fields)
#
#     model = Loiha41.objects.filter(district=request.user.district).values_list(
#         'district',
#         'bill_sum_industry',
#         'picture_of_growth_industry',
#         'forecast_industry',
#         'difference_industry',
#         'bill_sum_locality',
#         'picture_of_growth_locality',
#         'forecast_locality',
#         'difference_locality',
#         'bill_sum_construction',
#         'picture_of_growth_construction',
#         'forecast_construction',
#         'difference_construction',
#         'bill_sum_services',
#         'picture_of_growth_services',
#         'forecast_services',
#         'difference_services',
#         'bill_sum_retail',
#         'picture_of_growth_retail',
#         'forecast_retail',
#         'difference_retail',
#         'thousand_dollar_international_trade',
#         'picture_of_growth_international_trade',
#         'thousand_dollar_export',
#         'picture_of_growth_export',
#         'thousand_dollar_import',
#         'picture_of_growth_import',
#         'time_create'
#     )
#
#     for field in model:
#         writer.writerow(field)
#
#
#     return response


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
    ws.write_merge(0, 0, 0, 25, 'Чирчик тумани, Илова-4.1', cell_title)
    ws.write_merge(1, 1, 0, 3, 'SANOAT', cell_style)
    ws.write_merge(1, 1, 4, 7, 'QISHLOQ', cell_style)
    ws.write_merge(1, 1, 8, 11, 'QURILISH', cell_style)
    ws.write_merge(1, 1, 12, 15, 'XIZMATLAR', cell_style)
    ws.write_merge(1, 1, 16, 19, 'CHAKANA SAVDO', cell_style)
    ws.write_merge(1, 1, 20, 21,  'TASHQI SAVDO AYLANMASI', cell_style)
    ws.write_merge(1, 1, 22, 23, 'EKSPORT', cell_style)
    ws.write_merge(1, 1, 24, 25, 'IMPORT', cell_style)

    # ws.col(0).width = 4500
    # ws.col(21).width = 5000

    # "Район",
    columns = ["mlrd. so'm",
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

    for col_num in range(len(columns)):
        ws.col(col_num).width = 3800
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    # date_style = xlwt.XFStyle()
    # # datetime.utcfromtimestamp(int('time_create')).strftime('%Y-%m-%d %H:%M:%S')
    # date_style.num_format_str = '%d/%m/%y %h:%m:%s'
    # time_create = datetime.strftime('time_create', '%d/%m/%y %h:%m:%s')

    if filter_slug == 'week':
        now = timezone.now() - timedelta(minutes=60 * 24 * 7)
        rows = Loiha41.objects.filter(district=request.user.district, time_create__gte=now).values_list(
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
            )
    elif filter_slug == 'month':
        now = timezone.now() - timedelta(minutes=60 * 24 * 30)
        rows = Loiha41.objects.filter(district=request.user.district, time_create__gte=now).values_list(
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
            )
    else:
        rows = Loiha41.objects.filter(district=request.user.district).values_list(
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
            )

    for row in rows:
        row_num += 1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)
    return response


# def export_csv(request):
#     # csv.writerow(["Имя", "Класс", "Возраст"])
#
#     qs = Loiha41.objects.filter(district=request.user.district).values(
#         'district__district',
#         'bill_sum_industry',
#         'picture_of_growth_industry',
#         'forecast_industry',
#         'difference_industry',
#         'bill_sum_locality',
#         'picture_of_growth_locality',
#         'forecast_locality',
#         'difference_locality',
#         'bill_sum_construction',
#         'picture_of_growth_construction',
#         'forecast_construction',
#         'difference_construction',
#         'bill_sum_services',
#         'picture_of_growth_services',
#         'forecast_services',
#         'difference_services',
#         'bill_sum_retail',
#         'picture_of_growth_retail',
#         'forecast_retail',
#         'difference_retail',
#         'thousand_dollar_international_trade',
#         'picture_of_growth_international_trade',
#         'thousand_dollar_export',
#         'picture_of_growth_export',
#         'thousand_dollar_import',
#         'picture_of_growth_import',
#         'time_create'
#     )
#
#     return render_to_csv_response(qs, delimiter=' ')
# with open('table.csv', 'wb') as csv_file:
#     write_csv(qs, csv_file)

# def get_data_table(request):
#     for model in projects_department_models:
#         table_data = show_data_table(request, model)  # model
#         page_obj = paginate_page(request, table_data)
#         context = get_context_data(page_obj, 'Илова-4.1', projects_department, table_data)  # title
#         return render(request, src['loiha41'], context)


def get_data_table_Loiha41(request):
    table_data = show_data_table(request, Loiha41)  # model
    page_obj = paginate_page(request, table_data)
    context = get_context_data(page_obj, 'Илова-4.1', projects_department, table_data)  # title
    return render(request, src['loiha41'], context)


def get_data_table_Loiha52(request):
    table_data = show_data_table(request, Loiha52)
    page_obj = paginate_page(request, table_data)
    context = get_context_data(page_obj, 'Илова-5.2', projects_department, table_data)
    return render(request, src['loiha52'], context)


def get_data_table_Loiha14(request):
    table_data = show_data_table(request, Loiha14)
    page_obj = paginate_page(request, table_data)
    context = get_context_data(page_obj, 'Илова-14', projects_department, table_data)
    return render(request, src['loiha14'], context)


def get_data_table_Loiha131(request):
    table_data = show_data_table(request, Loiha131)
    page_obj = paginate_page(request, table_data)
    context = get_context_data(page_obj, 'Илова-13.1', projects_department, table_data)
    return render(request, src['loiha131'], context)


def get_data_table_Loiha122(request):
    table_data = show_data_table(request, Loiha122)
    page_obj = paginate_page(request, table_data)
    context = get_context_data(page_obj, 'Илова-12.2', projects_department, table_data)
    return render(request, src['loiha122'], context)


def get_data_table_Loiha121(request):
    table_data = show_data_table(request, Loiha121)
    page_obj = paginate_page(request, table_data)
    context = get_context_data(page_obj, 'Илова-12.1', projects_department, table_data)
    return render(request, src['loiha121'], context)


def get_data_table_Loiha12(request):
    table_data = show_data_table(request, Loiha12)
    page_obj = paginate_page(request, table_data)
    context = get_context_data(page_obj, 'Илова-12', projects_department, table_data)
    return render(request, src['loiha12'], context)


def get_data_table_Loiha10(request):
    table_data = show_data_table(request, Loiha10)
    page_obj = paginate_page(request, table_data)
    context = get_context_data(page_obj, 'Илова-10', projects_department, table_data)
    return render(request, src['loiha10'], context)


def get_data_table_Loiha6(request):
    table_data = show_data_table(request, Loiha6)
    page_obj = paginate_page(request, table_data)

    # user_district = District.objects.get(id=user.id)
    context = get_context_data(page_obj, 'Илова-6', projects_department, table_data)
    return render(request, src['loiha6'], context)


def get_data_table_Loiha13(request):
    table_data = show_data_table(request, Loiha13)
    page_obj = paginate_page(request, table_data)
    context = get_context_data(page_obj, 'Илова-13', projects_department, table_data)
    return render(request, src['loiha13'], context)


def logoutUser(request):
    logout(request)
    return render(request, 'mainapp/logout.html')
# TODO потом изменить кнопку назад, изменить дату в excel файле.
# TODO прочитать статью Django про итеграцию с телеграм ботом. Костамизация админкиз


@login_required
def add_data_table_Loiha41(request):
    table_data = show_data_table(request, Loiha41)
    page_obj = paginate_page(request, table_data)
    if request.method == 'POST':
        form = TableFormLoiha41(request.POST)
        if form.is_valid():
            try:
                Loiha41.objects.create(**form.cleaned_data, district=request.user.district)
                return redirect('table_loiha4.1')
            except:
                form.add_error(None, 'Ошибка добавления данных')
    else:
        form = TableFormLoiha41()
    context = make_context_by_form('Илова-4.1', form, projects_department, page_obj)
    return render(request, 'mainapp/forms/form_loiha41.html', context)


def add_data_table_Loiha52(request):
    table_data = show_data_table(request, Loiha52)
    page_obj = paginate_page(request, table_data)
    if request.method == 'POST':
        form = TableFormLoiha52(request.POST)
        if form.is_valid():
            try:
                create_data(request, Loiha52, form)
                return redirect('table_loiha5.2')
            except:
                form.add_error(None, 'Ошибка добавления данных')
    else:
        form = TableFormLoiha52()
    context = make_context_by_form('Илова-5.2', form, projects_department, page_obj)
    return render(request, 'mainapp/forms/form_loiha52.html', context)


@login_required
def add_data_table_Loiha14(request):
    table_data = show_data_table(request, Loiha14)
    page_obj = paginate_page(request, table_data)
    if request.method == 'POST':
        form = TableFormLoiha14(request.POST)
        if form.is_valid():
            try:
                Loiha14.objects.create(**form.cleaned_data, district=request.user.district)
                return redirect('table_loiha14')
            except:
                form.add_error(None, 'Ошибка добавления данных')
    else:
        form = TableFormLoiha14()
    context = make_context_by_form('Илова-14', form, projects_department, page_obj)
    return render(request, 'mainapp/forms/form_loiha14.html', context)


@login_required
def add_data_table_Loiha131(request):
    table_data = show_data_table(request, Loiha131)
    page_obj = paginate_page(request, table_data)
    if request.method == 'POST':
        form = TableFormLoiha131(request.POST)
        if form.is_valid():
            try:
                Loiha131.objects.create(**form.cleaned_data, district=request.user.district)
                return redirect('table_loiha13.1')
            except:
                form.add_error(None, 'Ошибка добавления данных')
    else:
        form = TableFormLoiha131()
    context = make_context_by_form('Илова-13.1', form, projects_department, page_obj)
    return render(request, 'mainapp/forms/form_loiha131.html', context)


@login_required
def add_data_table_Loiha122(request):
    table_data = show_data_table(request, Loiha122)
    page_obj = paginate_page(request, table_data)
    if request.method == 'POST':
        form = TableFormLoiha122(request.POST)
        if form.is_valid():
            try:
                Loiha122.objects.create(**form.cleaned_data, district=request.user.district)
                return redirect('table_loiha12.2')
            except:
                form.add_error(None, 'Ошибка добавления данных')
    else:
        form = TableFormLoiha122()
    context = make_context_by_form('Илова-12.2', form, projects_department, page_obj)
    return render(request, 'mainapp/forms/form_loiha122.html', context)


@login_required
def add_data_table_Loiha121(request):
    table_data = show_data_table(request, Loiha121)
    page_obj = paginate_page(request, table_data)
    if request.method == 'POST':
        form = TableFormLoiha121(request.POST)
        if form.is_valid():
            try:
                Loiha121.objects.create(**form.cleaned_data, district=request.user.district)
                return redirect('table_loiha12.1')
            except:
                form.add_error(None, 'Ошибка добавления данных')
    else:
        form = TableFormLoiha121()
    context = make_context_by_form('Илова-12.1', form, projects_department, page_obj)
    return render(request, 'mainapp/forms/form_loiha121.html', context)


@login_required
def add_data_table_Loiha12(request):
    table_data = show_data_table(request, Loiha12)
    page_obj = paginate_page(request, table_data)
    if request.method == 'POST':
        form = TableFormLoiha12(request.POST)
        if form.is_valid():
            try:
                Loiha12.objects.create(**form.cleaned_data, district=request.user.district)
                return redirect('table_loiha12')
            except:
                form.add_error(None, 'Ошибка добавления данных')
    else:
        form = TableFormLoiha12()
    context = make_context_by_form('Илова-12', form, projects_department, page_obj)
    return render(request, 'mainapp/forms/form_loiha12.html', context)


@login_required
def add_data_table_Loiha6(request):
    table_data = show_data_table(request, Loiha6)
    page_obj = paginate_page(request, table_data)
    if request.method == 'POST':
        form = TableFormLoiha6(request.POST)
        if form.is_valid():
            try:
                Loiha6.objects.create(**form.cleaned_data, district=request.user.district)
                return redirect('table_loiha6')
            except:
                form.add_error(None, 'Ошибка добавления данных')
    else:
        form = TableFormLoiha6()
    context = make_context_by_form('Илова-6', form, projects_department, page_obj)
    return render(request, 'mainapp/forms/form_loiha6.html', context)


@login_required
def add_data_table_Loiha10(request):
    table_data = show_data_table(request, Loiha10)
    page_obj = paginate_page(request, table_data)
    if request.method == 'POST':
        form = TableFormLoiha10(request.POST)
        if form.is_valid():
            try:
                Loiha10.objects.create(**form.cleaned_data, district=request.user.district)
                return redirect('table_loiha10')
            except:
                form.add_error(None, 'Ошибка добавления данных')
    else:
        form = TableFormLoiha10()
    context = make_context_by_form('Илова-10', form, projects_department, page_obj)
    return render(request, 'mainapp/forms/form_loiha10.html', context)


@login_required
def add_data_table_Loiha13(request):
    table_data = show_data_table(request, Loiha13)
    page_obj = paginate_page(request, table_data)
    if request.method == 'POST':
        form = TableFormLoiha13(request.POST)
        if form.is_valid():
            try:
                Loiha13.objects.create(**form.cleaned_data, district=request.user.district)
                return redirect('table_loiha13')
            except:
                form.add_error(None, 'Ошибка добавления данных')
    else:
        form = TableFormLoiha13()
    context = make_context_by_form('Илова-13', form, projects_department, page_obj)
    return render(request, 'mainapp/forms/form_loiha13.html', context)


def table_filter_loiha131(request, filter_slug):
    table = show_data_table(request, Loiha131)

    # table_data = show_data_table(request, Loiha131)
    if filter_slug == 'week':
        now = datetime.now() - timedelta(minutes=60 * 24 * 7)
        table = table.filter(time_create__gte=now)
    elif filter_slug == 'month':
        now = datetime.now() - timedelta(minutes=60 * 24 * 30)
        table = table.filter(time_create__gte=now)

    page_obj = paginate_page(request, table)
    context = get_context_data(page_obj, 'Илова-13.1', projects_department, table)
    return render(request, src['loiha131'], context)


def table_filter_loiha41(request, filter_slug):
    table = show_data_table(request, Loiha41)

    # table_data = show_data_table(request, Loiha131)
    if filter_slug == 'week':
        now = timezone.now() - timedelta(minutes=60 * 24 * 7)
        table = table.filter(time_create__gte=now)
    elif filter_slug == 'month':
        now = timezone.now() - timedelta(minutes=60 * 24 * 30)
        table = table.filter(time_create__gte=now)
    # elif filter_slug == 'all':
    #     table = table

    page_obj = paginate_page(request, table)
    context = get_context_data(page_obj, 'Илова-4.1', projects_department, table)
    return render(request, src['loiha41'], context)


def table_filter_loiha52(request, filter_slug):
    # table = Loiha52.objects.filter(district=request.user.district)
    table = show_data_table(request, Loiha52)

    # table_data = show_data_table(request, Loiha131)
    if filter_slug == 'week':
        now = timezone.now() - timedelta(minutes=60 * 24 * 7)
        table = table.filter(time_create__gte=now)
    elif filter_slug == 'month':
        now = timezone.now() - timedelta(minutes=60 * 24 * 30)
        table = table.filter(time_create__gte=now)

    page_obj = paginate_page(request, table)
    context = get_context_data(page_obj, 'Илова-5.2', projects_department, table)
    return render(request, src['loiha52'], context)


def table_filter_loiha14(request, filter_slug):
    # table = Loiha14.objects.filter(district=request.user.district)
    table = show_data_table(request, Loiha14)

    # table_data = show_data_table(request, Loiha131)
    if filter_slug == 'week':
        now = timezone.now() - timedelta(minutes=60 * 24 * 7)
        table = table.filter(time_create__gte=now)
    elif filter_slug == 'month':
        now = timezone.now() - timedelta(minutes=60 * 24 * 30)
        table = table.filter(time_create__gte=now)

    page_obj = paginate_page(request, table)
    context = get_context_data(page_obj, 'Илова-14', projects_department, table)
    return render(request, src['loiha14'], context)


def table_filter_loiha122(request, filter_slug):
    # table = Loiha14.objects.filter(district=request.user.district)
    table = show_data_table(request, Loiha122)

    # table_data = show_data_table(request, Loiha131)
    if filter_slug == 'week':
        now = timezone.now() - timedelta(minutes=60 * 24 * 7)
        table = table.filter(time_create__gte=now)
    elif filter_slug == 'month':
        now = timezone.now() - timedelta(minutes=60 * 24 * 30)
        table = table.filter(time_create__gte=now)

    page_obj = paginate_page(request, table)
    context = get_context_data(page_obj, 'Илова-12.2', projects_department, table)
    return render(request, src['loiha122'], context)


def table_filter_loiha121(request, filter_slug):
    # table = Loiha14.objects.filter(district=request.user.district)
    table = show_data_table(request, Loiha121)

    # table_data = show_data_table(request, Loiha131)
    if filter_slug == 'week':
        now = timezone.now() - timedelta(minutes=60 * 24 * 7)
        table = table.filter(time_create__gte=now)
    elif filter_slug == 'month':
        now = timezone.now() - timedelta(minutes=60 * 24 * 30)
        table = table.filter(time_create__gte=now)

    page_obj = paginate_page(request, table)
    context = get_context_data(page_obj, 'Илова-12.1', projects_department, table)
    return render(request, src['loiha121'], context)


def table_filter_loiha12(request, filter_slug):
    # table = Loiha14.objects.filter(district=request.user.district)
    table = show_data_table(request, Loiha12)

    # table_data = show_data_table(request, Loiha131)
    if filter_slug == 'week':
        now = timezone.now() - timedelta(minutes=60 * 24 * 7)
        table = table.filter(time_create__gte=now)
    elif filter_slug == 'month':
        now = timezone.now() - timedelta(minutes=60 * 24 * 30)
        table = table.filter(time_create__gte=now)

    page_obj = paginate_page(request, table)
    context = get_context_data(page_obj, 'Илова-12', projects_department, table)
    return render(request, src['loiha12'], context)


def table_filter_loiha10(request, filter_slug):
    # table = Loiha14.objects.filter(district=request.user.district)
    table = show_data_table(request, Loiha10)

    # table_data = show_data_table(request, Loiha131)
    if filter_slug == 'week':
        now = timezone.now() - timedelta(minutes=60 * 24 * 7)
        table = table.filter(time_create__gte=now)
    elif filter_slug == 'month':
        now = timezone.now() - timedelta(minutes=60 * 24 * 30)
        table = table.filter(time_create__gte=now)

    page_obj = paginate_page(request, table)
    context = get_context_data(page_obj, 'Илова-10', projects_department, table)
    return render(request, src['loiha10'], context)


def table_filter_loiha6(request, filter_slug):
    # table = Loiha14.objects.filter(district=request.user.district)
    table = show_data_table(request, Loiha6)

    # table_data = show_data_table(request, Loiha131)
    if filter_slug == 'week':
        now = timezone.now() - timedelta(minutes=60 * 24 * 7)
        table = table.filter(time_create__gte=now)
    elif filter_slug == 'month':
        now = timezone.now() - timedelta(minutes=60 * 24 * 30)
        table = table.filter(time_create__gte=now)

    page_obj = paginate_page(request, table)
    context = get_context_data(page_obj, 'Илова-6', projects_department, table)
    return render(request, src['loiha6'], context)


def table_filter_loiha13(request, filter_slug):
    # table = Loiha14.objects.filter(district=request.user.district)
    table = show_data_table(request, Loiha13)

    # table_data = show_data_table(request, Loiha131)
    if filter_slug == 'week':
        now = timezone.now() - timedelta(minutes=60 * 24 * 7)
        table = table.filter(time_create__gte=now)
    elif filter_slug == 'month':
        now = timezone.now() - timedelta(minutes=60 * 24 * 30)
        table = table.filter(time_create__gte=now)

    page_obj = paginate_page(request, table)
    context = get_context_data(page_obj, 'Илова-13', projects_department, table)
    return render(request, src['loiha13'], context)


# Второй отдел

# Sanoat

def get_data_table_sanoat(request):
    table_data = show_data_table(request, Sanoat)
    page_obj = paginate_page(request, table_data)
    context = get_context_data(page_obj, 'Sanoat', second_department_tables_menu, table_data)
    return render(request, src['sanoat'], context)


@login_required
def add_data_table_sanoat(request):
    table_data = show_data_table(request, Sanoat)
    page_obj = paginate_page(request, table_data)
    if request.method == 'POST':
        form = TableSanoat(request.POST)
        if form.is_valid():
            try:
                Sanoat.objects.create(**form.cleaned_data, district=request.user.district)
                return redirect('table_sanoat')
            except:
                form.add_error(None, 'Ошибка добавления данных')
    else:
        form = TableSanoat()
    context = make_context_by_form('Sanoat', form, second_department_tables_menu, page_obj)
    return render(request, 'mainapp/forms/form_sanoat.html', context)


def table_filter_sanoat(request, filter_slug):
    # table = Loiha14.objects.filter(district=request.user.district)
    table = show_data_table(request, Sanoat)

    # table_data = show_data_table(request, Loiha131)
    if filter_slug == 'week':
        now = timezone.now() - timedelta(minutes=60 * 24 * 7)
        table = table.filter(time_create__gte=now)
    elif filter_slug == 'month':
        now = timezone.now() - timedelta(minutes=60 * 24 * 30)
        table = table.filter(time_create__gte=now)

    page_obj = paginate_page(request, table)
    context = get_context_data(page_obj, 'Sanoat', second_department_tables_menu, table)
    return render(request, src['sanoat'], context)

# KX

def get_data_table_kh(request):
    table_data = show_data_table(request, KH)
    page_obj = paginate_page(request, table_data)
    context = get_context_data(page_obj, 'KX', second_department_tables_menu, table_data)
    return render(request, src['kx'], context)


@login_required
def add_data_table_kx(request):
    table_data = show_data_table(request, KH)
    page_obj = paginate_page(request, table_data)
    if request.method == 'POST':
        form = TableKX(request.POST)
        if form.is_valid():
            try:
                KH.objects.create(**form.cleaned_data, district=request.user.district)
                return redirect('table_kx')
            except:
                form.add_error(None, 'Ошибка добавления данных')
    else:
        form = TableKX()
    context = make_context_by_form('KX', form, second_department_tables_menu, page_obj)
    return render(request, 'mainapp/forms/form_kx.html', context)