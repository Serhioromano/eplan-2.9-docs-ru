docs/2.9/api/backup.md broken table



## Заголовок

В начале каждого файла маркдаун в docs/2.9/api есть

---
[![](images/EPLAN_Logo_black.png)](index.html)

API Help

[](webindex.html)

[EPLAN API](index.html) / [User Guide](API_UserGuide.html) / [API Framework](API_Framework.html) / [Add-ins](AddIns.html) / Actions

Collapse All Expand All

In This Topic




Actions
---

Нужно все удалить а строку типа Actions сделать заголовком первого уровня.

## Навигация

В навигации есть 3 раздела

Справка EPLAN
Обзоры EPLAN
Новости EPLAN

Нужно добавить туда 

API EPLAN

с ссылками и структурой дерева созданного файла tools/29/api-tree.json на файлы маркдаун в папке site/2.9/api.


## коды

В файлах например docs/2.9/api/AddinMenuPoints.md есть такие примеры кода выглядят вот так

---
  * C#
  * VB


    
    
    /// <summary>
    /// This function is called by the framework of EPLAN, when the framework already has initialized its
    /// graphical user interface (GUI) and the add-in can start to modify the GUI.
    /// The function only is called, if the add-in is loaded on system-startup.
    /// </summary>
    /// <returns>true, if function succeeds</returns>
    public bool OnInitGui()
    {
       Eplan.EplApi.Gui.Menu oMenu = new Eplan.EplApi.Gui.Menu();
       oMenu.AddMenuItem("CSharpAction", "CSharpAction");
       return true;
    }
    
    
    
    ''' <summary>
    ''' This function is called by the framework of EPLAN, when the framework already has initialized its
    ''' graphical user interface (GUI) and the add-in can start to modify the GUI.
    ''' The function only is called, if the add-in is loaded on system-startup.
    ''' </summary>
    ''' <returns>true, if function succeeds</returns>
    Public Function OnInitGui() As Boolean Implements IEplAddin.OnInitGui
       Dim oMenu As Eplan.EplApi.Gui.Menu = New Eplan.EplApi.Gui.Menu
       oMenu.AddMenuItem("CSharpAction", "CSharpAction")
       Return True
    End Function 'OnInitGui
---    


Их нужно превратить вот в такие

---
=== "C#"

    ```C#
    /// <summary>
    /// This function is called by the framework of EPLAN, when the framework already has initialized its
    /// graphical user interface (GUI) and the add-in can start to modify the GUI.
    /// The function only is called, if the add-in is loaded on system-startup.
    /// </summary>
    /// <returns>true, if function succeeds</returns>
    public bool OnInitGui()
    {
       Eplan.EplApi.Gui.Menu oMenu = new Eplan.EplApi.Gui.Menu();
       oMenu.AddMenuItem("CSharpAction", "CSharpAction");
       return true;
    }
    ```

=== "VB"

    ```vb
    ''' <summary>
    ''' This function is called by the framework of EPLAN, when the framework already has initialized its
    ''' graphical user interface (GUI) and the add-in can start to modify the GUI.
    ''' The function only is called, if the add-in is loaded on system-startup.
    ''' </summary>
    ''' <returns>true, if function succeeds</returns>
    Public Function OnInitGui() As Boolean Implements IEplAddin.OnInitGui
       Dim oMenu As Eplan.EplApi.Gui.Menu = New Eplan.EplApi.Gui.Menu
       oMenu.AddMenuItem("CSharpAction", "CSharpAction")
       Return True
    End Function 'OnInitGui
    ```
---



## Картика

Некоторые картинки не скачались. Код 404 например в docs/2.9/api/DataModelEObjectsOverview.htm

Вот базовый УЛР для картинок

https://www.eplan.help/en-us/Infoportal/Content/api/2.9/DataModel_EObjects_Graph.PNG

Можешь создать скрипт который пройдется по всем файлам htm в папке docs/2.9/api и от туда все картинки выбрать и скачать в папку docs/2.9/api/images. Каждую картинку только один раз скачать.


## Коды

В некоторых файлах есть вот такое.

The types of pages, which you can create are listed in the DocumentTypeManager.DocumentType enumeration.

Создай скрипт который такие конструкции возьмёт в обратные кавычки.

The types of pages, which you can create are listed in the `DocumentTypeManager.DocumentType enumeration`.


## Другое


- [![](Cabinet.jpg)](`Cabinet.jpg` "Click to enlarge") - (это ссылки на картики)
- To find out, which action is connected to which menu item, you can evaluate the "`onActionStart.String`.*" - (не включил .*)
- Sometimes `e.g`. project Ids are added to - (это просто текст)
- example. C:\WINDOWS\`Microsoft.NET`\Framework\v2.0.50727. This folde - (Не надо внтури ссылок)
- # `Eplan.EplApi.OnPostOpenProject` (не надо внутри заголовков)



Example
    
    
    m_EventHandler = new EventHandler("Eplan.EplApi.OnPostOpenProject");
    m_EventHandler.EplanEvent += delegate(IEventParameter parameter)
    {
        new Decider().Decide(EnumDecisionType.eOkDecision, " Project " + new EventParameterString(parameter).String + " was open!", "OnPostOpenProject", EnumDecisionReturn.eOK, EnumDecisionReturn.eOK);
    };

Parameter Type: AfEvParString  

<Add-on>

<Add-on version>

BIN Here, all binaries of the add-on are installed.

CFG Here, all XMLfiles and the `install.xmlare` installed. The `Install.xmlfile` is the base data. The names of the folders are listed in the `install.xml` for copying the data to the EPLAN base data

<Images>

<Scripts>

<XML>

<…>




This is MkDocs project. It is empty frame configured as I want it to look. I have to files 

1. file `tree.json` - contains structure tree
2. folder `docs/eplan` - contains files

Files are stored in Markdown format already. The name of the files matches end of the URL in structure tree ends with `.md` not `.htm` as in URL.

Can you modify `mkdocs.yml` and create a `nav:` structure according to structure tree.


At the end of each markdown file in `docs/new` there is a section

Пример

```
См. также

[Преобразование вспомогательной функции в главную](eplan/adjustdata_h_nebenfunktionaendern.md)

[Преобразовать излишние главные функции](eplan/adjustdata_h_funktionkorrigieren.md)

[Синхронизировать распределенно представленные функции](eplan/adjustdata_h_funktionabgleichen.md)
```

Я хочу получить

```
**См. также:**

* [Преобразование вспомогательной функции в главную](eplan/adjustdata_h_nebenfunktionaendern.md)
* [Преобразовать излишние главные функции](eplan/adjustdata_h_funktionkorrigieren.md)
* [Синхронизировать распределенно представленные функции](eplan/adjustdata_h_funktionabgleichen.md)
```

1. Make `См. также` bold
2. Place `:` after `См. также`
3. Make links into markdown list
4. Delete lines between links
5. Have one line after `См. также`

Other tasks for a file

1. Delete all double new lines and replace with a single empty line
2. In the lists starts with * or 1., 2., .. delete all white spaces because it starts like this

```md
  * Item1
  * Item2

  1. Item 3
  2. Item 4
```

3. At the beginning of each file delete any text before first title `## Это заголовок`
4. All links like `[ссылка](this_islink.htm)` change `.htm` to `.md`

Can you create a script that would make those changes to files and run it?
Do not delete that script it might be needed later.


Please analyze file `serve.log`. there you find something like this

```
WARNING -  Doc file 'eplan/messages_o_001Terminals.md' contains a link 'messages_p_001001.md', but the target 'eplan/messages_p_001001.md' is not found among documentation files.
```

Please extract unfound file that refer to .md not .png name and convert it to URL

https://www.eplan.help/ru-ru/Infoportal/Content/Plattform/2026/Content/htm/wirenumberinggui_h_netzerweiterung.htm

1. Change extension to `htm`
2. All URLs have to have same path

Create json file like `tree.json` with only one level of structure and put there all those links. keep json structure like in tree.json.


Create script any apply. When a line in the file that starts with arrow image, example

```
![](images/arrow.png) Функции будет присвоено свойство **Главная функция**.
```

convert into admonition info

```
!!! info "Для сведения:"

    Функции будет присвоено свойство Главная функция.
```

1. There should be one empty line before admonition
2. There should be one empty line after admonition
3. there should be a line between title and body


В тексте можно встретить такой пример.

[![](images/settingsmastergui_newsettingforpartreports_ls_thumb_0_60.png)](../Pictures/Gui/Lang/settingsmastergui_newsettingforpartreports_ls.png)

Это картинка превью (_thumb) как ссылка на полную картинку. Нужно сделать скрипт который уберет картинку превью и оставит только размещенную основную картинку, при этом нужно исправить ссылку на картинку. 

images/settingsmastergui_newsettingforpartreports_ls.png


Я вижу в тексте

кнопка++ OK++недоступна.

Создай и примери скрипт кторый исправит следюущую ошибку. В некоторых файлах есть такое

Щелкните по кнопке ++ OK++

1. Перед начало ++ должен быть пробле
2. После начало ++ пробела быть не должно
3. Перед концом ++ проблеа быть не должно
4. После конца ++ должен быть пробел если там не точка.

Исправь файлы и Добавь исправления в tools/fix_new_docs.py


В файлах маркдаун в docs есть такие примеры.

Создать(<текущий_номер>)

или

исходный_номер_изделия(<порядковый_номер>)

Можешь подобные патеры заключить в обратные кавычки типа 

`Создать(<текущий_номер>)`


Cоздай скрипт и примени

<Библиотека символов>;<Присвоение библиотеки символов в проекте>;<Номер символа>;<Вариант>


Can you create script that will check image size in docs/eplan/images and if it is less than 22x22 add a ui-icon class like this

![](images/all_new_as.png){ .ui-icon }

Also apply this to all images that are inside the string. Do not apply it to images that a on a separate line.