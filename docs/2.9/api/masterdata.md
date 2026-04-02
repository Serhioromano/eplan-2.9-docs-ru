# masterdata

    Action class for operations related to EPLAN master data.
   

 

Parameter | Description 

---|--- 

TYPE |

   

   

**    Type of task to be performed by the action:**
    UPDATEPROJECT: Updates project master data
     

 

PROJECTNAME |

   

   

    Project name with full path (optional).
    If not entered, the selected project is used when the action is called from GUI (like from a script or button bar).

    If called from the windows command line, PROJECTNAME must be set or the

    must be used first, otherwise an  exception is thrown.

     

 

 

**Example**

```
Update project master data from system

masterdata /TYPE:UPDATEPROJECT
```
