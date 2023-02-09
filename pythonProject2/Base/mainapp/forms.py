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
