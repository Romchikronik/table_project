from django.forms import ModelForm
from .models import *


class TableFormLoiha41(ModelForm):
    class Meta:
        model = Loiha41
        fields = [
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
        ]


class TableFormLoiha52(ModelForm):
    class Meta:
        model = Loiha52
        fields = [
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
        ]


class TableFormLoiha14(ModelForm):
    class Meta:
        model = Loiha14
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


class TableFormLoiha131(ModelForm):
    class Meta:
        model = Loiha131
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


class TableFormLoiha122(ModelForm):
    class Meta:
        model = Loiha122
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


class TableFormLoiha121(ModelForm):
    class Meta:
        model = Loiha121
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


class TableFormLoiha12(ModelForm):
    class Meta:
        model = Loiha12
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


class TableFormLoiha10(ModelForm):
    class Meta:
        model = Loiha10
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


class TableFormLoiha6(ModelForm):
    class Meta:
        model = Loiha6
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


class TableFormLoiha13(ModelForm):
    class Meta:
        model = Loiha13
        fields = [
            'project_name',
            'project_activity',
            'project_capacity',
            'grate_sources_of_financing',
            'foreign_financing_grate_sources_of_financing',
            'sources_sources_of_financing',
            'created_new_jobs'
        ]


class TableFormSanoat(ModelForm):
    class Meta:
        model = Sanoat
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


class TableFormKX(ModelForm):
    class Meta:
        model = KH

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


class TableFirstForm(ModelForm):
    class Meta:
        model = FirstTable

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


class TableKunliuForm(ModelForm):
    class Meta:
        model = Kunliu
        fields = [
            'sanoat',
            'meva_sabz',
            'overall',
            'date_of_forecast',
        ]


class TableJamiForm(ModelForm):
    class Meta:
        model = JamiVault
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


class TableQuarterForm(ModelForm):
    class Meta:
        model = QuarterVault
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


class TableMonthForm(ModelForm):
    class Meta:
        model = MonthVault
        fields = [
            'january_loiha_soni_reja',
            'january_loiha_soni_amalda',
            'january_umumiy_kiymati_reja',
            'january_umumiy_kiymati_amalda',
            'january_uz_mablag_reja',
            'january_uz_mablag_amalda',
            'january_bank_kredit_reja',
            'january_bank_kredit_amalda',
            'january_xorijiy_kredit_reja',
            'january_xorijiy_kredit_amalda',
            'january_xorijiy_invest_reja',
            'january_xorijiy_invest_amalda',
            'january_yangi_ish_reja',
            'january_yangi_ish_amalda',
            'january_ishlab_chiqarish_reja',
            'january_ishlab_chiqarish_amalda',
            'january_import_reja',
            'january_import_amalda',
            'january_export_reja',
            'january_export_amalda',
            'january_budget_reja',
            'january_budget_amalda',

            'february_loiha_soni_reja',
            'february_loiha_soni_amalda',
            'february_umumiy_kiymati_reja',
            'february_umumiy_kiymati_amalda',
            'february_uz_mablag_reja',
            'february_uz_mablag_amalda',
            'february_bank_kredit_reja',
            'february_bank_kredit_amalda',
            'february_xorijiy_kredit_reja',
            'february_xorijiy_kredit_amalda',
            'february_xorijiy_invest_reja',
            'february_xorijiy_invest_amalda',
            'february_yangi_ish_reja',
            'february_yangi_ish_amalda',
            'february_ishlab_chiqarish_reja',
            'february_ishlab_chiqarish_amalda',
            'february_import_reja',
            'february_import_amalda',
            'february_export_reja',
            'february_export_amalda',
            'february_budget_reja',
            'february_budget_amalda',

            'march_loiha_soni_reja',
            'march_loiha_soni_amalda',
            'march_umumiy_kiymati_reja',
            'march_umumiy_kiymati_amalda',
            'march_uz_mablag_reja',
            'march_uz_mablag_amalda',
            'march_bank_kredit_reja',
            'march_bank_kredit_amalda',
            'march_xorijiy_kredit_reja',
            'march_xorijiy_kredit_amalda',
            'march_xorijiy_invest_reja',
            'march_xorijiy_invest_amalda',
            'march_yangi_ish_reja',
            'march_yangi_ish_amalda',
            'march_ishlab_chiqarish_reja',
            'march_ishlab_chiqarish_amalda',
            'march_import_reja',
            'march_import_amalda',
            'march_export_reja',
            'march_export_amalda',
            'march_budget_reja',
            'march_budget_amalda',

            'april_loiha_soni_reja',
            'april_loiha_soni_amalda',
            'april_umumiy_kiymati_reja',
            'april_umumiy_kiymati_amalda',
            'april_uz_mablag_reja',
            'april_uz_mablag_amalda',
            'april_bank_kredit_reja',
            'april_bank_kredit_amalda',
            'april_xorijiy_kredit_reja',
            'april_xorijiy_kredit_amalda',
            'april_xorijiy_invest_reja',
            'april_xorijiy_invest_amalda',
            'april_yangi_ish_reja',
            'april_yangi_ish_amalda',
            'april_ishlab_chiqarish_reja',
            'april_ishlab_chiqarish_amalda',
            'april_import_reja',
            'april_import_amalda',
            'april_export_reja',
            'april_export_amalda',
            'april_budget_reja',
            'april_budget_amalda',

            'may_loiha_soni_reja',
            'may_loiha_soni_amalda',
            'may_umumiy_kiymati_reja',
            'may_umumiy_kiymati_amalda',
            'may_uz_mablag_reja',
            'may_uz_mablag_amalda',
            'may_bank_kredit_reja',
            'may_bank_kredit_amalda',
            'may_xorijiy_kredit_reja',
            'may_xorijiy_kredit_amalda',
            'may_xorijiy_invest_reja',
            'may_xorijiy_invest_amalda',
            'may_yangi_ish_reja',
            'may_yangi_ish_amalda',
            'may_ishlab_chiqarish_reja',
            'may_ishlab_chiqarish_amalda',
            'may_import_reja',
            'may_import_amalda',
            'may_export_reja',
            'may_export_amalda',
            'may_budget_reja',
            'may_budget_amalda',

            'june_loiha_soni_reja',
            'june_loiha_soni_amalda',
            'june_umumiy_kiymati_reja',
            'june_umumiy_kiymati_amalda',
            'june_uz_mablag_reja',
            'june_uz_mablag_amalda',
            'june_bank_kredit_reja',
            'june_bank_kredit_amalda',
            'june_xorijiy_kredit_reja',
            'june_xorijiy_kredit_amalda',
            'june_xorijiy_invest_reja',
            'june_xorijiy_invest_amalda',
            'june_yangi_ish_reja',
            'june_yangi_ish_amalda',
            'june_ishlab_chiqarish_reja',
            'june_ishlab_chiqarish_amalda',
            'june_import_reja',
            'june_import_amalda',
            'june_export_reja',
            'june_export_amalda',
            'june_budget_reja',
            'june_budget_amalda',

            'july_loiha_soni_reja',
            'july_loiha_soni_amalda',
            'july_umumiy_kiymati_reja',
            'july_umumiy_kiymati_amalda',
            'july_uz_mablag_reja',
            'july_uz_mablag_amalda',
            'july_bank_kredit_reja',
            'july_bank_kredit_amalda',
            'july_xorijiy_kredit_reja',
            'july_xorijiy_kredit_amalda',
            'july_xorijiy_invest_reja',
            'july_xorijiy_invest_amalda',
            'july_yangi_ish_reja',
            'july_yangi_ish_amalda',
            'july_ishlab_chiqarish_reja',
            'july_ishlab_chiqarish_amalda',
            'july_import_reja',
            'july_import_amalda',
            'july_export_reja',
            'july_export_amalda',
            'july_budget_reja',
            'july_budget_amalda',

            'august_loiha_soni_reja',
            'august_loiha_soni_amalda',
            'august_umumiy_kiymati_reja',
            'august_umumiy_kiymati_amalda',
            'august_uz_mablag_reja',
            'august_uz_mablag_amalda',
            'august_bank_kredit_reja',
            'august_bank_kredit_amalda',
            'august_xorijiy_kredit_reja',
            'august_xorijiy_kredit_amalda',
            'august_xorijiy_invest_reja',
            'august_xorijiy_invest_amalda',
            'august_yangi_ish_reja',
            'august_yangi_ish_amalda',
            'august_ishlab_chiqarish_reja',
            'august_ishlab_chiqarish_amalda',
            'august_import_reja',
            'august_import_amalda',
            'august_export_reja',
            'august_export_amalda',
            'august_budget_reja',
            'august_budget_amalda',

            'september_loiha_soni_reja',
            'september_loiha_soni_amalda',
            'september_umumiy_kiymati_reja',
            'september_umumiy_kiymati_amalda',
            'september_uz_mablag_reja',
            'september_uz_mablag_amalda',
            'september_bank_kredit_reja',
            'september_bank_kredit_amalda',
            'september_xorijiy_kredit_reja',
            'september_xorijiy_kredit_amalda',
            'september_xorijiy_invest_reja',
            'september_xorijiy_invest_amalda',
            'september_yangi_ish_reja',
            'september_yangi_ish_amalda',
            'september_ishlab_chiqarish_reja',
            'september_ishlab_chiqarish_amalda',
            'september_import_reja',
            'september_import_amalda',
            'september_export_reja',
            'september_export_amalda',
            'september_budget_reja',
            'september_budget_amalda',

            'october_loiha_soni_reja',
            'october_loiha_soni_amalda',
            'october_umumiy_kiymati_reja',
            'october_umumiy_kiymati_amalda',
            'october_uz_mablag_reja',
            'october_uz_mablag_amalda',
            'october_bank_kredit_reja',
            'october_bank_kredit_amalda',
            'october_xorijiy_kredit_reja',
            'october_xorijiy_kredit_amalda',
            'october_xorijiy_invest_reja',
            'october_xorijiy_invest_amalda',
            'october_yangi_ish_reja',
            'october_yangi_ish_amalda',
            'october_ishlab_chiqarish_reja',
            'october_ishlab_chiqarish_amalda',
            'october_import_reja',
            'october_import_amalda',
            'october_export_reja',
            'october_export_amalda',
            'october_budget_reja',
            'october_budget_amalda',

            'november_loiha_soni_reja',
            'november_loiha_soni_amalda',
            'november_umumiy_kiymati_reja',
            'november_umumiy_kiymati_amalda',
            'november_uz_mablag_reja',
            'november_uz_mablag_amalda',
            'november_bank_kredit_reja',
            'november_bank_kredit_amalda',
            'november_xorijiy_kredit_reja',
            'november_xorijiy_kredit_amalda',
            'november_xorijiy_invest_reja',
            'november_xorijiy_invest_amalda',
            'november_yangi_ish_reja',
            'november_yangi_ish_amalda',
            'november_ishlab_chiqarish_reja',
            'november_ishlab_chiqarish_amalda',
            'november_import_reja',
            'november_import_amalda',
            'november_export_reja',
            'november_export_amalda',
            'november_budget_reja',
            'november_budget_amalda',

            'december_loiha_soni_reja',
            'december_loiha_soni_amalda',
            'december_umumiy_kiymati_reja',
            'december_umumiy_kiymati_amalda',
            'december_uz_mablag_reja',
            'december_uz_mablag_amalda',
            'december_bank_kredit_reja',
            'december_bank_kredit_amalda',
            'december_xorijiy_kredit_reja',
            'december_xorijiy_kredit_amalda',
            'december_xorijiy_invest_reja',
            'december_xorijiy_invest_amalda',
            'december_yangi_ish_reja',
            'december_yangi_ish_amalda',
            'december_ishlab_chiqarish_reja',
            'december_ishlab_chiqarish_amalda',
            'december_import_reja',
            'december_import_amalda',
            'december_export_reja',
            'december_export_amalda',
            'december_budget_reja',
            'december_budget_amalda',
        ]


class TableBankForm(ModelForm):
    class Meta:
        model = BankVault
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


class TableRejaForm(ModelForm):
    class Meta:
        model = RejaVault

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


