# Операция: devicelist

**Параметр** |  **Описание**
---|---
TYPE  |  Вид задачи, которую должна выполнить операция:
IMPORT: Импортир. список устройств
EXPORT: Экспортир. список устройств
DELETE: Удалить список устройств
PROJECTNAME  |  Имя проекта с полным путем файла (является опцией).
Если не задано, то выбранный проект используется, когда операция вызывается через интерфейс пользователя (напр., через сценарий или панель инструментов). При вызове из командной строки Windows следует определить PROJECTNAME или сначала следует использовать ProjectAction. В противном случае отобразится системное сообщение.
IMPORTFILE  |  Здесь следует указать каталог и имя файла импортируемого списка устройств.
EXPORTFILE  |  Здесь следует указать каталог и имя файла экспортируемого списка устройств.
FORMAT  |  Необязательно: формат файла ("XDLXmlExporter", "XDLTxtImporterExporter", "XDLCsvImporterExporter" или определенный пользователем формат)
Значение по умолчанию: XDLXmlExporter

!!! example "Пример:"

    Импортировать:devicelist
    /TYPE:IMPORT
    /PROJECTNAME:C:\Projects\EPLAN\ESS_Sample_Project.elk
    /IMPORTFILE:C:\EPLAN\deviceListe.xmlЭкспортировать:devicelist
    /TYPE:EXPORT
    /PROJECTNAME:C:\Projects\EPLAN\ESS_Sample_Project.elk
    /EXPORTFILE:C:\EPLAN\deviceListe2.xmlУдалить:devicelist
    /TYPE:DELETE
    /PROJECTNAME:C:\Projects\EPLAN\ESS_Sample_Project.elk
