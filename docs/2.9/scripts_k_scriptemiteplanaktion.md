# Простые сценарии с операциями EPLAN

В простой сценарий можно встроить автоматические операции. С помощью этой [операции EPLAN](availableactions_k_start.md) можно задать автоматическое осуществление различных функций программы (например, резервировать данные, печать и т. д.).

В соответствии с классом атрибуту [Start], а также функции в сценарии в первую очередь нужно задать набор параметров операции, а затем выполняется операция CommandLineInterpreter().Execute().

Общая структура соответствующего сценария C# выглядит так:

    public class \<ScriptName\>
    {

         [Start]
         public void \<FunctionName\>
         {

               ActionCallingContext \<ActionName\>Context = new ActionCallingContext ();
               \<ActionName\>Context .AddParameter("\<ActionParameter1\>","\<Value\>");
               \<ActionName\>Context .AddParameter("\<ActionParameter2\>","\<Value\>");
               ...
               new CommandLineInterpreter().Execute("\<ActionName\>",\<ActionName\>Context);
               return;

         }

    }

!!! example "Пример:"

    Следующий пример демонстрирует сценарий на C# с операцией EPLANprint:public class PrintScript
    {

     [Start]
     public void PrintFunction()
     {

           ActionCallingContext printContext = new ActionCallingContext ();
           printContext .AddParameter("NUMBER","1");
           printContext .AddParameter("PRINTCHANGEDPAGES","0");
           printContext .AddParameter("PRINTREVERSE","0");
           printContext .AddParameter("PRINTCOLLATE","0");
           printContext .AddParameter("PRINTERNAME",@"\\FUEMON\Kyocera FS-1700+ TechDok KX");
           printContext .AddParameter("PROJECTNAME",@"C:\Program Files\EPLAN\Electric P8\Projects\EPLAN\ESS_Sample_Project.elk);
           printContext .AddParameter("TYPE","PAGES");
           printContext .AddParameter("PAGENAME","=GB1+A1&EFS1/1");
           new CommandLineInterpreter().Execute("print",printContext);
           return;

     }

}ЧерезActionCallingContextв вышеприведенном примере задается набор параметров для функцииPrintFunction. Затем перечисляются различные параметры, а также соответствующие значения для операцииprint. Задайте, например, через параметрNUMBERчисло распечаток. В примере было указано значение"1". Через менюExecuteвыполняется операцияprint.Аналогичный пример в Visual Basic.Net выглядит следующим обр.:Public Class PrintScript
{

     \<Start\> _
     Public Sub PrintFunction()

           Dim printContext As New ActionCallingContext ()
           printContext .AddParameter("NUMBER","1")
           printContext .AddParameter("PRINTCHANGEDPAGES","0")
           printContext .AddParameter("PRINTREVERSE","0")
           printContext .AddParameter("PRINTCOLLATE","0")
           printContext .AddParameter("PRINTERNAME", "\\FUEMON\Kyocera FS-1700+ TechDok KX")
           printContext .AddParameter("PROJECTNAME", "C:\Program Files\EPLAN\Electric P8\Projects\EPLAN\ESS_Sample_Project.elk)
           printContext .AddParameter("TYPE","PAGES")
           printContext .AddParameter("PAGENAME",""=GB1+A1&EFS1/1")
           Dim commandLineInterpreter As New CommandLineInterpreter()
           CommandLineInterpreter.Execute("print",printContext)
           Return

     End Sub 'PrintFunction

End Class 'PrintScript

!!! tip "Совет:"

    Функция Автоматизированная обработка (пункт Сервисные программы) используется для автоматического выполнения операций простых сценариев. Эти сценарии можно использовать для создания собственных сценариев. Прежде чем выполнить эти сценарии через пункты меню Сервисные программы > Сценарии > Выполнить, для функции AutoTreat необходимо удалить параметр String ProjectName и строку, в которой используется этот параметр.

**См. также:**

* [Сценарии](scripts_k_start.md)
* [Автоматизированная обработка проектов](autoprocgui_k_start.md)
