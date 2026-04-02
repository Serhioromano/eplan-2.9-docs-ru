# Простые сценарии для настроек

Простые сценарии можно использовать для того, чтобы считывать и изменять настройку из диалогового окна "Настройки".

!!! note "Замечание:"

    Это ***не*** касается ***настроек проекта***!

Перед считыванием настройки необходимо узнать ее имя. Для этого включите с помощью следующего сценария C# скрытое всплывающее меню:

    public class SetSettingScript
    {

         [Start]
         public void SetSetting()
         {

               Eplan.EplApi.Base.Settings oSettings = new Eplan.EplApi.Base.Settings();
               oSettings.SetBoolSetting("USER.EnfMVC.ContextMenuSetting.ShowExtended", true, 0);
               return;

         }

    }

После того как выполнен сценарий, необходимо в первую очередь заново запустить EPLAN. Затем в вашем распоряжении находится всплывающее меню диалогового окна Настройки, дополнительно пункт меню Скопировать путь настроек в буфер обмена. Выполните пункт меню для настройки и скопируйте имя в буфер обмена. Имя для настройки Отображать идентифицирующие номера может выглядеть, например, так: USER.SYSTEM.GUI.SHOW_PROPERTY_NR. Эти имена можно использовать в сценарии, чтобы изменить или считать соответствующую настройку.

!!! example "Пример:"

    Следующий пример демонстрирует сценарий на C#, через который можно активировать настройку Отображать идентифицирующие номера:public class SetSettingScript
    {

     [Start]
     public void SetSetting()
     {

           Eplan.EplApi.Base.Settings oSettings = new Eplan.EplApi.Base.Settings();
           oSettings.SetBoolSetting("USER.SYSTEM.GUI.SHOW_PROPERTY_NR", true, 0);
           return;

     }

}В примере с помощью классаSetBoolSettingнастройкаUSER.SYSTEM.GUI.SHOW_PROPERTY_NR(=Отображать идентифицирующие номера) установлена на "true", т. е. включена. Через "false" соответствующий флажок снова снимается.Аналогичный пример в Visual Basic.Net выглядит следующим обр.:Public Class SetSettingScript

     \<Start\> _
     Public Sub SetSetting()

           Dim oSettings As New Eplan.EplApi.Base.Settings()
           oSettings.SetBoolSetting("USER.SYSTEM.GUI.SHOW_PROPERTY_NR", True, 0)
           Return

     End Sub 'SetSetting

End Class 'SetSettingScriptДля считывания этой настройки или для изменения / считывания настроек с другими свойствами необходимо использовать в аналогичных сценариях похожие классы (например,GetBoolSetting,SetStringSettingи т. д.).

**См. также:**

* [Сценарии](scripts_k_start.md)
