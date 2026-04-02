# XSettingsUnregisterAction

     Deregistration of Addons
    

   

 

Parameter | Description 

---|--- 

path |

   

   

    The path the addon is located. p.e. addon/1.0.0 .
     

 

`installFile` |

   

   

    or the complete path of the install.xml file
     

 

`allowAutoInstall` |

   

   

    true: remove the marker for autoinstall, then the addon is autoinstalled next time.
     

 

 

Remarks

 

**Example**

```
Registering Add-ons with the path in which the addon is located

               XSettingsUnregisterAction /Path:c:\MyAddOn

Registering Add-ons with the complete path of the instal.xml file

               XSettingsUnregisterAction /InstallFile: c:\MyAddOn\CFG\Install.xml
```
