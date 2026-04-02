# subprojects

    Action class to export and import subprojects.
    

  
Parameter | Description  
---|---  
TYPE | 
    
    
    Type of task to be performed: FILEOFF:       Export Subproject action.
      
  
PROJECTNAME | 
    
    
    Project name with full path (optional).
    If not entered, the selected project is used when the action is called from GUI (like from a script or button bar). 
    If called from the windows command line, PROJECTNAME must be set. Project has to be opened in exclusive mode.
    After calling this method source project object becomes invalid.
      
  
DESTINATIONPATH | 
    
    
    Target directory (optional). Default value is $(MD_PROJECTS).
      
  
SPNR | 
    
    
    Subproject number.
      
  
EXTENDONLY | 
    
    
    Extend subproject only (optional). Default value is false.
      
  
  
**Example**

```
Export subproject.

subprojects /TYPE:FILEOFF /PROJECTNAME:C:\Projects\EPLAN\ESS_Sample_Project.elk /SPNR:1
```
