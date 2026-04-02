# ExecuteScript

     action name = ExecuteScript
   

     Runs the given script.
    

   

 

Parameter | Description 

---|--- 

ScriptFile |

   

   

    Script file to run.
     

 

 

Remarks
   

   

     Only scripts with the [Start] attribute can be run.
     When passed script takes as parameter ,
     ActionCallingContext passed for this action will be passed further to script.
    

   

 

**Example**

```
EPLAN.exe /Variant:"Electric P8" ExecuteScript /ScriptFile:"C:\...\EPLAN\Electric P8\Scripts\...\SimpleScriptWithParameters.cs /Param1:Hello /Param2:EPLAN /Param3:" API developer!"
```
