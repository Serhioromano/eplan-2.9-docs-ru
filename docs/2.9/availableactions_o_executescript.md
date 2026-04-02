# Операция: ExecuteScript

**Параметр** |  **Описание**
---|---
ScriptFile  |  Подлежащий выполнению файл сценария.

!!! note "Замечание:"

    Выполняются только сценарии с атрибутом [Пуск].

!!! example "Пример:"

    W3u.exe ExecuteScript
    /ScriptFile:"C:\...\EPLAN\Electric P8\...\Scripts\...\SimpleScriptWithParameters.cs"
    /Param1:Hello
    /Param2:EPLAN
    /Param3:" API developer!"
