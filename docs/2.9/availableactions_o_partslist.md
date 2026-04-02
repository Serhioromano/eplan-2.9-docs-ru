# Операция: partslist

**Параметр** |  **Описание**
---|---
TYPE  |  Вид выполняемой задачи:
IMPORT: Импортировать спецификации
EXPORT: Экспортировать спецификации
IMPORTTOSYSTEM: Импорт в базу данных изделий
EXPORTFROMSYSTEM: Экспорт из базы данных изделий
DELETESTOREDPROPERTIES: Удаление сохраненных свойств из проекта
PROJECTNAME  |  Имя проекта с полным путем файла (является опцией).
Если не задано, то выбранный проект используется, когда операция вызывается через интерфейс пользователя (напр., через сценарий или панель инструментов). При вызове из командной строки Windows следует определить PROJECTNAME или сначала следует использовать ProjectAction. В противном случае отобразится системное сообщение.
IMPORTFILE  |  Здесь следует указать каталог и имя импортируемого файла. Действительно только для импорта.
EXPORTFILE  |  Здесь следует указать каталог и имя экспортируемого файла. Система автоматически добавляет расширение имени файла. Действительно только для экспорта.
FORMAT  |  Дополнительно:  Форматы файлов для импорта (TYPE:IMPORT) / экспорта (TYPE:EXPORT) спецификаций:

* XPalXmlExporter
* или XPalCSVConverter

Значение по умолчанию: XPalXmlExporter Форматы файлов для импорта в базу данных изделий (IMPORTTOSYSTEM):

* IXPamImportE21
* IXPamImportE5
* IXPamImportText
* IXPamImportCSV
* IXPamImportEcad
* IXPamImportCSVAddresses
* XPamImportXml

Значение по умолчанию: XPamImportXml Форматы файлов для экспорта из базы данных изделий (EXPORTFROMSYSTEM):

* IXPamImportText
* IXPamImportCSV
* IXPamImportCSVAddresses
* XPamExportXml

Значение по умолчанию: XPamExportXml
SQLFILTERPART  |  Опционально: SQL-фильтр для продвинутых пользователей.
Значение по умолчанию: 1 = 1
SQLFILTERADDRESS  |  Опционально: SQL-фильтр для продвинутых пользователей (используется с форматом "IXPamImportCSVAddresses"). Используется для экспорта адресов.
Значение по умолчанию: 1 = 1
SQLFILTERCONSTRUCTION |  Опционально: SQL-фильтр для продвинутых пользователей. Используется для экспорта схем сверления. Значение по умолчанию: 1 = 0
SQLFILTERTERMINAL |  Опционально: SQL-фильтр для продвинутых пользователей. Используется для экспорта схем соединений. Значение по умолчанию: 1 = 0
SQLFILTERACCESSORYLIST |  Опционально: SQL-фильтр для продвинутых пользователей. Используется для экспорта списков принадлежностей. Значение по умолчанию: 1 = 0
SQLFILTERACCESSORYPLACEMENT |  Опционально: SQL-фильтр для продвинутых пользователей. Используется для экспорта размещений принадлежностей. Значение по умолчанию: 1 = 0
CFGFILE  |  Опционально: каталог и имя файла конфигурации.
Значение по умолчанию: используемый в данный момент файл конфигурации.
FIELDASSIGNMENTSCHEME  |  Опционально: имя схемы присвоения полей для импорта изделий.
MODE  |  Опционально: режим импорта. Поддерживаемые режимы:

* 0: только добавление новых записей данных (значение по умолчанию)
* 1: только обновление имеющихся записей данных
* 2: обновление имеющихся записей данных и добавление новых

При указании недействительного значения используется значение по умолчанию 0.
ADDITIONAL_LANGUAGE  |  Опциональн. Действительно, если TYPE = IMPORTTOSYSTEM. Если значение данного параметра равно 1, обновляются многоязычные свойства с другими параметрами языка. Если параметр не задан, значения многоязычных свойств заменяются содержимым файла.
CONFIGSCHEME  |  Схема конфигурации для удаления сохраненных свойств (необязательно).
Значение по умолчанию: последняя использованная схема конфигурации.

!!! note "Замечание:"

    Если при помощи операции partslist должен осуществляться полный экспорт всех типов записей данных их базы данных изделий (TYPE=EXPORTFROMSYSTEM), то дополнительно к параметрам SQLFILTERPART и SQLFILTERADDRESS нужно передать также параметры SQLFILTERCONSTRUCTION, SQLFILTERTERMINAL, SQLFILTERACCESSORYLIST и SQLFILTERACCESSORYPLACEMENT со значением 1=1.

!!! example "Пример:"

    Экспортировать:partslist
    /TYPE:EXPORT
    /PROJECTNAME:C:\Projects\EPLAN\ESS_Sample_Project.elk
    /FORMAT:XPalCSVConverter
    /EXPORTFILE:d:\temp\PartsList.csvИмпортировать:partslist
    /TYPE:IMPORT
    /PROJECTNAME:C:\Projects\EPLAN\ESS_Sample_Project.elk
    /FORMAT:XPalCSVConverter
    /IMPORTFILE:d:\temp\PartsList.csvУдалить сохраненные свойства из проекта:partslist
    /TYPE:DELETESTOREDPROPERTIES
    /PROJECTNAME:C:\Projects\EPLAN\ESS_Sample_Project.elk
    /CONFIGSCHEME:config_scheme
