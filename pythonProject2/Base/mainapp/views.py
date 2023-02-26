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
# def get_department(request, del_group_id, page_title, department_name, department_url):
#     if del_group_id(request):
#         # raise Exception('У вас нету доступа к этому департаменту')
#         messages.error(request, 'У вас нету доступа к этому департаменту')
#         return redirect('/')
#     else:
#         context = {
#             'title': page_title,
#             f'{department_name}': department_name
#         }
#         return render(request, f'mainapp/departments/{department_url}.html', context)


# @login_required
# def get_department_projects(request):
#     return get_department(request, del_group_loiha_id, 'Отдел - Лоиха', projects_department, 'projects_department')

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
            'title': 'Отдел экспорта',  # Отдел - 2
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
            'title': 'Сводный отдел',  # Отдел - 3
            'third_department_tables_menu': third_department_tables_menu
        }
        return render(request, 'mainapp/departments/department_3.html', context)


@login_required
def get_department_4(request):
    if del_group_post_monitoring_id(request):
        messages.error(request, 'У вас нету доступа к этому департаменту')
        return redirect('/')
    else:
        context = {
            'title': 'Отдел постмониторинга',
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


def export_excel_loiha41(request, filter_slug):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = f'attachment; filename=table{str(datetime.now())}.xls'
    # response['Content-Disposition'] = 'attachment; filename=table' + \
    #                                   str(datetime.now()) + '.xls'

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
        ws.write_merge(0, 0, 0, 25, f'{request.user.district}, Илова-4.1', cell_title)
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
            "Ҳудудлар",
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

    rows = filter_export_loiha_tables(request, filter_slug, Loiha41, fields, department_fields)

    for row in rows:
        row_num += 1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)
    return response


def export_excel_loiha52(request, filter_slug):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = f'attachment; filename=table{str(datetime.now())}.xls'

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
        ws.write_merge(0, 0, 0, 12, f'{request.user.district}, Илова-5.2', cell_title)
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
            "Ҳудудлар",
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

    rows = filter_export_loiha_tables(request, filter_slug, Loiha52, fields, department_fields)

    for row in rows:
        row_num += 1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)
    return response


def export_excel_loiha14(request, filter_slug):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = f'attachment; filename=table{str(datetime.now())}.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('table', cell_overwrite_ok=True)
    row_num = 3  # с какой строки начинается наша таблица
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    cell_style = xlwt.easyxf("font: bold on; align: vert center, horiz center")
    cell_title = xlwt.easyxf("font: bold on, height 280; align: vert center, horiz left")
    # cell_style = xlwt.easyxf("align: vert centre, horiz center")

    # ws.title = 'Илова-4.1' Поменять на один если добавлять столбик в начале
    if not get_group_loiha_id(request):
        ws.write_merge(0, 0, 0, 13, f'{request.user.district}, Илова-14', cell_title)
        ws.write_merge(1, 2, 0, 2, 'Доступная информация', cell_style)
        ws.write_merge(1, 1, 3, 9, 'Процесс реализации запланированных проектов', cell_style)
        ws.write_merge(1, 1, 10, 12, 'Финансирование', cell_style)

        ws.write_merge(2, 2, 5, 7, 'Из них', cell_style)
        ws.write_merge(2, 2, 11, 12, 'Иностранные', cell_style)
    else:
        ws.write_merge(0, 0, 0, 14, 'Илова-14', cell_title)
        # ws.write_merge(1, 2, 0, 1, 'Район', cell_style)
        ws.write_merge(1, 2, 1, 3, 'Доступная информация', cell_style)
        ws.write_merge(1, 1, 4, 10, 'Процесс реализации запланированных проектов', cell_style)
        ws.write_merge(1, 1, 11, 13, 'Финансирование', cell_style)

        ws.write_merge(2, 2, 6, 8, 'Из них', cell_style)
        ws.write_merge(2, 2, 12, 13, 'Иностранные', cell_style)

    # ws.col(0).width = 4500
    # ws.col(21).width = 5000

    # "Район",
    columns_list = ["Организация",
                    "Род деятельности",
                    "Имеющиеся рабочие места",
                    "Проектная деятельность",
                    "Оценка (млрд долл)",
                    "Собственные средства",
                    "Банковский кредит",
                    "Иностранные инвестиции",
                    "Созданные рабочие места",
                    "Обьем экспорта (млрд долл)",
                    "Название банка",
                    "Название страны",
                    "Название организации",
                    ]

    if not get_group_loiha_id(request):
        columns = [
            *columns_list
        ]
    else:
        columns = [
            "Ҳудудлар",
            *columns_list
        ]

    for col_num in range(len(columns)):
        ws.col(col_num).width = 3800
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    # date_style = xlwt.XFStyle()
    # time_create = datetime.strftime('time_create', '%d/%m/%y %h:%m:%s')
    fields = [
        'organization_available_information',
        'kind_of_activity_available_information',
        'available_jobs_available_information',
        'project_activity_at_work',
        'grade_at_work',
        'own_funds_grade_at_work',
        'bank_loan_grade_at_work',
        'sources_sources_of_financing',
        'created_new_jobs_at_work',
        'export_volume_at_work',
        'name_bank_financing',
        'name_country_financing',
        'organization_name_foreign_financing'
    ]

    department_fields = [
        'district__district',
        *fields
    ]

    rows = filter_export_loiha_tables(request, filter_slug, Loiha14, fields, department_fields)

    for row in rows:
        row_num += 1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)
    return response


def export_excel_loiha131(request, filter_slug):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = f'attachment; filename=table{str(datetime.now())}.xls'

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
        ws.write_merge(0, 0, 0, 10, f'{request.user.district}, Илова-13.1', cell_title)
        ws.write_merge(1, 1, 1, 8, 'Из них', cell_style)
    else:
        ws.write_merge(0, 0, 0, 11, 'Илова-13.1', cell_title)
        ws.write_merge(1, 1, 2, 9, 'Из них', cell_style)

    # "Район",
    columns_list = [
        "Известные проблемы",
        "Банк",
        "Земля и здание",
        "Коммунальные",
        "Таможня",
        "Налог",
        "Разрешения",
        "Бюрокартический барьер",
        "Другое",
        "Решенные проблемы"
    ]

    if not get_group_loiha_id(request):
        columns = [
            *columns_list
        ]
    else:
        columns = [
            "Ҳудудлар",
            *columns_list
        ]

    for col_num in range(len(columns)):
        ws.col(col_num).width = 3800
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    # date_style = xlwt.XFStyle()
    # time_create = datetime.strftime('time_create', '%d/%m/%y %h:%m:%s')
    fields = [
        'identified_problems',
        'bank_identified_problems',
        'land_and_building_identified_problems',
        'public_services_identified_problems',
        'customs_identified_problems',
        'tax_identified_problems',
        'permission_identified_problems',
        'bureaucratic_obstacles_identified_problems',
        'other_identified_problems',
        'resolved_problems_identified_problems',
    ]

    department_fields = [
        'district__district',
        *fields
    ]

    rows = filter_export_loiha_tables(request, filter_slug, Loiha131, fields, department_fields)

    for row in rows:
        row_num += 1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)
    return response


def export_excel_loiha122(request, filter_slug):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = f'attachment; filename=table{str(datetime.now())}.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('table', cell_overwrite_ok=True)
    row_num = 3  # с какой строки начинается наша таблица
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    cell_style = xlwt.easyxf("font: bold on; align: vert center, horiz center")
    cell_title = xlwt.easyxf("font: bold on, height 280; align: vert center, horiz left")
    # cell_style = xlwt.easyxf("align: vert centre, horiz center")

    # ws.title = 'Илова-4.1' Поменять на один если добавлять столбик в начале
    if not get_group_loiha_id(request):
        ws.write_merge(0, 0, 0, 12, f'{request.user.district}, Илова-12.2', cell_title)
        ws.write_merge(1, 1, 1, 8, 'в процессе', cell_style)
        ws.write_merge(1, 1, 9, 11, 'Финансирование', cell_style)

        ws.write_merge(2, 2, 4, 6, 'Из них', cell_style)
        ws.write_merge(2, 2, 10, 11, 'Иностранные', cell_style)
    else:
        ws.write_merge(0, 0, 0, 13, 'Илова-12.2', cell_title)
        ws.write_merge(1, 1, 2, 9, 'в процессе', cell_style)
        ws.write_merge(1, 1, 10, 12, 'Финансирование', cell_style)

        ws.write_merge(2, 2, 5, 7, 'Из них', cell_style)
        ws.write_merge(2, 2, 11, 12, 'Иностранные', cell_style)

    # "Район",
    columns_list = [
        "Сформированные советы",
        "Проекты",
        "Производсвенные мощности",
        "Оценка",
        "Собственные средства",
        "Банковский кредит",
        "Иностранные инвестиции",
        "Уровнь работы",
        "Обьем экспорта",
        "Название банка",
        "Название страны",
        "название организации",
    ]

    if not get_group_loiha_id(request):
        columns = [
            *columns_list
        ]
    else:
        columns = [
            "Ҳудудлар",
            *columns_list
        ]

    for col_num in range(len(columns)):
        ws.col(col_num).width = 3800
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    # date_style = xlwt.XFStyle()
    # time_create = datetime.strftime('time_create', '%d/%m/%y %h:%m:%s')
    fields = [
        'formed_tips',
        'projects_at_work',
        'production_capacity_at_work',
        'grade_at_work',
        'own_funds_grade_at_work',
        'bank_loan_grade_at_work',
        'foreign_investments_grade_at_work',
        'workplace_at_work',
        'export_volume_at_work',
        'name_bank_financing',
        'name_country_financing',
        'organization_name_foreign_financing'
    ]

    department_fields = [
        'district__district',
        *fields
    ]

    rows = filter_export_loiha_tables(request, filter_slug, Loiha122, fields, department_fields)

    for row in rows:
        row_num += 1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)
    return response


def export_excel_loiha121(request, filter_slug):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = f'attachment; filename=table{str(datetime.now())}.xls'

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
        ws.write_merge(0, 0, 0, 11, f'{request.user.district}, Илова-12.1', cell_title)
        ws.write_merge(1, 1, 2, 3, 'Приоритетные цели', cell_style)
        ws.write_merge(1, 1, 4, 10, 'Заявленные результаты', cell_style)
    else:
        ws.write_merge(0, 0, 0, 12, 'Илова-12.1', cell_title)
        ws.write_merge(1, 1, 3, 4, 'Приоритетные цели', cell_style)
        ws.write_merge(1, 1, 5, 11, 'Заявленные результаты', cell_style)
    # "Район",
    columns_list = [
        "Утвержденные холдинговые компании количество",
        "Предложения предпринимателей(ф.и.о)",
        "Название организации",
        "Тип деятельности",
        "Проекты",
        "Производственная мощность",
        "Оценка",
        "Рабочее место",
        "Экспорт",
        "Другое",
        "Финансирование",
    ]

    if not get_group_loiha_id(request):
        columns = [
            *columns_list
        ]
    else:
        columns = [
            "Ҳудудлар",
            *columns_list
        ]

    for col_num in range(len(columns)):
        ws.col(col_num).width = 3800
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    # date_style = xlwt.XFStyle()
    # time_create = datetime.strftime('time_create', '%d/%m/%y %h:%m:%s')
    fields = [
        'approved_holding_companies',
        'entrepreneur',
        'names_of_organizations_priority',
        'type_of_activity_priority',
        'projects_the_stated_results',
        'productive_capacity_stated_results',
        'grade_stated_results',
        'workplace_stated_results',
        'export_stated_results',
        'other_stated_results',
        'financing',
    ]

    department_fields = [
        'district__district',
        *fields
    ]

    rows = filter_export_loiha_tables(request, filter_slug, Loiha121, fields, department_fields)

    for row in rows:
        row_num += 1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)
    return response


def export_excel_loiha12(request, filter_slug):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = f'attachment; filename=table{str(datetime.now())}.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('table', cell_overwrite_ok=True)
    row_num = 3  # с какой строки начинается наша таблица
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    cell_style = xlwt.easyxf("font: bold on; align: vert center, horiz center")
    cell_title = xlwt.easyxf("font: bold on, height 280; align: vert center, horiz left")
    # cell_style = xlwt.easyxf("align: vert centre, horiz center")

    # ws.title = 'Илова-4.1' Поменять на один если добавлять столбик в начале
    if not get_group_loiha_id(request):
        ws.write_merge(0, 0, 0, 12, f'{request.user.district}, Илова-12', cell_title)
        ws.write_merge(1, 1, 3, 11, 'Из них', cell_style)

        ws.write_merge(2, 2, 3, 5, 'Выбранные проекты', cell_style)
        ws.write_merge(2, 2, 6, 8, 'В процессе', cell_style)
        ws.write_merge(2, 2, 9, 11, 'Будут завершены к концу года', cell_style)
    else:
        ws.write_merge(0, 0, 0, 13, 'Илова-12', cell_title)
        ws.write_merge(1, 1, 4, 12, 'Из них', cell_style)

        ws.write_merge(2, 2, 4, 6, 'Выбранные проекты', cell_style)
        ws.write_merge(2, 2, 7, 9, 'В процессе', cell_style)
        ws.write_merge(2, 2, 10, 12, 'Будут завершены к концу года', cell_style)
    # "Район",
    columns_list = [
        "Все проекты",
        "Оценка(млрд долл)",
        "Рабочее место",
        "Проекты",
        "Оценка",
        "Рабочее место",
        "Проекты",
        "Оценка (млрд долл)",
        "Рабочее место",
        "Проекты",
        "Оценка (млрд долл)",
        "Рабочее место",
    ]

    if not get_group_loiha_id(request):
        columns = [
            *columns_list
        ]
    else:
        columns = [
            "Ҳудудлар",
            *columns_list
        ]

    for col_num in range(len(columns)):
        ws.col(col_num).width = 3800
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    # date_style = xlwt.XFStyle()
    # time_create = datetime.strftime('time_create', '%d/%m/%y %h:%m:%s')
    fields = [
        'all_projects',
        'grade',
        'workplace',
        'projects_selected_projects_from_all_projects',
        'grade_selected_projects_from_all_projects',
        'workplace_selected_projects_from_all_projects',
        'all_projects_at_work_from_all_projects',
        'grade_at_work_from_all_projects',
        'workplace_at_work_from_all_projects',
        'all_projects_will_be_completed_end_the_year_from_all_projects',
        'grade_will_be_completed_end_the_year_all_projects',
        'workplace_will_be_completed_end_the_year_all_projects',
    ]

    department_fields = [
        'district__district',
        *fields
    ]

    rows = filter_export_loiha_tables(request, filter_slug, Loiha12, fields, department_fields)

    for row in rows:
        row_num += 1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)
    return response


def export_excel_loiha10(request, filter_slug):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = f'attachment; filename=table{str(datetime.now())}.xls'

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
        ws.write_merge(0, 0, 0, 20, f'{request.user.district}, Илова-10', cell_title)
        ws.write_merge(1, 1, 2, 3, 'Из них', cell_style)

        ws.write_merge(1, 1, 5, 16, 'Специализация', cell_style)
    else:
        ws.write_merge(0, 0, 0, 21, 'Илова-10', cell_title)
        ws.write_merge(1, 1, 3, 4, 'Из них', cell_style)
        ws.write_merge(1, 1, 6, 17, 'Специализация', cell_style)
    # "Район",
    columns_list = [
        "насленный пункт (количество)",
        "Жилые дома (количество)",
        "Желающие заняться предпринимательством (количество)",
        "процентное соотношение",
        "дома занятые в секторе",
        "животноводство",
        "птицеводство",
        "кроликоведение",
        "пчеловодство",
        "фермерство",
        "садоводство",
        "парники",
        "преподование",
        "мелькое производство",
        "туризм",
        "услуги",
        "другие",
        "железная тетрадь оставшиеся",
        "молодёжная тетрадь оставшиеся",
        "женская тетрадь оставшиеся",
    ]

    if not get_group_loiha_id(request):
        columns = [
            *columns_list
        ]
    else:
        columns = [
            "Ҳудудлар",
            *columns_list
        ]

    for col_num in range(len(columns)):
        ws.col(col_num).width = 3800
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    # date_style = xlwt.XFStyle()
    # time_create = datetime.strftime('time_create', '%d/%m/%y %h:%m:%s')
    fields = [
        'locality_amount',
        'residential_buildings_amount',
        'who_want_to_do_business_residential_buildings',
        'percent_residential_buildings',
        'employed_in_the_sector',
        'animal_husbandry_speciality',
        'poultry_farming_specialty',
        'rabbing_breeding_specialty',
        'Beekeeping_specialty',
        'farm_specialty',
        'gardening_specialty',
        'greenhouses_specialty',
        'teaching_specialty',
        'small_production_specialty',
        'tourism_specialty',
        'services_specialty',
        'other_specialty',
        'remaining_on_the_iron_notebook',
        'remaining_on_the_youth_notebook',
        'remaining_on_the_womens_notebook',
    ]

    department_fields = [
        'district__district',
        *fields
    ]

    rows = filter_export_loiha_tables(request, filter_slug, Loiha10, fields, department_fields)

    for row in rows:
        row_num += 1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)
    return response


def export_excel_loiha6(request, filter_slug):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = f'attachment; filename=table{str(datetime.now())}.xls'

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
        ws.write_merge(0, 0, 0, 11, f'{request.user.district}, Илова-6', cell_title)
        ws.write_merge(1, 1, 1, 4, 'Из них', cell_style)
        ws.write_merge(1, 1, 6, 7, 'Из них', cell_style)
        ws.write_merge(1, 1, 9, 10, 'Из них', cell_style)
    else:
        ws.write_merge(0, 0, 0, 12, 'Илова-6', cell_title)
        ws.write_merge(1, 1, 2, 5, 'Из них', cell_style)
        ws.write_merge(1, 1, 7, 8, 'Из них', cell_style)
        ws.write_merge(1, 1, 10, 11, 'Из них', cell_style)

    # "Район",
    columns_list = [
        "Пустующие объекты",
        "адрес",
        "владелец",
        "государственное имущество (количество)",
        "частное имущуство (количество)",
        "Неиспользуемые производственные площадки(Га)",
        "ориентированное на сельское хозяйство(Га)",
        "ориентированное на производство(Га)",
        "Предложения по инвестициям (источники)",
        "Предварительная стоимость проекта(млн.долл)",
        "количество созданных навых рабочих мест",
    ]

    if not get_group_loiha_id(request):
        columns = [
            *columns_list
        ]
    else:
        columns = [
            "Ҳудудлар",
            *columns_list
        ]

    for col_num in range(len(columns)):
        ws.col(col_num).width = 3800
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    # date_style = xlwt.XFStyle()
    # time_create = datetime.strftime('time_create', '%d/%m/%y %h:%m:%s')
    fields = [
        'empty_objects',
        'adress_empty_objects',
        'owner_empty_objects',
        'state_property_amount_empty_objects',
        'private_property_amount_empty_objects',
        'unused_production_sites',
        'focused_on_agriculture_unused_production_sites',
        'focused_on_production_unused_production_sites',
        'Investment_proposals_sources',
        'preliminary_project_cost_bil_sum_sources',
        'new_jobs_created_amount_sources'
    ]

    department_fields = [
        'district__district',
        *fields
    ]

    rows = filter_export_loiha_tables(request, filter_slug, Loiha6, fields, department_fields)

    for row in rows:
        row_num += 1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)
    return response


def export_excel_loiha13(request, filter_slug):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = f'attachment; filename=table{str(datetime.now())}.xls'

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
        ws.write_merge(0, 0, 0, 7, f'{request.user.district}, Илова-13', cell_title)
        ws.write_merge(1, 1, 3, 4, 'Источники финансирования', cell_style)

    else:
        ws.write_merge(0, 0, 0, 8, 'Илова-13', cell_title)
        ws.write_merge(1, 1, 4, 5, 'Источники финансирования', cell_style)

    # "Район",
    columns_list = [
        "Название проекта",
        "Проектная деятельность",
        "Проектная мощность",
        "Оценка в миллиардах долларах",
        "Иностранные инвестиции",
        "Cозданные новые рабочие места",
        "Источники",
    ]

    if not get_group_loiha_id(request):
        columns = [
            *columns_list
        ]
    else:
        columns = [
            "Ҳудудлар",
            *columns_list
        ]

    for col_num in range(len(columns)):
        ws.col(col_num).width = 3800
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    # date_style = xlwt.XFStyle()
    # time_create = datetime.strftime('time_create', '%d/%m/%y %h:%m:%s')
    fields = [
        'project_name',
        'project_activity',
        'project_capacity',
        'grate_sources_of_financing',
        'foreign_financing_grate_sources_of_financing',
        'sources_sources_of_financing',
        'created_new_jobs'
    ]

    department_fields = [
        'district__district',
        *fields
    ]

    rows = filter_export_loiha_tables(request, filter_slug, Loiha13, fields, department_fields)

    for row in rows:
        row_num += 1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)
    return response


# export second department
def export_excel_sanoat(request, filter_slug):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = f'attachment; filename=table{str(datetime.now())}.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('table', cell_overwrite_ok=True)
    row_num = 1  # с какой строки начинается наша таблица
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    cell_style = xlwt.easyxf("font: bold on; align: vert center, horiz center")
    cell_title = xlwt.easyxf("font: bold on, height 280; align: vert center, horiz left")
    # cell_style = xlwt.easyxf("align: vert centre, horiz center")

    # ws.title = 'Илова-4.1' Поменять на один если добавлять столбик в начале
    if not get_group_export_id(request):
        ws.write_merge(0, 0, 0, 18, f'{request.user.district}, Sanoat', cell_title)
    else:
        ws.write_merge(0, 0, 0, 19, 'Sanoat', cell_title)

    # ws.col(0).width = 4500
    # ws.col(21).width = 5000

    # "Район",
    columns_list = [
        "ИНН отправ./получ.",
        "ИНН",
        "Наим. отправителя",
        "Адрес отправителя",
        "Наим. получателя",
        "Адрес получателя",
        "Инн лица отв. за финансовое урегулирование",
        "лицо отв. за финансовое урегулирование",
        "Адрес лица отв. за финансовое урегулирование",
        "Валюта контракта",
        "Фактурная стоимость",
        "Код товара",
        "Наим. товара",
        "Вес. нетто",
        "Стат. стоимость",
        "Номер и дата контракта",
        "ИДН",
        "Страна отправления/назначения",
        "Дата выпуска",
    ]

    if not get_group_export_id(request):
        columns = [
            *columns_list
        ]
    else:
        columns = [
            "Ҳудудлар",
            *columns_list
        ]

    for col_num in range(len(columns)):
        ws.col(col_num).width = 3800
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    # date_style = xlwt.XFStyle()
    # time_create = datetime.strftime('time_create', '%d/%m/%y %h:%m:%s')
    fields = [
        'inn_of_sender_or_recipient',
        'inn',
        'name_of_sender',
        'address_of_sender',
        'name_of_recipient',
        'address_of_recipient',
        'financial_responsible_inn',
        'face_responsible_for_finance',
        'address_of_face_responsible_for_finance',
        'currency_of_contract',
        'invoice_value',
        'code_of_goods',
        'name_of_goods',
        'weight_netto',
        'stat_price',
        'number_and_date_of_contract',
        'idn',
        'destination_country',
        'date_of_issue'
    ]

    department_fields = [
        'district__district',
        *fields
    ]

    rows = filter_export_export_tables(request, filter_slug, Sanoat, fields, department_fields)

    for row in rows:
        row_num += 1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)
    return response


def export_excel_kx(request, filter_slug):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = f'attachment; filename=table{str(datetime.now())}.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('table', cell_overwrite_ok=True)
    row_num = 1  # с какой строки начинается наша таблица
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    cell_style = xlwt.easyxf("font: bold on; align: vert center, horiz center")
    cell_title = xlwt.easyxf("font: bold on, height 280; align: vert center, horiz left")
    # cell_style = xlwt.easyxf("align: vert centre, horiz center")

    # ws.title = 'Илова-4.1' Поменять на один если добавлять столбик в начале
    if not get_group_export_id(request):
        ws.write_merge(0, 0, 0, 19, f'{request.user.district}, KX', cell_title)
    else:
        ws.write_merge(0, 0, 0, 20, 'KX', cell_title)

    # ws.col(0).width = 4500
    # ws.col(21).width = 5000

    # "Район",
    columns_list = [
        "ИНН отправ./получ.",
        "ИНН",
        "Наим. отправителя",
        "Адрес отправителя",
        "Наим. получателя",
        "Адрес получателя",
        "Инн лица отв. за финансовое урегулирование",
        "лицо отв. за финансовое урегулирование",
        "Адрес лица отв. за финансовое урегулирование",
        "Валюта контракта",
        "Фактурная стоимость",
        "Код товара",
        "Наим. товара",
        "Вес. нетто",
        "Тонна",
        "Стат. стоимость",
        "Номер и дата контракта",
        "ИДН",
        "Страна отправления/назначения",
        "Дата выпуска",
    ]

    if not get_group_export_id(request):
        columns = [
            *columns_list
        ]
    else:
        columns = [
            "Ҳудудлар",
            *columns_list
        ]

    for col_num in range(len(columns)):
        ws.col(col_num).width = 3800
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    # date_style = xlwt.XFStyle()
    # time_create = datetime.strftime('time_create', '%d/%m/%y %h:%m:%s')
    fields = [
        'inn_of_sender_or_recipient',
        'inn',
        'name_of_sender',
        'address_of_sender',
        'name_of_recipient',
        'address_of_recipient',
        'financial_responsible_inn',
        'face_responsible_for_finance',
        'address_of_face_responsible_for_finance',
        'currency_of_contract',
        'invoice_value',
        'code_of_goods',
        'name_of_goods',
        'weight_netto',
        'ton',
        'stat_price',
        'number_and_date_of_contract',
        'idn',
        'destination_country',
        'date_of_issue'
    ]

    department_fields = [
        'district__district',
        *fields
    ]

    rows = filter_export_export_tables(request, filter_slug, KH, fields, department_fields)

    for row in rows:
        row_num += 1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)
    return response


def export_excel_table1(request, filter_slug):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = f'attachment; filename=table{str(datetime.now())}.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('table', cell_overwrite_ok=True)
    row_num = 3  # с какой строки начинается наша таблица
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    cell_style = xlwt.easyxf("font: bold on; align: vert center, horiz center")
    cell_title = xlwt.easyxf("font: bold on, height 280; align: vert center, horiz left")
    # cell_style = xlwt.easyxf("align: vert centre, horiz center")

    # ws.title = 'Илова-4.1' Поменять на один если добавлять столбик в начале
    if not get_group_export_id(request):
        ws.write_merge(0, 0, 0, 45, f'{request.user.district}, Таблица 1', cell_title)
        ws.write_merge(1, 1, 5, 8, 'Всего', cell_style)
        ws.write_merge(1, 1, 9, 11, 'Январь-март', cell_style)
        ws.write_merge(1, 1, 12, 14, 'Январь', cell_style)
        ws.write_merge(1, 1, 15, 17, 'Февраль', cell_style)
        ws.write_merge(1, 1, 18, 20, 'Март', cell_style)
        ws.write_merge(1, 1, 21, 23, 'Январь-Апрель', cell_style)
        ws.write_merge(1, 1, 24, 26, 'Январь-Май', cell_style)
        ws.write_merge(1, 1, 27, 29, 'Январь-Июнь', cell_style)
        ws.write_merge(1, 1, 30, 32, 'Январь-Июль', cell_style)
        ws.write_merge(1, 1, 33, 35, 'Январь-Август', cell_style)
        ws.write_merge(1, 1, 36, 38, 'Январь-Сентябрь', cell_style)
        ws.write_merge(1, 1, 39, 41, '24-окт', cell_style)
        ws.write_merge(1, 1, 42, 44, 'Октябрь', cell_style)

        ws.write_merge(2, 2, 7, 8, 'плод', cell_style)
        ws.write_merge(2, 2, 10, 11, 'плод', cell_style)
        ws.write_merge(2, 2, 13, 14, 'плод', cell_style)
        ws.write_merge(2, 2, 16, 17, 'плод', cell_style)
        ws.write_merge(2, 2, 19, 20, 'плод', cell_style)
        ws.write_merge(2, 2, 22, 23, 'плод', cell_style)
        ws.write_merge(2, 2, 25, 26, 'плод', cell_style)
        ws.write_merge(2, 2, 28, 29, 'плод', cell_style)
        ws.write_merge(2, 2, 31, 32, 'плод', cell_style)
        ws.write_merge(2, 2, 34, 35, 'плод', cell_style)
        ws.write_merge(2, 2, 37, 38, 'плод', cell_style)
        ws.write_merge(2, 2, 40, 41, 'плод', cell_style)
        ws.write_merge(2, 2, 43, 44, 'плод', cell_style)

    else:
        ws.write_merge(0, 0, 0, 46, 'Таблица 1', cell_title)
        ws.write_merge(1, 1, 6, 9, 'Всего', cell_style)
        ws.write_merge(1, 1, 10, 12, 'Январь-март', cell_style)
        ws.write_merge(1, 1, 13, 15, 'Январь', cell_style)
        ws.write_merge(1, 1, 16, 18, 'Февраль', cell_style)
        ws.write_merge(1, 1, 19, 21, 'Март', cell_style)

        ws.write_merge(1, 1, 22, 24, 'Январь-Апрель', cell_style)
        ws.write_merge(1, 1, 25, 27, 'Январь-Май', cell_style)
        ws.write_merge(1, 1, 28, 30, 'Январь-Июнь', cell_style)
        ws.write_merge(1, 1, 31, 33, 'Январь-Июль', cell_style)
        ws.write_merge(1, 1, 34, 36, 'Январь-Август', cell_style)
        ws.write_merge(1, 1, 37, 39, 'Январь-Сентябрь', cell_style)
        ws.write_merge(1, 1, 40, 42, '24-окт', cell_style)
        ws.write_merge(1, 1, 43, 45, 'Октябрь', cell_style)

        ws.write_merge(2, 2, 8, 9, 'плод', cell_style)
        ws.write_merge(2, 2, 11, 12, 'плод', cell_style)
        ws.write_merge(2, 2, 14, 15, 'плод', cell_style)
        ws.write_merge(2, 2, 17, 18, 'плод', cell_style)
        ws.write_merge(2, 2, 20, 21, 'плод', cell_style)
        ws.write_merge(2, 2, 23, 24, 'плод', cell_style)
        ws.write_merge(2, 2, 26, 27, 'плод', cell_style)
        ws.write_merge(2, 2, 29, 30, 'плод', cell_style)
        ws.write_merge(2, 2, 32, 33, 'плод', cell_style)
        ws.write_merge(2, 2, 35, 36, 'плод', cell_style)
        ws.write_merge(2, 2, 38, 39, 'плод', cell_style)
        ws.write_merge(2, 2, 41, 42, 'плод', cell_style)
        ws.write_merge(2, 2, 44, 45, 'плод', cell_style)

    # ws.col(0).width = 4500
    # ws.col(21).width = 5000

    # "Район",
    columns_list = [
        "",
        "",
        "Область",
        "",
        "Наименование организаций в разрезе регионов республики",
        "Всего",
        "пром",
        "тонна",
        "сумма",
        "пром",
        "тонна",
        "сумма",
        "пром",
        "тонна",
        "сумма",
        "пром",
        "тонна",
        "сумма",
        "пром",
        "тонна",
        "сумма",
        "пром",
        "тонна",
        "сумма",
        "пром",
        "тонна",
        "сумма",
        "пром",
        "тонна",
        "сумма",
        "пром",
        "тонна",
        "сумма",
        "пром",
        "тонна",
        "сумма",
        "пром",
        "тонна",
        "сумма",
        "пром",
        "тонна",
        "сумма",
        "пром",
        "тонна",
        "сумма",
        "Ички экспорт",
    ]

    if not get_group_export_id(request):
        columns = [
            *columns_list
        ]
    else:
        columns = [
            "Ҳудудлар",
            *columns_list
        ]

    for col_num in range(len(columns)):
        ws.col(col_num).width = 3800
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    # date_style = xlwt.XFStyle()
    # time_create = datetime.strftime('time_create', '%d/%m/%y %h:%m:%s')
    fields = [
        'table_id',
        'cell_name',
        'region',
        'date',
        'total',
        'total_total',
        'total_prom',
        'total_ton',
        'total_sum',
        'january_march_prom',
        'january_march_ton',
        'january_march_sum',
        'january_prom',
        'january_ton',
        'january_sum',
        'february_prom',
        'february_ton',
        'february_sum',
        'march_prom',
        'march_ton',
        'march_sum',
        'january_april_prom',
        'january_april_ton',
        'january_april_sum',
        'january_may_prom',
        'january_may_ton',
        'january_may_sum',
        'january_june_prom',
        'january_june_ton',
        'january_june_sum',
        'january_july_prom',
        'january_july_ton',
        'january_july_sum',
        'january_august_prom',
        'january_august_ton',
        'january_august_sum',
        'january_september_prom',
        'january_september_ton',
        'january_september_sum',
        'october_24_prom',
        'october_24_ton',
        'october_24_sum',
        'october_prom',
        'october_ton',
        'october_sum',
        'export',
    ]

    department_fields = [
        'district__district',
        *fields
    ]

    rows = filter_export_export_tables(request, filter_slug, FirstTable, fields, department_fields)

    for row in rows:
        row_num += 1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)
    return response


def export_excel_kunliu(request, filter_slug):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = f'attachment; filename=table{str(datetime.now())}.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('table', cell_overwrite_ok=True)
    row_num = 1  # с какой строки начинается наша таблица
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    cell_style = xlwt.easyxf("font: bold on; align: vert center, horiz center")
    cell_title = xlwt.easyxf("font: bold on, height 280; align: vert center, horiz left")
    # cell_style = xlwt.easyxf("align: vert centre, horiz center")

    # ws.title = 'Илова-4.1' Поменять на один если добавлять столбик в начале
    if not get_group_export_id(request):
        ws.write_merge(0, 0, 0, 3, f'{request.user.district}, кунлиу', cell_title)
    else:
        ws.write_merge(0, 0, 0, 4, 'кунлиу', cell_title)

    # ws.col(0).width = 4500
    # ws.col(21).width = 5000

    # "Район",
    columns_list = [
        "Дата прогноза",
        "Всего",
        "саноат маҳсулотлари",
        "мева-сабзавотлар",
    ]

    if not get_group_export_id(request):
        columns = [
            *columns_list
        ]
    else:
        columns = [
            "Ҳудудлар",
            *columns_list
        ]

    for col_num in range(len(columns)):
        ws.col(col_num).width = 3800
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    # date_style = xlwt.XFStyle()
    # time_create = datetime.strftime('time_create', '%d/%m/%y %h:%m:%s')
    fields = [
        'sanoat',
        'meva_sabz',
        'overall',
        'date_of_forecast',
    ]

    department_fields = [
        'district__district',
        *fields
    ]

    rows = filter_export_export_tables(request, filter_slug, Kunliu, fields, department_fields)

    for row in rows:
        row_num += 1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)
    return response


# export third department
def export_excel_bank(request, filter_slug):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = f'attachment; filename=table{str(datetime.now())}.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('table', cell_overwrite_ok=True)
    row_num = 3  # с какой строки начинается наша таблица
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    cell_style = xlwt.easyxf("font: bold on; align: vert center, horiz center")
    cell_title = xlwt.easyxf("font: bold on, height 280; align: vert center, horiz left")
    # cell_style = xlwt.easyxf("align: vert centre, horiz center")

    # ws.title = 'Илова-4.1' Поменять на один если добавлять столбик в начале
    if not get_group_vault_id(request):
        ws.write_merge(0, 0, 0, 22, f'{request.user.district}, Cвод банк', cell_title)
        ws.write_merge(1, 2, 1, 2, 'Лойиҳа сони', cell_style)
        ws.write_merge(1, 2, 3, 4, 'Умумий қиймати млн.сўм', cell_style)
        ws.write_merge(1, 1, 5, 12, 'шундан', cell_style)
        ws.write_merge(1, 2, 13, 14, 'Янги иш ўринлари сони', cell_style)
        ws.write_merge(1, 1, 15, 22, 'Иқтисодий самарадорлик', cell_style)

        ws.write_merge(2, 2, 5, 6, 'ўз маблағлари млн.сўм', cell_style)
        ws.write_merge(2, 2, 7, 8, 'банк кредитлари млн.сўм', cell_style)
        ws.write_merge(2, 2, 9, 10, 'хорижий кредитлар минг.долл', cell_style)
        ws.write_merge(2, 2, 11, 12, 'хорижий инвестициялар минг.долл', cell_style)
        ws.write_merge(2, 2, 15, 16, 'Ишлаб чиқариш қуввати млн.сўм', cell_style)
        ws.write_merge(2, 2, 17, 18, 'Импорт урнини босиш минг.долл', cell_style)
        ws.write_merge(2, 2, 19, 20, 'Экспорт ҳажми минг.долл', cell_style)
        ws.write_merge(2, 2, 21, 22, 'Бюджетга қўшимча тушум млн.сўм', cell_style)
    else:
        ws.write_merge(0, 0, 0, 23, 'Cвод банк', cell_title)
        ws.write_merge(1, 2, 2, 3, 'Лойиҳа сони', cell_style)
        ws.write_merge(1, 2, 4, 5, 'Умумий қиймати млн.сўм', cell_style)
        ws.write_merge(1, 1, 6, 13, 'шундан', cell_style)
        ws.write_merge(1, 2, 14, 15, 'Янги иш ўринлари сони', cell_style)
        ws.write_merge(1, 1, 16, 23, 'Иқтисодий самарадорлик', cell_style)

        ws.write_merge(2, 2, 6, 7, 'ўз маблағлари млн.сўм', cell_style)
        ws.write_merge(2, 2, 8, 9, 'банк кредитлари млн.сўм', cell_style)
        ws.write_merge(2, 2, 10, 11, 'хорижий кредитлар минг.долл', cell_style)
        ws.write_merge(2, 2, 12, 13, 'хорижий инвестициялар минг.долл', cell_style)
        ws.write_merge(2, 2, 16, 17, 'Ишлаб чиқариш қуввати млн.сўм', cell_style)
        ws.write_merge(2, 2, 18, 19, 'Импорт урнини босиш минг.долл', cell_style)
        ws.write_merge(2, 2, 20, 21, 'Экспорт ҳажми минг.долл', cell_style)
        ws.write_merge(2, 2, 22, 23, 'Бюджетга қўшимча тушум млн.сўм', cell_style)

    # ws.col(0).width = 4500
    # ws.col(21).width = 5000

    # "Район",
    columns_list = [
        "Banklar nomi",
        "Режа",
        "Амалда",
        "Режа",
        "Амалда",
        "Режа",
        "Амалда",
        "Режа",
        "Амалда",
        "Режа",
        "Амалда",
        "Режа",
        "Амалда",
        "Режа",
        "Амалда",
        "Режа",
        "Амалда",
        "Режа",
        "Амалда",
        "Режа",
        "Амалда",
        "Режа",
        "Амалда",
    ]

    if not get_group_vault_id(request):
        columns = [
            *columns_list
        ]
    else:
        columns = [
            "Ҳудудлар",
            *columns_list
        ]

    for col_num in range(len(columns)):
        ws.col(col_num).width = 3800
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    # date_style = xlwt.XFStyle()
    # time_create = datetime.strftime('time_create', '%d/%m/%y %h:%m:%s')
    fields = [
        'bank_name',
        'loiha_soni_reja',
        'loiha_soni_amalda',
        'umumiy_kiymati_reja',
        'umumiy_kiymati_amalda',
        'uz_mablag_reja',
        'uz_mablag_amalda',
        'bank_kredit_reja',
        'bank_kredit_amalda',
        'xorijiy_kredit_reja',
        'xorijiy_kredit_amalda',
        'xorijiy_invest_reja',
        'xorijiy_invest_amalda',

        'yangi_ish_reja',
        'yangi_ish_amalda',
        'ishlab_chiqarish_reja',
        'ishlab_chiqarish_amalda',
        'import_reja',
        'import_amalda',
        'export_reja',
        'export_amalda',
        'budget_reja',
        'budget_amalda',
    ]

    department_fields = [
        'district__district',
        *fields
    ]

    rows = filter_export_vault_tables(request, filter_slug, BankVault, fields, department_fields)

    for row in rows:
        row_num += 1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)
    return response


def export_excel_jami(request, filter_slug):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = f'attachment; filename=table{str(datetime.now())}.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('table', cell_overwrite_ok=True)
    row_num = 3  # с какой строки начинается наша таблица
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    cell_style = xlwt.easyxf("font: bold on; align: vert center, horiz center")
    cell_title = xlwt.easyxf("font: bold on, height 280; align: vert center, horiz left")
    # cell_style = xlwt.easyxf("align: vert centre, horiz center")

    # ws.title = 'Илова-4.1' Поменять на один если добавлять столбик в начале
    if not get_group_vault_id(request):
        ws.write_merge(0, 0, 0, 21, f'{request.user.district}, Жами свод', cell_title)
        ws.write_merge(1, 2, 0, 1, 'Лойиҳа сони', cell_style)
        ws.write_merge(1, 2, 2, 3, 'Умумий қиймати млн.сўм', cell_style)
        ws.write_merge(1, 1, 4, 11, 'шундан', cell_style)
        ws.write_merge(1, 2, 12, 13, 'Янги иш ўринлари сони', cell_style)
        ws.write_merge(1, 1, 14, 21, 'Иқтисодий самарадорлик', cell_style)

        ws.write_merge(2, 2, 4, 5, 'ўз маблағлари млн.сўм', cell_style)
        ws.write_merge(2, 2, 6, 7, 'банк кредитлари млн.сўм', cell_style)
        ws.write_merge(2, 2, 8, 9, 'хорижий кредитлар минг.долл', cell_style)
        ws.write_merge(2, 2, 10, 11, 'хорижий инвестициялар минг.долл', cell_style)
        ws.write_merge(2, 2, 14, 15, 'Ишлаб чиқариш қуввати млн.сўм', cell_style)
        ws.write_merge(2, 2, 16, 17, 'Импорт урнини босиш минг.долл', cell_style)
        ws.write_merge(2, 2, 18, 19, 'Экспорт ҳажми минг.долл', cell_style)
        ws.write_merge(2, 2, 20, 21, 'Бюджетга қўшимча тушум млн.сўм', cell_style)
    else:
        ws.write_merge(0, 0, 0, 22, 'Жами свод', cell_title)
        ws.write_merge(1, 2, 1, 2, 'Лойиҳа сони', cell_style)
        ws.write_merge(1, 2, 3, 4, 'Умумий қиймати млн.сўм', cell_style)
        ws.write_merge(1, 1, 5, 12, 'шундан', cell_style)
        ws.write_merge(1, 2, 13, 14, 'Янги иш ўринлари сони', cell_style)
        ws.write_merge(1, 1, 15, 22, 'Иқтисодий самарадорлик', cell_style)

        ws.write_merge(2, 2, 5, 6, 'ўз маблағлари млн.сўм', cell_style)
        ws.write_merge(2, 2, 7, 8, 'банк кредитлари млн.сўм', cell_style)
        ws.write_merge(2, 2, 9, 10, 'хорижий кредитлар минг.долл', cell_style)
        ws.write_merge(2, 2, 11, 12, 'хорижий инвестициялар минг.долл', cell_style)
        ws.write_merge(2, 2, 15, 16, 'Ишлаб чиқариш қуввати млн.сўм', cell_style)
        ws.write_merge(2, 2, 17, 18, 'Импорт урнини босиш минг.долл', cell_style)
        ws.write_merge(2, 2, 19, 20, 'Экспорт ҳажми минг.долл', cell_style)
        ws.write_merge(2, 2, 21, 22, 'Бюджетга қўшимча тушум млн.сўм', cell_style)

    # ws.col(0).width = 4500
    # ws.col(21).width = 5000

    # "Район",
    columns_list = [
        "Режа",
        "Амалда",
        "Режа",
        "Амалда",
        "Режа",
        "Амалда",
        "Режа",
        "Амалда",
        "Режа",
        "Амалда",
        "Режа",
        "Амалда",
        "Режа",
        "Амалда",
        "Режа",
        "Амалда",
        "Режа",
        "Амалда",
        "Режа",
        "Амалда",
        "Режа",
        "Амалда",
    ]

    if not get_group_vault_id(request):
        columns = [
            *columns_list
        ]
    else:
        columns = [
            "Ҳудудлар",
            *columns_list
        ]

    for col_num in range(len(columns)):
        ws.col(col_num).width = 3800
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    # date_style = xlwt.XFStyle()
    # time_create = datetime.strftime('time_create', '%d/%m/%y %h:%m:%s')
    fields = [
        'loiha_soni_reja',
        'loiha_soni_amalda',
        'umumiy_kiymati_reja',
        'umumiy_kiymati_amalda',
        'uz_mablag_reja',
        'uz_mablag_amalda',
        'bank_kredit_reja',
        'bank_kredit_amalda',
        'xorijiy_kredit_reja',
        'xorijiy_kredit_amalda',
        'xorijiy_invest_reja',
        'xorijiy_invest_amalda',
        'yangi_ish_reja',
        'yangi_ish_amalda',
        'ishlab_chiqarish_reja',
        'ishlab_chiqarish_amalda',
        'import_reja',
        'import_amalda',
        'export_reja',
        'export_amalda',
        'budget_reja',
        'budget_amalda',
    ]

    department_fields = [
        'district__district',
        *fields
    ]

    rows = filter_export_vault_tables(request, filter_slug, JamiVault, fields, department_fields)

    for row in rows:
        row_num += 1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)
    return response


def export_excel_reja(request, filter_slug):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = f'attachment; filename=table{str(datetime.now())}.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('table', cell_overwrite_ok=True)
    row_num = 3  # с какой строки начинается наша таблица
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    cell_style = xlwt.easyxf("font: bold on; align: vert center, horiz center")
    cell_title = xlwt.easyxf("font: bold on, height 280; align: vert center, horiz left")
    # cell_style = xlwt.easyxf("align: vert centre, horiz center")

    # ws.title = 'Илова-4.1' Поменять на один если добавлять столбик в начале
    if not get_group_vault_id(request):
        ws.write_merge(0, 0, 0, 55, f'{request.user.district}, Cвод режа', cell_title)
        ws.write_merge(1, 2, 0, 6, 'Режа (ҳисобот даври)', cell_style)
        ws.write_merge(1, 2, 7, 13, 'Режага нисбатан ишга тушган', cell_style)
        ws.write_merge(1, 2, 14, 19, 'Ишга тушмаган', cell_style)
        ws.write_merge(1, 1, 20, 34, 'шундан', cell_style)
        ws.write_merge(1, 2, 35, 41, 'Муддатидан аввал ишга тушган лойиҳалар', cell_style)
        ws.write_merge(1, 2, 42, 48, 'Қўшимча (резерв) лойиҳалар', cell_style)
        ws.write_merge(1, 2, 49, 55, 'Жами ишга тушган лойиҳалар', cell_style)

        ws.write_merge(2, 2, 20, 26, 'Истиқболсиз', cell_style)
        ws.write_merge(2, 2, 27, 34, 'Муддатини узайтириш', cell_style)

    else:
        ws.write_merge(0, 0, 0, 56, 'Cвод режа', cell_title)

        ws.write_merge(1, 2, 1, 7, 'Режа (ҳисобот даври)', cell_style)
        ws.write_merge(1, 2, 8, 14, 'Режага нисбатан ишга тушган', cell_style)
        ws.write_merge(1, 2, 15, 20, 'Ишга тушмаган', cell_style)
        ws.write_merge(1, 1, 21, 35, 'шундан', cell_style)
        ws.write_merge(1, 2, 36, 42, 'Муддатидан аввал ишга тушган лойиҳалар', cell_style)
        ws.write_merge(1, 2, 43, 49, 'Қўшимча (резерв) лойиҳалар', cell_style)
        ws.write_merge(1, 2, 50, 56, 'Жами ишга тушган лойиҳалар', cell_style)

        ws.write_merge(2, 2, 21, 27, 'Истиқболсиз', cell_style)
        ws.write_merge(2, 2, 28, 35, 'Муддатини узайтириш', cell_style)

    # ws.col(0).width = 4500
    # ws.col(21).width = 5000

    # "Район",
    columns_list = [
        "Лойиҳа сони",
        "Лойиҳа қиймати, (млн.сўм)",
        "ўз маблағлари млн.сўм",
        "банк кредитлари млн.сўм",
        "хорижий кредитлар минг.долл",
        "хорижий инвестициялар минг.долл",
        "Иш ўрни",
        "Лойиҳа сони",
        "Лойиҳа қиймати, (млн.сўм)",
        "ўз маблағлари млн.сўм",
        "банк кредитлари млн.сўм",
        "хорижий кредитлар минг.долл",
        "хорижий инвестициялар минг.долл",
        "Иш ўрни",
        "Лойиҳа сони",
        "Лойиҳа қиймати, (млн.сўм)",
        "ўз маблағлари млн.сўм",
        "банк кредитлари млн.сўм",
        "хорижий кредитлар минг.долл",
        "хорижий инвестициялар минг.долл",
        "Иш ўрни",
        "Лойиҳа сони",
        "Лойиҳа қиймати, (млн.сўм)",
        "ўз маблағлари млн.сўм",
        "банк кредитлари млн.сўм",
        "хорижий кредитлар минг.долл",
        "хорижий инвестициялар минг.долл",
        "Иш ўрни",
        "Лойиҳа сони",
        "Лойиҳа қиймати, (млн.сўм)",
        "ўз маблағлари млн.сўм",
        "банк кредитлари млн.сўм",
        "хорижий кредитлар минг.долл",
        "хорижий инвестициялар минг.долл",
        "Иш ўрни",
        "Лойиҳа сони",
        "Лойиҳа қиймати, (млн.сўм)",
        "ўз маблағлари млн.сўм",
        "банк кредитлари млн.сўм",
        "хорижий кредитлар минг.долл",
        "хорижий инвестициялар минг.долл",
        "Иш ўрни",
        "Лойиҳа сони",
        "Лойиҳа қиймати, (млн.сўм)",
        "ўз маблағлари млн.сўм",
        "банк кредитлари млн.сўм",
        "хорижий кредитлар минг.долл",
        "хорижий инвестициялар минг.долл",
        "Иш ўрни",
        "Лойиҳа сони",
        "Лойиҳа қиймати, (млн.сўм)",
        "ўз маблағлари млн.сўм",
        "банк кредитлари млн.сўм",
        "хорижий кредитлар минг.долл",
        "хорижий инвестициялар минг.долл",
        "Иш ўрни",
    ]

    if not get_group_vault_id(request):
        columns = [
            *columns_list
        ]
    else:
        columns = [
            "Ҳудудлар",
            *columns_list
        ]

    for col_num in range(len(columns)):
        ws.col(col_num).width = 3800
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    # date_style = xlwt.XFStyle()
    # time_create = datetime.strftime('time_create', '%d/%m/%y %h:%m:%s')
    fields = [
        'reja_loiha_soni',
        'reja_loiha_kiymati',
        'reja_mablag',
        'reja_kredit',
        'reja_xorijiy_kredit',
        'reja_xorijiy_invest',
        'reja_ish',

        'nisbatan_loiha_soni',
        'nisbatan_loiha_kiymati',
        'nisbatan_mablag',
        'nisbatan_kredit',
        'nisbatan_xorijiy_kredit',
        'nisbatan_xorijiy_invest',
        'nisbatan_ish',

        'ish_loiha_soni',
        'ish_loiha_kiymati',
        'ish_mablag',
        'ish_kredit',
        'ish_xorijiy_kredit',
        'ish_xorijiy_invest',

        'istik_ish',
        'istik_loiha_soni',
        'istik_loiha_kiymati',
        'istik_mablag',
        'istik_kredit',
        'istik_xorijiy_kredit',
        'istik_xorijiy_invest',

        'mud_ish',
        'mud_loiha_soni',
        'mud_loiha_kiymati',
        'mud_mablag',
        'mud_kredit',
        'mud_xorijiy_kredit',
        'mud_xorijiy_invest',
        'mud_ish_second',

        'aval_loiha_soni',
        'aval_loiha_kiymati',
        'aval_mablag',
        'aval_kredit',
        'aval_xorijiy_kredit',
        'aval_xorijiy_invest',
        'aval_ish',

        'reserve_loiha_soni',
        'reserve_loiha_kiymati',
        'reserve_mablag',
        'reserve_kredit',
        'reserve_xorijiy_kredit',
        'reserve_xorijiy_invest',
        'reserve_ish',

        'total_loiha_soni',
        'total_loiha_kiymati',
        'total_mablag',
        'total_kredit',
        'total_xorijiy_kredit',
        'total_xorijiy_invest',
        'total_ish',
    ]

    department_fields = [
        'district__district',
        *fields
    ]

    rows = filter_export_vault_tables(request, filter_slug, RejaVault, fields, department_fields)

    for row in rows:
        row_num += 1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)
    return response


# TODO Сделать поля Select
def export_excel_tarmok(request, filter_slug):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = f'attachment; filename=table{str(datetime.now())}.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('table', cell_overwrite_ok=True)
    row_num = 3  # с какой строки начинается наша таблица
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    cell_style = xlwt.easyxf("font: bold on; align: vert center, horiz center")
    cell_title = xlwt.easyxf("font: bold on, height 280; align: vert center, horiz left")
    # cell_style = xlwt.easyxf("align: vert centre, horiz center")

    # ws.title = 'Илова-4.1' Поменять на один если добавлять столбик в начале
    if not get_group_vault_id(request):
        ws.write_merge(0, 0, 0, 23, f'{request.user.district}, Cвод тармок', cell_title)
        ws.write_merge(1, 2, 2, 3, 'Лойиҳа сони', cell_style)
        ws.write_merge(1, 2, 4, 5, 'Умумий қиймати млн.сўм', cell_style)
        ws.write_merge(1, 1, 6, 13, 'шундан', cell_style)
        ws.write_merge(1, 2, 14, 15, 'Янги иш ўринлари сони', cell_style)
        ws.write_merge(1, 1, 16, 23, 'Иқтисодий самарадорлик', cell_style)

        ws.write_merge(2, 2, 6, 7, 'ўз маблағлари млн.сўм', cell_style)
        ws.write_merge(2, 2, 8, 9, 'банк кредитлари млн.сўм', cell_style)
        ws.write_merge(2, 2, 10, 11, 'хорижий кредитлар минг.долл', cell_style)
        ws.write_merge(2, 2, 12, 13, 'хорижий инвестициялар минг.долл', cell_style)
        ws.write_merge(2, 2, 16, 17, 'Ишлаб чиқариш қуввати млн.сўм', cell_style)
        ws.write_merge(2, 2, 18, 19, 'Импорт урнини босиш минг.долл', cell_style)
        ws.write_merge(2, 2, 20, 21, 'Экспорт ҳажми минг.долл', cell_style)
        ws.write_merge(2, 2, 22, 23, 'Бюджетга қўшимча тушум млн.сўм', cell_style)
    else:
        ws.write_merge(0, 0, 0, 24, 'Cвод тармок', cell_title)
        ws.write_merge(1, 2, 3, 4, 'Лойиҳа сони', cell_style)
        ws.write_merge(1, 2, 5, 6, 'Умумий қиймати млн.сўм', cell_style)
        ws.write_merge(1, 1, 7, 14, 'шундан', cell_style)
        ws.write_merge(1, 2, 15, 16, 'Янги иш ўринлари сони', cell_style)
        ws.write_merge(1, 1, 17, 24, 'Иқтисодий самарадорлик', cell_style)

        ws.write_merge(2, 2, 7, 8, 'ўз маблағлари млн.сўм', cell_style)
        ws.write_merge(2, 2, 9, 10, 'банк кредитлари млн.сўм', cell_style)
        ws.write_merge(2, 2, 11, 12, 'хорижий кредитлар минг.долл', cell_style)
        ws.write_merge(2, 2, 13, 14, 'хорижий инвестициялар минг.долл', cell_style)
        ws.write_merge(2, 2, 17, 18, 'Ишлаб чиқариш қуввати млн.сўм', cell_style)
        ws.write_merge(2, 2, 19, 20, 'Импорт урнини босиш минг.долл', cell_style)
        ws.write_merge(2, 2, 21, 22, 'Экспорт ҳажми минг.долл', cell_style)
        ws.write_merge(2, 2, 23, 24, 'Бюджетга қўшимча тушум млн.сўм', cell_style)

    # ws.col(0).width = 4500
    # ws.col(21).width = 5000

    # "Район",
    columns_list = [
        "Категория",
        "Тармоқлар номи",
        "Режа",
        "Амалда",
        "Режа",
        "Амалда",
        "Режа",
        "Амалда",
        "Режа",
        "Амалда",
        "Режа",
        "Амалда",
        "Режа",
        "Амалда",
        "Режа",
        "Амалда",
        "Режа",
        "Амалда",
        "Режа",
        "Амалда",
        "Режа",
        "Амалда",
        "Режа",
        "Амалда",
    ]

    if not get_group_vault_id(request):
        columns = [
            *columns_list
        ]
    else:
        columns = [
            "Ҳудудлар",
            *columns_list
        ]

    for col_num in range(len(columns)):
        ws.col(col_num).width = 3800
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    # date_style = xlwt.XFStyle()
    # time_create = datetime.strftime('time_create', '%d/%m/%y %h:%m:%s')
    # tarmok_model = show_data_table(request, TarmokVault)
    #
    # fields_with_choices = [f.name for f in TarmokVault._meta.get_fields() if f.choices]
    #
    # # Create a new list of fields that includes the choice values
    # new_fields = []
    # for field_name in fields_with_choices:
    #     # Get the field instance
    #     field = TarmokVault._meta.get_field(field_name)
    #
    #     # Get the choices as a list of tuples
    #     choices = field.choices
    #
    #     # Create a new list of choice values
    #     choice_values = [choice[1] for choice in choices]
    #
    #     # Add the choice values to the field list
    #     new_fields.append(field_name)
    #     new_fields.extend(choice_values)

    fields = [
        'category',
        'industry',

        'loiha_soni_reja',
        'loiha_soni_amalda',
        'umumiy_kiymati_reja',
        'umumiy_kiymati_amalda',
        'uz_mablag_reja',
        'uz_mablag_amalda',
        'bank_kredit_reja',
        'bank_kredit_amalda',
        'xorijiy_kredit_reja',
        'xorijiy_kredit_amalda',
        'xorijiy_invest_reja',
        'xorijiy_invest_amalda',

        'yangi_ish_reja',
        'yangi_ish_amalda',
        'ishlab_chiqarish_reja',
        'ishlab_chiqarish_amalda',
        'import_reja',
        'import_amalda',
        'export_reja',
        'export_amalda',
        'budget_reja',
        'budget_amalda',
    ]
    # fields.extend(new_fields)

    department_fields = [
        'district__district',
        *fields
    ]

    rows = filter_export_vault_tables(request, filter_slug, TarmokVault, fields, department_fields)

    for row in rows:
        row_num += 1

        for col_num in range(len(row)):
            ws.write(row_num, col_num, str(row[col_num]), font_style)

    wb.save(response)
    return response


def export_excel_quarter(request, filter_slug):
    response = HttpResponse(content_type='application/ms-excel')
    response['Content-Disposition'] = f'attachment; filename=table{str(datetime.now())}.xls'

    wb = xlwt.Workbook(encoding='utf-8')
    ws = wb.add_sheet('table', cell_overwrite_ok=True)
    row_num = 4  # с какой строки начинается наша таблица
    font_style = xlwt.XFStyle()
    font_style.font.bold = True

    cell_style = xlwt.easyxf("font: bold on; align: vert center, horiz center")
    cell_title = xlwt.easyxf("font: bold on, height 280; align: vert center, horiz left")
    # cell_style = xlwt.easyxf("align: vert centre, horiz center")

    # ws.title = 'Илова-4.1' Поменять на один если добавлять столбик в начале
    if not get_group_vault_id(request):
        ws.write_merge(0, 0, 0, 87, f'{request.user.district}, Cвод чорак', cell_title)
        ws.write_merge(1, 3, 0, 1, 'Лойиҳа сони', cell_style)
        ws.write_merge(1, 1, 2, 21, '1-Чорак', cell_style)

        ws.write_merge(1, 3, 22, 23, 'Лойиҳа сони', cell_style)
        ws.write_merge(1, 1, 24, 43, '2-Чорак', cell_style)

        ws.write_merge(1, 3, 44, 45, 'Лойиҳа сони', cell_style)
        ws.write_merge(1, 1, 46, 65, '3-Чорак', cell_style)

        ws.write_merge(1, 3, 66, 67, 'Лойиҳа сони', cell_style)
        ws.write_merge(1, 1, 68, 87, '4-Чорак', cell_style)

        ws.write_merge(2, 3, 2, 3, 'Умумий қиймати млн.сўм', cell_style)
        ws.write_merge(2, 2, 4, 11, 'шундан', cell_style)
        ws.write_merge(2, 3, 12, 13, 'Янги иш ўринлари сони', cell_style)
        ws.write_merge(2, 2, 14, 21, 'Иқтисодий самарадорлик', cell_style)

        ws.write_merge(3, 3, 4, 5, 'ўз маблағлари млн.сўм', cell_style)
        ws.write_merge(3, 3, 6, 7, 'банк кредитлари млн.сўм', cell_style)
        ws.write_merge(3, 3, 8, 9, 'хорижий кредитлар минг.долл', cell_style)
        ws.write_merge(3, 3, 10, 11, 'хорижий инвестициялар минг.долл', cell_style)
        ws.write_merge(3, 3, 14, 15, 'Ишлаб чиқариш қуввати млн.сўм', cell_style)
        ws.write_merge(3, 3, 16, 17, 'Импорт урнини босиш минг.долл', cell_style)
        ws.write_merge(3, 3, 18, 19, 'Экспорт ҳажми минг.долл', cell_style)
        ws.write_merge(3, 3, 20, 21, 'Бюджетга қўшимча тушум млн.сўм', cell_style)

        ws.write_merge(2, 3, 24, 25, 'Умумий қиймати млн.сўм', cell_style)
        ws.write_merge(2, 2, 26, 33, 'шундан', cell_style)
        ws.write_merge(2, 3, 34, 35, 'Янги иш ўринлари сони', cell_style)
        ws.write_merge(2, 2, 36, 43, 'Иқтисодий самарадорлик', cell_style)

        ws.write_merge(3, 3, 26, 27, 'ўз маблағлари млн.сўм', cell_style)
        ws.write_merge(3, 3, 28, 29, 'банк кредитлари млн.сўм', cell_style)
        ws.write_merge(3, 3, 30, 31, 'хорижий кредитлар минг.долл', cell_style)
        ws.write_merge(3, 3, 32, 33, 'хорижий инвестициялар минг.долл', cell_style)
        ws.write_merge(3, 3, 36, 37, 'Ишлаб чиқариш қуввати млн.сўм', cell_style)
        ws.write_merge(3, 3, 38, 39, 'Импорт урнини босиш минг.долл', cell_style)
        ws.write_merge(3, 3, 40, 41, 'Экспорт ҳажми минг.долл', cell_style)
        ws.write_merge(3, 3, 42, 43, 'Бюджетга қўшимча тушум млн.сўм', cell_style)

        ws.write_merge(2, 3, 46, 47, 'Умумий қиймати млн.сўм', cell_style)
        ws.write_merge(2, 2, 48, 55, 'шундан', cell_style)
        ws.write_merge(2, 3, 56, 57, 'Янги иш ўринлари сони', cell_style)
        ws.write_merge(2, 2, 58, 65, 'Иқтисодий самарадорлик', cell_style)

        ws.write_merge(3, 3, 48, 49, 'ўз маблағлари млн.сўм', cell_style)
        ws.write_merge(3, 3, 50, 51, 'банк кредитлари млн.сўм', cell_style)
        ws.write_merge(3, 3, 52, 53, 'хорижий кредитлар минг.долл', cell_style)
        ws.write_merge(3, 3, 54, 55, 'хорижий инвестициялар минг.долл', cell_style)
        ws.write_merge(3, 3, 58, 59, 'Ишлаб чиқариш қуввати млн.сўм', cell_style)
        ws.write_merge(3, 3, 60, 61, 'Импорт урнини босиш минг.долл', cell_style)
        ws.write_merge(3, 3, 62, 63, 'Экспорт ҳажми минг.долл', cell_style)
        ws.write_merge(3, 3, 64, 65, 'Бюджетга қўшимча тушум млн.сўм', cell_style)

        ws.write_merge(2, 3, 68, 69, 'Умумий қиймати млн.сўм', cell_style)
        ws.write_merge(2, 2, 70, 77, 'шундан', cell_style)
        ws.write_merge(2, 3, 78, 79, 'Янги иш ўринлари сони', cell_style)
        ws.write_merge(2, 2, 80, 87, 'Иқтисодий самарадорлик', cell_style)

        ws.write_merge(3, 3, 70, 71, 'ўз маблағлари млн.сўм', cell_style)
        ws.write_merge(3, 3, 72, 73, 'банк кредитлари млн.сўм', cell_style)
        ws.write_merge(3, 3, 74, 75, 'хорижий кредитлар минг.долл', cell_style)
        ws.write_merge(3, 3, 76, 77, 'хорижий инвестициялар минг.долл', cell_style)
        ws.write_merge(3, 3, 80, 81, 'Ишлаб чиқариш қуввати млн.сўм', cell_style)
        ws.write_merge(3, 3, 82, 83, 'Импорт урнини босиш минг.долл', cell_style)
        ws.write_merge(3, 3, 84, 85, 'Экспорт ҳажми минг.долл', cell_style)
        ws.write_merge(3, 3, 86, 87, 'Бюджетга қўшимча тушум млн.сўм', cell_style)

    else:
        ws.write_merge(0, 0, 0, 88, 'Cвод чорак', cell_title)

        ws.write_merge(1, 3, 1, 2, 'Лойиҳа сони', cell_style)
        ws.write_merge(1, 1, 3, 22, '1-Чорак', cell_style)

        ws.write_merge(1, 3, 23, 24, 'Лойиҳа сони', cell_style)
        ws.write_merge(1, 1, 25, 44, '2-Чорак', cell_style)

        ws.write_merge(1, 3, 45, 46, 'Лойиҳа сони', cell_style)
        ws.write_merge(1, 1, 47, 66, '3-Чорак', cell_style)

        ws.write_merge(1, 3, 67, 68, 'Лойиҳа сони', cell_style)
        ws.write_merge(1, 1, 69, 88, '4-Чорак', cell_style)

        ws.write_merge(2, 3, 3, 4, 'Умумий қиймати млн.сўм', cell_style)
        ws.write_merge(2, 2, 5, 12, 'шундан', cell_style)
        ws.write_merge(2, 3, 13, 14, 'Янги иш ўринлари сони', cell_style)
        ws.write_merge(2, 2, 15, 22, 'Иқтисодий самарадорлик', cell_style)

        ws.write_merge(3, 3, 5, 6, 'ўз маблағлари млн.сўм', cell_style)
        ws.write_merge(3, 3, 7, 8, 'банк кредитлари млн.сўм', cell_style)
        ws.write_merge(3, 3, 9, 10, 'хорижий кредитлар минг.долл', cell_style)
        ws.write_merge(3, 3, 11, 12, 'хорижий инвестициялар минг.долл', cell_style)
        ws.write_merge(3, 3, 15, 16, 'Ишлаб чиқариш қуввати млн.сўм', cell_style)
        ws.write_merge(3, 3, 17, 18, 'Импорт урнини босиш минг.долл', cell_style)
        ws.write_merge(3, 3, 19, 20, 'Экспорт ҳажми минг.долл', cell_style)
        ws.write_merge(3, 3, 21, 22, 'Бюджетга қўшимча тушум млн.сўм', cell_style)

        ws.write_merge(2, 3, 25, 26, 'Умумий қиймати млн.сўм', cell_style)
        ws.write_merge(2, 2, 27, 34, 'шундан', cell_style)
        ws.write_merge(2, 3, 35, 36, 'Янги иш ўринлари сони', cell_style)
        ws.write_merge(2, 2, 37, 44, 'Иқтисодий самарадорлик', cell_style)

        ws.write_merge(3, 3, 27, 28, 'ўз маблағлари млн.сўм', cell_style)
        ws.write_merge(3, 3, 29, 30, 'банк кредитлари млн.сўм', cell_style)
        ws.write_merge(3, 3, 31, 32, 'хорижий кредитлар минг.долл', cell_style)
        ws.write_merge(3, 3, 33, 34, 'хорижий инвестициялар минг.долл', cell_style)
        ws.write_merge(3, 3, 37, 38, 'Ишлаб чиқариш қуввати млн.сўм', cell_style)
        ws.write_merge(3, 3, 39, 40, 'Импорт урнини босиш минг.долл', cell_style)
        ws.write_merge(3, 3, 41, 42, 'Экспорт ҳажми минг.долл', cell_style)
        ws.write_merge(3, 3, 43, 44, 'Бюджетга қўшимча тушум млн.сўм', cell_style)

        ws.write_merge(2, 3, 47, 48, 'Умумий қиймати млн.сўм', cell_style)
        ws.write_merge(2, 2, 49, 56, 'шундан', cell_style)
        ws.write_merge(2, 3, 57, 58, 'Янги иш ўринлари сони', cell_style)
        ws.write_merge(2, 2, 59, 66, 'Иқтисодий самарадорлик', cell_style)

        ws.write_merge(3, 3, 49, 50, 'ўз маблағлари млн.сўм', cell_style)
        ws.write_merge(3, 3, 51, 52, 'банк кредитлари млн.сўм', cell_style)
        ws.write_merge(3, 3, 53, 54, 'хорижий кредитлар минг.долл', cell_style)
        ws.write_merge(3, 3, 55, 56, 'хорижий инвестициялар минг.долл', cell_style)
        ws.write_merge(3, 3, 59, 60, 'Ишлаб чиқариш қуввати млн.сўм', cell_style)
        ws.write_merge(3, 3, 61, 62, 'Импорт урнини босиш минг.долл', cell_style)
        ws.write_merge(3, 3, 63, 64, 'Экспорт ҳажми минг.долл', cell_style)
        ws.write_merge(3, 3, 65, 66, 'Бюджетга қўшимча тушум млн.сўм', cell_style)

        ws.write_merge(2, 3, 69, 70, 'Умумий қиймати млн.сўм', cell_style)
        ws.write_merge(2, 2, 71, 78, 'шундан', cell_style)
        ws.write_merge(2, 3, 79, 80, 'Янги иш ўринлари сони', cell_style)
        ws.write_merge(2, 2, 81, 88, 'Иқтисодий самарадорлик', cell_style)

        ws.write_merge(3, 3, 71, 72, 'ўз маблағлари млн.сўм', cell_style)
        ws.write_merge(3, 3, 73, 74, 'банк кредитлари млн.сўм', cell_style)
        ws.write_merge(3, 3, 75, 76, 'хорижий кредитлар минг.долл', cell_style)
        ws.write_merge(3, 3, 77, 78, 'хорижий инвестициялар минг.долл', cell_style)
        ws.write_merge(3, 3, 81, 82, 'Ишлаб чиқариш қуввати млн.сўм', cell_style)
        ws.write_merge(3, 3, 83, 84, 'Импорт урнини босиш минг.долл', cell_style)
        ws.write_merge(3, 3, 85, 86, 'Экспорт ҳажми минг.долл', cell_style)
        ws.write_merge(3, 3, 87, 88, 'Бюджетга қўшимча тушум млн.сўм', cell_style)

    # ws.col(0).width = 4500
    # ws.col(21).width = 5000

    # "Район",
    columns_list = [
        'Режa',
        'Амалда',
        'Режa',
        'Амалда',
        'Режa',
        'Амалда',
        'Режa',
        'Амалда',
        'Режa',
        'Амалда',
        'Режa',
        'Амалда',
        'Режa',
        'Амалда',
        'Режa',
        'Амалда',
        'Режa',
        'Амалда',
        'Режa',
        'Амалда',
        'Режa',
        'Амалда',
        'Режa',
        'Амалда',
        'Режa',
        'Амалда',
        'Режa',
        'Амалда',
        'Режa',
        'Амалда',
        'Режa',
        'Амалда',
        'Режa',
        'Амалда',
        'Режa',
        'Амалда',
        'Режa',
        'Амалда',
        'Режa',
        'Амалда',
        'Режa',
        'Амалда',
        'Режa',
        'Амалда',
        'Режa',
        'Амалда',
        'Режa',
        'Амалда',
        'Режa',
        'Амалда',
        'Режa',
        'Амалда',
        'Режa',
        'Амалда',
        'Режa',
        'Амалда',
        'Режa',
        'Амалда',
        'Режa',
        'Амалда',
        'Режa',
        'Амалда',
        'Режa',
        'Амалда',
        'Режa',
        'Амалда',
        'Режa',
        'Амалда',
        'Режa',
        'Амалда',
        'Режa',
        'Амалда',
        'Режa',
        'Амалда',
        'Режa',
        'Амалда',
        'Режa',
        'Амалда',
        'Режa',
        'Амалда',
        'Режa',
        'Амалда',
        'Режa',
        'Амалда',
        'Режa',
        'Амалда',
        'Режa',
        'Амалда',
    ]

    if not get_group_vault_id(request):
        columns = [
            *columns_list
        ]
    else:
        columns = [
            "Ҳудудлар",
            *columns_list
        ]

    for col_num in range(len(columns)):
        ws.col(col_num).width = 3800
        ws.write(row_num, col_num, columns[col_num], font_style)

    font_style = xlwt.XFStyle()
    # date_style = xlwt.XFStyle()
    # time_create = datetime.strftime('time_create', '%d/%m/%y %h:%m:%s')
    fields = [
        'loiha_soni_reja',
        'loiha_soni_amalda',
        'umumiy_kiymati_reja',
        'umumiy_kiymati_amalda',
        'uz_mablag_reja',
        'uz_mablag_amalda',
        'bank_kredit_reja',
        'bank_kredit_amalda',
        'xorijiy_kredit_reja',
        'xorijiy_kredit_amalda',
        'xorijiy_invest_reja',
        'xorijiy_invest_amalda',
        'first_quarter_yangi_ish_reja',
        'first_quarter_yangi_ish_amalda',
        'first_quarter_ishlab_chiqarish_reja',
        'first_quarter_ishlab_chiqarish_amalda',
        'first_quarter_import_reja',
        'first_quarter_import_amalda',
        'first_quarter_export_reja',
        'first_quarter_export_amalda',
        'first_quarter_budget_reja',
        'first_quarter_budget_amalda',

        'second_quarter_loiha_soni_reja',
        'second_quarter_loiha_soni_amalda',
        'second_quarter_umumiy_kiymati_reja',
        'second_quarter_umumiy_kiymati_amalda',
        'second_quarter_uz_mablag_reja',
        'second_quarter_uz_mablag_amalda',
        'second_quarter_bank_kredit_reja',
        'second_quarter_bank_kredit_amalda',
        'second_quarter_xorijiy_kredit_reja',
        'second_quarter_xorijiy_kredit_amalda',
        'second_quarter_xorijiy_invest_reja',
        'second_quarter_xorijiy_invest_amalda',
        'second_quarter_yangi_ish_reja',
        'second_quarter_yangi_ish_amalda',
        'second_quarter_ishlab_chiqarish_reja',
        'second_quarter_ishlab_chiqarish_amalda',
        'second_quarter_import_reja',
        'second_quarter_import_amalda',
        'second_quarter_export_reja',
        'second_quarter_export_amalda',
        'second_quarter_budget_reja',
        'second_quarter_budget_amalda',

        'third_quarter_loiha_soni_reja',
        'third_quarter_loiha_soni_amalda',
        'third_quarter_umumiy_kiymati_reja',
        'third_quarter_umumiy_kiymati_amalda',
        'third_quarter_uz_mablag_reja',
        'third_quarter_uz_mablag_amalda',
        'third_quarter_bank_kredit_reja',
        'third_quarter_bank_kredit_amalda',
        'third_quarter_xorijiy_kredit_reja',
        'third_quarter_xorijiy_kredit_amalda',
        'third_quarter_xorijiy_invest_reja',
        'third_quarter_xorijiy_invest_amalda',
        'third_quarter_yangi_ish_reja',
        'third_quarter_yangi_ish_amalda',
        'third_quarter_ishlab_chiqarish_reja',
        'third_quarter_ishlab_chiqarish_amalda',
        'third_quarter_import_reja',
        'third_quarter_import_amalda',
        'third_quarter_export_reja',
        'third_quarter_export_amalda',
        'third_quarter_budget_reja',
        'third_quarter_budget_amalda',

        'fourth_quarter_loiha_soni_reja',
        'fourth_quarter_loiha_soni_amalda',
        'fourth_quarter_umumiy_kiymati_reja',
        'fourth_quarter_umumiy_kiymati_amalda',
        'fourth_quarter_uz_mablag_reja',
        'fourth_quarter_uz_mablag_amalda',
        'fourth_quarter_bank_kredit_reja',
        'fourth_quarter_bank_kredit_amalda',
        'fourth_quarter_xorijiy_kredit_reja',
        'fourth_quarter_xorijiy_kredit_amalda',
        'fourth_quarter_xorijiy_invest_reja',
        'fourth_quarter_xorijiy_invest_amalda',
        'fourth_quarter_yangi_ish_reja',
        'fourth_quarter_yangi_ish_amalda',
        'fourth_quarter_ishlab_chiqarish_reja',
        'fourth_quarter_ishlab_chiqarish_amalda',
        'fourth_quarter_import_reja',
        'fourth_quarter_import_amalda',
        'fourth_quarter_export_reja',
        'fourth_quarter_export_amalda',
        'fourth_quarter_budget_reja',
        'fourth_quarter_budget_amalda',
    ]

    department_fields = [
        'district__district',
        *fields
    ]

    rows = filter_export_vault_tables(request, filter_slug, QuarterVault, fields, department_fields)

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


def get_data_table_4(request, model_name, page_title):
    model = fourth_department_models_dict.get(model_name, None)
    if not model:
        # Handle invalid model name
        raise ValueError("Invalid model name: %s" % model_name)

    if get_group_post_monitoring_id(request):
        table_data = show_data_table_to_departament(model)
    else:
        table_data = show_data_table(request, model)

    page_obj = paginate_page(request, table_data)
    context = get_context_data(page_obj, page_title, fourth_department_tables_menu, table_data)
    return render(request, src[model_name], context)


def get_data_table_manzil(request):
    return get_data_table_4(request, 'manzil', '2017-2020 манзилли')


def get_data_table_subtotals(request):
    return get_data_table_4(request, 'subtotals', 'Промежуточный итоги')


def get_data_table_addressed(request):
    return get_data_table_4(request, 'addressed', 'Манзилли')


def get_data_table_networkAdministrations(request):
    return get_data_table_4(request, 'networkAdministrations', 'Тармоқ бошқармалари')


def get_data_table_totalCleaning(request):
    return get_data_table_4(request, 'totalCleaning', 'ЖАМИ чистка')


def get_data_table_totalCleaningNetwork(request):
    return get_data_table_4(request, 'totalCleaningNetwork', 'ЖАМИ чистка тармоқ')


def get_data_table_totalDone(request):
    return get_data_table_4(request, 'totalDone', 'ЖАМИ бажарилган')


def get_data_table_totalCompletedNetwork(request):
    return get_data_table_4(request, 'totalCompletedNetwork', 'ЖАМИ бажарилган тармоқ')


def get_data_table_totalProblem(request):
    return get_data_table_4(request, 'totalProblem', 'ЖАМИ муаммо')


def get_data_table_performanceAddressed(request):
    return get_data_table_4(request, 'performanceAddressed', 'манзилли')


def get_data_table_filter_fourth_departament(request, model_name, page_title, filter_slug):
    model = fourth_department_models_dict.get(model_name, None)
    if not model:
        # Handle invalid model name
        raise ValueError("Invalid model name: %s" % model_name)

    if not get_group_post_monitoring_id(request):
        table_data = show_data_table(request, model)
    else:
        table_data = show_data_table_to_departament(model)

    table_data = filter_tables(filter_slug, table_data)
    page_obj = paginate_page(request, table_data)
    context = get_context_data(page_obj, page_title, fourth_department_tables_menu, table_data)
    return render(request, src[model_name], context)


def table_filter_table_manzil(request, filter_slug):
    return get_data_table_filter_fourth_departament(request, 'manzil', '2017-2020 манзилли', filter_slug)


def table_filter_table_subtotals(request, filter_slug):
    return get_data_table_filter_fourth_departament(request, 'subtotals', 'Промежуточный итоги', filter_slug)


def table_filter_table_addressed(request, filter_slug):
    return get_data_table_filter_fourth_departament(request, 'addressed', 'Манзилли', filter_slug)


def table_filter_table_networkAdministrations(request, filter_slug):
    return get_data_table_filter_fourth_departament(request, 'networkAdministrations', 'Тармоқ бошқармалари',
                                                    filter_slug)


def table_filter_table_totalCleaning(request, filter_slug):
    return get_data_table_filter_fourth_departament(request, 'totalCleaning', 'ЖАМИ чистка', filter_slug)


def table_filter_table_totalCleaningNetwork(request, filter_slug):
    return get_data_table_filter_fourth_departament(request, 'totalCleaningNetwork', 'ЖАМИ чистка тармоқ', filter_slug)


def table_filter_table_totalDone(request, filter_slug):
    return get_data_table_filter_fourth_departament(request, 'totalDone', 'ЖАМИ бажарилган', filter_slug)


def table_filter_table_totalCompletedNetwork(request, filter_slug):
    return get_data_table_filter_fourth_departament(request, 'totalCompletedNetwork', 'ЖАМИ бажарилган тармоқ',
                                                    filter_slug)


def table_filter_table_totalProblem(request, filter_slug):
    return get_data_table_filter_fourth_departament(request, 'totalProblem', 'ЖАМИ муаммо', filter_slug)


def table_filter_table_performanceAddressed(request, filter_slug):
    return get_data_table_filter_fourth_departament(request, 'performanceAddressed', 'манзилли', filter_slug)


@login_required
def add_data_table_fourth_department(request, model_name, model_form, redirect_url, page_title):
    model = fourth_department_models_dict.get(model_name, None)
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
    context = make_context_by_form(page_title, form, fourth_department_tables_menu, page_obj)
    return render(request, f'mainapp/forms/fourth_department/form_{model_name}.html', context)


def add_data_table_manzil(request):
    return add_data_table_fourth_department(request, 'manzil', TableManzilForm, 'table_manzil', '2017-2020 манзилли')


def add_data_table_subtotals(request):
    return add_data_table_fourth_department(request, 'subtotals', TableSubtotalsForm, 'table_subtotals',
                                            'Промежуточный итоги')


def add_data_table_addressed(request):
    return add_data_table_fourth_department(request, 'addressed', TableAddressedForm, 'table_addressed', 'Манзилли')


def add_data_table_networkAdministrations(request):
    return add_data_table_fourth_department(request, 'networkAdministrations', TableNetworkAdministrationsForm,
                                            'table_networkAdministrations', 'Тармоқ бошқармалари')


def add_data_table_totalCleaning(request):
    return add_data_table_fourth_department(request, 'totalCleaning', TableTotalCleaningForm, 'table_totalCleaning',
                                            'ЖАМИ чистка')


def add_data_table_totalCleaningNetwork(request):
    return add_data_table_fourth_department(request, 'totalCleaningNetwork', TableTotalCleaningNetworkForm,
                                            'table_totalCleaningNetwork', 'ЖАМИ чистка тармоқ')


def add_data_table_totalDone(request):
    return add_data_table_fourth_department(request, 'totalDone', TableTotalDoneForm, 'table_totalDone',
                                            'ЖАМИ бажарилган')


def add_data_table_totalCompletedNetwork(request):
    return add_data_table_fourth_department(request, 'totalCompletedNetwork', TableTotalCompletedNetworkForm,
                                            'table_totalCompletedNetwork', 'ЖАМИ бажарилган тармоқ')


def add_data_table_totalProblem(request):
    return add_data_table_fourth_department(request, 'totalProblem', TableTotalProblemForm, 'table_totalProblem',
                                            'ЖАМИ муаммо')


def add_data_table_performanceAddressed(request):
    return add_data_table_fourth_department(request, 'performanceAddressed', TablePerformanceIsAddressedForm,
                                            'table_performanceAddressed', 'манзилли')
