from django.test import TestCase

# Create your tests here.

# def get_data_table_Loiha41(request):
#     # user = get_user(request)
#     if get_group_loiha_id(request):
#         # print('I am department user')
#         table_data = show_data_table_to_departament(Loiha41)
#     else:
#         table_data = show_data_table(request, Loiha41)  # model
#
#     page_obj = paginate_page(request, table_data)
#     context = get_context_data(page_obj, 'Илова-4.1', projects_department, table_data)  # title
#     return render(request, src['loiha41'], context)


# def get_data_table_Loiha52(request):
#     if get_group_loiha_id(request):
#         table_data = show_data_table_to_departament(Loiha52)
#     else:
#         table_data = show_data_table(request, Loiha52)
#
#     page_obj = paginate_page(request, table_data)
#     context = get_context_data(page_obj, 'Илова-5.2', projects_department, table_data)
#     return render(request, src['loiha52'], context)


# def get_data_table_Loiha14(request):
#     if get_group_loiha_id(request):
#         table_data = show_data_table_to_departament(Loiha14)
#     else:
#         table_data = show_data_table(request, Loiha14)
#     page_obj = paginate_page(request, table_data)
#     context = get_context_data(page_obj, 'Илова-14', projects_department, table_data)
#     return render(request, src['loiha14'], context)


# def get_data_table_Loiha131(request):
#     if get_group_loiha_id(request):
#         table_data = show_data_table_to_departament(Loiha131)
#     else:
#         table_data = show_data_table(request, Loiha131)
#     page_obj = paginate_page(request, table_data)
#     context = get_context_data(page_obj, 'Илова-13.1', projects_department, table_data)
#     return render(request, src['loiha131'], context)


# def get_data_table_Loiha122(request):
#     if get_group_loiha_id(request):
#         table_data = show_data_table_to_departament(Loiha122)
#     else:
#         table_data = show_data_table(request, Loiha122)
#     page_obj = paginate_page(request, table_data)
#     context = get_context_data(page_obj, 'Илова-12.2', projects_department, table_data)
#     return render(request, src['loiha122'], context)


# def get_data_table_Loiha121(request):
#     if get_group_loiha_id(request):
#         table_data = show_data_table_to_departament(Loiha121)
#     else:
#         table_data = show_data_table(request, Loiha121)
#     page_obj = paginate_page(request, table_data)
#     context = get_context_data(page_obj, 'Илова-12.1', projects_department, table_data)
#     return render(request, src['loiha121'], context)


# def get_data_table_Loiha12(request):
#     if get_group_loiha_id(request):
#         table_data = show_data_table_to_departament(Loiha12)
#     else:
#         table_data = show_data_table(request, Loiha12)
#     page_obj = paginate_page(request, table_data)
#     context = get_context_data(page_obj, 'Илова-12', projects_department, table_data)
#     return render(request, src['loiha12'], context)


# def get_data_table_Loiha10(request):
#     if get_group_loiha_id(request):
#         table_data = show_data_table_to_departament(Loiha10)
#     else:
#         table_data = show_data_table(request, Loiha10)
#     page_obj = paginate_page(request, table_data)
#     context = get_context_data(page_obj, 'Илова-10', projects_department, table_data)
#     return render(request, src['loiha10'], context)


# def get_data_table_Loiha6(request):
#     if get_group_loiha_id(request):
#         table_data = show_data_table_to_departament(Loiha6)
#     else:
#         table_data = show_data_table(request, Loiha6)
#     # table_data = show_data_table(request, Loiha6)
#     page_obj = paginate_page(request, table_data)
#
#     # user_district = District.objects.get(id=user.id)
#     context = get_context_data(page_obj, 'Илова-6', projects_department, table_data)
#     return render(request, src['loiha6'], context)


# def get_data_table_Loiha13(request):
#     if get_group_loiha_id(request):
#         table_data = show_data_table_to_departament(Loiha13)
#     else:
#         table_data = show_data_table(request, Loiha13)
#     page_obj = paginate_page(request, table_data)
#     context = get_context_data(page_obj, 'Илова-13', projects_department, table_data)
#     return render(request, src['loiha13'], context)

# 2 департамент

# def get_data_table_sanoat(request):
#     if get_group_export_id(request):
#         # print('I am department user')
#         table_data = show_data_table_to_departament(Sanoat)
#     else:
#         table_data = show_data_table(request, Sanoat)
#     page_obj = paginate_page(request, table_data)
#     context = get_context_data(page_obj, 'Sanoat', second_department_tables_menu, table_data)
#     return render(request, src['sanoat'], context)


# KX
#
# def get_data_table_kh(request):
#     if get_group_export_id(request):
#         table_data = show_data_table_to_departament(KH)
#     else:
#         table_data = show_data_table(request, KH)
#     page_obj = paginate_page(request, table_data)
#     context = get_context_data(page_obj, 'KX', second_department_tables_menu, table_data)
#     return render(request, src['kx'], context)


# def get_data_table_first_table(request):
#     if get_group_export_id(request):
#         table_data = show_data_table_to_departament(FirstTable)
#     else:
#         table_data = show_data_table(request, FirstTable)
#     page_obj = paginate_page(request, table_data)
#     context = get_context_data(page_obj, 'Таблица 1', second_department_tables_menu, table_data)
#     return render(request, src['table_1'], context)


# def get_data_table_kunliu(request):
#     if get_group_export_id(request):
#         table_data = show_data_table_to_departament(Kunliu)
#     else:
#         table_data = show_data_table(request, Kunliu)
#     page_obj = paginate_page(request, table_data)
#     context = get_context_data(page_obj, 'кунлиу', second_department_tables_menu, table_data)
#     return render(request, src['kunliu'], context)


# 3 департамент
# def get_data_table_jami(request):
#     if get_group_vault_id(request):
#         table_data = show_data_table_to_departament(JamiVault)
#     else:
#         table_data = show_data_table(request, JamiVault)
#     page_obj = paginate_page(request, table_data)
#     context = get_context_data(page_obj, 'Жами свод', third_department_tables_menu, table_data)
#     return render(request, src['jami'], context)


# def get_data_table_quarter(request):
#     if get_group_vault_id(request):
#         table_data = show_data_table_to_departament(QuarterVault)
#     else:
#         table_data = show_data_table(request, QuarterVault)
#     page_obj = paginate_page(request, table_data)
#     context = get_context_data(page_obj, 'Cвод чорак', third_department_tables_menu, table_data)
#     return render(request, src['quarter'], context)

# def get_data_table_month(request):
#     if get_group_vault_id(request):
#         table_data = show_data_table_to_departament(MonthVault)
#     else:
#         table_data = show_data_table(request, MonthVault)
#     page_obj = paginate_page(request, table_data)
#     context = get_context_data(page_obj, 'Cвод ойлар', third_department_tables_menu, table_data)
#     return render(request, src['monthly'], context)

# def get_data_table_bank(request):
#     if get_group_vault_id(request):
#         table_data = show_data_table_to_departament(BankVault)
#     else:
#         table_data = show_data_table(request, BankVault)
#     page_obj = paginate_page(request, table_data)
#     context = get_context_data(page_obj, 'Cвод банк', third_department_tables_menu, table_data)
#     return render(request, src['bank'], context)

# def get_data_table_reja(request):
#     if get_group_vault_id(request):
#         table_data = show_data_table_to_departament(RejaVault)
#     else:
#         table_data = show_data_table(request, RejaVault)
#     page_obj = paginate_page(request, table_data)
#     context = get_context_data(page_obj, 'Cвод режа', third_department_tables_menu, table_data)
#     return render(request, src['reja'], context)

# def get_data_table_tarmok(request):
#     if get_group_vault_id(request):
#         table_data = show_data_table_to_departament(TarmokVault)
#     else:
#         table_data = show_data_table(request, TarmokVault)
#     page_obj = paginate_page(request, table_data)
#     context = get_context_data(page_obj, 'Cвод тармок', third_department_tables_menu, table_data)
#     return render(request, src['tarmok'], context)

# filters

# def table_filter_loiha131(request, filter_slug):
#     if not get_group_loiha_id(request):
#         table = show_data_table(request, Loiha131)
#     else:
#         table = show_data_table_to_departament(Loiha131)
#
#     table = filter_tables(filter_slug, table)
#
#     page_obj = paginate_page(request, table)
#     context = get_context_data(page_obj, 'Илова-13.1', projects_department, table)
#     return render(request, src['loiha131'], context)

#
# def table_filter_loiha41(request, filter_slug):
#
#     if not get_group_loiha_id(request):
#         table = show_data_table(request, Loiha41)
#     else:
#         table = show_data_table_to_departament(Loiha41)
#     # table_data = show_data_table(request, Loiha131)
#     table = filter_tables(filter_slug, table)
#
#     # if filter_slug == 'week':
#     #     now = timezone.now() - timedelta(minutes=60 * 24 * 7)
#     #     table = table.filter(time_create__gte=now)
#     # elif filter_slug == 'month':
#     #     now = timezone.now() - timedelta(minutes=60 * 24 * 30)
#     #     table = table.filter(time_create__gte=now)
#     # elif filter_slug == 'all':
#     #     table = table
#
#     page_obj = paginate_page(request, table)
#     context = get_context_data(page_obj, 'Илова-4.1', projects_department, table)
#     return render(request, src['loiha41'], context)


# def table_filter_loiha52(request, filter_slug):
#     # table = Loiha52.objects.filter(district=request.user.district)
#     if not get_group_loiha_id(request):
#         table = show_data_table(request, Loiha52)
#     else:
#         table = show_data_table_to_departament(Loiha52)
#
#     # table_data = show_data_table(request, Loiha131)
#     table = filter_tables(filter_slug, table)
#
#     page_obj = paginate_page(request, table)
#     context = get_context_data(page_obj, 'Илова-5.2', projects_department, table)
#     return render(request, src['loiha52'], context)


# def table_filter_loiha14(request, filter_slug):
#     # table = Loiha14.objects.filter(district=request.user.district)
#     if not get_group_loiha_id(request):
#         table = show_data_table(request, Loiha14)
#     else:
#         table = show_data_table_to_departament(Loiha14)
#
#     # table_data = show_data_table(request, Loiha131)
#     table = filter_tables(filter_slug, table)
#
#     page_obj = paginate_page(request, table)
#     context = get_context_data(page_obj, 'Илова-14', projects_department, table)
#     return render(request, src['loiha14'], context)


# def table_filter_loiha122(request, filter_slug):
#     if not get_group_loiha_id(request):
#         table = show_data_table(request, Loiha122)
#     else:
#         table = show_data_table_to_departament(Loiha122)
#
#     # table_data = show_data_table(request, Loiha131)
#     table = filter_tables(filter_slug, table)
#
#     page_obj = paginate_page(request, table)
#     context = get_context_data(page_obj, 'Илова-12.2', projects_department, table)
#     return render(request, src['loiha122'], context)


# def table_filter_loiha121(request, filter_slug):
#     if not get_group_loiha_id(request):
#         table = show_data_table(request, Loiha121)
#     else:
#         table = show_data_table_to_departament(Loiha121)
#
#     # table_data = show_data_table(request, Loiha131)
#     table = filter_tables(filter_slug, table)
#
#     page_obj = paginate_page(request, table)
#     context = get_context_data(page_obj, 'Илова-12.1', projects_department, table)
#     return render(request, src['loiha121'], context)


# def table_filter_loiha12(request, filter_slug):
#     if not get_group_loiha_id(request):
#         table = show_data_table(request, Loiha12)
#     else:
#         table = show_data_table_to_departament(Loiha12)
#
#     # table_data = show_data_table(request, Loiha131)
#     table = filter_tables(filter_slug, table)
#
#     page_obj = paginate_page(request, table)
#     context = get_context_data(page_obj, 'Илова-12', projects_department, table)
#     return render(request, src['loiha12'], context)


# def table_filter_loiha10(request, filter_slug):
#     # table = Loiha14.objects.filter(district=request.user.district)
#     # table = show_data_table(request, Loiha10)
#     if not get_group_loiha_id(request):
#         table = show_data_table(request, Loiha10)
#     else:
#         table = show_data_table_to_departament(Loiha10)
#
#     # table_data = show_data_table(request, Loiha131)
#     table = filter_tables(filter_slug, table)
#
#     page_obj = paginate_page(request, table)
#     context = get_context_data(page_obj, 'Илова-10', projects_department, table)
#     return render(request, src['loiha10'], context)

#
# def table_filter_loiha6(request, filter_slug):
#     # table = Loiha14.objects.filter(district=request.user.district)
#     if not get_group_loiha_id(request):
#         table = show_data_table(request, Loiha6)
#     else:
#         table = show_data_table_to_departament(Loiha6)
#
#     # table_data = show_data_table(request, Loiha131)
#     table = filter_tables(filter_slug, table)
#
#     page_obj = paginate_page(request, table)
#     context = get_context_data(page_obj, 'Илова-6', projects_department, table)
#     return render(request, src['loiha6'], context)


# def table_filter_loiha13(request, filter_slug):
#     # table = Loiha14.objects.filter(district=request.user.district)
#     if not get_group_loiha_id(request):
#         table = show_data_table(request, Loiha13)
#     else:
#         table = show_data_table_to_departament(Loiha13)
#
#     # table_data = show_data_table(request, Loiha131)
#     table = filter_tables(filter_slug, table)
#
#     page_obj = paginate_page(request, table)
#     context = get_context_data(page_obj, 'Илова-13', projects_department, table)
#     return render(request, src['loiha13'], context)


# def table_filter_sanoat(request, filter_slug):
#     # table = show_data_table(request, Sanoat)
#     if not get_group_export_id(request):
#         table = show_data_table(request, Sanoat)
#     else:
#         table = show_data_table_to_departament(Sanoat)
#
#     # table_data = show_data_table(request, Loiha131)
#     table = filter_tables(filter_slug, table)
#
#     page_obj = paginate_page(request, table)
#     context = get_context_data(page_obj, 'Sanoat', second_department_tables_menu, table)
#     return render(request, src['sanoat'], context)


#
# def table_filter_kx(request, filter_slug):
#     # table = Loiha14.objects.filter(district=request.user.district)
#     if not get_group_export_id(request):
#         table = show_data_table(request, KH)
#     else:
#         table = show_data_table_to_departament(KH)
#     # table_data = show_data_table(request, Loiha131)
#     table = filter_tables(filter_slug, table)
#
#     page_obj = paginate_page(request, table)
#     context = get_context_data(page_obj, 'KX', second_department_tables_menu, table)
#     return render(request, src['kx'], context)

# def table_filter_first_table(request, filter_slug):
#     # table = Loiha14.objects.filter(district=request.user.district)
#     if not get_group_export_id(request):
#         table = show_data_table(request, FirstTable)
#     else:
#         table = show_data_table_to_departament(FirstTable)
#
#     # table_data = show_data_table(request, Loiha131)
#     table = filter_tables(filter_slug, table)
#
#     page_obj = paginate_page(request, table)
#     context = get_context_data(page_obj, 'Таблица 1', second_department_tables_menu, table)
#     return render(request, src['table_1'], context)

# def table_filter_kunliu(request, filter_slug):
#     if not get_group_export_id(request):
#         table = show_data_table(request, Kunliu)
#     else:
#         table = show_data_table_to_departament(Kunliu)
#
#     # table_data = show_data_table(request, Loiha131)
#     table = filter_tables(filter_slug, table)
#
#     page_obj = paginate_page(request, table)
#     context = get_context_data(page_obj, 'кунлиу', second_department_tables_menu, table)
#     return render(request, src['kunliu'], context)


# 3 department


# def table_filter_table_jami(request, filter_slug):
#     if not get_group_vault_id(request):
#         table = show_data_table(request, JamiVault)
#     else:
#         table = show_data_table_to_departament(JamiVault)
#     table = filter_tables(filter_slug, table)
#
#     page_obj = paginate_page(request, table)
#     context = get_context_data(page_obj, 'Жами свод', third_department_tables_menu, table)
#     return render(request, src['jami'], context)

# Свод Чорак

#
# def table_filter_table_quarter(request, filter_slug):
#     if not get_group_vault_id(request):
#         table = show_data_table(request, QuarterVault)
#     else:
#         table = show_data_table_to_departament(QuarterVault)
#     table = filter_tables(filter_slug, table)
#
#     page_obj = paginate_page(request, table)
#     context = get_context_data(page_obj, 'Cвод чорак', third_department_tables_menu, table)
#     return render(request, src['quarter'], context)

# Свод Ойлар


# def table_filter_table_month(request, filter_slug):
#     if not get_group_vault_id(request):
#         table = show_data_table(request, MonthVault)
#     else:
#         table = show_data_table_to_departament(MonthVault)
#     table = filter_tables(filter_slug, table)
#
#     page_obj = paginate_page(request, table)
#     context = get_context_data(page_obj, 'Cвод ойлар', third_department_tables_menu, table)
#     return render(request, src['monthly'], context)


# Свод Банк

#
# def table_filter_table_bank(request, filter_slug):
#     if not get_group_vault_id(request):
#         table = show_data_table(request, BankVault)
#     else:
#         table = show_data_table_to_departament(BankVault)
#     table = filter_tables(filter_slug, table)
#
#     page_obj = paginate_page(request, table)
#     context = get_context_data(page_obj, 'Cвод банк', third_department_tables_menu, table)
#     return render(request, src['bank'], context)



# Свод Режа

#
# def table_filter_table_reja(request, filter_slug):
#     if not get_group_vault_id(request):
#         table = show_data_table(request, RejaVault)
#     else:
#         table = show_data_table_to_departament(RejaVault)
#     table = filter_tables(filter_slug, table)
#
#     page_obj = paginate_page(request, table)
#     context = get_context_data(page_obj, 'Cвод режа', third_department_tables_menu, table)
#     return render(request, src['reja'], context)


# Свод Tarmok


# def table_filter_table_tarmok(request, filter_slug):
#     if not get_group_vault_id(request):
#         table = show_data_table(request, TarmokVault)
#     else:
#         table = show_data_table_to_departament(TarmokVault)
#     table = filter_tables(filter_slug, table)
#
#     page_obj = paginate_page(request, table)
#     context = get_context_data(page_obj, 'Cвод тармок', third_department_tables_menu, table)
#     return render(request, src['tarmok'], context)


# adddatta

# @login_required
# def add_data_table_Loiha41(request):
#     table_data = show_data_table(request, Loiha41)
#     page_obj = paginate_page(request, table_data)
#     if request.method == 'POST':
#         form = TableFormLoiha41(request.POST)
#         if form.is_valid():
#             try:
#                 Loiha41.objects.create(**form.cleaned_data, district=request.user.district)
#                 return redirect('table_loiha4.1')
#             except:
#                 form.add_error(None, 'Ошибка добавления данных')
#     else:
#         form = TableFormLoiha41()
#     context = make_context_by_form('Илова-4.1', form, projects_department, page_obj)
#     return render(request, 'mainapp/forms/form_loiha41.html', context)
#
#
# def add_data_table_Loiha52(request):
#     table_data = show_data_table(request, Loiha52)
#     page_obj = paginate_page(request, table_data)
#     if request.method == 'POST':
#         form = TableFormLoiha52(request.POST)
#         if form.is_valid():
#             try:
#                 create_data(request, Loiha52, form)
#                 return redirect('table_loiha5.2')
#             except:
#                 form.add_error(None, 'Ошибка добавления данных')
#     else:
#         form = TableFormLoiha52()
#     context = make_context_by_form('Илова-5.2', form, projects_department, page_obj)
#     return render(request, 'mainapp/forms/form_loiha52.html', context)

#
# @login_required
# def add_data_table_Loiha14(request):
#     table_data = show_data_table(request, Loiha14)
#     page_obj = paginate_page(request, table_data)
#     if request.method == 'POST':
#         form = TableFormLoiha14(request.POST)
#         if form.is_valid():
#             try:
#                 Loiha14.objects.create(**form.cleaned_data, district=request.user.district)
#                 return redirect('table_loiha14')
#             except:
#                 form.add_error(None, 'Ошибка добавления данных')
#     else:
#         form = TableFormLoiha14()
#     context = make_context_by_form('Илова-14', form, projects_department, page_obj)
#     return render(request, 'mainapp/forms/form_loiha14.html', context)


# @login_required
# def add_data_table_Loiha131(request):
#     table_data = show_data_table(request, Loiha131)
#     page_obj = paginate_page(request, table_data)
#     if request.method == 'POST':
#         form = TableFormLoiha131(request.POST)
#         if form.is_valid():
#             try:
#                 Loiha131.objects.create(**form.cleaned_data, district=request.user.district)
#                 return redirect('table_loiha13.1')
#             except:
#                 form.add_error(None, 'Ошибка добавления данных')
#     else:
#         form = TableFormLoiha131()
#     context = make_context_by_form('Илова-13.1', form, projects_department, page_obj)
#     return render(request, 'mainapp/forms/form_loiha131.html', context)

#
# @login_required
# def add_data_table_Loiha122(request):
#     table_data = show_data_table(request, Loiha122)
#     page_obj = paginate_page(request, table_data)
#     if request.method == 'POST':
#         form = TableFormLoiha122(request.POST)
#         if form.is_valid():
#             try:
#                 Loiha122.objects.create(**form.cleaned_data, district=request.user.district)
#                 return redirect('table_loiha12.2')
#             except:
#                 form.add_error(None, 'Ошибка добавления данных')
#     else:
#         form = TableFormLoiha122()
#     context = make_context_by_form('Илова-12.2', form, projects_department, page_obj)
#     return render(request, 'mainapp/forms/form_loiha122.html', context)
#
#
# @login_required
# def add_data_table_Loiha121(request):
#     table_data = show_data_table(request, Loiha121)
#     page_obj = paginate_page(request, table_data)
#     if request.method == 'POST':
#         form = TableFormLoiha121(request.POST)
#         if form.is_valid():
#             try:
#                 Loiha121.objects.create(**form.cleaned_data, district=request.user.district)
#                 return redirect('table_loiha12.1')
#             except:
#                 form.add_error(None, 'Ошибка добавления данных')
#     else:
#         form = TableFormLoiha121()
#     context = make_context_by_form('Илова-12.1', form, projects_department, page_obj)
#     return render(request, 'mainapp/forms/form_loiha121.html', context)

# @login_required
# def add_data_table_Loiha12(request):
#     table_data = show_data_table(request, Loiha12)
#     page_obj = paginate_page(request, table_data)
#     if request.method == 'POST':
#         form = TableFormLoiha12(request.POST)
#         if form.is_valid():
#             try:
#                 Loiha12.objects.create(**form.cleaned_data, district=request.user.district)
#                 return redirect('table_loiha12')
#             except:
#                 form.add_error(None, 'Ошибка добавления данных')
#     else:
#         form = TableFormLoiha12()
#     context = make_context_by_form('Илова-12', form, projects_department, page_obj)
#     return render(request, 'mainapp/forms/form_loiha12.html', context)


# @login_required
# def add_data_table_Loiha6(request):
#     table_data = show_data_table(request, Loiha6)
#     page_obj = paginate_page(request, table_data)
#     if request.method == 'POST':
#         form = TableFormLoiha6(request.POST)
#         if form.is_valid():
#             try:
#                 Loiha6.objects.create(**form.cleaned_data, district=request.user.district)
#                 return redirect('table_loiha6')
#             except:
#                 form.add_error(None, 'Ошибка добавления данных')
#     else:
#         form = TableFormLoiha6()
#     context = make_context_by_form('Илова-6', form, projects_department, page_obj)
#     return render(request, 'mainapp/forms/form_loiha6.html', context)

#
# @login_required
# def add_data_table_Loiha10(request):
#     table_data = show_data_table(request, Loiha10)
#     page_obj = paginate_page(request, table_data)
#     if request.method == 'POST':
#         form = TableFormLoiha10(request.POST)
#         if form.is_valid():
#             try:
#                 Loiha10.objects.create(**form.cleaned_data, district=request.user.district)
#                 return redirect('table_loiha10')
#             except:
#                 form.add_error(None, 'Ошибка добавления данных')
#     else:
#         form = TableFormLoiha10()
#     context = make_context_by_form('Илова-10', form, projects_department, page_obj)
#     return render(request, 'mainapp/forms/form_loiha10.html', context)


# @login_required
# def add_data_table_Loiha13(request):
#     table_data = show_data_table(request, Loiha13)
#     page_obj = paginate_page(request, table_data)
#     if request.method == 'POST':
#         form = TableFormLoiha13(request.POST)
#         if form.is_valid():
#             try:
#                 Loiha13.objects.create(**form.cleaned_data, district=request.user.district)
#                 return redirect('table_loiha13')
#             except:
#                 form.add_error(None, 'Ошибка добавления данных')
#     else:
#         form = TableFormLoiha13()
#     context = make_context_by_form('Илова-13', form, projects_department, page_obj)
#     return render(request, 'mainapp/forms/form_loiha13.html', context)



# @login_required
# def add_data_table_sanoat(request):
#     table_data = show_data_table(request, Sanoat)
#     page_obj = paginate_page(request, table_data)
#     if request.method == 'POST':
#         form = TableFormSanoat(request.POST)
#         if form.is_valid():
#             try:
#                 Sanoat.objects.create(**form.cleaned_data, district=request.user.district)
#                 return redirect('table_sanoat')
#             except:
#                 form.add_error(None, 'Ошибка добавления данных')
#     else:
#         form = TableFormSanoat()
#     context = make_context_by_form('Sanoat', form, second_department_tables_menu, page_obj)
#     return render(request, 'mainapp/forms/second_departament/form_sanoat.html', context)



# @login_required
# def add_data_table_kx(request):
#     table_data = show_data_table(request, KH)
#     page_obj = paginate_page(request, table_data)
#     if request.method == 'POST':
#         form = TableFormKX(request.POST)
#         if form.is_valid():
#             try:
#                 KH.objects.create(**form.cleaned_data, district=request.user.district)
#                 return redirect('table_kx')
#             except:
#                 form.add_error(None, 'Ошибка добавления данных')
#     else:
#         form = TableFormKX()
#     context = make_context_by_form('KX', form, second_department_tables_menu, page_obj)
#     return render(request, 'mainapp/forms/second_departament/form_kx.html', context)
#
#
# @login_required
# def add_data_table_1(request):
#     table_data = show_data_table(request, FirstTable)
#     page_obj = paginate_page(request, table_data)
#     if request.method == 'POST':
#         form = TableFirstForm(request.POST)
#         if form.is_valid():
#             try:
#                 FirstTable.objects.create(**form.cleaned_data, district=request.user.district)
#                 return redirect('table_first')
#             except:
#                 form.add_error(None, 'Ошибка добавления данных')
#     else:
#         form = TableFirstForm()
#     context = make_context_by_form('Таблица 1', form, second_department_tables_menu, page_obj)
#     return render(request, 'mainapp/forms/second_departament/form_table_1.html', context)


# Kunliu
#
# @login_required
# def add_data_table_kunliu(request):
#     table_data = show_data_table(request, Kunliu)
#     page_obj = paginate_page(request, table_data)
#     if request.method == 'POST':
#         form = TableKunliuForm(request.POST)
#         if form.is_valid():
#             try:
#                 Kunliu.objects.create(**form.cleaned_data, district=request.user.district)
#                 return redirect('table_kunliu')
#             except:
#                 form.add_error(None, 'Ошибка добавления данных')
#     else:
#         form = TableKunliuForm()
#     context = make_context_by_form('кунлиу', form, second_department_tables_menu, page_obj)
#     return render(request, 'mainapp/forms/second_departament/form_kunliu.html', context)

# @login_required
# def add_data_table_jami(request):
#     table_data = show_data_table(request, JamiVault)
#     page_obj = paginate_page(request, table_data)
#     if request.method == 'POST':
#         form = TableJamiForm(request.POST)
#         if form.is_valid():
#             try:
#                 JamiVault.objects.create(**form.cleaned_data, district=request.user.district)
#                 return redirect('table_jami')
#             except:
#                 form.add_error(None, 'Ошибка добавления данных')
#     else:
#         form = TableJamiForm()
#     context = make_context_by_form('Жами свод', form, third_department_tables_menu, page_obj)
#     return render(request, 'mainapp/forms/third_departament/form_jami.html', context)

# @login_required
# def add_data_table_quarter(request):
#     table_data = show_data_table(request, QuarterVault)
#     page_obj = paginate_page(request, table_data)
#     if request.method == 'POST':
#         form = TableQuarterForm(request.POST)
#         if form.is_valid():
#             try:
#                 QuarterVault.objects.create(**form.cleaned_data, district=request.user.district)
#                 return redirect('table_quarter')
#             except:
#                 form.add_error(None, 'Ошибка добавления данных')
#     else:
#         form = TableQuarterForm()
#     context = make_context_by_form('Cвод чорак', form, third_department_tables_menu, page_obj)
#     return render(request, 'mainapp/forms/third_departament/form_quarter.html', context)
#
#
# @login_required
# def add_data_table_month(request):
#     table_data = show_data_table(request, MonthVault)
#     page_obj = paginate_page(request, table_data)
#     if request.method == 'POST':
#         form = TableMonthForm(request.POST)
#         if form.is_valid():
#             try:
#                 MonthVault.objects.create(**form.cleaned_data, district=request.user.district)
#                 return redirect('table_monthly')
#             except:
#                 form.add_error(None, 'Ошибка добавления данных')
#     else:
#         form = TableMonthForm()
#     context = make_context_by_form('Cвод ойлар', form, third_department_tables_menu, page_obj)
#     return render(request, 'mainapp/forms/third_departament/form_monthly.html', context)

# @login_required
# def add_data_table_bank(request):
#     table_data = show_data_table(request, BankVault)
#     page_obj = paginate_page(request, table_data)
#     if request.method == 'POST':
#         form = TableBankForm(request.POST)
#         if form.is_valid():
#             try:
#                 BankVault.objects.create(**form.cleaned_data, district=request.user.district)
#                 return redirect('table_bank')
#             except:
#                 form.add_error(None, 'Ошибка добавления данных')
#     else:
#         form = TableBankForm()
#     context = make_context_by_form('Cвод банк', form, third_department_tables_menu, page_obj)
#     return render(request, 'mainapp/forms/third_departament/form_bank.html', context)

#
# @login_required
# def add_data_table_reja(request):
#     table_data = show_data_table(request, RejaVault)
#     page_obj = paginate_page(request, table_data)
#     if request.method == 'POST':
#         form = TableRejaForm(request.POST)
#         if form.is_valid():
#             try:
#                 RejaVault.objects.create(**form.cleaned_data, district=request.user.district)
#                 return redirect('table_reja')
#             except:
#                 form.add_error(None, 'Ошибка добавления данных')
#     else:
#         form = TableRejaForm()
#     context = make_context_by_form('Cвод режа', form, third_department_tables_menu, page_obj)
#     return render(request, 'mainapp/forms/third_departament/form_reja.html', context)

#
# @login_required
# def add_data_table_tarmok(request):
#     table_data = show_data_table(request, TarmokVault)
#     page_obj = paginate_page(request, table_data)
#     if request.method == 'POST':
#         form = TableTarmokForm(request.POST)
#         if form.is_valid():
#             try:
#                 TarmokVault.objects.create(**form.cleaned_data, district=request.user.district)
#                 return redirect('table_tarmok')
#             except:
#                 form.add_error(None, 'Ошибка добавления данных')
#     else:
#         form = TableTarmokForm()
#     context = make_context_by_form('Cвод тармок', form, third_department_tables_menu, page_obj)
#     return render(request, 'mainapp/forms/third_departament/form_tarmok.html', context)


# class TableFormLoiha41(ModelForm):
#     class Meta:
#         model = Loiha41
#         fields = [
#             'bill_sum_industry',
#             'picture_of_growth_industry',
#             'forecast_industry',
#             'difference_industry',
#             'bill_sum_locality',
#             'picture_of_growth_locality',
#             'forecast_locality',
#             'difference_locality',
#             'bill_sum_construction',
#             'picture_of_growth_construction',
#             'forecast_construction',
#             'difference_construction',
#             'bill_sum_services',
#             'picture_of_growth_services',
#             'forecast_services',
#             'difference_services',
#             'bill_sum_retail',
#             'picture_of_growth_retail',
#             'forecast_retail',
#             'difference_retail',
#             'thousand_dollar_international_trade',
#             'picture_of_growth_international_trade',
#             'thousand_dollar_export',
#             'picture_of_growth_export',
#             'thousand_dollar_import',
#             'picture_of_growth_import',
#         ]
#
#
# class TableFormLoiha52(ModelForm):
#     class Meta:
#         model = Loiha52
#         fields = [
#             'places_of_exploration',
#             'sites_of_geo_formations',
#             'name_of_formations',
#             'unit',
#             'abc_categories',
#             'c2_category',
#             'lvl_development_operational_information',
#             'date_license_operational_information',
#             'volume_of_production_2017',
#             'ministry_and_department',
#             'confirmed_stock_and_date',
#             'comment'
#         ]
#
#
# class TableFormLoiha14(ModelForm):
#     class Meta:
#         model = Loiha14
#         fields = [
#             'organization_available_information',
#             'kind_of_activity_available_information',
#             'available_jobs_available_information',
#             'project_activity_at_work',
#             'grade_at_work',
#             'own_funds_grade_at_work',
#             'bank_loan_grade_at_work',
#             'sources_sources_of_financing',
#             'created_new_jobs_at_work',
#             'export_volume_at_work',
#             'name_bank_financing',
#             'name_country_financing',
#             'organization_name_foreign_financing'
#         ]
#
#
# class TableFormLoiha131(ModelForm):
#     class Meta:
#         model = Loiha131
#         fields = [
#             'identified_problems',
#             'bank_identified_problems',
#             'land_and_building_identified_problems',
#             'public_services_identified_problems',
#             'customs_identified_problems',
#             'tax_identified_problems',
#             'permission_identified_problems',
#             'bureaucratic_obstacles_identified_problems',
#             'other_identified_problems',
#             'resolved_problems_identified_problems',
#         ]
#
#
# class TableFormLoiha122(ModelForm):
#     class Meta:
#         model = Loiha122
#         fields = [
#             'formed_tips',
#             'projects_at_work',
#             'production_capacity_at_work',
#             'grade_at_work',
#             'own_funds_grade_at_work',
#             'bank_loan_grade_at_work',
#             'foreign_investments_grade_at_work',
#             'workplace_at_work',
#             'export_volume_at_work',
#             'name_bank_financing',
#             'name_country_financing',
#             'organization_name_foreign_financing'
#         ]
#
#
# class TableFormLoiha121(ModelForm):
#     class Meta:
#         model = Loiha121
#         fields = [
#             'approved_holding_companies',
#             'entrepreneur',
#             'names_of_organizations_priority',
#             'type_of_activity_priority',
#             'projects_the_stated_results',
#             'productive_capacity_stated_results',
#             'grade_stated_results',
#             'workplace_stated_results',
#             'export_stated_results',
#             'other_stated_results',
#             'financing',
#         ]
#
#
# class TableFormLoiha12(ModelForm):
#     class Meta:
#         model = Loiha12
#         fields = [
#             'all_projects',
#             'grade',
#             'workplace',
#             'projects_selected_projects_from_all_projects',
#             'grade_selected_projects_from_all_projects',
#             'workplace_selected_projects_from_all_projects',
#             'all_projects_at_work_from_all_projects',
#             'grade_at_work_from_all_projects',
#             'workplace_at_work_from_all_projects',
#             'all_projects_will_be_completed_end_the_year_from_all_projects',
#             'grade_will_be_completed_end_the_year_all_projects',
#             'workplace_will_be_completed_end_the_year_all_projects',
#         ]
#
#
# class TableFormLoiha10(ModelForm):
#     class Meta:
#         model = Loiha10
#         fields = [
#             'locality_amount',
#             'residential_buildings_amount',
#             'who_want_to_do_business_residential_buildings',
#             'percent_residential_buildings',
#             'employed_in_the_sector',
#             'animal_husbandry_speciality',
#             'poultry_farming_specialty',
#             'rabbing_breeding_specialty',
#             'Beekeeping_specialty',
#             'farm_specialty',
#             'gardening_specialty',
#             'greenhouses_specialty',
#             'teaching_specialty',
#             'small_production_specialty',
#             'tourism_specialty',
#             'services_specialty',
#             'other_specialty',
#             'remaining_on_the_iron_notebook',
#             'remaining_on_the_youth_notebook',
#             'remaining_on_the_womens_notebook',
#         ]
#
#
# class TableFormLoiha6(ModelForm):
#     class Meta:
#         model = Loiha6
#         fields = [
#             'empty_objects',
#             'adress_empty_objects',
#             'owner_empty_objects',
#             'state_property_amount_empty_objects',
#             'private_property_amount_empty_objects',
#             'unused_production_sites',
#             'focused_on_agriculture_unused_production_sites',
#             'focused_on_production_unused_production_sites',
#             'Investment_proposals_sources',
#             'preliminary_project_cost_bil_sum_sources',
#             'new_jobs_created_amount_sources'
#         ]
#
#
# class TableFormLoiha13(ModelForm):
#     class Meta:
#         model = Loiha13
#         fields = [
#             'project_name',
#             'project_activity',
#             'project_capacity',
#             'grate_sources_of_financing',
#             'foreign_financing_grate_sources_of_financing',
#             'sources_sources_of_financing',
#             'created_new_jobs'
#         ]
#
#
# class TableFormSanoat(ModelForm):
#     class Meta:
#         model = Sanoat
#         fields = [
#             'inn_of_sender_or_recipient',
#             'inn',
#             'name_of_sender',
#             'address_of_sender',
#             'name_of_recipient',
#             'address_of_recipient',
#             'financial_responsible_inn',
#             'face_responsible_for_finance',
#             'address_of_face_responsible_for_finance',
#             'currency_of_contract',
#             'invoice_value',
#             'code_of_goods',
#             'name_of_goods',
#             'weight_netto',
#             'stat_price',
#             'number_and_date_of_contract',
#             'idn',
#             'destination_country',
#             'date_of_issue'
#         ]
#
#
# class TableFormKX(ModelForm):
#     class Meta:
#         model = KH
#
#         fields = [
#             'inn_of_sender_or_recipient',
#             'inn',
#             'name_of_sender',
#             'address_of_sender',
#             'name_of_recipient',
#             'address_of_recipient',
#             'financial_responsible_inn',
#             'face_responsible_for_finance',
#             'address_of_face_responsible_for_finance',
#             'currency_of_contract',
#             'invoice_value',
#             'code_of_goods',
#             'name_of_goods',
#             'weight_netto',
#             'ton',
#             'stat_price',
#             'number_and_date_of_contract',
#             'idn',
#             'destination_country',
#             'date_of_issue'
#         ]
#
#
# class TableFirstForm(ModelForm):
#     class Meta:
#         model = FirstTable
#
#         fields = [
#             'table_id',
#             'cell_name',
#             'region',
#             'date',
#             'total',
#             'total_total',
#             'total_prom',
#             'total_ton',
#             'total_sum',
#             'january_march_prom',
#             'january_march_ton',
#             'january_march_sum',
#             'january_prom',
#             'january_ton',
#             'january_sum',
#             'february_prom',
#             'february_ton',
#             'february_sum',
#             'march_prom',
#             'march_ton',
#             'march_sum',
#             'january_april_prom',
#             'january_april_ton',
#             'january_april_sum',
#             'january_may_prom',
#             'january_may_ton',
#             'january_may_sum',
#             'january_june_prom',
#             'january_june_ton',
#             'january_june_sum',
#             'january_july_prom',
#             'january_july_ton',
#             'january_july_sum',
#             'january_august_prom',
#             'january_august_ton',
#             'january_august_sum',
#             'january_september_prom',
#             'january_september_ton',
#             'january_september_sum',
#             'october_24_prom',
#             'october_24_ton',
#             'october_24_sum',
#             'october_prom',
#             'october_ton',
#             'october_sum',
#             'export',
#         ]
#
#
# class TableKunliuForm(ModelForm):
#     class Meta:
#         model = Kunliu
#         fields = [
#             'sanoat',
#             'meva_sabz',
#             'overall',
#             'date_of_forecast',
#         ]
#
#
# class TableJamiForm(ModelForm):
#     class Meta:
#         model = JamiVault
#         fields = [
#             'loiha_soni_reja',
#             'loiha_soni_amalda',
#             'umumiy_kiymati_reja',
#             'umumiy_kiymati_amalda',
#             'uz_mablag_reja',
#             'uz_mablag_amalda',
#             'bank_kredit_reja',
#             'bank_kredit_amalda',
#             'xorijiy_kredit_reja',
#             'xorijiy_kredit_amalda',
#             'xorijiy_invest_reja',
#             'xorijiy_invest_amalda',
#             'yangi_ish_reja',
#             'yangi_ish_amalda',
#             'ishlab_chiqarish_reja',
#             'ishlab_chiqarish_amalda',
#             'import_reja',
#             'import_amalda',
#             'export_reja',
#             'export_amalda',
#             'budget_reja',
#             'budget_amalda',
#         ]
#
#
# class TableQuarterForm(ModelForm):
#     class Meta:
#         model = QuarterVault
#         fields = [
#             'loiha_soni_reja',
#             'loiha_soni_amalda',
#             'umumiy_kiymati_reja',
#             'umumiy_kiymati_amalda',
#             'uz_mablag_reja',
#             'uz_mablag_amalda',
#             'bank_kredit_reja',
#             'bank_kredit_amalda',
#             'xorijiy_kredit_reja',
#             'xorijiy_kredit_amalda',
#             'xorijiy_invest_reja',
#             'xorijiy_invest_amalda',
#             'first_quarter_yangi_ish_reja',
#             'first_quarter_yangi_ish_amalda',
#             'first_quarter_ishlab_chiqarish_reja',
#             'first_quarter_ishlab_chiqarish_amalda',
#             'first_quarter_import_reja',
#             'first_quarter_import_amalda',
#             'first_quarter_export_reja',
#             'first_quarter_export_amalda',
#             'first_quarter_budget_reja',
#             'first_quarter_budget_amalda',
#
#             'second_quarter_loiha_soni_reja',
#             'second_quarter_loiha_soni_amalda',
#             'second_quarter_umumiy_kiymati_reja',
#             'second_quarter_umumiy_kiymati_amalda',
#             'second_quarter_uz_mablag_reja',
#             'second_quarter_uz_mablag_amalda',
#             'second_quarter_bank_kredit_reja',
#             'second_quarter_bank_kredit_amalda',
#             'second_quarter_xorijiy_kredit_reja',
#             'second_quarter_xorijiy_kredit_amalda',
#             'second_quarter_xorijiy_invest_reja',
#             'second_quarter_xorijiy_invest_amalda',
#             'second_quarter_yangi_ish_reja',
#             'second_quarter_yangi_ish_amalda',
#             'second_quarter_ishlab_chiqarish_reja',
#             'second_quarter_ishlab_chiqarish_amalda',
#             'second_quarter_import_reja',
#             'second_quarter_import_amalda',
#             'second_quarter_export_reja',
#             'second_quarter_export_amalda',
#             'second_quarter_budget_reja',
#             'second_quarter_budget_amalda',
#
#             'third_quarter_loiha_soni_reja',
#             'third_quarter_loiha_soni_amalda',
#             'third_quarter_umumiy_kiymati_reja',
#             'third_quarter_umumiy_kiymati_amalda',
#             'third_quarter_uz_mablag_reja',
#             'third_quarter_uz_mablag_amalda',
#             'third_quarter_bank_kredit_reja',
#             'third_quarter_bank_kredit_amalda',
#             'third_quarter_xorijiy_kredit_reja',
#             'third_quarter_xorijiy_kredit_amalda',
#             'third_quarter_xorijiy_invest_reja',
#             'third_quarter_xorijiy_invest_amalda',
#             'third_quarter_yangi_ish_reja',
#             'third_quarter_yangi_ish_amalda',
#             'third_quarter_ishlab_chiqarish_reja',
#             'third_quarter_ishlab_chiqarish_amalda',
#             'third_quarter_import_reja',
#             'third_quarter_import_amalda',
#             'third_quarter_export_reja',
#             'third_quarter_export_amalda',
#             'third_quarter_budget_reja',
#             'third_quarter_budget_amalda',
#
#             'fourth_quarter_loiha_soni_reja',
#             'fourth_quarter_loiha_soni_amalda',
#             'fourth_quarter_umumiy_kiymati_reja',
#             'fourth_quarter_umumiy_kiymati_amalda',
#             'fourth_quarter_uz_mablag_reja',
#             'fourth_quarter_uz_mablag_amalda',
#             'fourth_quarter_bank_kredit_reja',
#             'fourth_quarter_bank_kredit_amalda',
#             'fourth_quarter_xorijiy_kredit_reja',
#             'fourth_quarter_xorijiy_kredit_amalda',
#             'fourth_quarter_xorijiy_invest_reja',
#             'fourth_quarter_xorijiy_invest_amalda',
#             'fourth_quarter_yangi_ish_reja',
#             'fourth_quarter_yangi_ish_amalda',
#             'fourth_quarter_ishlab_chiqarish_reja',
#             'fourth_quarter_ishlab_chiqarish_amalda',
#             'fourth_quarter_import_reja',
#             'fourth_quarter_import_amalda',
#             'fourth_quarter_export_reja',
#             'fourth_quarter_export_amalda',
#             'fourth_quarter_budget_reja',
#             'fourth_quarter_budget_amalda',
#         ]
#
#
# class TableMonthForm(ModelForm):
#     class Meta:
#         model = MonthVault
#         fields = [
#             'january_loiha_soni_reja',
#             'january_loiha_soni_amalda',
#             'january_umumiy_kiymati_reja',
#             'january_umumiy_kiymati_amalda',
#             'january_uz_mablag_reja',
#             'january_uz_mablag_amalda',
#             'january_bank_kredit_reja',
#             'january_bank_kredit_amalda',
#             'january_xorijiy_kredit_reja',
#             'january_xorijiy_kredit_amalda',
#             'january_xorijiy_invest_reja',
#             'january_xorijiy_invest_amalda',
#             'january_yangi_ish_reja',
#             'january_yangi_ish_amalda',
#             'january_ishlab_chiqarish_reja',
#             'january_ishlab_chiqarish_amalda',
#             'january_import_reja',
#             'january_import_amalda',
#             'january_export_reja',
#             'january_export_amalda',
#             'january_budget_reja',
#             'january_budget_amalda',
#
#             'february_loiha_soni_reja',
#             'february_loiha_soni_amalda',
#             'february_umumiy_kiymati_reja',
#             'february_umumiy_kiymati_amalda',
#             'february_uz_mablag_reja',
#             'february_uz_mablag_amalda',
#             'february_bank_kredit_reja',
#             'february_bank_kredit_amalda',
#             'february_xorijiy_kredit_reja',
#             'february_xorijiy_kredit_amalda',
#             'february_xorijiy_invest_reja',
#             'february_xorijiy_invest_amalda',
#             'february_yangi_ish_reja',
#             'february_yangi_ish_amalda',
#             'february_ishlab_chiqarish_reja',
#             'february_ishlab_chiqarish_amalda',
#             'february_import_reja',
#             'february_import_amalda',
#             'february_export_reja',
#             'february_export_amalda',
#             'february_budget_reja',
#             'february_budget_amalda',
#
#             'march_loiha_soni_reja',
#             'march_loiha_soni_amalda',
#             'march_umumiy_kiymati_reja',
#             'march_umumiy_kiymati_amalda',
#             'march_uz_mablag_reja',
#             'march_uz_mablag_amalda',
#             'march_bank_kredit_reja',
#             'march_bank_kredit_amalda',
#             'march_xorijiy_kredit_reja',
#             'march_xorijiy_kredit_amalda',
#             'march_xorijiy_invest_reja',
#             'march_xorijiy_invest_amalda',
#             'march_yangi_ish_reja',
#             'march_yangi_ish_amalda',
#             'march_ishlab_chiqarish_reja',
#             'march_ishlab_chiqarish_amalda',
#             'march_import_reja',
#             'march_import_amalda',
#             'march_export_reja',
#             'march_export_amalda',
#             'march_budget_reja',
#             'march_budget_amalda',
#
#             'april_loiha_soni_reja',
#             'april_loiha_soni_amalda',
#             'april_umumiy_kiymati_reja',
#             'april_umumiy_kiymati_amalda',
#             'april_uz_mablag_reja',
#             'april_uz_mablag_amalda',
#             'april_bank_kredit_reja',
#             'april_bank_kredit_amalda',
#             'april_xorijiy_kredit_reja',
#             'april_xorijiy_kredit_amalda',
#             'april_xorijiy_invest_reja',
#             'april_xorijiy_invest_amalda',
#             'april_yangi_ish_reja',
#             'april_yangi_ish_amalda',
#             'april_ishlab_chiqarish_reja',
#             'april_ishlab_chiqarish_amalda',
#             'april_import_reja',
#             'april_import_amalda',
#             'april_export_reja',
#             'april_export_amalda',
#             'april_budget_reja',
#             'april_budget_amalda',
#
#             'may_loiha_soni_reja',
#             'may_loiha_soni_amalda',
#             'may_umumiy_kiymati_reja',
#             'may_umumiy_kiymati_amalda',
#             'may_uz_mablag_reja',
#             'may_uz_mablag_amalda',
#             'may_bank_kredit_reja',
#             'may_bank_kredit_amalda',
#             'may_xorijiy_kredit_reja',
#             'may_xorijiy_kredit_amalda',
#             'may_xorijiy_invest_reja',
#             'may_xorijiy_invest_amalda',
#             'may_yangi_ish_reja',
#             'may_yangi_ish_amalda',
#             'may_ishlab_chiqarish_reja',
#             'may_ishlab_chiqarish_amalda',
#             'may_import_reja',
#             'may_import_amalda',
#             'may_export_reja',
#             'may_export_amalda',
#             'may_budget_reja',
#             'may_budget_amalda',
#
#             'june_loiha_soni_reja',
#             'june_loiha_soni_amalda',
#             'june_umumiy_kiymati_reja',
#             'june_umumiy_kiymati_amalda',
#             'june_uz_mablag_reja',
#             'june_uz_mablag_amalda',
#             'june_bank_kredit_reja',
#             'june_bank_kredit_amalda',
#             'june_xorijiy_kredit_reja',
#             'june_xorijiy_kredit_amalda',
#             'june_xorijiy_invest_reja',
#             'june_xorijiy_invest_amalda',
#             'june_yangi_ish_reja',
#             'june_yangi_ish_amalda',
#             'june_ishlab_chiqarish_reja',
#             'june_ishlab_chiqarish_amalda',
#             'june_import_reja',
#             'june_import_amalda',
#             'june_export_reja',
#             'june_export_amalda',
#             'june_budget_reja',
#             'june_budget_amalda',
#
#             'july_loiha_soni_reja',
#             'july_loiha_soni_amalda',
#             'july_umumiy_kiymati_reja',
#             'july_umumiy_kiymati_amalda',
#             'july_uz_mablag_reja',
#             'july_uz_mablag_amalda',
#             'july_bank_kredit_reja',
#             'july_bank_kredit_amalda',
#             'july_xorijiy_kredit_reja',
#             'july_xorijiy_kredit_amalda',
#             'july_xorijiy_invest_reja',
#             'july_xorijiy_invest_amalda',
#             'july_yangi_ish_reja',
#             'july_yangi_ish_amalda',
#             'july_ishlab_chiqarish_reja',
#             'july_ishlab_chiqarish_amalda',
#             'july_import_reja',
#             'july_import_amalda',
#             'july_export_reja',
#             'july_export_amalda',
#             'july_budget_reja',
#             'july_budget_amalda',
#
#             'august_loiha_soni_reja',
#             'august_loiha_soni_amalda',
#             'august_umumiy_kiymati_reja',
#             'august_umumiy_kiymati_amalda',
#             'august_uz_mablag_reja',
#             'august_uz_mablag_amalda',
#             'august_bank_kredit_reja',
#             'august_bank_kredit_amalda',
#             'august_xorijiy_kredit_reja',
#             'august_xorijiy_kredit_amalda',
#             'august_xorijiy_invest_reja',
#             'august_xorijiy_invest_amalda',
#             'august_yangi_ish_reja',
#             'august_yangi_ish_amalda',
#             'august_ishlab_chiqarish_reja',
#             'august_ishlab_chiqarish_amalda',
#             'august_import_reja',
#             'august_import_amalda',
#             'august_export_reja',
#             'august_export_amalda',
#             'august_budget_reja',
#             'august_budget_amalda',
#
#             'september_loiha_soni_reja',
#             'september_loiha_soni_amalda',
#             'september_umumiy_kiymati_reja',
#             'september_umumiy_kiymati_amalda',
#             'september_uz_mablag_reja',
#             'september_uz_mablag_amalda',
#             'september_bank_kredit_reja',
#             'september_bank_kredit_amalda',
#             'september_xorijiy_kredit_reja',
#             'september_xorijiy_kredit_amalda',
#             'september_xorijiy_invest_reja',
#             'september_xorijiy_invest_amalda',
#             'september_yangi_ish_reja',
#             'september_yangi_ish_amalda',
#             'september_ishlab_chiqarish_reja',
#             'september_ishlab_chiqarish_amalda',
#             'september_import_reja',
#             'september_import_amalda',
#             'september_export_reja',
#             'september_export_amalda',
#             'september_budget_reja',
#             'september_budget_amalda',
#
#             'october_loiha_soni_reja',
#             'october_loiha_soni_amalda',
#             'october_umumiy_kiymati_reja',
#             'october_umumiy_kiymati_amalda',
#             'october_uz_mablag_reja',
#             'october_uz_mablag_amalda',
#             'october_bank_kredit_reja',
#             'october_bank_kredit_amalda',
#             'october_xorijiy_kredit_reja',
#             'october_xorijiy_kredit_amalda',
#             'october_xorijiy_invest_reja',
#             'october_xorijiy_invest_amalda',
#             'october_yangi_ish_reja',
#             'october_yangi_ish_amalda',
#             'october_ishlab_chiqarish_reja',
#             'october_ishlab_chiqarish_amalda',
#             'october_import_reja',
#             'october_import_amalda',
#             'october_export_reja',
#             'october_export_amalda',
#             'october_budget_reja',
#             'october_budget_amalda',
#
#             'november_loiha_soni_reja',
#             'november_loiha_soni_amalda',
#             'november_umumiy_kiymati_reja',
#             'november_umumiy_kiymati_amalda',
#             'november_uz_mablag_reja',
#             'november_uz_mablag_amalda',
#             'november_bank_kredit_reja',
#             'november_bank_kredit_amalda',
#             'november_xorijiy_kredit_reja',
#             'november_xorijiy_kredit_amalda',
#             'november_xorijiy_invest_reja',
#             'november_xorijiy_invest_amalda',
#             'november_yangi_ish_reja',
#             'november_yangi_ish_amalda',
#             'november_ishlab_chiqarish_reja',
#             'november_ishlab_chiqarish_amalda',
#             'november_import_reja',
#             'november_import_amalda',
#             'november_export_reja',
#             'november_export_amalda',
#             'november_budget_reja',
#             'november_budget_amalda',
#
#             'december_loiha_soni_reja',
#             'december_loiha_soni_amalda',
#             'december_umumiy_kiymati_reja',
#             'december_umumiy_kiymati_amalda',
#             'december_uz_mablag_reja',
#             'december_uz_mablag_amalda',
#             'december_bank_kredit_reja',
#             'december_bank_kredit_amalda',
#             'december_xorijiy_kredit_reja',
#             'december_xorijiy_kredit_amalda',
#             'december_xorijiy_invest_reja',
#             'december_xorijiy_invest_amalda',
#             'december_yangi_ish_reja',
#             'december_yangi_ish_amalda',
#             'december_ishlab_chiqarish_reja',
#             'december_ishlab_chiqarish_amalda',
#             'december_import_reja',
#             'december_import_amalda',
#             'december_export_reja',
#             'december_export_amalda',
#             'december_budget_reja',
#             'december_budget_amalda',
#         ]
#
#
# class TableBankForm(ModelForm):
#     class Meta:
#         model = BankVault
#         fields = [
#             'bank_name',
#             'loiha_soni_reja',
#             'loiha_soni_amalda',
#             'umumiy_kiymati_reja',
#             'umumiy_kiymati_amalda',
#             'uz_mablag_reja',
#             'uz_mablag_amalda',
#             'bank_kredit_reja',
#             'bank_kredit_amalda',
#             'xorijiy_kredit_reja',
#             'xorijiy_kredit_amalda',
#             'xorijiy_invest_reja',
#             'xorijiy_invest_amalda',
#
#             'yangi_ish_reja',
#             'yangi_ish_amalda',
#             'ishlab_chiqarish_reja',
#             'ishlab_chiqarish_amalda',
#             'import_reja',
#             'import_amalda',
#             'export_reja',
#             'export_amalda',
#             'budget_reja',
#             'budget_amalda',
#         ]
#
#
# class TableRejaForm(ModelForm):
#     class Meta:
#         model = RejaVault
#
#         fields = [
#             'reja_loiha_soni',
#             'reja_loiha_kiymati',
#             'reja_mablag',
#             'reja_kredit',
#             'reja_xorijiy_kredit',
#             'reja_xorijiy_invest',
#             'reja_ish',
#
#             'nisbatan_loiha_soni',
#             'nisbatan_loiha_kiymati',
#             'nisbatan_mablag',
#             'nisbatan_kredit',
#             'nisbatan_xorijiy_kredit',
#             'nisbatan_xorijiy_invest',
#             'nisbatan_ish',
#
#             'ish_loiha_soni',
#             'ish_loiha_kiymati',
#             'ish_mablag',
#             'ish_kredit',
#             'ish_xorijiy_kredit',
#             'ish_xorijiy_invest',
#
#             'istik_ish',
#             'istik_loiha_soni',
#             'istik_loiha_kiymati',
#             'istik_mablag',
#             'istik_kredit',
#             'istik_xorijiy_kredit',
#             'istik_xorijiy_invest',
#
#             'mud_ish',
#             'mud_loiha_soni',
#             'mud_loiha_kiymati',
#             'mud_mablag',
#             'mud_kredit',
#             'mud_xorijiy_kredit',
#             'mud_xorijiy_invest',
#             'mud_ish_second',
#
#             'aval_loiha_soni',
#             'aval_loiha_kiymati',
#             'aval_mablag',
#             'aval_kredit',
#             'aval_xorijiy_kredit',
#             'aval_xorijiy_invest',
#             'aval_ish',
#
#             'reserve_loiha_soni',
#             'reserve_loiha_kiymati',
#             'reserve_mablag',
#             'reserve_kredit',
#             'reserve_xorijiy_kredit',
#             'reserve_xorijiy_invest',
#             'reserve_ish',
#
#             'total_loiha_soni',
#             'total_loiha_kiymati',
#             'total_mablag',
#             'total_kredit',
#             'total_xorijiy_kredit',
#             'total_xorijiy_invest',
#             'total_ish',
#         ]
#
#
# class TableTarmokForm(ModelForm):
#     class Meta:
#         model = TarmokVault
#
#         fields = [
#             'category',
#             'industry',
#
#             'loiha_soni_reja',
#             'loiha_soni_amalda',
#             'umumiy_kiymati_reja',
#             'umumiy_kiymati_amalda',
#             'uz_mablag_reja',
#             'uz_mablag_amalda',
#             'bank_kredit_reja',
#             'bank_kredit_amalda',
#             'xorijiy_kredit_reja',
#             'xorijiy_kredit_amalda',
#             'xorijiy_invest_reja',
#             'xorijiy_invest_amalda',
#
#             'yangi_ish_reja',
#             'yangi_ish_amalda',
#             'ishlab_chiqarish_reja',
#             'ishlab_chiqarish_amalda',
#             'import_reja',
#             'import_amalda',
#             'export_reja',
#             'export_amalda',
#             'budget_reja',
#             'budget_amalda',
#         ]



#            {% for group in request.user.groups.all %}
#             {% if group.id == 3 %}
#             <th rowspan="3" class="table-primary">HUDUDLAR</th>
#             {% endif %}
#             {% endfor %}



# export html table
#
# from openpyxl import Workbook
# from bs4 import BeautifulSoup
# import requests
# from django.core.paginator import Paginator
#
# def export_table_to_excel(url, filename):
#     # Получаем HTML-страницу
#     response = requests.get(url)
#
#     # Create an HttpResponse object with the file content and appropriate headers
#     soup = BeautifulSoup(response.text, 'html.parser')
#
#     print(url)
#     # Находим таблицу на странице
#     table = soup.find('table')  # https://www.w3schools.com/html/html_tables.aspz
#
#     print(table)
#
#     # Создаем новый Excel-файл
#     wb = Workbook()
#     ws = wb.active
#
#     # Парсим таблицу и записываем ее в Excel-файл
#     for row in table.find_all('tr'):
#         # row_data = []
#         # for cell in row.find_all(['td', 'th']):
#         #     row_data.append(cell.get_text())
#         # ws.append(row_data)
#         row_data = []
#         next_cell_index = 0
#         for cell in row.find_all(['td', 'th']):
#             # Check if the current cell has a rowspan attribute
#             rowspan = int(cell.get('rowspan', 1))
#             colspan = int(cell.get('colspan', 1))
#             if rowspan > 1:
#                 # If the cell has a rowspan, update the index of the next cell to append to the row
#                 next_cell_index += colspan
#
#             # Add the cell's text to the row data
#             row_data.append(cell.get_text())
#
#             # Update the index of the next cell to append to the row
#             next_cell_index += 1
#             if next_cell_index >= len(row_data):
#                 row_data.append('')
#
#         ws.append(row_data)
#
#     # Сохраняем Excel-файл
#     wb.save(filename)
#
#     # Create a file response
#     # with open(filename, 'rb') as f:
#     #     response = HttpResponse(f.read(), content_type='application/vnd.ms-excel')
#     #     response['Content-Disposition'] = f'attachment; filename="{filename}"'
#
#
#     # Open and read the file contents
#     with open(filename, 'rb') as f:
#         file_contents = f.read()
#
#     # Create an HTML response with the file contents
#     response = HttpResponse(file_contents, content_type='application/vnd.ms-excel')
#     response['Content-Disposition'] = f'attachment; filename="{filename}"'
#
#     return response
#
#
# def export_excel_table1(request):
#     page_obj = paginate_page(request, show_data_table(request, FirstTable))
#     for i in range(1, page_obj.paginator.num_pages + 1):  # num_pages - количество страниц в таблице
#         url = f'http://127.0.0.1:8000/exports-department/table/table_1?page={i}'
#         return export_table_to_excel(url, 'table.xlsx')  # .html