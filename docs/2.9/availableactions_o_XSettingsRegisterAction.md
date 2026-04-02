# Операция: XSettingsRegisterAction

**Параметр** |  **Описание**
---|---
path  |  Путь файла, в котором находится Add-on.
installFile |  Этот параметр можно использовать вместо параметра path для указания полного пути к файлу install.xml.

!!! example "Пример:"

    Регистрация Add-ons с помощью указания пути к файлу, в котором находится Add-on:XSettingsRegisterAction /Path:c:\MyAddOnРегистрация Add-ons с помощью указания полного пути к файлу install.xml:XSettingsRegisterAction /InstallFile: c:\MyAddOn\CFG\Install.xml
