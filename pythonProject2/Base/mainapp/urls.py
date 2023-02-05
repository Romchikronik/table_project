from django.urls import path
from .import views

# groups id: departament_group: 3; Loiha group: 1; export group: 2

urlpatterns = [
    path('', views.mainPage, name='main'),
    path('project-department/', views.get_department_projects, name='department_projects'),
    path('exports-department/', views.get_department_exports, name='department_exports'),
    path('department-3/', views.get_department_3, name='department_3'),
    path('department-4/', views.get_department_4, name='department_4'),
    path('department-5/', views.get_department_5, name='department_5'),
    path('export-excel/<slug:filter_slug>', views.export_excel, name='export-excel'),

    path('login/', views.loginPage, name='login'),
    path('logout/', views.logoutUser, name='logout'),

    path('form/loiha4.1', views.add_data_table_Loiha41, name='form_loiha4.1'),
    path('form/loiha5.2', views.add_data_table_Loiha52, name='form_loiha5.2'),
    path('form/loiha14', views.add_data_table_Loiha14, name='form_loiha14'),
    path('form/loiha13.1', views.add_data_table_Loiha131, name='form_loiha13.1'),
    path('form/loiha12.2', views.add_data_table_Loiha122, name='form_loiha12.2'),
    path('form/loiha12.1', views.add_data_table_Loiha121, name='form_loiha12.1'),
    path('form/loiha12', views.add_data_table_Loiha12, name='form_loiha12'),
    path('form/loiha10', views.add_data_table_Loiha10, name='form_loiha10'),
    path('form/loiha6', views.add_data_table_Loiha6, name='form_loiha6'),
    path('form/loiha13', views.add_data_table_Loiha13, name='form_loiha13'),

    # 2 отдел
    path('form/sanoat', views.add_data_table_sanoat, name='form_sanoat'),
    path('form/kx', views.add_data_table_kx, name='form_kx'),
    path('form/table_1', views.add_data_table_1, name='form_table1'),
    path('form/kunliu', views.add_data_table_kunliu, name='form_kunliu'),

    # path('projects-department/table/<slug:table_slug>', views.get_data_table_Loiha41, name='table'),

    path('projects-department/table/ilova-4.1/', views.get_data_table_Loiha41, name='table_loiha4.1'),
    path('projects-department/table/ilova-5.2', views.get_data_table_Loiha52, name='table_loiha5.2'),
    path('projects-department/table/ilova-14', views.get_data_table_Loiha14, name='table_loiha14'),
    path('projects-department/table/ilova-13.1', views.get_data_table_Loiha131, name='table_loiha13.1'),
    path('projects-department/table/ilova-12.2', views.get_data_table_Loiha122, name='table_loiha12.2'),
    path('projects-department/table/ilova-12.1', views.get_data_table_Loiha121, name='table_loiha12.1'),
    path('projects-department/table/ilova-12', views.get_data_table_Loiha12, name='table_loiha12'),
    path('projects-department/table/ilova-10', views.get_data_table_Loiha10, name='table_loiha10'),
    path('projects-department/table/ilova-6', views.get_data_table_Loiha6, name='table_loiha6'),
    path('projects-department/table/ilova-13', views.get_data_table_Loiha13, name='table_loiha13'),

    # 2 departament
    path('exports-department/table/sanoat', views.get_data_table_sanoat, name='table_sanoat'),
    path('exports-department/table/kx', views.get_data_table_kh, name='table_kx'),
    path('exports-department/table/table_1', views.get_data_table_first_table, name='table_first'),
    path('exports-department/table/kunliu', views.get_data_table_kunliu, name='table_kunliu'),

    path('projects-department/table/ilova-13.1/filter/<slug:filter_slug>', views.table_filter_loiha131, name='table_filter_loiha131'),
    path('projects-department/table/ilova-4.1/filter/<slug:filter_slug>', views.table_filter_loiha41, name='table_filter_loiha41'),
    path('projects-department/table/ilova-5.2/filter/<slug:filter_slug>', views.table_filter_loiha52, name='table_filter_loiha52'),
    path('projects-department/table/ilova-14/filter/<slug:filter_slug>', views.table_filter_loiha14, name='table_filter_loiha14'),
    path('projects-department/table/ilova-12.2/filter/<slug:filter_slug>', views.table_filter_loiha122, name='table_filter_loiha122'),
    path('projects-department/table/ilova-12.1/filter/<slug:filter_slug>', views.table_filter_loiha121, name='table_filter_loiha121'),
    path('projects-department/table/ilova-12/filter/<slug:filter_slug>', views.table_filter_loiha12, name='table_filter_loiha12'),
    path('projects-department/table/ilova-10/filter/<slug:filter_slug>', views.table_filter_loiha10, name='table_filter_loiha10'),
    path('projects-department/table/ilova-6/filter/<slug:filter_slug>', views.table_filter_loiha6, name='table_filter_loiha6'),
    path('projects-department/table/ilova-13/filter/<slug:filter_slug>', views.table_filter_loiha13, name='table_filter_loiha13'),

    # 2 departament
    path('exports-department/table/sanoat/filter/<slug:filter_slug>', views.table_filter_sanoat, name="table_filter_sanoat"),
    path('exports-department/table/kx/filter/<slug:filter_slug>', views.table_filter_kx, name="table_filter_kx"),
    path('exports-department/table/table_1/filter/<slug:filter_slug>', views.table_filter_first_table, name="table_filter_first_table"),
    path('exports-department/table/kunliu/filter/<slug:filter_slug>', views.table_filter_kunliu, name="table_filter_kunliu")
]