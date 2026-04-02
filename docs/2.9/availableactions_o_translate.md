# Операция: translate

**Параметр** |  **Описание**
---|---
TYPE  |  Вид задачи, которую должна выполнить операция: TRANSLATEPROJECT: Перевести проект
TRANSLATEPAGES: Перевести указанные страницы
REMOVELANGUAGE: Убрать языковую запись
EXPORTMISSINGTRANSLATIONS: Экспортировать список отсутствующих слов IMPORTTOTRANSDB: Импортировать базу данных (словарь) EXPORTFROMTRANSDB: Экспортировать базу данных (словарь)

PROJECTNAME  |  Имя проекта с полным путем файла (является опцией).
Если не задано, то выбранный проект используется, когда операция вызывается через интерфейс пользователя (напр., через сценарий или панель инструментов). При вызове из командной строки Windows следует определить PROJECTNAME или сначала следует использовать ProjectAction. В противном случае отобразится системное сообщение.
IMPORTFILE  |  Имя файла с импортируемой базой данных (словарем). Этот параметр оказывает влияние, только когда параметр TYPE имеет следующее значение: IMPORTTOTRANSDB.
EXPORTFILE  |  Имя файла с экспортированным списком отсутствующих слов. Этот параметр оказывает влияние, только когда параметр TYPE имеет следующее значение: EXPORTMISSINGTRANSLATIONS.
CONVERTER  |  Имя конвертера (необязательно).
Это имя используется как формат вывода для списка отсутствующих слов. Возможные форматы вывода:

* XTrLanguageDbXml2TabConverterImpl (файл в формате Юникод с разделением табуляцией)
* XTrLanguageDbXml2E21UnicodeTabConverterImpl (файл EPLAN 21 в формате Юникод с разделением табуляцией)

Значение по умолчанию: XTrLanguageDbXml2TabConverterImpl. Этот параметр оказывает влияние, только когда параметр TYPE имеет следующее значение: EXPORTMISSINGTRANSLATIONS.
LANGUAGE  |  Язык перевода (напр., fr_FR).
Действительно только для параметров:
REMOVELANGUAGE
EXPORTMISSINGTRANSLATIONS
USEPAGEFILTER |  Определяет, должны ли использоваться только отфильтрованные страницы или все страницы проекта (необязательно). Соответствует активации фильтра в интерфейсе пользователя. Этот параметр оказывает влияние, только когда параметр TYPE имеет следующее значение: TRANSLATEPAGES.
Значение по умолчанию: 0
PAGEFILTERNAME |  Имя фильтра страницы. Переводятся только те страницы, которые прошли через фильтр с именем PAGEFILTERNAME. Этот параметр оказывает влияние, только когда параметр TYPE имеет следующее значение: TRANSLATEPAGES.
PAGENAME |  Имя переводимой страницы (не обязательно).
PAGENAMEn |  Имена переводимых страниц (не обязательно). При этом n — это номер, например: /PAGENAME1:=EB3+ET1/2 /PAGENAME2:=EB3+ET1/4 /PAGENAME3:=EB3+ET1/7 и т. д. Эти параметры оказывают влияние, только когда параметр TYPE имеет следующее значение: TRANSLATEPAGES.
SELn |  Ид. объекта переводимых страниц (необязательно). При этом n — это номер, например /SEL1:38/4/12/0. В качестве альтернативы для PAGENAMEn. Этот параметр оказывает влияние, только когда параметр TYPE имеет следующее значение: TRANSLATEPAGES.

!!! note "Замечание:"

    Нельзя убрать исходный язык из проекта. Чтобы убрать несколько языков из одного проекта, необходимо перечислить языки через запятую (напр., /LANGUAGE:en_US,fr_FR,da_DK).

!!! example "Пример:"

    Перевести проект:translate
    /TYPE:TRANSLATEPROJECT
    /PROJECTNAME:C:\Projects\EPLAN\ESS_Sample_Project.elkУбрать перевод из проекта:translate
    /PROJECTNAME:C:\Projects\EPLAN\ESS_Sample_Project.elk
    /TYPE:REMOVELANGUAGE
    /LANGUAGE:en_USЭкспортировать список отсутствующих слов:translate
    /TYPE:EXPORTMISSINGTRANSLATIONS
    /PROJECTNAME:C:\Projects\EPLAN\ESS_Sample_Project.elk
    /LANGUAGE:en_US
    /EXPORTFILE:d:\temp\missingTransFile.txt
    /CONVERTER:XE5LanguageDbXmlConverterImpl
