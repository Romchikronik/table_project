from django.urls import path
# from .import views

from .views import *

# groups id: departament_group: 3; Loiha group: 1; export group: 2

urlpatterns = [
    path('', mainPage, name='main'),
    path('project-department/', get_department_projects, name='department_projects'),
    path('exports-department/', get_department_exports, name='department_exports'),
    path('vault-department/', get_department_3, name='department_3'),
    path('department-4/', get_department_4, name='department_4'),
    path('department-5/', get_department_5, name='department_5'),

    path('export-excel-loiha41/<slug:filter_slug>', export_excel_loiha41, name='export-excel-loiha41'),
    path('export-excel-loiha52/<slug:filter_slug>', export_excel_loiha52, name='export-excel-loiha52'),
    path('export-excel-loiha14/<slug:filter_slug>', export_excel_loiha14, name='export-excel-loiha14'),
    path('export-excel-loiha131/<slug:filter_slug>', export_excel_loiha131, name='export-excel-loiha131'),
    path('export-excel-loiha122/<slug:filter_slug>', export_excel_loiha122, name='export-excel-loiha122'),
    path('export-excel-loiha121/<slug:filter_slug>', export_excel_loiha121, name='export-excel-loiha121'),
    path('export-excel-loiha12/<slug:filter_slug>', export_excel_loiha12, name='export-excel-loiha12'),
    path('export-excel-loiha10/<slug:filter_slug>', export_excel_loiha10, name='export-excel-loiha10'),
    path('export-excel-loiha6/<slug:filter_slug>', export_excel_loiha6, name='export-excel-loiha6'),
    path('export-excel-loiha13/<slug:filter_slug>', export_excel_loiha13, name='export-excel-loiha13'),

    path('login/', loginPage, name='login'),
    path('logout/', logoutUser, name='logout'),

    path('form/loiha4.1', add_data_table_Loiha41, name='form_loiha4.1'),
    path('form/loiha5.2', add_data_table_Loiha52, name='form_loiha5.2'),
    path('form/loiha14', add_data_table_Loiha14, name='form_loiha14'),
    path('form/loiha13.1', add_data_table_Loiha131, name='form_loiha13.1'),
    path('form/loiha12.2', add_data_table_Loiha122, name='form_loiha12.2'),
    path('form/loiha12.1', add_data_table_Loiha121, name='form_loiha12.1'),
    path('form/loiha12', add_data_table_Loiha12, name='form_loiha12'),
    path('form/loiha10', add_data_table_Loiha10, name='form_loiha10'),
    path('form/loiha6', add_data_table_Loiha6, name='form_loiha6'),
    path('form/loiha13', add_data_table_Loiha13, name='form_loiha13'),

    # 2 отдел
    path('form/sanoat', add_data_table_sanoat, name='form_sanoat'),
    path('form/kx', add_data_table_kx, name='form_kx'),
    path('form/table_1', add_data_table_1, name='form_table1'),
    path('form/kunliu', add_data_table_kunliu, name='form_kunliu'),

    # 3 отдел
    path('form/jami', add_data_table_jami, name='form_jami'),
    path('form/quarter', add_data_table_quarter, name='form_quarter'),
    path('form/monthly', add_data_table_month, name='form_monthly'),
    path('form/bank', add_data_table_bank, name='form_bank'),
    path('form/reja', add_data_table_reja, name='form_reja'),
    path('form/tarmok', add_data_table_tarmok, name='form_tarmok'),

    # 4 отдел
    path('form/manzil', add_data_table_manzil, name='form_manzil'),

    # path('projects-department/table/<slug:table_slug>', views.get_data_table_Loiha41, name='table'),

    path('projects-department/table/ilova-4.1/', get_data_table_Loiha41, name='table_loiha4.1'),
    path('projects-department/table/ilova-5.2', get_data_table_Loiha52, name='table_loiha5.2'),
    path('projects-department/table/ilova-14', get_data_table_Loiha14, name='table_loiha14'),
    path('projects-department/table/ilova-13.1', get_data_table_Loiha131, name='table_loiha13.1'),
    path('projects-department/table/ilova-12.2', get_data_table_Loiha122, name='table_loiha12.2'),
    path('projects-department/table/ilova-12.1', get_data_table_Loiha121, name='table_loiha12.1'),
    path('projects-department/table/ilova-12', get_data_table_Loiha12, name='table_loiha12'),
    path('projects-department/table/ilova-10', get_data_table_Loiha10, name='table_loiha10'),
    path('projects-department/table/ilova-6', get_data_table_Loiha6, name='table_loiha6'),
    path('projects-department/table/ilova-13', get_data_table_Loiha13, name='table_loiha13'),

    # 2 departament
    path('exports-department/table/sanoat', get_data_table_sanoat, name='table_sanoat'),
    path('exports-department/table/kx', get_data_table_kh, name='table_kx'),
    path('exports-department/table/table_1', get_data_table_first_table, name='table_first'),
    path('exports-department/table/kunliu', get_data_table_kunliu, name='table_kunliu'),

    # 3 departament
    path('vault-department/table/jami', get_data_table_jami, name='table_jami'),
    path('vault-department/table/quarter', get_data_table_quarter, name='table_quarter'),
    path('vault-department/table/monthly', get_data_table_month, name='table_monthly'),
    path('vault-department/table/bank', get_data_table_bank, name='table_bank'),
    path('vault-department/table/reja', get_data_table_reja, name='table_reja'),
    path('vault-department/table/tarmok', get_data_table_tarmok, name='table_tarmok'),

    # 4 departament
    path('postmonitoring-department/table/manzil', get_data_table_manzil, name='table_manzil'),

    # filters

    path('projects-department/table/ilova-13.1/filter/<slug:filter_slug>', table_filter_loiha131, name='table_filter_loiha131'),
    path('projects-department/table/ilova-4.1/filter/<slug:filter_slug>', table_filter_loiha41, name='table_filter_loiha41'),
    path('projects-department/table/ilova-5.2/filter/<slug:filter_slug>', table_filter_loiha52, name='table_filter_loiha52'),
    path('projects-department/table/ilova-14/filter/<slug:filter_slug>', table_filter_loiha14, name='table_filter_loiha14'),
    path('projects-department/table/ilova-12.2/filter/<slug:filter_slug>', table_filter_loiha122, name='table_filter_loiha122'),
    path('projects-department/table/ilova-12.1/filter/<slug:filter_slug>', table_filter_loiha121, name='table_filter_loiha121'),
    path('projects-department/table/ilova-12/filter/<slug:filter_slug>', table_filter_loiha12, name='table_filter_loiha12'),
    path('projects-department/table/ilova-10/filter/<slug:filter_slug>', table_filter_loiha10, name='table_filter_loiha10'),
    path('projects-department/table/ilova-6/filter/<slug:filter_slug>', table_filter_loiha6, name='table_filter_loiha6'),
    path('projects-department/table/ilova-13/filter/<slug:filter_slug>', table_filter_loiha13, name='table_filter_loiha13'),

    # 2 departament
    path('exports-department/table/sanoat/filter/<slug:filter_slug>', table_filter_sanoat, name="table_filter_sanoat"),
    path('exports-department/table/kx/filter/<slug:filter_slug>', table_filter_kx, name="table_filter_kx"),
    path('exports-department/table/table_1/filter/<slug:filter_slug>', table_filter_first_table, name="table_filter_first_table"),
    path('exports-department/table/kunliu/filter/<slug:filter_slug>', table_filter_kunliu, name="table_filter_kunliu"),

    # 3 departament
    path('vault-department/table/jami/filter/<slug:filter_slug>', table_filter_table_jami,
         name="table_filter_table_jami"),
    path('vault-department/table/quarter/filter/<slug:filter_slug>', table_filter_table_quarter,
         name="table_filter_table_quarter"),
    path('vault-department/table/monthly/filter/<slug:filter_slug>', table_filter_table_month,
         name="table_filter_table_month"),
    path('vault-department/table/bank/filter/<slug:filter_slug>', table_filter_table_bank,
         name="table_filter_table_bank"),
    path('vault-department/table/reja/filter/<slug:filter_slug>', table_filter_table_reja,
         name="table_filter_table_reja"),
    path('vault-department/table/tarmok/filter/<slug:filter_slug>', table_filter_table_tarmok,
         name="table_filter_table_tarmok"),

    # 4 department
    path('postmonitoring-department/table/manzil/filter/<slug:filter_slug>', table_filter_table_manzil,
         name="table_filter_table_manzil"),
]