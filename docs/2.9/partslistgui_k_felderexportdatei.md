# Спецификации: Поля в файле экспорта

При экспорте спецификации данные изделий выводятся в файл экспорта. Экспортированные таким образом данные можно обрабатывать и снова экспортировать. Однако при импорте записываются только перечисленные далее свойства:

Имя поля в файле экспорта |  Свойство
---|---
P_ARTICLEREF_PARTNO |  Номер изделия
P_ARTICLEREF_VARIANT |  Вариант изделия, Категория Данные ссылки изделия
P_ARTICLEREF_PARTTYPE |  Тип записи данных, Категория Данные ссылки изделия
P_ARTICLEREF_COUNT |  Число штук / количество
P_ARTICLEREF_FUNCTIONGROUP |  Группа функций, Категория Данные ссылки изделия
P_ARTICLEREF_PIECETYPE |  Вид изделия, Категория Данные ссылки изделия
P_ARTICLEREF_ASSIGNMENT |  Присвоение изделия, Категория Данные ссылки изделия
P_ARTICLEREF_ASSEMBLY |  Узел, Категория Данные ссылки изделия
P_ARTICLEREF_POSNR |  Номер позиции, Категория Данные ссылки изделия
P_ARTICLEREF_ADDITIONAL_TEXTFIELD |  Дополнительное поле Текст, Категория Данные ссылки изделия
P_ARTICLEREF_ADDITIONAL_BOOLFIELD |  Дополнительное поле Да/Нет, Категория Данные ссылки изделия
P_ARTICLE_EXTERNAL_PLACEMENT |  Внешнее размещение, Категория Данные ссылки изделия

Следующая таблица содержит список свойств, записываемых в файл экспорта:

Имя поля в файле экспорта |  Свойство
---|---
P_ARTICLEREF_IDENTNAME |  ОУ
P_DESIGNATION_PLANT |  Установка (Главный ид.)
P_DESIGNATION_FULLPLANT |  Установка
P_DESIGNATION_LOCATION |  Место установки (главный ид.)
P_DESIGNATION_FULLLOCATION |  Место установки
P_DESIGNATION_FUNCTIONALASSIGNMENT |  Функц. присвоение (Глав. идентификатор)
P_DESIGNATION_FULLFUNCTIONALASSIGNMENT |  Функциональное присвоение
P_DESIGNATION_PLACEOFINSTALLATION |  Место сборки (главный идентификатор)
P_DESIGNATION_FULLPLACEOFINSTALLATION |  Место сборки
P_DESIGNATION_USERDEFINED |  Определенная пользователем структура (глав. ид.)
P_DESIGNATION_FULLUSERDEFINED |  Опред. пользователем структура
P_DESIGNATION_INSTALLATIONNUMBER |  Номер установки (Главный идентификатор)
P_DESIGNATION_FULLINSTALLATIONNUMBER |  Номер установки
P_DESIGNATION_FULLSUBINSTALLATIONNUMBER |  Номер установки более низкого уровня
P_PROPUSER_DBOBJECTID |  Идентификация объекта
P_INSTANCE_FULLPLACEMENTLOCATION |  Размещение
P_FUNC_DEVICETAG_MAIN |  ОУ (вышестоящее, без структуры проекта)
P_FUNC_DEVICETAG_NESTED |  ОУ (нижестоящее, без структуры проекта)
P_FUNC_PREFIX |  ОУ: предш. цифра
P_FUNC_CODE |  ОУ: буквенное обозначение
P_FUNC_COUNTER |  ОУ: счетчик
P_FUNC_SUFFIX |  ОУ: нижестоящ. счетчик
P_FUNC_NESTEDPREFIX |  ОУ (нижестоящее): Предшествующая цифра
P_FUNC_NESTEDCODE |  ОУ (нижестоящее): Буквенное обозначение
P_FUNC_NESTEDCOUNTER |  ОУ (нижестоящее): Счетчик
P_FUNC_NESTEDSUFFIX |  ОУ (нижестоящее): Подсчетчик
P_FUNC_MOUNTINGLOCATION |  Место монтажа (описат.)
P_FUNC_GRAVINGTEXT |  Текст гравировки
P_FUNC_COMPONENTTYPE |  Определение функции
P_FUNC_TECHNICAL_CHARACTERISTIC |  Технические параметры
P_FUNC_TEXT_AUTOMATIC |  Функциональный текст (автоматически)
P_FUNC_DEVICETAG_FULLNAME |  Имя (без структуры проекта)
P_FUNC_CABLE_LAYOUT_FORM |  Форма схемы кабельных соединений
P_FUNC_TYPE |  Вид представления
P_FUNC_DT_PAGECOUNTER |  ОУ: страница
P_FUNC_DT_PAGESUBCOUNTER |  ОУ: подстраница
P_FUNC_DT_COLUMN |  ОУ: столбец
P_FUNC_DT_ROW |  ОУ: строка
P_FUNC_DT_SECTION |  ОУ: раздел
P_FUNC_DT_FUNCTIONCODE |  ОУ: применение
P_FUNC_DT_SUPPLEMENTARYFIELD01 |  ОУ: доп. поле 1
P_FUNC_DT_SUPPLEMENTARYFIELD02 |  ОУ: доп. поле 2
P_FUNC_DT_SUPPLEMENTARYFIELD03 |  ОУ: доп. поле 3
P_FUNC_DT_SUPPLEMENTARYFIELD04 |  ОУ: доп. поле 4
P_FUNC_DT_SUPPLEMENTARYFIELD05 |  ОУ: доп. поле 5
P_FUNC_DT2_PAGECOUNTER |  ОУ (нижестоящее): Страница
P_FUNC_DT2_PAGESUBCOUNTER |  ОУ (нижестоящее): Подстраница
P_FUNC_DT2_COLUMN |  ОУ (нижестоящее): Столбец
P_FUNC_DT2_ROW |  ОУ (нижестоящее): Строка
P_FUNC_DT2_SECTION |  ОУ (нижестоящее): Раздел
P_FUNC_DT2_FUNCTIONCODE |  ОУ (нижестоящее): Приложение
P_FUNC_DT2_SUPPLEMENTARYFIELD01 |  ОУ (нижестоящее): Дополнительное поле 1
P_FUNC_DT2_SUPPLEMENTARYFIELD02 |  ОУ (нижестоящее): Дополнительное поле 2
P_FUNC_DT2_SUPPLEMENTARYFIELD03 |  ОУ (нижестоящее): Дополнительное поле 3
P_FUNC_DT2_SUPPLEMENTARYFIELD04 |  ОУ (нижестоящее): Дополнительное поле 4
P_FUNC_DT2_SUPPLEMENTARYFIELD05 |  ОУ (нижестоящее): Дополнительное поле 5
P_FUNC_CRAFT |  Раздел
P_FUNC_SUBCRAFT |  Подраздел
P_FUNC_ISPLACEDIN_CIRCUIT |  Функция с представлением вида "Многополюсный"
P_FUNC_ISPLACEDIN_SINGLELINE |  Функция с представлением вида "Однополюсный"
P_FUNC_ISPLACEDIN_PAIRCROSSREFERENCE |  Функция с представлением вида "Парная перекрестная ссылка"
P_FUNC_ISPLACEDIN_OVERVIEW |  Функция с представлением вида "Обзор"
P_FUNC_ISPLACEDIN_PROCESSANDINSTDIAGRAM |  Функция с представлением вида "Функциональная схема автоматизации"
P_ARTICLEREF_PARTNO |  Номер изделия
P_ARTICLEREF_COUNT |  Количество
P_ARTICLEREF_COUNT_PLACED |  Колич. (размещ.)
P_ARTICLEREF_COUNT_NOTPLACED |  Колич. (не размещ.)
P_ARTICLEREF_MOUNTINGPLATE |  Монтажная плата
P_ARTICLEREF_PARTTYPE |  Тип записи данных
P_ARTICLEREF_POSNR |  Номер позиции
P_ARTICLEREF_VARIANT |  Вариант
P_ARTICLEREF_FUNCTIONGROUP |  Группа функций
P_ARTICLEREF_PIECETYPE |  Вид изделия
P_ARTICLEREF_ASSIGNMENT |  Присвоение изделия
P_ARTICLEREF_ASSEMBLY |  Узел
P_ARTICLEREF_MODULE_PART |  Изделие модуля
P_ARTICLEREF_SUPPRESSINPARTSLIST |  Подавить в спецификации (если отфильтр.)
P_ARTICLEREF_PROJECTARTICLE |  Покупные изделия
P_ARTICLEREF_COUNT_TOTAL |  Общ. количество (число штук)
P_ARTICLEREF_LENGTH_SUM |  Сумма длин кабелей
P_ARTICLEREF_ADDITIONAL_TEXTFIELD |  Доп. поле, текст
P_ARTICLEREF_ADDITIONAL_BOOLFIELD |  Доп. поле, Да / Нет
P_ARTICLEREF_TOTALPURCHASEPRICE_1 |  Общая покупная цена 1
P_ARTICLEREF_TOTALPURCHASEPRICE_2 |  Общая покупная цена 2
P_ARTICLE_TYPENR |  Номер типа
P_ARTICLE_ORDERNR |  Номер для заказа
P_ARTICLE_DESCR1 |  Обозначение 1
P_ARTICLE_DESCR2 |  Обозначение 2
P_ARTICLE_DESCR3 |  Обозначение 3
P_ARTICLE_MANUFACTURER |  Производитель
P_ARTICLE_SUPPLIER |  Поставщик
P_ARTICLE_MACRO |  Графич. макрос (включая каталог)
P_ARTICLE_HEIGHT |  Высота
P_ARTICLE_WIDTH |  Ширина
P_ARTICLE_DEPTH |  Глубина
P_ARTICLE_MACRONAME |  Графический макрос
P_ARTICLE_PRODUCTSUBGROUP |  Подгруппа продуктов
P_ARTICLE_PICTUREFILE |  Графич. файл
P_ARTICLE_CABLEDESIGNATION |  Обозначение кабеля в графике
P_ARTICLE_SALESPRICE_1 |  Продажная цена 1
P_ARTICLE_SALESPRICE_2 |  Продажная цена 2
P_ARTICLE_WEAR |  Изнашиваемая деталь
P_ARTICLE_SPARE |  Запчасть
P_ARTICLE_MAINTENANCE |  Смазка / техобслуживание
P_ARTICLE_LIFETIME |  Срок службы
P_ARTICLE_STRESS |  Нагрузка
P_ARTICLE_USAGE |  Приобретение
P_ARTICLE_FREE_DATA_DESCRIPTION |  Произв. свойство / описание
P_ARTICLE_FREE_DATA_VALUE |  Произв. свойство / значение
P_ARTICLE_FREE_DATA_UNIT |  Произвольн. свойство / единица измерения
P_ARTICLE_EXTERNAL_PLACEMENT |  Внешнее размещение
REFERENCE_POS |  Базовая позиция изделия задает (при присвоении нескольких изделий) последовательность внесения изделий в диалоговом окне Свойства ++...++ во вкладке Изделия.

**См. также:**

* [Экспортировать спецификации](partslistgui_h_stuecklistenexportieren.md)
* [Импортировать спецификации](partslistgui_h_stuecklistenimportieren.md)
