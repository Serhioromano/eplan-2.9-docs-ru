# Операция: EplApiModuleAction

**Параметр** |  **Описание**
---|---
register  |  Полное имя регистрируемого DLL-файла Add-in.
unregister  |  Полное имя Add-in, регистрация которого отменяется.
unregisterInternal  |  Полное имя Add-in, регистрация которого отменяется. Если модуль не может быть выгружен из-за ошибки, то выполняется только отмена его регистрации.

!!! example "Пример:"

    Вызов операции для загрузки Add-in:W3u.exe EplApiModuleAction
    /register:"C:\...\EPLAN\Electric P8\...\Bin\Eplan.EplAddin.MyAddin3.dll"Вызов операции для выгрузки дополнительного модуля:W3u.exe EplApiModuleAction
    /unregister:"Eplan.EplAddin.MyAddin3"
