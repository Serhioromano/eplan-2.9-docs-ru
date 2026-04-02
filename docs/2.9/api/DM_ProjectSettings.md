# Project settings

Each project has its own set of settings. For getting and setting these settings, as well as for creating new settings the DataModel namespace provides a class called ProjectSettings. It has similar methods like the settings class in Eplan.EplApi.Base, however an instance of this class is initialized with the project object. In contrary to the "normal" settings, project settings keys **don't** start with "PROJECT", where the other settings start with "USER", "STATION", or "COMPANY". 

Example for project related settings Projects->(project name)->Connections->General 

```example title
<?xml version="1.0" encoding="utf-8" ?>
<Settings ver="2.4.1" format="2">
 <CAT name="PROJECT">
<MOD name="EsConnection">
   <Setting name="ManageConnectionsInNDPDialog" type="bool">
    <Val>0</Val>
   </Setting>
   <Setting name="ManageSaddleJumperConnPointsInNDPDialog" type="bool">
    <Val>0</Val>
   </Setting>
   <Setting name="SortConnectionsByPlacement" type="bool" desc="2058">
    <Val>0</Val>
   </Setting>
</MOD>
 </CAT>
</Settings>
```

The following example shows, how to get the project setting for the project's display languages. 

=== "C#"

    ```csharp
    Eplan.EplApi.DataModel.ProjectSettings projectSettings =
              new Eplan.EplApi.DataModel.ProjectSettings(oProject);
    string languages = projectSettings.GetExpandedStringSetting("TRANSLATEGUI.DISPLAYED_LANGUAGES", 0)
    ```

=== "VB"

    ```vb
    Dim projectSettings As New Eplan.EplApi.DataModel.ProjectSettings(oProject)
    Dim languages As String
    languages = projectSettings.GetExpandedStringSetting("TRANSLATEGUI.DISPLAYED_LANGUAGES", _
                                                           System.Convert.ToUInt32(0))
    ```

![](sectionminus.png)See Also

[Working with settings](WorkingWithSettings.html)
