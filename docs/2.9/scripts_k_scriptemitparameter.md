# Простые сценарии с параметрами

Функция сценариев принимает также параметр. Это имеет смысл, если при запуске сценарию передается параметр /Param. Это возможно при вызове EPLAN через командную строку:

W3u.exe ExecuteScript /ScriptFile:<Значение> /Param:<Значение>

Если EPLAN запускается через командную строку, чтобы выполнить сценарий, первый параметр — это операция, которую надо выполнить. Операция для выполнения сценариев называется ExecuteScript. Эта операция обладает параметром /ScriptFile, через который задается имя выполняемого сценария. Каждый дальнейший дополнительный параметр (Param1, Param2, Param3, ...) передается функции запуска сценария.

!!! example "Пример:"

    В следующем примере (в C#) сценарию (функции запуска) требуется три параметра символьной строкиParam1,Param2иParam3:public class SimpleScriptWithParameters
    {

     [Start]
     public void FunctionWithParameters(String Param1, String Param2, String Param3)
     {

           MessageBox.Show(Param1 + Param2 + Param3, "SimpleScriptWithParameters")
           return;

     }

}Аналогичный пример в Visual Basic.Net выглядит следующим обр.:Public Class SimpleScriptWithParameters

     \<Start\> _
     Public Sub FunctionWithParameters(ByVal Param1 As String, ByVal Param2 As String, ByVal Param3 As String)

           MessageBox.Show(Param1 + Param2 + Param3, "SimpleScriptWithParameters")
           Return

     End Sub "FunctionWithParameters

End Class "SimpleScriptWithParameters

Важно, что все параметры, которые используются в функции сценария, также применяются при вызове. В ином случае сценарий не выполняется.

!!! example "Пример:"

    Для приложения EPLAN Electric P8 ввод в командную строку для операционной системы Windows 7 выглядел бы следующим образом:"C:\Program Files (x86)\EPLAN\Electric P8\<Номер версии>\BIN\W3u.exe" ExecuteScript /ScriptFile:"C:\Users\Public\EPLAN\Electric P8\Scripte\<Идентификатор фирмы>\SimpleScriptWithParameters.cs" /Param1:Hello /Param2:" EPLAN " /Param3:User!

С помощью этой функции можно расширить вызов командной строки EPLAN на собственный параметр.

С помощью использования общих параметров командной строки, например /NoSplash, /Frame:0 и /Auto, можно запустить программу в невидимом режиме и после выполнения сценария снова закрыть.

**См. также:**

* [Сценарии](scripts_k_start.md)
* [Параметры командной строки EPLAN](commandlinecall_k_start.md)
