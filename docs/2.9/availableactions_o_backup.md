# Операция: backup

**Параметр** |  **Описание**
---|---
TYPE  |  Вид выполняемой задачи:
PROJECT: Резервирование всего проекта
MASTERDATA: Резервирование основных данных
PROJECTNAME  |  Имя проекта с полным путем файла (является опцией).
Если не задано, то выбранный проект используется, когда операция вызывается через интерфейс пользователя (напр., через сценарий или панель инструментов). При вызове из командной строки Windows следует определить PROJECTNAME или сначала следует использовать ProjectAction. В противном случае отобразится системное сообщение.
ARCHIVENAME  |  Имя архива.
Имя файла, в котором должны сохраняться данные резервирования (без указания пути).
DESTINATIONPATH  |  Целевой каталог
COMMENT  |  Комментарий для резервирования (необязательно).
Комментарий записывается в виде строки в соответствующем свойстве резервируемого проекта.
Значение по умолчанию: соответствующее свойство не задано.
BACKUPMEDIA  |  Вид сохранения:
EMAIL: Проект отправляется по электронной почте.
DISK: Проект резервируется на жесткий диск, дискету и т.д.
SPLITSIZE  |  Если подлежащий резервированию проект следует запаковать (заархивировать), то целевой файл может быть автоматически разделен на несколько частей, чтобы его можно было отправлять по электронной почте. SPLITSIZE указывает максимальный размер файла в мегабайтах. Если SPLITSIZE = 0, то файл не делится. Если значение параметра BACKUPMEDIA = DISK, то SPLITSIZE игнорируется. Параметр является опцией (значение по умолчанию: 0.0).
BACKUPAMOUNT  |  Константа enum, которая может принимать следующие значения:
BACKUPAMOUNT_ALL: Резервируется все содержание каталога проекта.
BACKUPAMOUNT_MIN: Резервируются только файлы базы данных, необходимые для восстановления проекта, излишние файлы базы данных игнорируются.
Значение по умолчанию: BACKUPAMOUNT_ALL.
COMPRESSPRJ  |  Указывает, следует ли перед резервированием сжать базу данных (необязательно, 0 = нет, 1 = да).
Значение по умолчанию: 0
INCLEXTDOCS  |  Указывает, следует ли учесть в резервировании внешние документы (необязательно, 0 = нет, 1 = да).
Значение по умолчанию: 0
INCLIMAGES  |  Указывает, следует ли учесть в резервировании графические файлы (необязательно, 0 = нет, 1 = да).
Значение по умолчанию: 0
COPYREFDATA  |  Указывает, следует ли перед резервированием копировать указанные данные (внешние документы, графические файлы) в соответствующий каталог проекта (...\ "Имя проекта"\DOC\\*.* и .\ "Имя проекта"\Images\\*.*) (необязательно, 0 = нет, 1 = да).
Значение по умолчанию: 0
Действительно, только если параметр TYPE имеет следующее значение: PROJECT.
BACKUPMETHOD  |  Вид резервирования:
BACKUP: Проект резервируется
PACK: Проект упаковывается
SOURCEOUT: Проект выгружается
ARCHIVE: Проект архивируется. Нельзя указывать, если значение параметра BACKUPMEDIA = EMAIL.
MDTYPE  |  Тип резервируемых основных данных:
SYMBOLS: Библиотеки символов
MACROS: Макросы
FORMS: Формы
ARTICLES: Данные изделий
LANGUAGES: Словари
STANDARDSHEET: Рамки
STATIONDATA: Данные пользователя, рабочей станции
SOURCEPATH  |  Исходный каталог, применимо только при резервировании основных данных.
FILENAME  |  Имя резервируемого файла.
Имя файла может быть введено с указанием или без указания полного пути.
Расширение имени файла должно быть указано.
Возможно расширение имени файла с заполнителями (пример: /FILENAME:*.fn1, /FILENAME:*.*, /FILENAME:*sh).
Это относится только к резервированию основных данных.

!!! example "Пример:"

    Резервировать проект:backup
    /TYPE:PROJECT
    /PROJECTNAME:C:\Projects\EPLAN\ESS_Sample_Project.elk
    /DESTINATIONPATH:U:\temp
    /ARCHIVENAME:my_prj.zw1
    /COMMENT:Hello
    /BACKUPMETHOD:BACKUP
    /BACKUPMEDIA:DISK
    /SPLITSIZE:0.0
    /BACKUPAMOUNT:BACKUPAMOUNT_ALL
    /COMPRESSPRJ:0
    /INCLEXTDOCS:1
    /INCLIMAGES:1backup
    /TYPE:PROJECT
    /COMMENT:Hello
    /DESTINATIONPATH:U:\temp
    /ARCHIVENAME:my_prj.zw1
    /BACKUPMETHOD:BACKUP
    /BACKUPMEDIA:DISK
    /SPLITSIZE:0.0
    /BACKUPAMOUNT:BACKUPAMOUNT_ALL
    /COMPRESSPRJ:0
    /INCLEXTDOCS:1
    /INCLIMAGES:1Резервировать основные данные:Резервировать рамку с полным путем файла:backup
    /TYPE:MASTERDATA
    /FILENAME:C:\PlotFrames\EPLAN\ESS_A3DP.fn1
    /SOURCEPATH:C:\PlotFrames\EPLAN
    /DESTINATIONPATH:U:\temp
    /ARCHIVENAME:my_MasterData
    /COMMENT:"Hello world"
    /BACKUPMEDIA:DISK
    /SPLITSIZE:0.0
    /MDTYPE:STANDARDSHEETРезервировать рамку без полного пути файла:backup
    /TYPE:MASTERDATA
    /FILENAME:ESS_A3DP.fn1
    /SOURCEPATH:C:\PlotFrames\EPLAN
    /DESTINATIONPATH:U:\temp
    /ARCHIVENAME:my_MasterData
    /COMMENT:"Hello world"
    /BACKUPMEDIA:DISK
    /SPLITSIZE:0.0
    /MDTYPE:STANDARDSHEETРезервировать все рамки (*.fn1):backup
    /TYPE:MASTERDATA
    /FILENAME:*.fn1
    /SOURCEPATH:C:\PlotFrames\EPLAN
    /DESTINATIONPATH:U:\temp
    /ARCHIVENAME:my_MasterData
    /COMMENT:"Hello world"
    /BACKUPMEDIA:DISK
    /SPLITSIZE:0.0
    /MDTYPE:STANDARDSHEETРезервировать все файлы (*.*) в указанном исходном каталоге:backup
    /TYPE:MASTERDATA
    /FILENAME:*.*
    /SOURCEPATH:C:\PlotFrames\EPLAN
    /DESTINATIONPATH:U:\temp
    /ARCHIVENAME:my_MasterData
    /COMMENT:"Hello world"
    /BACKUPMEDIA:DISK
    /SPLITSIZE:0.0
    /MDTYPE:STANDARDSHEETРезервировать в указанном исходном каталоге все файлы (*.*), в расширении имени которых есть 'sh'.backup
    /TYPE:MASTERDATA
    /FILENAME:*sh
    /SOURCEPATH:C:\PlotFrames\EPLAN
    /DESTINATIONPATH:U:\temp
    /ARCHIVENAME:my_MasterData
    /COMMENT:"Hello world"
    /BACKUPMEDIA:DISK
    /SPLITSIZE:0.0
    /MDTYPE:STANDARDSHEET
