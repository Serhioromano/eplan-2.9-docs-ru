# Операция: import

**Параметр** |  **Описание**
---|---
TYPE |  Вид задачи, которую должна выполнить операция:
PXFPROJECT: Импортировать проект EPJ
DXFDWGFILES: Вставить в макросы чертежи DXF / DWG
DXFPAGE: Вставить на страницу чертеж DXF
DWGPAGE: Вставить на страницу чертеж DWG
PDFCOMMENTS: Импорт PDF-комментариев в проект
PROJECTNAME |  Имя проекта с полным путем к файлу.
Обязательно, если параметр TYPE имеет следующее значение: PDFCOMMENTS.
Необязательно, если параметр TYPE имеет следующие значения: PXFPROJECT, DXFDWGFILES, DXFPAGE и DWGPAGE. Если не задано, то выбранный проект используется, когда операция вызывается через интерфейс пользователя (напр., через сценарий или панель инструментов). При вызове из командной строки Windows следует определить PROJECTNAME или сначала следует использовать ProjectAction. В противном случае отобразится системное сообщение.
IMPORTFILE  |  Путь и имя файла. Значение этого параметра для значений параметра TYPE:
PXFPROJECT: Путь и имя импортируемого файла.
DXFPAGE, DWGPAGE, PDFCOMMENTS: Путь и имя импортируемого файла.
SOURCEPATH  |  Каталог, в котором находятся файлы DXF/DWG. Действительно только для значения DXFDWGFILES параметра TYPE.
DESTINATIONPATH |  Целевой каталог, в котором сохраняются импортированные проекты и макросы. Действительно только для значения DXFDWGFILES параметра TYPE.
Если указанные для DESTINATIONPATH каталоги не существуют, они создаются при импорте.
IMPORTSCHEME  |  Имя схемы импорта DXF / DWG (только имя, без полного пути файла) (необязательно). Значение по умолчанию: последняя использованная схема. Если данный параметр отсутствует или пуст (""), то используется последняя использованная схема. Действительно только для следующих значений параметра TYPE: DXFPAGE, DWGPAGE, DXFDWGFILES.
PAGENAME |  Имя страницы, в которую следует вставить чертеж CAD. Действительно только для значений DXFPAGE и DWGPAGE параметра TYPE.
XSCALE  |  Масштабирование в направлении X (необязательно). Значение по умолчанию: 1\. Действительно только для значений DXFPAGE и DWGPAGE параметра TYPE.
YSCALE  |  Масштабирование в направлении Y (необязательно). Значение по умолчанию: 1\. Действительно только для значений DXFPAGE и DWGPAGE параметра TYPE.
XOFFSET  |  Перемещение в направлении X (необязательно). Значение по умолчанию: 0\. Действительно только для значений DXFPAGE и DWGPAGE параметра TYPE.
YOFFSET  |  Перемещение в направлении Y (необязательно). Значение по умолчанию: 0\. Действительно только для значений DXFPAGE и DWGPAGE параметра TYPE.

!!! example "Пример:"

    Импортировать проект EPJ:import
    /TYPE:PXFPROJECT
    /IMPORTFILE:C:\Projects\DEMO_D.epj
    /PROJECTNAME:C:\Projects\EPLAN\Imported_DEMO_D.elkИмпортировать чертежи DXF/DWG в макросы:import
    /TYPE:DXFDWGFILES
    /PROJECTNAME:C:\Projects\ESS_Sample_Project.elk
    /SOURCEPATH:C:\Projects\DXF_DWG
    /DESTINATIONPATH:D:\MacrosВставить чертеж DXF / DWG на страницу:import
    /TYPE:DWGPAGE
    /PROJECTNAME:C:\Projects\EPLAN\ESS_Sample_Project.elk
    /PAGENAME:=EB3+ET1/2
    /IMPORTFILE:C:\Projects\EPLAN\DXF_DWG\pline_1.dwg
    /XSCALE:0.5
    /YSCALE:0.5
    /XOFFSET:100.0
    /YOFFSET:100.0
