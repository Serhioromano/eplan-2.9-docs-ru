# Операция: XSettingsUnregisterAction

**Параметр** |  **Описание**
---|---
path  |  Путь файла, в котором находится Add-on.
installFile |  Этот параметр можно использовать вместо параметра path для указания полного пути к файлу install.xml.
allowAutoInstall |  Если для этого параметра установлено значение "1", при следующем запуске программы Add-on устанавливается автоматически.

!!! example "Пример:"

    Отмена регистрации Add-ons с помощью указания пути к файлу, в котором находится Add-on:XSettingsUnregisterAction /Path:c:\MyAddOnОтмена регистрации Add-ons с помощью указания полного пути к файлу install.xml:XSettingsUnregisterAction /InstallFile: c:\MyAddOn\CFG\Install.xml
