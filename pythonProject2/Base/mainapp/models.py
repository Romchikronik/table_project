from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse


# class Departament(models.Model):
#     title = models.CharField(max_length=50, verbose_name="Департамент", blank=True, name=True)
#     slug = models.SlugField(max_length=50, verbose_name='URL', blank=True, name=True)


class District(models.Model):
    id = models.AutoField(primary_key=True)
    district = models.CharField(max_length=50, verbose_name="Район", blank=True, null=True)

    def __str__(self):
        return self.district

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'


class CustomUser(AbstractUser):
    district = models.ForeignKey(District, on_delete=models.PROTECT, blank=True, null=True)

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'

    def __str__(self):
        return self.username


class Loiha41(models.Model):
    district = models.ForeignKey(District, on_delete=models.PROTECT, verbose_name='Район')
    bill_sum_industry = models.FloatField(blank=True, verbose_name="mlrd. so'm")
    picture_of_growth_industry = models.FloatField(blank=True, verbose_name="o'shish sur'ti%")
    forecast_industry = models.FloatField(blank=True, verbose_name="prognoz")
    difference_industry = models.FloatField(blank=True, verbose_name="farqi (-;+)")
    bill_sum_locality = models.FloatField(blank=True, verbose_name="mlrd. so'm")
    picture_of_growth_locality = models.FloatField(blank=True, verbose_name="o'shish sur'ti%")
    forecast_locality = models.FloatField(blank=True, verbose_name="prognoz")
    difference_locality = models.FloatField(blank=True, verbose_name="farqi (-;+)")
    bill_sum_construction = models.FloatField(blank=True, verbose_name="mlrd. so'm")
    picture_of_growth_construction = models.FloatField(blank=True, verbose_name="o'shish sur'ti%")
    forecast_construction = models.FloatField(blank=True, verbose_name="prognoz")
    difference_construction = models.FloatField(blank=True, verbose_name="farqi (-;+)")
    bill_sum_services = models.FloatField(blank=True, verbose_name="mlrd. so'm")
    picture_of_growth_services = models.FloatField(blank=True, verbose_name="o'shish sur'ti%")
    forecast_services = models.FloatField(blank=True, verbose_name="prognoz")
    difference_services = models.FloatField(blank=True, verbose_name="farqi (-;+)")
    bill_sum_retail = models.FloatField(blank=True, verbose_name="mlrd. so'm")
    picture_of_growth_retail = models.FloatField(blank=True, verbose_name="o'shish sur'ti%")
    forecast_retail = models.FloatField(blank=True, verbose_name="prognoz")
    difference_retail = models.FloatField(blank=True, verbose_name="farqi (-;+)")
    thousand_dollar_international_trade = models.FloatField(blank=True, verbose_name="ming. AQSh doll")
    picture_of_growth_international_trade = models.FloatField(blank=True, verbose_name="o'shish sur'ti%")
    thousand_dollar_export = models.FloatField(blank=True, verbose_name="ming. AQSh doll")
    picture_of_growth_export = models.FloatField(blank=True, verbose_name="o'shish sur'ti%")
    thousand_dollar_import = models.FloatField(blank=True, verbose_name="ming. AQSh doll")
    picture_of_growth_import = models.FloatField(blank=True, verbose_name="o'shish sur'ti%")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name='Дата и время создания')
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата обновления")
    is_published = models.BooleanField(default=True, verbose_name='Опубликовано')

    class Meta:
        verbose_name = 'Таблица 4.1'
        verbose_name_plural = 'Таблицы 4.1'
        ordering = ['-time_update']

    def __str__(self):
        return self.district.district

    def get_absolute_url(self):
        return reverse('loiha4.1', kwargs={'table_id': self.district})


class Loiha52(models.Model):
    district = models.ForeignKey(District, on_delete=models.PROTECT, verbose_name="Район")
    places_of_exploration = models.CharField(max_length=255, verbose_name="Название места, где расположены природные ресурсы(Объекты геологоразведки)")
    sites_of_geo_formations = models.CharField(max_length=255, verbose_name="Участки геологических образований")
    name_of_formations = models.CharField(max_length=255, verbose_name="Наименование месторождений геологических формаций (сырых)")
    unit = models.CharField(max_length=255, verbose_name="Единица измерения")
    abc_categories = models.FloatField(blank=True, verbose_name="A+B+C1 категории")
    c2_category = models.FloatField(blank=True, verbose_name="С2 категория")
    lvl_development_operational_information = models.CharField(max_length=255, verbose_name="Уровень развития")
    date_license_operational_information = models.CharField(max_length=255, verbose_name="Дата и номер лицензии")
    volume_of_production_2017 = models.FloatField(blank=True, verbose_name="Объем добычи в 2017 г.")
    ministry_and_department = models.CharField(max_length=255, verbose_name="Соответствующее министерство и ведомство")
    confirmed_stock_and_date = models.CharField(max_length=255, verbose_name="Подтвержденный отчет о запасах и его дата")
    comment = models.CharField(max_length=255, blank=True, verbose_name="Комментарий")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания записи")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата обновления записи")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    class Meta:
        verbose_name = 'Таблица 5.2'
        verbose_name_plural = 'Таблицы 5.2'
        ordering = ['-time_create']

    def __str__(self):
        return self.district.district


class Loiha6(models.Model):
    district = models.ForeignKey(District, on_delete=models.PROTECT, verbose_name="Район")
    empty_objects = models.CharField(max_length=255, verbose_name="Пустующие объекты")
    adress_empty_objects = models.CharField(max_length=255, verbose_name="Aдрес")
    owner_empty_objects = models.CharField(max_length=255, verbose_name="владелец")
    state_property_amount_empty_objects = models.CharField(max_length=255, verbose_name="государственное имущество (количество)")
    private_property_amount_empty_objects = models.CharField(max_length=255, verbose_name="частное имущуство (количество)")
    unused_production_sites = models.FloatField(blank=True, verbose_name="Неиспользуемые производственные площадки(Га)")
    focused_on_agriculture_unused_production_sites = models.FloatField(blank=True, verbose_name="ориентированное на сельское хозяйство(Га)")
    focused_on_production_unused_production_sites = models.FloatField(blank=True, verbose_name="ориентированное на производство(Га)")
    Investment_proposals_sources = models.CharField(max_length=255, verbose_name="Предложения по инвестициям (источники)")
    preliminary_project_cost_bil_sum_sources = models.CharField(max_length=255, verbose_name="Предварительная стоимость проекта(млн.долл)")
    new_jobs_created_amount_sources = models.CharField(max_length=255, verbose_name="количество созданных навых рабочих мест")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания записи")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата обновления записи")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    class Meta:
        verbose_name = 'Таблица 6'
        verbose_name_plural = 'Таблицы 6'
        ordering = ['-time_create']

    def __str__(self):
        return self.district.district


class Loiha10(models.Model):
    district = models.ForeignKey(District, on_delete=models.PROTECT, verbose_name="Район")
    locality_amount = models.CharField(max_length=255, verbose_name="насленный пункт (количество)")
    residential_buildings_amount = models.CharField(max_length=255, verbose_name="Жилые дома (количество)")
    who_want_to_do_business_residential_buildings = models.CharField(max_length=255, verbose_name="Желающие заняться предпринимательством (количество)")
    percent_residential_buildings = models.CharField(max_length=255, verbose_name="процентное соотношение")
    employed_in_the_sector = models.CharField(max_length=255, verbose_name="дома занятые в секторе")
    animal_husbandry_speciality = models.CharField(max_length=255, verbose_name="животноводство")
    poultry_farming_specialty = models.CharField(max_length=255, verbose_name="птицеводство")
    rabbing_breeding_specialty = models.CharField(max_length=255, verbose_name="кроликоведение")
    Beekeeping_specialty = models.CharField(max_length=255, verbose_name="пчеловодство")
    farm_specialty = models.CharField(max_length=255, verbose_name="фермерство")
    gardening_specialty = models.CharField(max_length=255, verbose_name="садоводство")
    greenhouses_specialty = models.CharField(max_length=255, verbose_name="парники")
    teaching_specialty = models.CharField(max_length=255, verbose_name="преподование")
    small_production_specialty = models.CharField(max_length=255, verbose_name="мелькое производство")
    tourism_specialty = models.CharField(max_length=255, verbose_name="туризм")
    services_specialty = models.CharField(max_length=255, verbose_name="услуги")
    other_specialty = models.CharField(max_length=255, verbose_name="другие")
    remaining_on_the_iron_notebook = models.CharField(max_length=255, verbose_name="железная тетрадь оставшиеся")
    remaining_on_the_youth_notebook = models.CharField(max_length=255, verbose_name="молодёжная тетрадь оставшиеся")
    remaining_on_the_womens_notebook = models.CharField(max_length=255, verbose_name="женская тетрадь оставшиеся")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания записи")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата обновления записи")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    class Meta:
        verbose_name = 'Таблица 10'
        verbose_name_plural = 'Таблицы 10'
        ordering = ['-time_create']

    def __str__(self):
        return self.district.district


class Loiha12(models.Model):
    district = models.ForeignKey(District, on_delete=models.PROTECT, verbose_name="Район")
    all_projects = models.CharField(max_length=255, verbose_name="Все проекты")
    grade = models.CharField(max_length=255, verbose_name="Оценка(млрд долл)")
    workplace = models.CharField(max_length=255, verbose_name="Рабочее место")
    projects_selected_projects_from_all_projects = models.CharField(max_length=255, verbose_name="Проекты")
    grade_selected_projects_from_all_projects = models.CharField(max_length=255, verbose_name="Оценка")
    workplace_selected_projects_from_all_projects = models.CharField(max_length=255, verbose_name="Рабочее место")
    all_projects_at_work_from_all_projects = models.CharField(max_length=255, verbose_name="Проекты")
    grade_at_work_from_all_projects = models.CharField(max_length=255, verbose_name="Оценка (млрд долл)")
    workplace_at_work_from_all_projects = models.CharField(max_length=255, verbose_name="Рабочее место")
    all_projects_will_be_completed_end_the_year_from_all_projects = models.CharField(max_length=255, verbose_name="Проекты")
    grade_will_be_completed_end_the_year_all_projects = models.CharField(max_length=255, verbose_name="Оценка (млрд долл)")
    workplace_will_be_completed_end_the_year_all_projects = models.CharField(max_length=255, verbose_name="Рабочее место")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания записи")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата обновления записи")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    class Meta:
        verbose_name = 'Таблица 12'
        verbose_name_plural = 'Таблицы 12'
        ordering = ['-time_create']

    def __str__(self):
        return self.district.district


class Loiha121(models.Model):
    district = models.ForeignKey(District, on_delete=models.PROTECT, verbose_name="Район")
    approved_holding_companies = models.CharField(max_length=255, verbose_name="Утвержденные холдинговые компании количество")
    entrepreneur = models.CharField(max_length=255, verbose_name="Предложения предпринимателей(ф.и.о)")
    names_of_organizations_priority = models.CharField(max_length=255, verbose_name="Название организации")
    type_of_activity_priority = models.CharField(max_length=255, verbose_name="Тип деятельности")
    projects_the_stated_results = models.CharField(max_length=255, verbose_name="Проекты")
    productive_capacity_stated_results = models.CharField(max_length=255, verbose_name="Производственная мощность")
    grade_stated_results = models.CharField(max_length=255, verbose_name="Оценка")
    workplace_stated_results = models.CharField(max_length=255, verbose_name="Рабочее место")
    export_stated_results = models.CharField(max_length=255, verbose_name="Экспорт")
    other_stated_results = models.CharField(max_length=255, verbose_name="Другое")
    financing = models.CharField(max_length=255, verbose_name="Финансирование")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания записи")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата обновления записи")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    class Meta:
        verbose_name = 'Таблица 12.1'
        verbose_name_plural = 'Таблицы 12.1'
        ordering = ['-time_create']

    def __str__(self):
        return self.district.district


class Loiha122(models.Model):
    district = models.ForeignKey(District, on_delete=models.PROTECT, verbose_name="Район")
    formed_tips = models.CharField(max_length=255, verbose_name="Сформированные советы")
    projects_at_work = models.CharField(max_length=255, verbose_name="Проекты")
    production_capacity_at_work = models.CharField(max_length=255, verbose_name="Производсвенные мощности")
    grade_at_work = models.CharField(max_length=255, verbose_name="Оценка")
    own_funds_grade_at_work = models.CharField(max_length=255, verbose_name="Собственные средства")
    bank_loan_grade_at_work = models.CharField(max_length=255, verbose_name="Банковский кредит")
    foreign_investments_grade_at_work = models.CharField(max_length=255, verbose_name="Иностранные инвестиции")
    workplace_at_work = models.CharField(max_length=255, verbose_name="Уровнь работы")
    export_volume_at_work = models.CharField(max_length=255, verbose_name="Обьем экспорта")
    name_bank_financing = models.CharField(max_length=255, verbose_name="Название банка")
    name_country_financing = models.CharField(max_length=255, verbose_name="название страны")
    organization_name_foreign_financing = models.CharField(max_length=255, verbose_name="название организации")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания записи")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата обновления записи")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    class Meta:
        verbose_name = 'Таблица 12.2'
        verbose_name_plural = 'Таблицы 12.2'
        ordering = ['-time_create']

    def __str__(self):
        return self.district.district


class Loiha13(models.Model):
    district = models.ForeignKey(District, on_delete=models.PROTECT, verbose_name="Район")
    project_name = models.CharField(max_length=255, verbose_name="Название проекта")
    project_activity = models.CharField(max_length=255, verbose_name="Проектная деятельность")
    project_capacity = models.CharField(max_length=255, verbose_name="Проектная мощность")
    grate_sources_of_financing = models.CharField(max_length=255, verbose_name="Оценка в миллиардах долларах")
    foreign_financing_grate_sources_of_financing = models.CharField(max_length=255, verbose_name="Иностранные инвестиции")
    sources_sources_of_financing = models.CharField(max_length=255, verbose_name="Источники")
    created_new_jobs = models.CharField(max_length=255, verbose_name="Cозданные новые рабочие места")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания записи")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата обновления записи")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    class Meta:
        verbose_name = 'Таблица 13'
        verbose_name_plural = 'Таблицы 13'
        ordering = ['-time_create']

    def __str__(self):
        return self.district.district


class Loiha131(models.Model):
    district = models.ForeignKey(District, on_delete=models.PROTECT, verbose_name="Район")
    identified_problems = models.CharField(max_length=255, verbose_name="Известные проблемы")
    bank_identified_problems = models.CharField(max_length=255, verbose_name="Банк")
    land_and_building_identified_problems = models.CharField(max_length=255, verbose_name="Земля и здание")
    public_services_identified_problems = models.CharField(max_length=255, verbose_name="Коммунальные")
    customs_identified_problems = models.CharField(max_length=255, verbose_name="Таможня")
    tax_identified_problems = models.CharField(max_length=255, verbose_name="Налог")
    permission_identified_problems = models.CharField(max_length=255, verbose_name="Разрешения")
    bureaucratic_obstacles_identified_problems = models.CharField(max_length=255, verbose_name="Бюрокартический барьер")
    other_identified_problems = models.CharField(max_length=255, verbose_name="Другое")
    resolved_problems_identified_problems = models.CharField(max_length=255, verbose_name="Решенные проблемы")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания записи")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата обновления записи")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    class Meta:
        verbose_name = 'Таблица 13.1'
        verbose_name_plural = 'Таблицы 13.1'
        ordering = ['-time_create']

    def __str__(self):
        return self.district.district


class Loiha14(models.Model):
    district = models.ForeignKey(District, on_delete=models.PROTECT, verbose_name="Район")
    organization_available_information = models.CharField(max_length=255, verbose_name="Организация")
    kind_of_activity_available_information = models.CharField(max_length=255, verbose_name="Род деятельности")
    available_jobs_available_information = models.CharField(max_length=255, verbose_name="Имеющиеся рабочие места")
    project_activity_at_work = models.CharField(max_length=255, verbose_name="Проектная деятельность")
    grade_at_work = models.CharField(max_length=255, verbose_name="Оценка (млрд долл)")
    own_funds_grade_at_work = models.CharField(max_length=255, verbose_name="Собственные средства")
    bank_loan_grade_at_work = models.CharField(max_length=255, verbose_name="Банковский кредит")
    sources_sources_of_financing = models.CharField(max_length=255, verbose_name="Иностранные инвестиции")
    created_new_jobs_at_work = models.CharField(max_length=255, verbose_name="Созданные рабочие места")
    export_volume_at_work = models.CharField(max_length=255, verbose_name="Обьем экспорта (млрд долл)")
    name_bank_financing = models.CharField(max_length=255, verbose_name="Название банка")
    name_country_financing = models.CharField(max_length=255, verbose_name="Название страны")
    organization_name_foreign_financing = models.CharField(max_length=255, verbose_name="Название организации")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания записи")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата обновления записи")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    class Meta:
        verbose_name = 'Таблица 14'
        verbose_name_plural = 'Таблицы 14'
        ordering = ['-time_create']

    def __str__(self):
        return self.district.district

# 2 отдел


class Sanoat(models.Model):
    district = models.ForeignKey(District, on_delete=models.PROTECT, verbose_name="Район")
    inn_of_sender_or_recipient = models.IntegerField(verbose_name="ИНН отправ./получ.")
    inn = models.IntegerField(verbose_name="ИНН")
    name_of_sender = models.CharField(max_length=255, verbose_name="Наим. отправителя")
    address_of_sender = models.CharField(max_length=255, verbose_name="Адрес отправителя")
    name_of_recipient = models.CharField(max_length=255, verbose_name="Наим. получателя")
    address_of_recipient = models.CharField(max_length=255, verbose_name="Адрес получателя")
    financial_responsible_inn = models.IntegerField(verbose_name="Инн лица отв. за финансовое урегулирование")
    face_responsible_for_finance = models.CharField(max_length=255, verbose_name="лица отв. за финансовое урегулирование")
    address_of_face_responsible_for_finance = models.CharField(max_length=255, verbose_name="Адрес лица отв. за финансовое урегулирование")
    currency_of_contract = models.CharField(max_length=255, verbose_name="Валюта контракта")
    invoice_value = models.FloatField(max_length=255, verbose_name="Фактурная стоимость")
    code_of_goods = models.IntegerField(verbose_name="Код товара")
    name_of_goods = models.CharField(max_length=255, verbose_name="Наим. товара")
    weight_netto = models.FloatField(max_length=255, verbose_name="Вес. нетто")
    stat_price = models.FloatField(max_length=255, verbose_name="Стат. стоимость")
    number_and_date_of_contract = models.CharField(max_length=255, verbose_name="Номер и дата контракта")
    idn = models.IntegerField(verbose_name="ИДН")
    destination_country = models.CharField(max_length=255, verbose_name="Страна отправления/назначения")
    date_of_issue = models.CharField(max_length=255, verbose_name="Дата выпуска")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания записи")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата обновления записи")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    class Meta:
        verbose_name = 'Таблица Саноат'
        verbose_name_plural = 'Таблицы Саноат'
        ordering = ['-time_create']

    def __str__(self):
        return self.district.district


# как именовтать таблицы

class KH(models.Model):
    district = models.ForeignKey(District, on_delete=models.PROTECT, verbose_name="Район")
    inn_of_sender_or_recipient = models.IntegerField(verbose_name="ИНН отправ./получ.")
    inn = models.IntegerField(verbose_name="ИНН")
    name_of_sender = models.CharField(max_length=255, verbose_name="Наим. отправителя")
    address_of_sender = models.CharField(max_length=255, verbose_name="Адрес отправителя")
    name_of_recipient = models.CharField(max_length=255, verbose_name="Наим. получателя")
    address_of_recipient = models.CharField(max_length=255, verbose_name="Адрес получателя")
    financial_responsible_inn = models.IntegerField(verbose_name="Инн лица отв. за финансовое урегулирование")
    face_responsible_for_finance = models.CharField(max_length=255, verbose_name="лица отв. за финансовое урегулирование")
    address_of_face_responsible_for_finance = models.CharField(max_length=255, verbose_name="Адрес лица отв. за финансовое урегулирование")
    currency_of_contract = models.CharField(max_length=255, verbose_name="Валюта контракта")
    invoice_value = models.FloatField(max_length=255, verbose_name="Фактурная стоимость")
    code_of_goods = models.IntegerField(verbose_name="Код товара")
    name_of_goods = models.CharField(max_length=255, verbose_name="Наим. товара")
    weight_netto = models.FloatField(max_length=255, verbose_name="Вес. нетто")
    ton = models.FloatField(max_length=255, verbose_name="Тонна")
    stat_price = models.FloatField(max_length=255, verbose_name="Стат. стоимость")
    number_and_date_of_contract = models.CharField(max_length=255, verbose_name="Номер и дата контракта")
    idn = models.IntegerField(verbose_name="ИДН")
    destination_country = models.CharField(max_length=255, verbose_name="Страна отправления/назначения")
    date_of_issue = models.CharField(max_length=255, verbose_name="Дата выпуска")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания записи")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата обновления записи")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    class Meta:
        verbose_name = 'Таблица KX'
        verbose_name_plural = 'Таблицы KX'
        ordering = ['-time_create']

    def __str__(self):
        return self.district.district


class FirstTable(models.Model):
    district = models.ForeignKey(District, on_delete=models.PROTECT, verbose_name="Район")
    table_id = models.IntegerField(verbose_name="ID")
    cell_name = models.CharField(max_length=255)
    region = models.CharField(max_length=255, verbose_name="Обл")
    date = models.CharField(max_length=255, verbose_name="Дата")
    total = models.CharField(max_length=255, verbose_name="Всего")
    total_total = models.FloatField(max_length=255, verbose_name="Всего")
    total_prom = models.FloatField(max_length=255, verbose_name="пром")
    total_ton = models.FloatField(max_length=255, verbose_name="тонна")
    total_sum = models.FloatField(max_length=255, verbose_name="cумма")
    january_march_prom = models.FloatField(max_length=255, verbose_name="пром")
    january_march_ton = models.FloatField(max_length=255, verbose_name="тонна")
    january_march_sum = models.FloatField(max_length=255, verbose_name="сумма")
    january_prom = models.FloatField(max_length=255, verbose_name="пром")
    january_ton = models.FloatField(max_length=255, verbose_name="тонна")
    january_sum = models.FloatField(max_length=255, verbose_name="сумма")
    february_prom = models.FloatField(max_length=255, verbose_name="пром")
    february_ton = models.FloatField(max_length=255, verbose_name="тонна")
    february_sum = models.FloatField(max_length=255, verbose_name="сумма")
    march_prom = models.FloatField(max_length=255, verbose_name="пром")
    march_ton = models.FloatField(max_length=255, verbose_name="тонна")
    march_sum = models.FloatField(max_length=255, verbose_name="сумма")
    january_april_prom = models.FloatField(max_length=255, verbose_name="пром")
    january_april_ton = models.FloatField(max_length=255, verbose_name="тонна")
    january_april_sum = models.FloatField(max_length=255, verbose_name="сумма")
    january_may_prom = models.FloatField(max_length=255, verbose_name="пром")
    january_may_ton = models.FloatField(max_length=255, verbose_name="тонна")
    january_may_sum = models.FloatField(max_length=255, verbose_name="сумма")
    january_june_prom = models.FloatField(max_length=255, verbose_name="пром")
    january_june_ton = models.FloatField(max_length=255, verbose_name="тонна")
    january_june_sum = models.FloatField(max_length=255, verbose_name="сумма")
    january_july_prom = models.FloatField(max_length=255, verbose_name="пром")
    january_july_ton = models.FloatField(max_length=255, verbose_name="тонна")
    january_july_sum = models.FloatField(max_length=255, verbose_name="сумма")
    january_august_prom = models.FloatField(max_length=255, verbose_name="пром")
    january_august_ton = models.FloatField(max_length=255, verbose_name="тонна")
    january_august_sum = models.FloatField(max_length=255, verbose_name="сумма")
    january_september_prom = models.FloatField(max_length=255, verbose_name="пром")
    january_september_ton = models.FloatField(max_length=255, verbose_name="тонна")
    january_september_sum = models.FloatField(max_length=255, verbose_name="сумма")
    october_24_prom = models.FloatField(max_length=255, verbose_name="пром")
    october_24_ton = models.FloatField(max_length=255, verbose_name="тонна")
    october_24_sum = models.FloatField(max_length=255, verbose_name="сумма")
    october_prom = models.FloatField(max_length=255, verbose_name="пром")
    october_ton = models.FloatField(max_length=255, verbose_name="тонна")
    october_sum = models.FloatField(max_length=255, verbose_name="сумма")
    export = models.FloatField(max_length=255, verbose_name="Ички экспорт")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания записи")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата обновления записи")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    class Meta:
        verbose_name = 'Таблица'
        verbose_name_plural = 'Таблицы'
        ordering = ['-time_create']

    def __str__(self):
        return self.district.district


class Kunliu(models.Model):
    district = models.ForeignKey(District, on_delete=models.PROTECT, verbose_name="Район")
    sanoat = models.CharField(max_length=255, verbose_name="саноат маҳсулотлари")
    meva_sabz = models.CharField(max_length=255, verbose_name="мева-сабзавотлар")
    overall = models.CharField(default="", max_length=255, verbose_name="всего")
    date_of_forecast = models.CharField(max_length=255, verbose_name="Дата прогноза")
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания записи")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата обновления записи")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    class Meta:
        verbose_name = 'Kунлиу'
        verbose_name_plural = 'Kунлиу'
        ordering = ['-time_create']

    def __str__(self):
        return self.district.district

    # general = models.FloatField(verbose_name="Жами")


class JamiVault(models.Model):
    district = models.ForeignKey(District, on_delete=models.PROTECT, verbose_name="Район")

    loiha_soni_reja = models.CharField(max_length=255, verbose_name='Режа')
    loiha_soni_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    umumiy_kiymati_reja = models.CharField(max_length=255, verbose_name='Режа')
    umumiy_kiymati_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    uz_mablag_reja = models.CharField(max_length=255, verbose_name='Режа')
    uz_mablag_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    bank_kredit_reja = models.CharField(max_length=255, verbose_name='Режа')
    bank_kredit_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    xorijiy_kredit_reja = models.CharField(max_length=255, verbose_name='Режа')
    xorijiy_kredit_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    xorijiy_invest_reja = models.CharField(max_length=255, verbose_name='Режа')
    xorijiy_invest_amalda = models.CharField(max_length=255, verbose_name='Амалда')

    yangi_ish_reja = models.CharField(max_length=255, verbose_name='Режа')
    yangi_ish_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    ishlab_chiqarish_reja = models.CharField(max_length=255, verbose_name='Режа')
    ishlab_chiqarish_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    import_reja = models.CharField(max_length=255, verbose_name='Режа')
    import_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    export_reja = models.CharField(max_length=255, verbose_name='Режа')
    export_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    budget_reja = models.CharField(max_length=255, verbose_name='Режа')
    budget_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания записи")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата обновления записи")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    class Meta:
        verbose_name = 'Жами Свод'
        verbose_name_plural = 'Жами Свод'
        ordering = ['-time_create']

    def __str__(self):
        return self.district.district


class QuarterVault(models.Model):
    district = models.ForeignKey(District, on_delete=models.PROTECT, verbose_name="Район")

    loiha_soni_reja = models.CharField(max_length=255, verbose_name='Режа')
    loiha_soni_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    umumiy_kiymati_reja = models.CharField(max_length=255, verbose_name='Режа')
    umumiy_kiymati_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    uz_mablag_reja = models.CharField(max_length=255, verbose_name='Режа')
    uz_mablag_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    bank_kredit_reja = models.CharField(max_length=255, verbose_name='Режа')
    bank_kredit_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    xorijiy_kredit_reja = models.CharField(max_length=255, verbose_name='Режа')
    xorijiy_kredit_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    xorijiy_invest_reja = models.CharField(max_length=255, verbose_name='Режа')
    xorijiy_invest_amalda = models.CharField(max_length=255, verbose_name='Амалда')

    first_quarter_yangi_ish_reja = models.CharField(max_length=255, verbose_name='Режа')
    first_quarter_yangi_ish_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    first_quarter_ishlab_chiqarish_reja = models.CharField(max_length=255, verbose_name='Режа')
    first_quarter_ishlab_chiqarish_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    first_quarter_import_reja = models.CharField(max_length=255, verbose_name='Режа')
    first_quarter_import_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    first_quarter_export_reja = models.CharField(max_length=255, verbose_name='Режа')
    first_quarter_export_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    first_quarter_budget_reja = models.CharField(max_length=255, verbose_name='Режа')
    first_quarter_budget_amalda = models.CharField(max_length=255, verbose_name='Амалда')

    second_quarter_loiha_soni_reja = models.CharField(max_length=255, verbose_name='Режа')
    second_quarter_loiha_soni_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    second_quarter_umumiy_kiymati_reja = models.CharField(max_length=255, verbose_name='Режа')
    second_quarter_umumiy_kiymati_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    second_quarter_uz_mablag_reja = models.CharField(max_length=255, verbose_name='Режа')
    second_quarter_uz_mablag_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    second_quarter_bank_kredit_reja = models.CharField(max_length=255, verbose_name='Режа')
    second_quarter_bank_kredit_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    second_quarter_xorijiy_kredit_reja = models.CharField(max_length=255, verbose_name='Режа')
    second_quarter_xorijiy_kredit_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    second_quarter_xorijiy_invest_reja = models.CharField(max_length=255, verbose_name='Режа')
    second_quarter_xorijiy_invest_amalda = models.CharField(max_length=255, verbose_name='Амалда')

    second_quarter_yangi_ish_reja = models.CharField(max_length=255, verbose_name='Режа')
    second_quarter_yangi_ish_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    second_quarter_ishlab_chiqarish_reja = models.CharField(max_length=255, verbose_name='Режа')
    second_quarter_ishlab_chiqarish_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    second_quarter_import_reja = models.CharField(max_length=255, verbose_name='Режа')
    second_quarter_import_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    second_quarter_export_reja = models.CharField(max_length=255, verbose_name='Режа')
    second_quarter_export_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    second_quarter_budget_reja = models.CharField(max_length=255, verbose_name='Режа')
    second_quarter_budget_amalda = models.CharField(max_length=255, verbose_name='Амалда')

    third_quarter_loiha_soni_reja = models.CharField(max_length=255, verbose_name='Режа')
    third_quarter_loiha_soni_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    third_quarter_umumiy_kiymati_reja = models.CharField(max_length=255, verbose_name='Режа')
    third_quarter_umumiy_kiymati_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    third_quarter_uz_mablag_reja = models.CharField(max_length=255, verbose_name='Режа')
    third_quarter_uz_mablag_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    third_quarter_bank_kredit_reja = models.CharField(max_length=255, verbose_name='Режа')
    third_quarter_bank_kredit_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    third_quarter_xorijiy_kredit_reja = models.CharField(max_length=255, verbose_name='Режа')
    third_quarter_xorijiy_kredit_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    third_quarter_xorijiy_invest_reja = models.CharField(max_length=255, verbose_name='Режа')
    third_quarter_xorijiy_invest_amalda = models.CharField(max_length=255, verbose_name='Амалда')

    third_quarter_yangi_ish_reja = models.CharField(max_length=255, verbose_name='Режа')
    third_quarter_yangi_ish_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    third_quarter_ishlab_chiqarish_reja = models.CharField(max_length=255, verbose_name='Режа')
    third_quarter_ishlab_chiqarish_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    third_quarter_import_reja = models.CharField(max_length=255, verbose_name='Режа')
    third_quarter_import_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    third_quarter_export_reja = models.CharField(max_length=255, verbose_name='Режа')
    third_quarter_export_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    third_quarter_budget_reja = models.CharField(max_length=255, verbose_name='Режа')
    third_quarter_budget_amalda = models.CharField(max_length=255, verbose_name='Амалда')

    fourth_quarter_loiha_soni_reja = models.CharField(max_length=255, verbose_name='Режа')
    fourth_quarter_loiha_soni_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    fourth_quarter_umumiy_kiymati_reja = models.CharField(max_length=255, verbose_name='Режа')
    fourth_quarter_umumiy_kiymati_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    fourth_quarter_uz_mablag_reja = models.CharField(max_length=255, verbose_name='Режа')
    fourth_quarter_uz_mablag_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    fourth_quarter_bank_kredit_reja = models.CharField(max_length=255, verbose_name='Режа')
    fourth_quarter_bank_kredit_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    fourth_quarter_xorijiy_kredit_reja = models.CharField(max_length=255, verbose_name='Режа')
    fourth_quarter_xorijiy_kredit_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    fourth_quarter_xorijiy_invest_reja = models.CharField(max_length=255, verbose_name='Режа')
    fourth_quarter_xorijiy_invest_amalda = models.CharField(max_length=255, verbose_name='Амалда')

    fourth_quarter_yangi_ish_reja = models.CharField(max_length=255, verbose_name='Режа')
    fourth_quarter_yangi_ish_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    fourth_quarter_ishlab_chiqarish_reja = models.CharField(max_length=255, verbose_name='Режа')
    fourth_quarter_ishlab_chiqarish_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    fourth_quarter_import_reja = models.CharField(max_length=255, verbose_name='Режа')
    fourth_quarter_import_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    fourth_quarter_export_reja = models.CharField(max_length=255, verbose_name='Режа')
    fourth_quarter_export_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    fourth_quarter_budget_reja = models.CharField(max_length=255, verbose_name='Режа')
    fourth_quarter_budget_amalda = models.CharField(max_length=255, verbose_name='Амалда')

    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания записи")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата обновления записи")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    class Meta:
        verbose_name = 'Свод Чорак'
        verbose_name_plural = 'Свод Чорак'
        ordering = ['-time_create']

    def __str__(self):
        return self.district.district


class TarmokVault(models.Model):
    district = models.ForeignKey(District, on_delete=models.PROTECT, verbose_name="Район")
    tormok_name = models.CharField(max_length=255, verbose_name='Тармоқлар номи')

    loiha_soni_reja = models.CharField(max_length=255, verbose_name='Режа')
    loiha_soni_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    umumiy_kiymati_reja = models.CharField(max_length=255, verbose_name='Режа')
    umumiy_kiymati_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    uz_mablag_reja = models.CharField(max_length=255, verbose_name='Режа')
    uz_mablag_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    bank_kredit_reja = models.CharField(max_length=255, verbose_name='Режа')
    bank_kredit_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    xorijiy_kredit_reja = models.CharField(max_length=255, verbose_name='Режа')
    xorijiy_kredit_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    xorijiy_invest_reja = models.CharField(max_length=255, verbose_name='Режа')
    xorijiy_invest_amalda = models.CharField(max_length=255, verbose_name='Амалда')

    yangi_ish_reja = models.CharField(max_length=255, verbose_name='Режа')
    yangi_ish_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    ishlab_chiqarish_reja = models.CharField(max_length=255, verbose_name='Режа')
    ishlab_chiqarish_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    import_reja = models.CharField(max_length=255, verbose_name='Режа')
    import_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    export_reja = models.CharField(max_length=255, verbose_name='Режа')
    export_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    budget_reja = models.CharField(max_length=255, verbose_name='Режа')
    budget_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания записи")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата обновления записи")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    class Meta:
        verbose_name = 'Свод Тармок'
        verbose_name_plural = 'Свод Тармок'
        ordering = ['-time_create']

    def __str__(self):
        return self.district.district


class BankVault(models.Model):
    district = models.ForeignKey(District, on_delete=models.PROTECT, verbose_name="Район")

    loiha_soni_reja = models.CharField(max_length=255, verbose_name='Режа')
    loiha_soni_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    umumiy_kiymati_reja = models.CharField(max_length=255, verbose_name='Режа')
    umumiy_kiymati_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    uz_mablag_reja = models.CharField(max_length=255, verbose_name='Режа')
    uz_mablag_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    bank_kredit_reja = models.CharField(max_length=255, verbose_name='Режа')
    bank_kredit_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    xorijiy_kredit_reja = models.CharField(max_length=255, verbose_name='Режа')
    xorijiy_kredit_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    xorijiy_invest_reja = models.CharField(max_length=255, verbose_name='Режа')
    xorijiy_invest_amalda = models.CharField(max_length=255, verbose_name='Амалда')

    yangi_ish_reja = models.CharField(max_length=255, verbose_name='Режа')
    yangi_ish_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    ishlab_chiqarish_reja = models.CharField(max_length=255, verbose_name='Режа')
    ishlab_chiqarish_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    import_reja = models.CharField(max_length=255, verbose_name='Режа')
    import_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    export_reja = models.CharField(max_length=255, verbose_name='Режа')
    export_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    budget_reja = models.CharField(max_length=255, verbose_name='Режа')
    budget_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания записи")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата обновления записи")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    class Meta:
        verbose_name = 'Свод Банк'
        verbose_name_plural = 'Свод Банк'
        ordering = ['-time_create']

    def __str__(self):
        return self.district.district


class MonthVault(models.Model):
    district = models.ForeignKey(District, on_delete=models.PROTECT, verbose_name="Район")

    january_loiha_soni_reja = models.CharField(max_length=255, verbose_name='Режа')
    january_loiha_soni_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    january_umumiy_kiymati_reja = models.CharField(max_length=255, verbose_name='Режа')
    january_umumiy_kiymati_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    january_uz_mablag_reja = models.CharField(max_length=255, verbose_name='Режа')
    january_uz_mablag_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    january_bank_kredit_reja = models.CharField(max_length=255, verbose_name='Режа')
    january_bank_kredit_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    january_xorijiy_kredit_reja = models.CharField(max_length=255, verbose_name='Режа')
    january_xorijiy_kredit_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    january_xorijiy_invest_reja = models.CharField(max_length=255, verbose_name='Режа')
    january_xorijiy_invest_amalda = models.CharField(max_length=255, verbose_name='Амалда')

    january_yangi_ish_reja = models.CharField(max_length=255, verbose_name='Режа')
    january_yangi_ish_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    january_ishlab_chiqarish_reja = models.CharField(max_length=255, verbose_name='Режа')
    january_ishlab_chiqarish_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    january_import_reja = models.CharField(max_length=255, verbose_name='Режа')
    january_import_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    january_export_reja = models.CharField(max_length=255, verbose_name='Режа')
    january_export_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    january_budget_reja = models.CharField(max_length=255, verbose_name='Режа')
    january_budget_amalda = models.CharField(max_length=255, verbose_name='Амалда')

    february_loiha_soni_reja = models.CharField(max_length=255, verbose_name='Режа')
    february_loiha_soni_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    february_umumiy_kiymati_reja = models.CharField(max_length=255, verbose_name='Режа')
    february_umumiy_kiymati_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    february_uz_mablag_reja = models.CharField(max_length=255, verbose_name='Режа')
    february_uz_mablag_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    february_bank_kredit_reja = models.CharField(max_length=255, verbose_name='Режа')
    february_bank_kredit_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    february_xorijiy_kredit_reja = models.CharField(max_length=255, verbose_name='Режа')
    february_xorijiy_kredit_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    february_xorijiy_invest_reja = models.CharField(max_length=255, verbose_name='Режа')
    february_xorijiy_invest_amalda = models.CharField(max_length=255, verbose_name='Амалда')

    february_yangi_ish_reja = models.CharField(max_length=255, verbose_name='Режа')
    february_yangi_ish_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    february_ishlab_chiqarish_reja = models.CharField(max_length=255, verbose_name='Режа')
    february_ishlab_chiqarish_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    february_import_reja = models.CharField(max_length=255, verbose_name='Режа')
    february_import_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    february_export_reja = models.CharField(max_length=255, verbose_name='Режа')
    february_export_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    february_budget_reja = models.CharField(max_length=255, verbose_name='Режа')
    february_budget_amalda = models.CharField(max_length=255, verbose_name='Амалда')

    march_loiha_soni_reja = models.CharField(max_length=255, verbose_name='Режа')
    march_loiha_soni_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    march_umumiy_kiymati_reja = models.CharField(max_length=255, verbose_name='Режа')
    march_umumiy_kiymati_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    march_uz_mablag_reja = models.CharField(max_length=255, verbose_name='Режа')
    march_uz_mablag_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    march_bank_kredit_reja = models.CharField(max_length=255, verbose_name='Режа')
    march_bank_kredit_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    march_xorijiy_kredit_reja = models.CharField(max_length=255, verbose_name='Режа')
    march_xorijiy_kredit_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    march_xorijiy_invest_reja = models.CharField(max_length=255, verbose_name='Режа')
    march_xorijiy_invest_amalda = models.CharField(max_length=255, verbose_name='Амалда')

    march_yangi_ish_reja = models.CharField(max_length=255, verbose_name='Режа')
    march_yangi_ish_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    march_ishlab_chiqarish_reja = models.CharField(max_length=255, verbose_name='Режа')
    march_ishlab_chiqarish_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    march_import_reja = models.CharField(max_length=255, verbose_name='Режа')
    march_import_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    march_export_reja = models.CharField(max_length=255, verbose_name='Режа')
    march_export_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    march_budget_reja = models.CharField(max_length=255, verbose_name='Режа')
    march_budget_amalda = models.CharField(max_length=255, verbose_name='Амалда')

    april_loiha_soni_reja = models.CharField(max_length=255, verbose_name='Режа')
    april_loiha_soni_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    april_umumiy_kiymati_reja = models.CharField(max_length=255, verbose_name='Режа')
    april_umumiy_kiymati_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    april_uz_mablag_reja = models.CharField(max_length=255, verbose_name='Режа')
    april_uz_mablag_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    april_bank_kredit_reja = models.CharField(max_length=255, verbose_name='Режа')
    april_bank_kredit_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    april_xorijiy_kredit_reja = models.CharField(max_length=255, verbose_name='Режа')
    april_xorijiy_kredit_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    april_xorijiy_invest_reja = models.CharField(max_length=255, verbose_name='Режа')
    april_xorijiy_invest_amalda = models.CharField(max_length=255, verbose_name='Амалда')

    april_yangi_ish_reja = models.CharField(max_length=255, verbose_name='Режа')
    april_yangi_ish_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    april_ishlab_chiqarish_reja = models.CharField(max_length=255, verbose_name='Режа')
    april_ishlab_chiqarish_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    april_import_reja = models.CharField(max_length=255, verbose_name='Режа')
    april_import_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    april_export_reja = models.CharField(max_length=255, verbose_name='Режа')
    april_export_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    april_budget_reja = models.CharField(max_length=255, verbose_name='Режа')
    april_budget_amalda = models.CharField(max_length=255, verbose_name='Амалда')

    may_loiha_soni_reja = models.CharField(max_length=255, verbose_name='Режа')
    may_loiha_soni_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    may_umumiy_kiymati_reja = models.CharField(max_length=255, verbose_name='Режа')
    may_umumiy_kiymati_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    may_uz_mablag_reja = models.CharField(max_length=255, verbose_name='Режа')
    may_uz_mablag_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    may_bank_kredit_reja = models.CharField(max_length=255, verbose_name='Режа')
    may_bank_kredit_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    may_xorijiy_kredit_reja = models.CharField(max_length=255, verbose_name='Режа')
    may_xorijiy_kredit_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    may_xorijiy_invest_reja = models.CharField(max_length=255, verbose_name='Режа')
    may_xorijiy_invest_amalda = models.CharField(max_length=255, verbose_name='Амалда')

    may_yangi_ish_reja = models.CharField(max_length=255, verbose_name='Режа')
    may_yangi_ish_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    may_ishlab_chiqarish_reja = models.CharField(max_length=255, verbose_name='Режа')
    may_ishlab_chiqarish_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    may_import_reja = models.CharField(max_length=255, verbose_name='Режа')
    may_import_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    may_export_reja = models.CharField(max_length=255, verbose_name='Режа')
    may_export_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    may_budget_reja = models.CharField(max_length=255, verbose_name='Режа')
    may_budget_amalda = models.CharField(max_length=255, verbose_name='Амалда')

    june_loiha_soni_reja = models.CharField(max_length=255, verbose_name='Режа')
    june_loiha_soni_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    june_umumiy_kiymati_reja = models.CharField(max_length=255, verbose_name='Режа')
    june_umumiy_kiymati_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    june_uz_mablag_reja = models.CharField(max_length=255, verbose_name='Режа')
    june_uz_mablag_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    june_bank_kredit_reja = models.CharField(max_length=255, verbose_name='Режа')
    june_bank_kredit_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    june_xorijiy_kredit_reja = models.CharField(max_length=255, verbose_name='Режа')
    june_xorijiy_kredit_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    june_xorijiy_invest_reja = models.CharField(max_length=255, verbose_name='Режа')
    june_xorijiy_invest_amalda = models.CharField(max_length=255, verbose_name='Амалда')

    june_yangi_ish_reja = models.CharField(max_length=255, verbose_name='Режа')
    june_yangi_ish_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    june_ishlab_chiqarish_reja = models.CharField(max_length=255, verbose_name='Режа')
    june_ishlab_chiqarish_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    june_import_reja = models.CharField(max_length=255, verbose_name='Режа')
    june_import_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    june_export_reja = models.CharField(max_length=255, verbose_name='Режа')
    june_export_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    june_budget_reja = models.CharField(max_length=255, verbose_name='Режа')
    june_budget_amalda = models.CharField(max_length=255, verbose_name='Амалда')

    july_loiha_soni_reja = models.CharField(max_length=255, verbose_name='Режа')
    july_loiha_soni_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    july_umumiy_kiymati_reja = models.CharField(max_length=255, verbose_name='Режа')
    july_umumiy_kiymati_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    july_uz_mablag_reja = models.CharField(max_length=255, verbose_name='Режа')
    july_uz_mablag_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    july_bank_kredit_reja = models.CharField(max_length=255, verbose_name='Режа')
    july_bank_kredit_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    july_xorijiy_kredit_reja = models.CharField(max_length=255, verbose_name='Режа')
    july_xorijiy_kredit_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    july_xorijiy_invest_reja = models.CharField(max_length=255, verbose_name='Режа')
    july_xorijiy_invest_amalda = models.CharField(max_length=255, verbose_name='Амалда')

    july_yangi_ish_reja = models.CharField(max_length=255, verbose_name='Режа')
    july_yangi_ish_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    july_ishlab_chiqarish_reja = models.CharField(max_length=255, verbose_name='Режа')
    july_ishlab_chiqarish_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    july_import_reja = models.CharField(max_length=255, verbose_name='Режа')
    july_import_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    july_export_reja = models.CharField(max_length=255, verbose_name='Режа')
    july_export_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    july_budget_reja = models.CharField(max_length=255, verbose_name='Режа')
    july_budget_amalda = models.CharField(max_length=255, verbose_name='Амалда')

    august_loiha_soni_reja = models.CharField(max_length=255, verbose_name='Режа')
    august_loiha_soni_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    august_umumiy_kiymati_reja = models.CharField(max_length=255, verbose_name='Режа')
    august_umumiy_kiymati_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    august_uz_mablag_reja = models.CharField(max_length=255, verbose_name='Режа')
    august_uz_mablag_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    august_bank_kredit_reja = models.CharField(max_length=255, verbose_name='Режа')
    august_bank_kredit_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    august_xorijiy_kredit_reja = models.CharField(max_length=255, verbose_name='Режа')
    august_xorijiy_kredit_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    august_xorijiy_invest_reja = models.CharField(max_length=255, verbose_name='Режа')
    august_xorijiy_invest_amalda = models.CharField(max_length=255, verbose_name='Амалда')

    august_yangi_ish_reja = models.CharField(max_length=255, verbose_name='Режа')
    august_yangi_ish_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    august_ishlab_chiqarish_reja = models.CharField(max_length=255, verbose_name='Режа')
    august_ishlab_chiqarish_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    august_import_reja = models.CharField(max_length=255, verbose_name='Режа')
    august_import_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    august_export_reja = models.CharField(max_length=255, verbose_name='Режа')
    august_export_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    august_budget_reja = models.CharField(max_length=255, verbose_name='Режа')
    august_budget_amalda = models.CharField(max_length=255, verbose_name='Амалда')

    september_loiha_soni_reja = models.CharField(max_length=255, verbose_name='Режа')
    september_loiha_soni_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    september_umumiy_kiymati_reja = models.CharField(max_length=255, verbose_name='Режа')
    september_umumiy_kiymati_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    september_uz_mablag_reja = models.CharField(max_length=255, verbose_name='Режа')
    september_uz_mablag_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    september_bank_kredit_reja = models.CharField(max_length=255, verbose_name='Режа')
    september_bank_kredit_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    september_xorijiy_kredit_reja = models.CharField(max_length=255, verbose_name='Режа')
    september_xorijiy_kredit_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    september_xorijiy_invest_reja = models.CharField(max_length=255, verbose_name='Режа')
    september_xorijiy_invest_amalda = models.CharField(max_length=255, verbose_name='Амалда')

    september_yangi_ish_reja = models.CharField(max_length=255, verbose_name='Режа')
    september_yangi_ish_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    september_ishlab_chiqarish_reja = models.CharField(max_length=255, verbose_name='Режа')
    september_ishlab_chiqarish_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    september_import_reja = models.CharField(max_length=255, verbose_name='Режа')
    september_import_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    september_export_reja = models.CharField(max_length=255, verbose_name='Режа')
    september_export_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    september_budget_reja = models.CharField(max_length=255, verbose_name='Режа')

    october_loiha_soni_reja = models.CharField(max_length=255, verbose_name='Режа')
    october_loiha_soni_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    october_umumiy_kiymati_reja = models.CharField(max_length=255, verbose_name='Режа')
    october_umumiy_kiymati_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    october_uz_mablag_reja = models.CharField(max_length=255, verbose_name='Режа')
    october_uz_mablag_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    october_bank_kredit_reja = models.CharField(max_length=255, verbose_name='Режа')
    october_bank_kredit_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    october_xorijiy_kredit_reja = models.CharField(max_length=255, verbose_name='Режа')
    october_xorijiy_kredit_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    october_xorijiy_invest_reja = models.CharField(max_length=255, verbose_name='Режа')
    october_xorijiy_invest_amalda = models.CharField(max_length=255, verbose_name='Амалда')

    october_yangi_ish_reja = models.CharField(max_length=255, verbose_name='Режа')
    october_yangi_ish_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    october_ishlab_chiqarish_reja = models.CharField(max_length=255, verbose_name='Режа')
    october_ishlab_chiqarish_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    october_import_reja = models.CharField(max_length=255, verbose_name='Режа')
    october_import_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    october_export_reja = models.CharField(max_length=255, verbose_name='Режа')
    october_export_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    october_budget_reja = models.CharField(max_length=255, verbose_name='Режа')
    october_budget_amalda = models.CharField(max_length=255, verbose_name='Амалда')

    november_loiha_soni_reja = models.CharField(max_length=255, verbose_name='Режа')
    november_loiha_soni_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    november_umumiy_kiymati_reja = models.CharField(max_length=255, verbose_name='Режа')
    november_umumiy_kiymati_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    november_uz_mablag_reja = models.CharField(max_length=255, verbose_name='Режа')
    november_uz_mablag_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    november_bank_kredit_reja = models.CharField(max_length=255, verbose_name='Режа')
    november_bank_kredit_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    november_xorijiy_kredit_reja = models.CharField(max_length=255, verbose_name='Режа')
    november_xorijiy_kredit_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    november_xorijiy_invest_reja = models.CharField(max_length=255, verbose_name='Режа')
    november_xorijiy_invest_amalda = models.CharField(max_length=255, verbose_name='Амалда')

    november_yangi_ish_reja = models.CharField(max_length=255, verbose_name='Режа')
    november_yangi_ish_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    november_ishlab_chiqarish_reja = models.CharField(max_length=255, verbose_name='Режа')
    november_ishlab_chiqarish_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    november_import_reja = models.CharField(max_length=255, verbose_name='Режа')
    november_import_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    november_export_reja = models.CharField(max_length=255, verbose_name='Режа')
    november_export_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    november_budget_reja = models.CharField(max_length=255, verbose_name='Режа')
    november_budget_amalda = models.CharField(max_length=255, verbose_name='Амалда')

    december_loiha_soni_reja = models.CharField(max_length=255, verbose_name='Режа')
    december_loiha_soni_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    december_umumiy_kiymati_reja = models.CharField(max_length=255, verbose_name='Режа')
    december_umumiy_kiymati_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    december_uz_mablag_reja = models.CharField(max_length=255, verbose_name='Режа')
    december_uz_mablag_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    december_bank_kredit_reja = models.CharField(max_length=255, verbose_name='Режа')
    december_bank_kredit_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    december_xorijiy_kredit_reja = models.CharField(max_length=255, verbose_name='Режа')
    december_xorijiy_kredit_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    december_xorijiy_invest_reja = models.CharField(max_length=255, verbose_name='Режа')
    december_xorijiy_invest_amalda = models.CharField(max_length=255, verbose_name='Амалда')

    december_yangi_ish_reja = models.CharField(max_length=255, verbose_name='Режа')
    december_yangi_ish_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    december_ishlab_chiqarish_reja = models.CharField(max_length=255, verbose_name='Режа')
    december_ishlab_chiqarish_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    december_import_reja = models.CharField(max_length=255, verbose_name='Режа')
    december_import_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    december_export_reja = models.CharField(max_length=255, verbose_name='Режа')
    december_export_amalda = models.CharField(max_length=255, verbose_name='Амалда')
    december_budget_reja = models.CharField(max_length=255, verbose_name='Режа')
    december_budget_amalda = models.CharField(max_length=255, verbose_name='Амалда')

    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания записи")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата обновления записи")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    class Meta:
        verbose_name = 'Свод Ойлар'
        verbose_name_plural = 'Свод Ойлар'
        ordering = ['-time_create']

    def __str__(self):
        return self.district.district


class RejaVault(models.Model):
    district = models.ForeignKey(District, on_delete=models.PROTECT, verbose_name="Район")

    reja_loiha_soni = models.CharField(max_length=255, verbose_name='Лойиҳа сони')
    reja_loiha_kiymati = models.CharField(max_length=255, verbose_name='Лойиҳа қиймати, (млн.сўм)')
    reja_mablag = models.CharField(max_length=255, verbose_name='ўз маблағлари млн.сўм')
    reja_kredit = models.CharField(max_length=255, verbose_name='анк кредитлари млн.сўм')
    reja_xorijiy_kredit = models.CharField(max_length=255, verbose_name='хорижий кредитлар минг.долл')
    reja_xorijiy_invest = models.CharField(max_length=255, verbose_name='хорижий инвестициялар минг.долл ')
    reja_ish = models.CharField(max_length=255, verbose_name='Иш ўрни')

    nisbatan_loiha_soni = models.CharField(max_length=255, verbose_name='Лойиҳа сони')
    nisbatan_loiha_kiymati = models.CharField(max_length=255, verbose_name='Лойиҳа қиймати, (млн.сўм)')
    nisbatan_mablag = models.CharField(max_length=255, verbose_name='ўз маблағлари млн.сўм')
    nisbatan_kredit = models.CharField(max_length=255, verbose_name='анк кредитлари млн.сўм')
    nisbatan_xorijiy_kredit = models.CharField(max_length=255, verbose_name='хорижий кредитлар минг.долл')
    nisbatan_xorijiy_invest = models.CharField(max_length=255, verbose_name='хорижий инвестициялар минг.долл ')
    nisbatan_ish = models.CharField(max_length=255, verbose_name='Иш ўрни')

    ish_loiha_soni = models.CharField(max_length=255, verbose_name='Лойиҳа сони')
    ish_loiha_kiymati = models.CharField(max_length=255, verbose_name='Лойиҳа қиймати, (млн.сўм)')
    ish_mablag = models.CharField(max_length=255, verbose_name='ўз маблағлари млн.сўм')
    ish_kredit = models.CharField(max_length=255, verbose_name='анк кредитлари млн.сўм')
    ish_xorijiy_kredit = models.CharField(max_length=255, verbose_name='хорижий кредитлар минг.долл')
    ish_xorijiy_invest = models.CharField(max_length=255, verbose_name='хорижий инвестициялар минг.долл ')

    mud_ish = models.CharField(max_length=255, verbose_name='Иш ўрни')
    mud_loiha_soni = models.CharField(max_length=255, verbose_name='Лойиҳа сони')
    mud_loiha_kiymati = models.CharField(max_length=255, verbose_name='Лойиҳа қиймати, (млн.сўм)')
    mud_mablag = models.CharField(max_length=255, verbose_name='ўз маблағлари млн.сўм')
    mud_kredit = models.CharField(max_length=255, verbose_name='анк кредитлари млн.сўм')
    mud_xorijiy_kredit = models.CharField(max_length=255, verbose_name='хорижий кредитлар минг.долл')
    mud_xorijiy_invest = models.CharField(max_length=255, verbose_name='хорижий инвестициялар минг.долл ')
    mud_ish_second = models.CharField(max_length=255, verbose_name='Иш ўрни')

    aval_loiha_soni = models.CharField(max_length=255, verbose_name='Лойиҳа сони')
    aval_loiha_kiymati = models.CharField(max_length=255, verbose_name='Лойиҳа қиймати, (млн.сўм)')
    aval_mablag = models.CharField(max_length=255, verbose_name='ўз маблағлари млн.сўм')
    aval_kredit = models.CharField(max_length=255, verbose_name='анк кредитлари млн.сўм')
    aval_xorijiy_kredit = models.CharField(max_length=255, verbose_name='хорижий кредитлар минг.долл')
    aval_xorijiy_invest = models.CharField(max_length=255, verbose_name='хорижий инвестициялар минг.долл ')
    aval_ish = models.CharField(max_length=255, verbose_name='Иш ўрни')

    reserve_loiha_soni = models.CharField(max_length=255, verbose_name='Лойиҳа сони')
    reserve_loiha_kiymati = models.CharField(max_length=255, verbose_name='Лойиҳа қиймати, (млн.сўм)')
    reserve_mablag = models.CharField(max_length=255, verbose_name='ўз маблағлари млн.сўм')
    reserve_kredit = models.CharField(max_length=255, verbose_name='анк кредитлари млн.сўм')
    reserve_xorijiy_kredit = models.CharField(max_length=255, verbose_name='хорижий кредитлар минг.долл')
    reserve_xorijiy_invest = models.CharField(max_length=255, verbose_name='хорижий инвестициялар минг.долл ')
    reserve_ish = models.CharField(max_length=255, verbose_name='Иш ўрни')

    total_loiha_soni = models.CharField(max_length=255, verbose_name='Лойиҳа сони')
    total_loiha_kiymati = models.CharField(max_length=255, verbose_name='Лойиҳа қиймати, (млн.сўм)')
    total_mablag = models.CharField(max_length=255, verbose_name='ўз маблағлари млн.сўм')
    total_kredit = models.CharField(max_length=255, verbose_name='анк кредитлари млн.сўм')
    total_xorijiy_kredit = models.CharField(max_length=255, verbose_name='хорижий кредитлар минг.долл')
    total_xorijiy_invest = models.CharField(max_length=255, verbose_name='хорижий инвестициялар минг.долл ')
    total_ish = models.CharField(max_length=255, verbose_name='Иш ўрни')

    time_create = models.DateTimeField(auto_now_add=True, verbose_name="Дата создания записи")
    time_update = models.DateTimeField(auto_now=True, verbose_name="Дата обновления записи")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    class Meta:
        verbose_name = 'Свод Режа'
        verbose_name_plural = 'Свод Режа'
        ordering = ['-time_create']

    def __str__(self):
        return self.district.district








