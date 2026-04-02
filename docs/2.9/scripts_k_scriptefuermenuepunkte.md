# Добавить пункт меню через сценарий

С помощью сценария можно добавить к меню Сервисные программы один или несколько пунктов меню. Для этого в соответствующем сценарии используется атрибут [DeclareMenu], через этот атрибут вызывается функция MenuFunction(). При загрузке сценария создается пункт меню, определяемый через функцию AddMenuItem.

Общая структура соответствующего сценария C# выглядит так:

    public class \<ScriptName\>
    {

         [DeclareMenu]
         public void MenuFunction()
         {

               Eplan.EplApi.Gui.Menu oMenu = new Eplan.EplApi.Gui.Menu();
               oMenu.AddMenuItem("\<MenuText\>","\<ActionName\>");

         }

    }

Пункт меню всегда связан с операцией, которая вызывается при выполнении пункта меню. Это означает, что либо сценарий дополнительно регистрирует операцию (через [DeclareAction]), либо пункт меню присваивается уже существующей операции.

!!! example "Пример:"

    Следующий пример демонстрирует сценарий на C#, который регистрирует операцию или пункт меню:public class RegisterScriptMenu
    {

     [DeclareAction("MyScriptActionWithMenu")]
     public void MyFunctionAsAction()
     {

           MessageBox.Show("MyFunctionAsAction was called!", "RegisterScriptMenu");
           return;

     }

     [DeclareMenu]
     public void MenuFunction()
     {

           Eplan.EplApi.Gui.Menu oMenu = new Eplan.EplApi.Gui.Menu();
           oMenu.AddMenuItem("MyMenuText", "MyScriptActionWithMenu");

     }

}В вышеприведенном примере функцияAddMenuItem()из классаEplan.EplApi.Gui.Menuсоздает новый пункт менюMyMenuTextи соединяет его с операциейMyScriptActionWithMenu.Аналогичный пример в Visual Basic.Net выглядит следующим обр.:Public Class RegisterScriptMenu

     <DeclareAction("MyScriptActionWithMenu")> _
     Public Sub MyFunctionAsAction()

           MessageBox.Show("MyFunctionAsAction was called!", "RegisterScriptMenu")
           Return

     End Sub 'MyFunctionAsAction

     <DeclareMenu()> _
     Public Sub MenuFunction()

           Dim oMenu As New Eplan.EplApi.Gui.Menu()
           oMenu.AddMenuItem("MyMenuText", "MyScriptActionWithMenu")

     End Sub 'MenuFunction

End Class 'RegisterScriptMenu

**См. также:**

* [Сценарии](scripts_k_start.md)
* [Выполнить или загрузить сценарии](scripts_h_scripteausfuehren.md)
