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

# @login_required
# def get_department_projects(request, departament_slug):
#     context = {
#         'title': 'Отдел - Лоиха',
#         'projects_department': projects_department
#     }
#     return render(request, 'mainapp/departments/projects_department.html', context)

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
    # user = get_user(request)
    if get_group_loiha_id(request):
        # print('I am department user')
        table_data = show_data_table_to_departament(Loiha41)
    else:
        table_data = show_data_table(request, Loiha41)  # model

    page_obj = paginate_page(request, table_data)
    context = get_context_data(page_obj, 'Илова-4.1', projects_department, table_data)  # title
    return render(request, src['loiha41'], context)


def get_data_table_Loiha52(request):
    if get_group_loiha_id(request):
        table_data = show_data_table_to_departament(Loiha52)
    else:
        table_data = show_data_table(request, Loiha52)

    page_obj = paginate_page(request, table_data)
    context = get_context_data(page_obj, 'Илова-5.2', projects_department, table_data)
    return render(request, src['loiha52'], context)


def get_data_table_Loiha14(request):
    if get_group_loiha_id(request):
        table_data = show_data_table_to_departament(Loiha14)
    else:
        table_data = show_data_table(request, Loiha14)
    page_obj = paginate_page(request, table_data)
    context = get_context_data(page_obj, 'Илова-14', projects_department, table_data)
    return render(request, src['loiha14'], context)


def get_data_table_Loiha131(request):
    if get_group_loiha_id(request):
        table_data = show_data_table_to_departament(Loiha131)
    else:
        table_data = show_data_table(request, Loiha131)
    page_obj = paginate_page(request, table_data)
    context = get_context_data(page_obj, 'Илова-13.1', projects_department, table_data)
    return render(request, src['loiha131'], context)


def get_data_table_Loiha122(request):
    if get_group_loiha_id(request):
        table_data = show_data_table_to_departament(Loiha122)
    else:
        table_data = show_data_table(request, Loiha122)
    page_obj = paginate_page(request, table_data)
    context = get_context_data(page_obj, 'Илова-12.2', projects_department, table_data)
    return render(request, src['loiha122'], context)


def get_data_table_Loiha121(request):
    if get_group_loiha_id(request):
        table_data = show_data_table_to_departament(Loiha121)
    else:
        table_data = show_data_table(request, Loiha121)
    page_obj = paginate_page(request, table_data)
    context = get_context_data(page_obj, 'Илова-12.1', projects_department, table_data)
    return render(request, src['loiha121'], context)


def get_data_table_Loiha12(request):
    if get_group_loiha_id(request):
        table_data = show_data_table_to_departament(Loiha12)
    else:
        table_data = show_data_table(request, Loiha12)
    page_obj = paginate_page(request, table_data)
    context = get_context_data(page_obj, 'Илова-12', projects_department, table_data)
    return render(request, src['loiha12'], context)


def get_data_table_Loiha10(request):
    if get_group_loiha_id(request):
        table_data = show_data_table_to_departament(Loiha10)
    else:
        table_data = show_data_table(request, Loiha10)
    page_obj = paginate_page(request, table_data)
    context = get_context_data(page_obj, 'Илова-10', projects_department, table_data)
    return render(request, src['loiha10'], context)


def get_data_table_Loiha6(request):
    if get_group_loiha_id(request):
        table_data = show_data_table_to_departament(Loiha6)
    else:
        table_data = show_data_table(request, Loiha6)
    # table_data = show_data_table(request, Loiha6)
    page_obj = paginate_page(request, table_data)

    # user_district = District.objects.get(id=user.id)
    context = get_context_data(page_obj, 'Илова-6', projects_department, table_data)
    return render(request, src['loiha6'], context)


def get_data_table_Loiha13(request):
    if get_group_loiha_id(request):
        table_data = show_data_table_to_departament(Loiha13)
    else:
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
    if not get_group_loiha_id(request):
        table = show_data_table(request, Loiha131)
    else:
        table = show_data_table_to_departament(Loiha131)

    table = filter_tables(filter_slug, table)

    page_obj = paginate_page(request, table)
    context = get_context_data(page_obj, 'Илова-13.1', projects_department, table)
    return render(request, src['loiha131'], context)


def table_filter_loiha41(request, filter_slug):

    if not get_group_loiha_id(request):
        table = show_data_table(request, Loiha41)
    else:
        table = show_data_table_to_departament(Loiha41)
    # table_data = show_data_table(request, Loiha131)
    table = filter_tables(filter_slug, table)

    # if filter_slug == 'week':
    #     now = timezone.now() - timedelta(minutes=60 * 24 * 7)
    #     table = table.filter(time_create__gte=now)
    # elif filter_slug == 'month':
    #     now = timezone.now() - timedelta(minutes=60 * 24 * 30)
    #     table = table.filter(time_create__gte=now)
    # elif filter_slug == 'all':
    #     table = table

    page_obj = paginate_page(request, table)
    context = get_context_data(page_obj, 'Илова-4.1', projects_department, table)
    return render(request, src['loiha41'], context)


def table_filter_loiha52(request, filter_slug):
    # table = Loiha52.objects.filter(district=request.user.district)
    if not get_group_loiha_id(request):
        table = show_data_table(request, Loiha52)
    else:
        table = show_data_table_to_departament(Loiha52)

    # table_data = show_data_table(request, Loiha131)
    table = filter_tables(filter_slug, table)

    page_obj = paginate_page(request, table)
    context = get_context_data(page_obj, 'Илова-5.2', projects_department, table)
    return render(request, src['loiha52'], context)


def table_filter_loiha14(request, filter_slug):
    # table = Loiha14.objects.filter(district=request.user.district)
    if not get_group_loiha_id(request):
        table = show_data_table(request, Loiha14)
    else:
        table = show_data_table_to_departament(Loiha14)

    # table_data = show_data_table(request, Loiha131)
    table = filter_tables(filter_slug, table)

    page_obj = paginate_page(request, table)
    context = get_context_data(page_obj, 'Илова-14', projects_department, table)
    return render(request, src['loiha14'], context)


def table_filter_loiha122(request, filter_slug):
    if not get_group_loiha_id(request):
        table = show_data_table(request, Loiha122)
    else:
        table = show_data_table_to_departament(Loiha122)

    # table_data = show_data_table(request, Loiha131)
    table = filter_tables(filter_slug, table)

    page_obj = paginate_page(request, table)
    context = get_context_data(page_obj, 'Илова-12.2', projects_department, table)
    return render(request, src['loiha122'], context)


def table_filter_loiha121(request, filter_slug):
    if not get_group_loiha_id(request):
        table = show_data_table(request, Loiha121)
    else:
        table = show_data_table_to_departament(Loiha121)

    # table_data = show_data_table(request, Loiha131)
    table = filter_tables(filter_slug, table)

    page_obj = paginate_page(request, table)
    context = get_context_data(page_obj, 'Илова-12.1', projects_department, table)
    return render(request, src['loiha121'], context)


def table_filter_loiha12(request, filter_slug):
    if not get_group_loiha_id(request):
        table = show_data_table(request, Loiha12)
    else:
        table = show_data_table_to_departament(Loiha12)

    # table_data = show_data_table(request, Loiha131)
    table = filter_tables(filter_slug, table)

    page_obj = paginate_page(request, table)
    context = get_context_data(page_obj, 'Илова-12', projects_department, table)
    return render(request, src['loiha12'], context)


def table_filter_loiha10(request, filter_slug):
    # table = Loiha14.objects.filter(district=request.user.district)
    # table = show_data_table(request, Loiha10)
    if not get_group_loiha_id(request):
        table = show_data_table(request, Loiha10)
    else:
        table = show_data_table_to_departament(Loiha10)

    # table_data = show_data_table(request, Loiha131)
    table = filter_tables(filter_slug, table)

    page_obj = paginate_page(request, table)
    context = get_context_data(page_obj, 'Илова-10', projects_department, table)
    return render(request, src['loiha10'], context)


def table_filter_loiha6(request, filter_slug):
    # table = Loiha14.objects.filter(district=request.user.district)
    if not get_group_loiha_id(request):
        table = show_data_table(request, Loiha6)
    else:
        table = show_data_table_to_departament(Loiha6)

    # table_data = show_data_table(request, Loiha131)
    table = filter_tables(filter_slug, table)

    page_obj = paginate_page(request, table)
    context = get_context_data(page_obj, 'Илова-6', projects_department, table)
    return render(request, src['loiha6'], context)


def table_filter_loiha13(request, filter_slug):
    # table = Loiha14.objects.filter(district=request.user.district)
    if not get_group_loiha_id(request):
        table = show_data_table(request, Loiha13)
    else:
        table = show_data_table_to_departament(Loiha13)

    # table_data = show_data_table(request, Loiha131)
    table = filter_tables(filter_slug, table)

    page_obj = paginate_page(request, table)
    context = get_context_data(page_obj, 'Илова-13', projects_department, table)
    return render(request, src['loiha13'], context)


# Второй отдел

# Sanoat

def get_data_table_sanoat(request):
    if get_group_export_id(request):
        # print('I am department user')
        table_data = show_data_table_to_departament(Sanoat)
    else:
        table_data = show_data_table(request, Sanoat)
    page_obj = paginate_page(request, table_data)
    context = get_context_data(page_obj, 'Sanoat', second_department_tables_menu, table_data)
    return render(request, src['sanoat'], context)


@login_required
def add_data_table_sanoat(request):
    table_data = show_data_table(request, Sanoat)
    page_obj = paginate_page(request, table_data)
    if request.method == 'POST':
        form = TableFormSanoat(request.POST)
        if form.is_valid():
            try:
                Sanoat.objects.create(**form.cleaned_data, district=request.user.district)
                return redirect('table_sanoat')
            except:
                form.add_error(None, 'Ошибка добавления данных')
    else:
        form = TableFormSanoat()
    context = make_context_by_form('Sanoat', form, second_department_tables_menu, page_obj)
    return render(request, 'mainapp/forms/second_departament/form_sanoat.html', context)


def table_filter_sanoat(request, filter_slug):
    # table = show_data_table(request, Sanoat)
    if not get_group_export_id(request):
        table = show_data_table(request, Sanoat)
    else:
        table = show_data_table_to_departament(Sanoat)

    # table_data = show_data_table(request, Loiha131)
    table = filter_tables(filter_slug, table)

    page_obj = paginate_page(request, table)
    context = get_context_data(page_obj, 'Sanoat', second_department_tables_menu, table)
    return render(request, src['sanoat'], context)


# KX

def get_data_table_kh(request):
    if get_group_export_id(request):
        table_data = show_data_table_to_departament(KH)
    else:
        table_data = show_data_table(request, KH)
    page_obj = paginate_page(request, table_data)
    context = get_context_data(page_obj, 'KX', second_department_tables_menu, table_data)
    return render(request, src['kx'], context)


@login_required
def add_data_table_kx(request):
    table_data = show_data_table(request, KH)
    page_obj = paginate_page(request, table_data)
    if request.method == 'POST':
        form = TableFormKX(request.POST)
        if form.is_valid():
            try:
                KH.objects.create(**form.cleaned_data, district=request.user.district)
                return redirect('table_kx')
            except:
                form.add_error(None, 'Ошибка добавления данных')
    else:
        form = TableFormKX()
    context = make_context_by_form('KX', form, second_department_tables_menu, page_obj)
    return render(request, 'mainapp/forms/second_departament/form_kx.html', context)


def table_filter_kx(request, filter_slug):
    # table = Loiha14.objects.filter(district=request.user.district)
    if not get_group_export_id(request):
        table = show_data_table(request, KH)
    else:
        table = show_data_table_to_departament(KH)
    # table_data = show_data_table(request, Loiha131)
    table = filter_tables(filter_slug, table)

    page_obj = paginate_page(request, table)
    context = get_context_data(page_obj, 'KX', second_department_tables_menu, table)
    return render(request, src['kx'], context)


# first_table

def get_data_table_first_table(request):
    if get_group_export_id(request):
        table_data = show_data_table_to_departament(FirstTable)
    else:
        table_data = show_data_table(request, FirstTable)
    page_obj = paginate_page(request, table_data)
    context = get_context_data(page_obj, 'Таблица 1', second_department_tables_menu, table_data)
    return render(request, src['table_1'], context)


@login_required
def add_data_table_1(request):
    table_data = show_data_table(request, FirstTable)
    page_obj = paginate_page(request, table_data)
    if request.method == 'POST':
        form = TableFirstForm(request.POST)
        if form.is_valid():
            try:
                FirstTable.objects.create(**form.cleaned_data, district=request.user.district)
                return redirect('table_first')
            except:
                form.add_error(None, 'Ошибка добавления данных')
    else:
        form = TableFirstForm()
    context = make_context_by_form('Таблица 1', form, second_department_tables_menu, page_obj)
    return render(request, 'mainapp/forms/second_departament/form_table1.html', context)


def table_filter_first_table(request, filter_slug):
    # table = Loiha14.objects.filter(district=request.user.district)
    if not get_group_export_id(request):
        table = show_data_table(request, FirstTable)
    else:
        table = show_data_table_to_departament(FirstTable)

    # table_data = show_data_table(request, Loiha131)
    table = filter_tables(filter_slug, table)

    page_obj = paginate_page(request, table)
    context = get_context_data(page_obj, 'Таблица 1', second_department_tables_menu, table)
    return render(request, src['table_1'], context)


# Kunliu

def get_data_table_kunliu(request):
    if get_group_export_id(request):
        table_data = show_data_table_to_departament(Kunliu)
    else:
        table_data = show_data_table(request, Kunliu)
    page_obj = paginate_page(request, table_data)
    context = get_context_data(page_obj, 'кунлиу', second_department_tables_menu, table_data)
    return render(request, src['kunliu'], context)


@login_required
def add_data_table_kunliu(request):
    table_data = show_data_table(request, Kunliu)
    page_obj = paginate_page(request, table_data)
    if request.method == 'POST':
        form = TableKunliuForm(request.POST)
        if form.is_valid():
            try:
                Kunliu.objects.create(**form.cleaned_data, district=request.user.district)
                return redirect('table_kunliu')
            except:
                form.add_error(None, 'Ошибка добавления данных')
    else:
        form = TableKunliuForm()
    context = make_context_by_form('кунлиу', form, second_department_tables_menu, page_obj)
    return render(request, 'mainapp/forms/second_departament/form_kunliu.html', context)


def table_filter_kunliu(request, filter_slug):
    if not get_group_export_id(request):
        table = show_data_table(request, Kunliu)
    else:
        table = show_data_table_to_departament(Kunliu)

    # table_data = show_data_table(request, Loiha131)
    table = filter_tables(filter_slug, table)

    page_obj = paginate_page(request, table)
    context = get_context_data(page_obj, 'кунлиу', second_department_tables_menu, table)
    return render(request, src['kunliu'], context)


# 3 Сводный отдел
# Жами Свод

def get_data_table_jami(request):
    if get_group_vault_id(request):
        table_data = show_data_table_to_departament(JamiVault)
    else:
        table_data = show_data_table(request, JamiVault)
    page_obj = paginate_page(request, table_data)
    context = get_context_data(page_obj, 'Жами свод', third_department_tables_menu, table_data)
    return render(request, src['jami'], context)


def table_filter_table_jami(request, filter_slug):
    if not get_group_vault_id(request):
        table = show_data_table(request, JamiVault)
    else:
        table = show_data_table_to_departament(JamiVault)
    table = filter_tables(filter_slug, table)

    page_obj = paginate_page(request, table)
    context = get_context_data(page_obj, 'Жами свод', third_department_tables_menu, table)
    return render(request, src['jami'], context)


@login_required
def add_data_table_jami(request):
    table_data = show_data_table(request, JamiVault)
    page_obj = paginate_page(request, table_data)
    if request.method == 'POST':
        form = TableJamiForm(request.POST)
        if form.is_valid():
            try:
                JamiVault.objects.create(**form.cleaned_data, district=request.user.district)
                return redirect('table_jami')
            except:
                form.add_error(None, 'Ошибка добавления данных')
    else:
        form = TableJamiForm()
    context = make_context_by_form('Жами свод', form, third_department_tables_menu, page_obj)
    return render(request, 'mainapp/forms/third_departament/form_jami.html', context)


# Свод Чорак

def get_data_table_quarter(request):
    if get_group_vault_id(request):
        table_data = show_data_table_to_departament(QuarterVault)
    else:
        table_data = show_data_table(request, QuarterVault)
    page_obj = paginate_page(request, table_data)
    context = get_context_data(page_obj, 'Cвод чорак', third_department_tables_menu, table_data)
    return render(request, src['quarter'], context)


def table_filter_table_quarter(request, filter_slug):
    if not get_group_vault_id(request):
        table = show_data_table(request, QuarterVault)
    else:
        table = show_data_table_to_departament(QuarterVault)
    table = filter_tables(filter_slug, table)

    page_obj = paginate_page(request, table)
    context = get_context_data(page_obj, 'Cвод чорак', third_department_tables_menu, table)
    return render(request, src['quarter'], context)


@login_required
def add_data_table_quarter(request):
    table_data = show_data_table(request, QuarterVault)
    page_obj = paginate_page(request, table_data)
    if request.method == 'POST':
        form = TableQuarterForm(request.POST)
        if form.is_valid():
            try:
                QuarterVault.objects.create(**form.cleaned_data, district=request.user.district)
                return redirect('table_quarter')
            except:
                form.add_error(None, 'Ошибка добавления данных')
    else:
        form = TableQuarterForm()
    context = make_context_by_form('Cвод чорак', form, third_department_tables_menu, page_obj)
    return render(request, 'mainapp/forms/third_departament/form_quarter.html', context)


# Свод Ойлар
def get_data_table_month(request):
    if get_group_vault_id(request):
        table_data = show_data_table_to_departament(MonthVault)
    else:
        table_data = show_data_table(request, MonthVault)
    page_obj = paginate_page(request, table_data)
    context = get_context_data(page_obj, 'Cвод ойлар', third_department_tables_menu, table_data)
    return render(request, src['monthly'], context)


def table_filter_table_month(request, filter_slug):
    if not get_group_vault_id(request):
        table = show_data_table(request, MonthVault)
    else:
        table = show_data_table_to_departament(MonthVault)
    table = filter_tables(filter_slug, table)

    page_obj = paginate_page(request, table)
    context = get_context_data(page_obj, 'Cвод ойлар', third_department_tables_menu, table)
    return render(request, src['monthly'], context)


@login_required
def add_data_table_month(request):
    table_data = show_data_table(request, MonthVault)
    page_obj = paginate_page(request, table_data)
    if request.method == 'POST':
        form = TableMonthForm(request.POST)
        if form.is_valid():
            try:
                MonthVault.objects.create(**form.cleaned_data, district=request.user.district)
                return redirect('table_monthly')
            except:
                form.add_error(None, 'Ошибка добавления данных')
    else:
        form = TableMonthForm()
    context = make_context_by_form('Cвод ойлар', form, third_department_tables_menu, page_obj)
    return render(request, 'mainapp/forms/third_departament/form_monthly.html', context)


# Свод Банк
def get_data_table_bank(request):
    if get_group_vault_id(request):
        table_data = show_data_table_to_departament(BankVault)
    else:
        table_data = show_data_table(request, BankVault)
    page_obj = paginate_page(request, table_data)
    context = get_context_data(page_obj, 'Cвод банк', third_department_tables_menu, table_data)
    return render(request, src['bank'], context)


def table_filter_table_bank(request, filter_slug):
    if not get_group_vault_id(request):
        table = show_data_table(request, BankVault)
    else:
        table = show_data_table_to_departament(BankVault)
    table = filter_tables(filter_slug, table)

    page_obj = paginate_page(request, table)
    context = get_context_data(page_obj, 'Cвод банк', third_department_tables_menu, table)
    return render(request, src['bank'], context)


@login_required
def add_data_table_bank(request):
    table_data = show_data_table(request, BankVault)
    page_obj = paginate_page(request, table_data)
    if request.method == 'POST':
        form = TableBankForm(request.POST)
        if form.is_valid():
            try:
                BankVault.objects.create(**form.cleaned_data, district=request.user.district)
                return redirect('table_bank')
            except:
                form.add_error(None, 'Ошибка добавления данных')
    else:
        form = TableBankForm()
    context = make_context_by_form('Cвод банк', form, third_department_tables_menu, page_obj)
    return render(request, 'mainapp/forms/third_departament/form_bank.html', context)


# Свод Режа

def get_data_table_reja(request):
    if get_group_vault_id(request):
        table_data = show_data_table_to_departament(RejaVault)
    else:
        table_data = show_data_table(request, RejaVault)
    page_obj = paginate_page(request, table_data)
    context = get_context_data(page_obj, 'Cвод режа', third_department_tables_menu, table_data)
    return render(request, src['reja'], context)


def table_filter_table_reja(request, filter_slug):
    if not get_group_vault_id(request):
        table = show_data_table(request, RejaVault)
    else:
        table = show_data_table_to_departament(RejaVault)
    table = filter_tables(filter_slug, table)

    page_obj = paginate_page(request, table)
    context = get_context_data(page_obj, 'Cвод режа', third_department_tables_menu, table)
    return render(request, src['reja'], context)


@login_required
def add_data_table_reja(request):
    table_data = show_data_table(request, RejaVault)
    page_obj = paginate_page(request, table_data)
    if request.method == 'POST':
        form = TableRejaForm(request.POST)
        if form.is_valid():
            try:
                RejaVault.objects.create(**form.cleaned_data, district=request.user.district)
                return redirect('table_reja')
            except:
                form.add_error(None, 'Ошибка добавления данных')
    else:
        form = TableRejaForm()
    context = make_context_by_form('Cвод режа', form, third_department_tables_menu, page_obj)
    return render(request, 'mainapp/forms/third_departament/form_reja.html', context)


# Свод Tarmok

def get_data_table_tarmok(request):
    if get_group_vault_id(request):
        table_data = show_data_table_to_departament(TarmokVault)
    else:
        table_data = show_data_table(request, TarmokVault)
    page_obj = paginate_page(request, table_data)
    context = get_context_data(page_obj, 'Cвод тармок', third_department_tables_menu, table_data)
    return render(request, src['tarmok'], context)


def table_filter_table_tarmok(request, filter_slug):
    if not get_group_vault_id(request):
        table = show_data_table(request, TarmokVault)
    else:
        table = show_data_table_to_departament(TarmokVault)
    table = filter_tables(filter_slug, table)

    page_obj = paginate_page(request, table)
    context = get_context_data(page_obj, 'Cвод тармок', third_department_tables_menu, table)
    return render(request, src['tarmok'], context)


@login_required
def add_data_table_tarmok(request):
    table_data = show_data_table(request, TarmokVault)
    page_obj = paginate_page(request, table_data)
    if request.method == 'POST':
        form = TableTarmokForm(request.POST)
        if form.is_valid():
            try:
                TarmokVault.objects.create(**form.cleaned_data, district=request.user.district)
                return redirect('table_tarmok')
            except:
                form.add_error(None, 'Ошибка добавления данных')
    else:
        form = TableTarmokForm()
    context = make_context_by_form('Cвод тармок', form, third_department_tables_menu, page_obj)
    return render(request, 'mainapp/forms/third_departament/form_tarmok.html', context)
