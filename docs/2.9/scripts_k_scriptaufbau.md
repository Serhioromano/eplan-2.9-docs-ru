# Создание простого сценария

Простой сценарий, который можно выполнить, состоит по крайней мере из одного общего класса как минимум с одной функцией. Эту функцию всегда необходимо выделять атрибутом [Пуск].

Общая структура простого сценария C# выглядит так:

    public class \<ScriptName\>
    {

         [Start]
         public void \<FunctionName\>
         {

               //<Enter your code text here>
               return;

         }

    }

!!! example "Пример:"

    Следующий пример демонстрирует очень простой сценарий на C#:public class SimpleScript
    {

     [Start]
     public void MyFunction()
     {

           MessageBox.Show("MyFunction was called!", "SimpleScript");
           return;

     }

}В этом примере классSimpleScriptсоздается через функциюMyFunction. Эта функция выделяется через атрибут[Start]. Если сценарий выполняется через путь меню Сервисные программы > Сценарии > Выполнить, появляется сообщениеMyFunction was called!.Аналогичный пример в Visual Basic.Net выглядит следующим обр.:Public Class SimpleScript

     \<Start\> _
     Public Sub MyFunction()

           MessageBox.Show("MyFunction was called!", "SimpleScript")
           Return

     End Sub 'MyFunction

End Class 'SimpleScript

Сценарий может содержать больше чем одну функцию и различные классы. В каждом случае одна функция должна быть обозначена через атрибут [Start].

**См. также:**

* [Сценарии](scripts_k_start.md)
