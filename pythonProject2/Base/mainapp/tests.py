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