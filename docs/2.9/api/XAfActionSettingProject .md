# XAfActionSettingProject

     sets the value of a project setting.
    

   

 

Parameter | Description 

---|--- 

Project |

   

   

    fullname of the target project. When empty the currently selected project is used.
     

 

set |

   

   

    name of the project setting to set
     

 

index |

   

   

    optional index of setting.if missing, then 0 is used
     

 

value |

   

   

    new value of setting
     

 

 

Remarks
   

   

     See also "XAfActionSetting" to change other than project settings
    

   

 

**Example**

```
XAfActionSettingProject /set:EsCrossReference.ContactImage.MotorSwitchDisplayBitMask /value:1
```
