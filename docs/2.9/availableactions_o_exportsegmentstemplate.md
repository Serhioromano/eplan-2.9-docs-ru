# Операция: ExportSegmentsTemplate

**Параметр** |  **Описание**
---|---
PROJECTNAME  |  Имя проекта с полным путем файла (является опцией).
Если не задано, то выбранный проект используется, когда операция вызывается через интерфейс пользователя (напр., через сценарий или панель инструментов). При вызове из командной строки Windows следует определить PROJECTNAME или сначала следует использовать ProjectAction. В противном случае отобразится системное сообщение.
FILENAME  |  Полный путь и имя целевого файла. Не может быть пустым.
DESCRIPTION  |  Описание внутри экспортируемого файла (многоязычная символьная строка).

!!! example "Пример:"

    ExportSegmentsTemplate
    /PROJECTNAME:C:\Projects\EPLAN\ESS_Sample_Project.elk
    /FILENAME:C:\EPLAN\Templates\SegmentTemplates.txt
    /DESCRIPTION:Segment templates exported from ESS_Sample_Project
