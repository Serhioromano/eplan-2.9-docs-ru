# XAfActionSetting

     sets the value of a setting
    

   

 

Parameter | Description 

---|--- 

set |

   

   

    name of the setting to set
     

 

index |

   

   

    optional index of setting.if missing, then 0 is used
     

 

value |

   

   

    new value of setting
     

 

 

Remarks
   

   

     See also "XAfActionSettingProject" to change project settings
    

   

 

**Example**

```
XAfActionSetting /set:USER.MacrosLog.Pxf.writeDebugInfo /value:1
```
